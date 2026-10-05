"""Synthetic clients for the two-player flow; no client files or game data needed."""
import asyncio
import importlib
import json
import pathlib
import struct
import tempfile
import unittest

import ai
import handlers
import loot
import sessions
import skills
import stub
import world
from proto import HEADER, MAGIC, build, deobfuscate, split


def request(opcode, size, uid=0):
    return bytearray(build(opcode, bytes(size - 16), extra=uid))


def token_login(token):
    p = request(0x4207, 0x9C)
    p[0x14:0x94] = token.ljust(128, b"\0")
    struct.pack_into("<I", p, 0x94, 0x41E)
    p[0x98] = 0xFF
    return p


def game_login(reply):
    p = request(0x4200, 0x60)
    p[0x10:0x30] = reply[0x20:0x40]
    p[0x50:0x58] = reply[0x18:0x20]
    struct.pack_into("<I", p, 0x48, 0x41E)
    p[0x4C] = 0xFF
    return p


def create(uid, name, class_id=1, weapon=10017):
    p = request(0x407, 0x260, uid)
    p[0x18] = 1
    p[0x28:0x50] = name.ljust(40, b"\0")
    struct.pack_into("<H", p, 0x56, class_id)
    struct.pack_into("<H", p, 0x60, weapon)
    return p


def select(uid, char_id):
    p = request(0x406, 0x20, uid)
    struct.pack_into("<Q", p, 0x10, char_id)
    return p


def movement(uid, x, z, kind=2):
    return build(0x416, struct.pack("<BBBBHHff", 17, kind, 0, 0, 450, 0, x, z), extra=uid)


def obfuscate(packet, key):
    p = bytearray(packet)
    struct.pack_into("<I", p, 12, key)
    for offset in range(16, len(p) - 3, 4):
        value = struct.unpack_from("<I", p, offset)[0]
        struct.pack_into("<I", p, offset, ~((value - key) & 0xFFFFFFFF) & 0xFFFFFFFF)
    return p


def ops(data):
    packets, rest = split(data)
    assert not rest
    return [(struct.unpack_from("<H", p, 4)[0], p) for p in packets]


class StateFixture:
    def setup_state(self):
        self.directory = tempfile.TemporaryDirectory()
        self.old_state = sessions.STATE_DIR
        sessions.STATE_DIR = pathlib.Path(self.directory.name)
        sessions.CONNECTED.clear()
        sessions.TICKETS.clear()
        world.INITIALIZED = False
        world.CENTRE = (handlers.SPAWN_X, handlers.SPAWN_Z)
        world.reset()
        ai._last["now"] = None

    def cleanup_state(self):
        sessions.CONNECTED.clear()
        sessions.TICKETS.clear()
        sessions.STATE_DIR = self.old_state
        self.directory.cleanup()

    def player(self, name, class_id=1, weapon=10017):
        received = []
        session = sessions.connect(received.append)
        reply = handlers.dispatch("LOGIN_REPLIES", token_login(name))
        handlers.dispatch("GAME_REPLIES", game_login(reply), session)
        reply = handlers.dispatch("GAME_REPLIES", create(session.uid, name, class_id, weapon), session)
        char_id = struct.unpack_from("<Q", reply, 0x20)[0]
        burst = handlers.dispatch("GAME_REPLIES", select(session.uid, char_id), session)
        return session, received, burst


