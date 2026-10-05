"""Durable progress and tutorial quest regression tests; no game assets required."""
import copy
import json
import os
import pathlib
import struct
import subprocess
import sys
import unittest
from unittest.mock import patch

import handlers
import loot
import persistence
import quests
import sessions
import skills
import world
from proto import build
from test_multiplayer import StateFixture, create, game_login, ops, select, token_login


class GameTestCase(StateFixture, unittest.TestCase):
    def setUp(self):
        self.setup_state()

    def tearDown(self):
        self.cleanup_state()

    def reconnect(self, account, character_id):
        returning = sessions.connect(lambda data: None)
        login = handlers.dispatch("LOGIN_REPLIES", token_login(account))
        listing = handlers.dispatch("GAME_REPLIES", game_login(login), returning)
        burst = handlers.dispatch("GAME_REPLIES", select(returning.uid, character_id), returning)
        return returning, listing, burst

class ProgressTests(GameTestCase):
    def test_level_threshold_boundaries_and_missing_data(self):
        with patch.object(quests, "LEVELS", {0: 0, 1: 100, 2: 300, 3: 600, 4: 1000, 5: 1500}):
            for exp, expected in ((0, 1), (99, 1), (100, 2), (299, 2),
                                  (300, 3), (999, 4), (1000, 5), (99999, 5)):
                with self.subTest(exp=exp):
                    self.assertEqual(quests.level_for_experience(exp), expected)
        with patch.object(quests, "LEVELS", {}):
            self.assertEqual(quests.level_for_experience(99999, 4), 4)

    def test_live_level_repair_keeps_xp_and_survives_reconnect(self):
        with patch.object(quests, "LEVELS", {0: 0, 1: 100, 2: 300, 3: 600, 4: 1000}):
            s, inbox, _ = self.player(b"LevelRepair")
            char_id = struct.unpack_from("<Q", s.record)[0]
            s.experience, s.level, s.quest_flags = 750, 3, 30
            persistence.save_progress(s)
            inventory = copy.deepcopy(s.inventory)
            inbox.clear()
            handlers.tick()
            handlers.tick()
            updates = [p for data in inbox for op, p in ops(data) if op == 0x422]
            self.assertEqual(len(updates), 1)
            self.assertEqual(struct.unpack_from("<BBHI", updates[0], 0x10), (4, 1, 0, 750))
            self.assertEqual((s.level, s.experience, s.quest_flags), (4, 750, 30))
            self.assertEqual(s.inventory, inventory)
            saved = persistence.read_progress(s.account, s.record)
            self.assertEqual((saved["level"], saved["experience"]), (4, 750))
            # An older save must also be repaired on entry, before the next tick.
            s.level = 3
            handlers.disconnect(s)
            returning, _, burst = self.reconnect(b"LevelRepair", char_id)
            self.assertEqual((returning.level, returning.experience), (4, 750))
            update = next(p for op, p in ops(burst) if op == 0x422)
            self.assertEqual(struct.unpack_from("<BBHI", update, 0x10), (4, 0, 0, 750))

    def test_kill_equip_quickbar_survive_new_connection_and_process(self):
        s, _, _ = self.player(b"Alice")
        char_id = struct.unpack_from("<Q", s.record)[0]
        original_record = sessions.character_path(s.account).read_bytes()
        slime = world.UNITS[world.MONSTER_UID_BASE]
        slime.hp = 1
        with sessions.use(s):
            hit = world._client_hit(slime.uid)
        handlers.dispatch("GAME_REPLIES", hit, s)
        handlers.dispatch("GAME_REPLIES", build(0x42A, bytes([3, 0, 1, 0]) + bytes(4), extra=s.uid), s)
        quick = bytes([0] * 8) + struct.pack("<8H", 2550, 0, 0, 0, 0, 0, 0, 0)
        handlers.dispatch("GAME_REPLIES", build(0x494, quick, extra=s.uid), s)
        expected = copy.deepcopy(s.inventory)
        gold = s.loot["gold"]
        self.assertGreater(gold, 0)
        # Read from a fresh interpreter while this connection is still open:
        # progress was saved on the action, not just during orderly logout.
        code = ('import json,sys,sessions,persistence; '
                'r=next(iter(sessions.load_characters(sys.argv[1]).values())); '
                'print(json.dumps(persistence.read_progress(sys.argv[1],r)))')
        result = subprocess.run([sys.executable, "-B", "-c", code, s.account],
                                cwd=pathlib.Path(__file__).parent,
                                env={**os.environ, "WARMONGER_STATE": str(sessions.STATE_DIR)},
                                capture_output=True, text=True, check=True)
        disk = json.loads(result.stdout)
        self.assertEqual(disk["inventory"]["equip"][0], 10011)
        self.assertEqual(disk["gold"], gold)
        handlers.disconnect(s)
        sessions.TICKETS.clear()
        again, listing, burst = self.reconnect(b"Alice", char_id)
        self.assertEqual(again.inventory, expected)
        self.assertEqual(again.loot["gold"], gold)
        self.assertEqual(struct.unpack_from("<H", listing, 0x50)[0], 10011)
        initial = ops(burst)[0][1]
        self.assertEqual(initial[0x51C:0x524] + initial[0x50C:0x51C], quick)
        self.assertEqual(sessions.character_path(s.account).read_bytes(), original_record)

    def test_empty_bag_and_unequipped_weapon_stay_empty(self):
        s, _, _ = self.player(b"Empty")
        char_id = struct.unpack_from("<Q", s.record)[0]
        s.inventory.update(bag=[0] * 70, count=[0] * 70, equip=[0, 0])
        handlers.disconnect(s)
        again, listing, burst = self.reconnect(b"Empty", char_id)
        self.assertFalse(any(again.inventory["bag"]))
        self.assertEqual(again.inventory["equip"], [0, 0])
        self.assertEqual(struct.unpack_from("<H", listing, 0x50)[0], 0)
        self.assertEqual(next(p for op, p in ops(burst) if op == 0x427)[0x18:0x1A], bytes(2))

    def test_character_and_account_isolation(self):
        a, _, _ = self.player(b"Alice")
        first = struct.unpack_from("<Q", a.record)[0]
        a.loot["gold"] = 91
        handlers.dispatch("GAME_REPLIES", build(0x409, bytes(4), extra=a.uid), a)
        packet = create(a.uid, b"Second", 4, 15007)
        struct.pack_into("<I", packet, 0x10, 1)
        made = handlers.dispatch("GAME_REPLIES", packet, a)
        second = struct.unpack_from("<Q", made, 0x20)[0]
        handlers.dispatch("GAME_REPLIES", select(a.uid, second), a)
        self.assertEqual(a.loot["gold"], 0)
        self.assertEqual(a.inventory["equip"][0], 15007)
        handlers.disconnect(a)
        b, _, _ = self.player(b"Bob")
        self.assertEqual(b.loot["gold"], 0)
        again, _, _ = self.reconnect(b"Alice", first)
        self.assertEqual(again.loot["gold"], 91)
        self.assertEqual(again.inventory["equip"][0], 10017)

    def test_failed_atomic_replace_keeps_last_valid_save(self):
        s, _, _ = self.player(b"Atomic")
        path = persistence.progress_path(s.account, struct.unpack_from("<Q", s.record)[0])
        original = path.read_bytes()
        s.loot["gold"] = 123
        replace = pathlib.Path.replace
        def fail_final(source, destination):
            if source.name.endswith(".json.tmp"):
                raise OSError("simulated interrupted checkpoint")
            return replace(source, destination)
        with patch.object(pathlib.Path, "replace", fail_final), self.assertRaises(OSError):
            persistence.save_progress(s)
        self.assertEqual(path.read_bytes(), original)
        self.assertEqual(path.with_suffix(".json.bak").read_bytes(), original)

    def test_corrupt_save_is_preserved_and_rejected(self):
        s, _, _ = self.player(b"Corrupt")
        path = persistence.progress_path(s.account, struct.unpack_from("<Q", s.record)[0])
        path.write_text('{"version": 999}')
        with self.assertRaises(ValueError):
            persistence.restore_progress(s)
        self.assertEqual(path.read_text(), '{"version": 999}')

    def test_disconnect_despawns_even_if_checkpoint_fails(self):
        a, _, _ = self.player(b"Alice")
        b, inbox_b, _ = self.player(b"Bob")
        with patch.object(persistence, "save_progress", side_effect=OSError("disk full")):
            with self.assertRaises(OSError):
                handlers.disconnect(a)
        self.assertNotIn(a.uid, sessions.CONNECTED)
        self.assertFalse(a.player["in_world"])
        self.assertEqual(ops(inbox_b[-1])[0][0], 0x806)
        self.assertTrue(b.player["in_world"])

    def test_all_starting_weapons_round_trip(self):
        for class_id, weapons in skills.CLASS_WEAPONS.items():
            for weapon in weapons:
                with self.subTest(class_id=class_id, weapon=weapon):
                    name = f"W{weapon}".encode()
                    s, _, _ = self.player(name, class_id, weapon)
                    char_id = struct.unpack_from("<Q", s.record)[0]
                    self.assertEqual(len(skills.skills_of(weapon)), 4)
                    handlers.disconnect(s)
                    again, _, _ = self.reconnect(name, char_id)
                    self.assertEqual(again.inventory["equip"][0], weapon)
                    handlers.disconnect(again)


class QuestTests(GameTestCase):
    # Synthetic table rows test the protocol/state machine independently of assets.
    def setUp(self):
        super().setUp()
        self.definitions_patch = patch.object(quests, "DEFINITIONS", {
            1: {"id": 1, "bit": 1, "prerequisite": 0, "exclusion": 0,
                "maps": (handlers.SPAWN_MAP,) * 3, "giver": 201, "receiver": 201,
                "stages": (5,) * 5, "objectives": [(4, 201, 0, 0, 0)] + [(0,) * 5] * 4,
                "rewards": [(2, 37, 0, 0)]},
            2: {"id": 2, "bit": 2, "prerequisite": 1, "exclusion": 0,
                "maps": (handlers.SPAWN_MAP,) * 3, "giver": 201, "receiver": 201,
                "stages": (5,) * 5, "objectives": [(1, 604, 3, 100, 2550)] + [(0,) * 5] * 4,
                "rewards": [(1, 0, 403, 1), (4, 17, 0, 0)]}})
        self.definitions_patch.start()
        self.addCleanup(self.definitions_patch.stop)

    def accept(self, s, qid):
        return handlers.dispatch("GAME_REPLIES", build(0x48E, struct.pack("<HhHH", 0, 1, 0, qid), extra=s.uid), s)

    def turn_in(self, s, qid):
        return handlers.dispatch("GAME_REPLIES", build(0x48F, struct.pack("<HHhH", qid, 0, 0, 0), extra=s.uid), s)

    def test_talk_quest_persists_and_cannot_reward_twice(self):
        s, _, _ = self.player(b"Talk")
        char_id = struct.unpack_from("<Q", s.record)[0]
        self.assertIsNone(self.accept(s, 2))  # prerequisite missing
        self.assertIn(0x491, [op for op, _ in ops(self.accept(s, 1))])
        bad = build(0x492, struct.pack("<HHHhi", 0, 1, 999, 0, 4), extra=s.uid)
        self.assertIsNone(handlers.dispatch("GAME_REPLIES", bad, s))
        good = build(0x492, struct.pack("<HHHhi", 0, 1, 201, 0, 4), extra=s.uid)
        handlers.dispatch("GAME_REPLIES", good, s)
        self.assertEqual(s.quest_slots[0][2], 2)
        handlers.disconnect(s)
        s, _, burst = self.reconnect(b"Talk", char_id)
        self.assertEqual(ops(burst)[0][1][0x526], 2)
        result = self.turn_in(s, 1)
        self.assertIn(0x422, [op for op, _ in ops(result)])
        self.assertEqual(s.experience, 37)
        self.assertEqual(s.quest_flags, 2)
        self.assertIsNone(self.turn_in(s, 1))
        self.assertEqual(s.experience, 37)
        handlers.disconnect(s)
        s, _, _ = self.reconnect(b"Talk", char_id)
        self.assertEqual((s.experience, s.quest_flags), (37, 2))

    def test_kill_collect_turn_in_is_private(self):
        a, _, _ = self.player(b"Alice")
        b, inbox_b, _ = self.player(b"Bob")
        a.quest_flags = 2
        self.accept(a, 2)
        slime = world.UNITS[world.MONSTER_UID_BASE]
        for _ in range(3):
            slime.hp, slime.dead_until = 1, None
            with sessions.use(a):
                hit = world._client_hit(slime.uid)
            handlers.dispatch("GAME_REPLIES", hit, a)
        self.assertEqual(a.quest_slots[0][2], 2)
        self.assertNotIn(0x491, [op for op, _ in ops(inbox_b[-1])])
        gold = a.loot["gold"]
        self.turn_in(a, 2)
        self.assertEqual(a.loot["gold"], gold + 17)
        self.assertIn(403, a.inventory["bag"])
        self.assertNotIn(2550, a.inventory["bag"])
        self.assertEqual(b.loot["gold"], 0)

    def test_full_bag_rejects_reward_without_consuming_quest(self):
        s, _, _ = self.player(b"Full")
        s.quest_flags = 2
        self.accept(s, 2)
        s.inventory["bag"] = [692] * 70
        s.inventory["count"] = [1] * 70
        s.inventory["bag"][0], s.inventory["count"][0] = 2550, 4
        before = copy.deepcopy(s.inventory)
        result = self.turn_in(s, 2)
        self.assertTrue(result)
        self.assertEqual(s.inventory, before)
        self.assertEqual(s.quest_flags, 2)
        self.assertEqual(s.loot["gold"], 0)

    def test_accept_rejects_wrong_map_and_distant_npc(self):
        s, _, _ = self.player(b"Far")
        s.player["map"] = 999
        self.assertIsNone(self.accept(s, 1))
        s.player["map"] = handlers.SPAWN_MAP
        s.player["x"] += 1000
        self.assertIsNone(self.accept(s, 1))

    def test_zero_receiver_talk_quest_finishes_on_captured_report(self):
        quests.DEFINITIONS[1].update(receiver=0, automatic=True)
        s, _, _ = self.player(b"AutoTalk")
        self.accept(s, 1)
        with sessions.use(s):
            self.assertEqual(quests.finish_automatic(), b"")
        # Live 2026-10-05: slot 0, quest 1, Shaia 201, objective 0, talk type 4.
        packet = build(0x492, bytes.fromhex("00000100c900000004000000"), extra=s.uid)
        result = handlers.dispatch("GAME_REPLIES", packet, s)
        completion = ops(result)[-1]
        self.assertEqual((completion[0], completion[1][0x11]), (0x491, 1))
        self.assertFalse(any(s.quest_slots[0]))
        self.assertEqual((s.quest_flags, s.experience), (2, 37))
        self.assertIsNone(handlers.dispatch("GAME_REPLIES", packet, s))
        self.assertEqual(s.experience, 37)

    def test_saved_ready_zero_receiver_quest_recovers_once(self):
        quests.DEFINITIONS[1].update(receiver=0, automatic=True)
        s, _, _ = self.player(b"Ready")
        char_id = struct.unpack_from("<Q", s.record)[0]
        # The old handler left this validated talk objective waiting for a
        # receiver the client does not have. This is the observed slot layout.
        s.quest_slots[0] = bytes.fromhex("010002000000000001000000000001000000000000000000")
        handlers.disconnect(s)
        s, _, _ = self.reconnect(b"Ready", char_id)
        handlers.tick()
        handlers.tick()
        self.assertEqual((s.quest_flags, s.experience), (2, 37))
        self.assertEqual(persistence.read_progress(s.account, s.record)["experience"], 37)

    def test_floyd_handoff_is_accepted_then_completed_at_shaia(self):
        # Synthetic no-objective handoff; the installed-table test below also
        # checks the real quest. Replay the repeatedly rejected live accept.
        row = [b"0"] * 141
        fields = {0: 4, 3: 3, 5: 4, 7: handlers.SPAWN_MAP,
                  10: 239, 17: 201, **{i: 5 for i in range(51, 56)}}
        for index, value in fields.items():
            row[index] = str(value).encode()
        with patch.object(quests, "rows", return_value=[row]):
            definitions = quests.definitions()
        self.assertIn(4, definitions)
        quests.DEFINITIONS.update(definitions)
        s, _, _ = self.player(b"Handoff")
        shaia = next(u for u in world.UNITS.values() if u.unit_id == 201)
        shaia.x = s.player["x"] + 100
        world.UNITS[world.NPC_UID_BASE + 1] = world.Unit(
            world.NPC_UID_BASE + 1, 239, "Floyd", 10, 1000,
            s.player["x"], s.player["z"], world.NPC_TEAM)
        packet = build(0x48E, bytes.fromhex("0000010000000400"), extra=s.uid)
        self.assertIsNone(handlers.dispatch("GAME_REPLIES", packet, s))
        s.quest_flags = 14  # first three quests complete, as in the live save
        result = handlers.dispatch("GAME_REPLIES", packet, s)
        update = ops(result)[-1][1]
        self.assertEqual(struct.unpack_from("<HB", update, 0x44), (4, 2))
        self.assertEqual(update[0x11], 0)  # ready for Shaia, not completed
        self.assertIsNone(handlers.dispatch("GAME_REPLIES", packet, s))
        with sessions.use(s):
            self.assertEqual(quests.finish_automatic(), b"")
        self.assertIsNone(self.turn_in(s, 4))  # standing by Floyd is insufficient
        s.player["x"], s.player["z"] = shaia.x, shaia.z
        self.assertTrue(self.turn_in(s, 4))
        self.assertEqual(s.quest_flags, 30)
        self.assertFalse(any(s.quest_slots[0]))
        self.assertIsNone(self.turn_in(s, 4))
        saved = persistence.read_progress(s.account, s.record)
        self.assertEqual(saved["quest_flags"], 30)