class MultiplayerTests(StateFixture, unittest.TestCase):
    def setUp(self):
        self.setup_state()

    def tearDown(self):
        self.cleanup_state()

    def test_mutual_spawns_and_shared_monsters(self):
        a, inbox_a, _ = self.player(b"Alice")
        slime = world.UNITS[world.MONSTER_UID_BASE]
        slime.hp = 37
        b, inbox_b, burst = self.player(b"Bob", 4, 15007)
        self.assertNotEqual(a.uid, b.uid)
        self.assertEqual(slime.hp, 37)
        remote_a = [p for op, p in ops(burst) if op == 0x803 and HEADER.unpack_from(p)[3] == a.uid][0]
        remote_b = inbox_a[-1]
        self.assertEqual(len(remote_a), 0x270)
        self.assertEqual(remote_a[0x10:0x15], b"Alice")
        self.assertEqual(struct.unpack_from("<H", remote_b, 0x40)[0], 4)
        self.assertEqual(struct.unpack_from("<H", remote_b, 0xBC)[0], 15007)
        self.assertEqual(struct.unpack_from("<I", remote_b, 0x60)[0], 1000)
        self.assertEqual(struct.unpack_from("<H", remote_b, 0x96)[0], 450)
        self.assertIsNot(a.inventory, b.inventory)
        handlers.dispatch("GAME_REPLIES", movement(a.uid, 1431, 433), a)
        self.assertEqual(HEADER.unpack_from(inbox_b[-1])[2:4], (0x416, a.uid))
        self.assertEqual(struct.unpack_from("<ff", inbox_b[-1], 0x18), (1431, 433))
        self.assertEqual(len(inbox_a), 1)  # own movement was not echoed
        correction = handlers.dispatch("GAME_REPLIES", movement(a.uid, 0, 0, 1), a)
        self.assertEqual(struct.unpack_from("<ff", correction, 0x18), (1431, 433))
        with self.assertRaises(ValueError):
            handlers.dispatch("GAME_REPLIES", movement(b.uid, 10, 20), a)

    def test_private_loot_and_reload_preserve_progress(self):
        a, inbox_a, _ = self.player(b"Alice")
        b, inbox_b, _ = self.player(b"Bob")
        slime = world.UNITS[world.MONSTER_UID_BASE]
        slime.hp = 1
        with sessions.use(a):
            hit = world._client_hit(slime.uid)
        reply = handlers.dispatch("GAME_REPLIES", hit, a)
        self.assertIn(0x428, [op for op, _ in ops(reply)])
        self.assertEqual([op for op, _ in ops(inbox_b[-1])], [0x411, 0x420])
        self.assertGreater(a.loot["gold"], 0)
        self.assertEqual(b.loot["gold"], 0)
        self.assertIn(2550, a.inventory["bag"])
        self.assertNotIn(2550, b.inventory["bag"])
        before = (a.inventory.copy(), a.loot.copy(), a.player.copy())
        importlib.reload(handlers)
        self.assertEqual((a.inventory, a.loot, a.player), before)
        self.assertIs(world.UNITS[slime.uid], slime)
        self.assertEqual(slime.hp, 0)

    def test_leave_reenter_and_disconnect(self):
        a, inbox_a, _ = self.player(b"Alice")
        b, inbox_b, _ = self.player(b"Bob")
        a.inventory["bag"][10] = 2550
        a.inventory["count"][10] = 3
        char_id = struct.unpack_from("<Q", a.record)[0]
        reply = handlers.dispatch("GAME_REPLIES", build(0x409, struct.pack("<I", 0), extra=a.uid), a)
        self.assertEqual(HEADER.unpack_from(reply)[2], 0x2001)
        self.assertEqual(HEADER.unpack_from(inbox_b[-1])[2:4], (0x806, a.uid))
        self.assertFalse(a.player["in_world"])
        handlers.dispatch("GAME_REPLIES", select(a.uid, char_id), a)
        self.assertEqual(a.inventory["count"][10], 3)
        handlers.disconnect(a)
        self.assertNotIn(a.uid, sessions.CONNECTED)
        self.assertTrue(b.player["in_world"])
        self.assertEqual(HEADER.unpack_from(inbox_b[-1])[2:4], (0x806, a.uid))

    def test_monster_attacks_one_target_per_world_tick(self):
        a, inbox_a, _ = self.player(b"Alice")
        b, inbox_b, _ = self.player(b"Bob")
        slime = world.UNITS[world.MONSTER_UID_BASE]
        a.player.update(x=slime.x, z=slime.z)
        b.player.update(x=slime.x + 100, z=slime.z + 100)
        for uid in list(world.UNITS):
            if uid != slime.uid:
                del world.UNITS[uid]
        ai.tick_world(10.0, [a, b])
        ai.tick_world(10.6, [a, b])
        self.assertLess(a.player["hp"], 1000)
        self.assertEqual(b.player["hp"], 1000)
        self.assertEqual(inbox_a[-1], inbox_b[-1])
        hp = a.player["hp"]
        ai.tick_world(10.7, [a, b])
        self.assertEqual(a.player["hp"], hp)

    def test_foreign_character_and_ticket_are_rejected(self):
        a, _, _ = self.player(b"Alice")
        b = sessions.connect(lambda data: None)
        with self.assertRaises(ValueError):
            handlers.dispatch("GAME_REPLIES", game_login(build(0x4201, bytes(48))), b)
        reply = handlers.dispatch("LOGIN_REPLIES", token_login(b"Bob"))
        handlers.dispatch("GAME_REPLIES", game_login(reply), b)
        reply = handlers.dispatch("GAME_REPLIES", select(b.uid, struct.unpack_from("<Q", a.record)[0]), b)
        self.assertEqual(HEADER.unpack_from(reply)[2], 0x2001)
        self.assertFalse(b.player["in_world"])

    def test_default_launcher_account_keeps_existing_characters(self):
        original = sessions.connect(lambda data: None)
        login = handlers.dispatch("LOGIN_REPLIES", token_login(b""))
        handlers.dispatch("GAME_REPLIES", game_login(login), original)
        created = handlers.dispatch("GAME_REPLIES", create(original.uid, b"Legacy"), original)
        character_id = struct.unpack_from("<Q", created, 0x20)[0]
        handlers.disconnect(original)
        returning = sessions.connect(lambda data: None)
        login = handlers.dispatch("LOGIN_REPLIES", token_login(b"player"))
        listing = handlers.dispatch("GAME_REPLIES", game_login(login), returning)
        self.assertEqual(returning.account, "player")
        self.assertEqual(struct.unpack_from("<Q", listing, 0x10)[0], character_id)
        self.assertTrue((sessions.STATE_DIR / "characters.json").exists())
        self.assertFalse((sessions.STATE_DIR / "accounts").exists())