class ClientDataQuestTests(GameTestCase):
    @unittest.skipUnless(all(q in quests.DEFINITIONS for q in (1, 2, 3)), "requires the user's Quest.cdb")
    def test_first_four_quests_using_installed_client_tables(self):
        s, _, _ = self.player(b"DataQuest")
        s.player["map"] = 89
        world.UNITS[world.NPC_UID_BASE + 1] = world.Unit(
            world.NPC_UID_BASE + 1, 239, "Floyd", 10, 1000,
            s.player["x"] + 9, s.player["z"] + 3, world.NPC_TEAM)
        for unit in world.UNITS.values():
            unit.map_id, unit.scene = s.player["map"], s.player["scene"]
        for qid in (1, 2, 3, 4):
            giver = next(u for u in world.UNITS.values() if u.unit_id == quests.DEFINITIONS[qid]["giver"])
            s.player["x"], s.player["z"] = giver.x, giver.z
            self.assertTrue(QuestTests.accept(self, s, qid))
            definition = quests.DEFINITIONS[qid]
            if qid == 4:
                self.assertEqual((definition["giver"], definition["receiver"]), (239, 201))
                self.assertFalse(definition["automatic"])
            for index, (kind, target, count, rate, item) in enumerate(definition["objectives"]):
                if kind == 4:
                    report = build(0x492, struct.pack("<HHHhi", 0, qid, target, index, kind), extra=s.uid)
                    handlers.dispatch("GAME_REPLIES", report, s)
                elif kind == 1:
                    unit = next(u for u in world.UNITS.values() if u.unit_id == target)
                    for _ in range(count):
                        unit.hp, unit.dead_until = 1, None
                        unit.x, unit.z = s.player["x"] + 1, s.player["z"]
                        with sessions.use(s):
                            hit = world._client_hit(unit.uid)
                        handlers.dispatch("GAME_REPLIES", hit, s)
            if definition["automatic"]:
                self.assertTrue(s.quest_flags & (1 << definition["bit"]))
            else:
                self.assertEqual(s.quest_slots[0][2], 2, qid)
                receiver = next(u for u in world.UNITS.values() if u.unit_id == definition["receiver"])
                s.player["x"], s.player["z"] = receiver.x, receiver.z
                self.assertTrue(QuestTests.turn_in(self, s, qid))
            self.assertFalse(any(s.quest_slots[0]))
        self.assertEqual(s.quest_flags & 30, 30)
        self.assertEqual(s.experience, 5720)
        self.assertEqual(s.level, 5)
        self.assertIn(403, s.inventory["bag"])
        self.assertIn(401, s.inventory["bag"])


if __name__ == "__main__":
    unittest.main()