class ProtocolTests(unittest.TestCase):
    def test_fragmentation_coalescing_and_obfuscation(self):
        first = bytes(obfuscate(movement(2, 1431, 433), 2))
        second = HEADER.pack(16, MAGIC, 0x401, 2, 0, 2)
        packets, rest = split(first[:7])
        self.assertFalse(packets)
        packets, rest = split(rest + first[7:] + second)
        self.assertEqual(packets, [first, second])
        self.assertFalse(rest)
        self.assertEqual(deobfuscate(first)[4], movement(2, 1431, 433)[16:])

    def test_short_headers_are_rejected(self):
        for size in range(12, 16):
            with self.subTest(size=size), self.assertRaises(ValueError):
                split(struct.pack("<HH", size, MAGIC) + bytes(size - 4))


class SocketTests(StateFixture, unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.setup_state()
        self.writers = []
        self.login = await asyncio.start_server(stub.handler("login", "LOGIN_REPLIES"), "127.0.0.1", 0)
        self.game = await asyncio.start_server(stub.handler("game", "GAME_REPLIES", ticks=True), "127.0.0.1", 0)
        self.web = await asyncio.start_server(stub.handle_http, "127.0.0.1", 0)

    async def asyncTearDown(self):
        for writer in self.writers:
            writer.close()
            await writer.wait_closed()
        for _ in range(20):
            if not sessions.CONNECTED:
                break
            await asyncio.sleep(0.01)
        for server in (self.login, self.game, self.web):
            server.close()
            await server.wait_closed()
        self.cleanup_state()

    async def test_fragmented_world_status_form(self):
        reader, writer = await asyncio.open_connection("127.0.0.1", self.web.sockets[0].getsockname()[1])
        self.writers.append(writer)
        for page in ("WorldChannel.asp", "ChannelList.asp"):
            if page == "ChannelList.asp":
                reader, writer = await asyncio.open_connection("127.0.0.1", self.web.sockets[0].getsockname()[1])
                self.writers.append(writer)
            body = b"world=%37"
            writer.write(f"POST /JoyImpact/{page} HTTP/1.1\r\nContent-Length: {len(body)}\r\n\r\n".encode())
            await writer.drain()
            await asyncio.sleep(0.01)
            writer.write(body[:3])
            await writer.drain()
            await asyncio.sleep(0.01)
            writer.write(body[3:])
            response = await asyncio.wait_for(reader.read(), 2)
            head, content = response.split(b"\r\n\r\n", 1)
            self.assertIn(b"application/json", head)
            row, = json.loads(content)
            self.assertEqual(row["WORLD"], 7)
            self.assertEqual(row["WORLD_STATE"], 1)
            self.assertEqual(row["CH_01"], 0)
            self.assertEqual(row["CH_02"], -1)

    async def packet(self, reader):
        head = await asyncio.wait_for(reader.readexactly(16), 2)
        return head + await asyncio.wait_for(reader.readexactly(HEADER.unpack(head)[0] - 16), 2)

    async def client(self, name):
        r, w = await asyncio.open_connection("127.0.0.1", self.login.sockets[0].getsockname()[1])
        w.write(token_login(name))
        login = await self.packet(r)
        w.close()
        await w.wait_closed()
        r, w = await asyncio.open_connection("127.0.0.1", self.game.sockets[0].getsockname()[1])
        self.writers.append(w)
        w.write(game_login(login))
        reply = await self.packet(r)
        uid = HEADER.unpack_from(reply)[3]
        w.write(create(uid, name))
        reply = await self.packet(r)
        char_id = struct.unpack_from("<Q", reply, 0x20)[0]
        w.write(select(uid, char_id))
        while HEADER.unpack_from(await self.packet(r))[2] != 0x428:
            pass
        return r, w, uid, char_id

    async def test_two_real_sockets_and_malformed_disconnect(self):
        ar, aw, auid, aid = await self.client(b"Alice")
        br, bw, buid, bid = await self.client(b"Bob")
        self.assertEqual(HEADER.unpack_from(await self.packet(ar))[2:4], (0x803, buid))
        self.assertEqual(HEADER.unpack_from(await self.packet(br))[2:4], (0x803, auid))
        packet = obfuscate(movement(buid, 1435, 438), buid)
        bw.write(packet[:7])
        await bw.drain()
        bw.write(packet[7:])
        self.assertEqual(struct.unpack_from("<ff", await self.packet(ar), 0x18), (1435, 438))
        bw.write(obfuscate(build(0x409, bytes(4), extra=buid), buid))
        self.assertEqual(HEADER.unpack_from(await self.packet(br))[2], 0x2001)
        self.assertEqual(HEADER.unpack_from(await self.packet(ar))[2:4], (0x806, buid))
        bw.write(obfuscate(select(buid, bid), buid))
        while HEADER.unpack_from(await self.packet(br))[2] != 0x428:
            pass
        await self.packet(br)
        await self.packet(ar)
        bw.write(struct.pack("<HH", 12, MAGIC) + bytes(8))
        self.assertEqual(HEADER.unpack_from(await self.packet(ar))[2:4], (0x806, buid))
        self.assertEqual(await asyncio.wait_for(br.read(), 2), b"")
        self.assertNotIn(buid, sessions.CONNECTED)
        # The other connection is still usable after the malformed peer exits.
        aw.write(obfuscate(movement(auid, 0, 0, 1), auid))
        self.assertEqual(HEADER.unpack_from(await self.packet(ar))[2:4], (0x416, auid))


if __name__ == "__main__":
    unittest.main()
