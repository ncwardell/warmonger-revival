"""Portal, map isolation and quest-5 regression tests, without game assets."""
import json
import struct
import unittest
from unittest.mock import patch

import ai
import handlers
import persistence
import quests
import sessions
import travel
import world
from proto import build
from test_multiplayer import movement, ops, request
import test_progress


class TravelTests(test_progress.GameTestCase):
    def setUp(self):
        for module, values in ((world, {"QUEST_TEST": True, "MAP_ID": 89, "SCENE_ID": 89,
                                       "SPAWN_X": 419.0, "SPAWN_Z": 3661.0}),
                               (handlers, {"SPAWN_MAP": 89, "SPAWN_SCENE": 89,
                                           "SPAWN_X": 419.0, "SPAWN_Z": 3661.0})):
            for name, value in values.items():
                p = patch.object(module, name, value)
                p.start()
                self.addCleanup(p.stop)
        super().setUp()
        # Exercise the real table loader, including distinct giver/receiver maps.
        row = [b"0"] * 143
        fields = {0: 5, 3: 4, 5: 5, 7: 89, 10: 201, 14: 88, 17: 198,
                  **{i: 5 for i in range(51, 56)},
                  111: 2, 112: 2750, 117: 1, 119: 402, 120: 1, 123: 4, 124: 500}
        for i, value in fields.items():
            row[i] = str(value).encode()
        with patch.object(quests, "rows", return_value=[row]):
            definitions = quests.definitions()
        p = patch.object(quests, "DEFINITIONS", definitions)
        p.start()
        self.addCleanup(p.stop)

    def portal(self, s, destination):
        packet = request(0x44E, 0x28, s.uid)
        struct.pack_into("<I", packet, 0x14, destination)
        return packet

    def depart(self, s, destination=1202):
        s.quest_flags |= 1 << 4
        _, anchor, _, _ = travel.PORTALS[destination]
        s.player["x"], s.player["z"] = anchor
        return handlers.dispatch("GAME_REPLIES", self.portal(s, destination), s)

    def test_letter_quest_map_handoff_rewards_once_and_reconnects(self):
        s, _, _ = self.player(b"Letter")
        char_id = struct.unpack_from("<Q", s.record)[0]
        self.assertIsNone(test_progress.QuestTests.accept(self, s, 5))
        s.quest_flags = 30
        self.assertTrue(test_progress.QuestTests.accept(self, s, 5))
        self.assertEqual(s.quest_slots[0][2], 2)
        self.assertIsNone(test_progress.QuestTests.turn_in(self, s, 5))
        before = s.experience, s.loot["gold"]
        burst = self.depart(s)
        warp = ops(burst)[0][1]
        self.assertEqual((ops(burst)[0][0], len(warp)), (0x44E, 0x2C))
        self.assertEqual(struct.unpack_from("<HH", warp, 0x10), (88, 88))
        self.assertEqual(warp[0x1E], 255)
        self.assertNotIn(0x2000, [op for op, _ in ops(burst)])
        self.assertEqual((s.experience, s.loot["gold"]), before)
        self.assertIsNone(test_progress.QuestTests.turn_in(self, s, 5))  # still at arrival gate
        handlers.disconnect(s)
        s, _, burst = self.reconnect(b"Letter", char_id)
        self.assertEqual(struct.unpack_from("<hh", ops(burst)[0][1], 0x18), (88, 88))
        self.assertEqual(s.quest_slots[0][2], 2)
        frei = world.UNITS[world.NPC_UID_BASE + 2]
        s.player.update(x=frei.x, z=frei.z)
        self.assertTrue(test_progress.QuestTests.turn_in(self, s, 5))
        self.assertEqual((s.experience, s.loot["gold"]), (before[0] + 2750, before[1] + 500))
        self.assertIn(402, s.inventory["bag"])
        self.assertEqual(s.quest_flags, 62)
        self.assertIsNone(test_progress.QuestTests.turn_in(self, s, 5))
        saved = persistence.read_progress(s.account, s.record)
        self.assertEqual((saved["checkpoint_map"], saved["quest_flags"]), (88, 62))

    def test_portal_rejects_wrong_gate_map_distance_modes_and_dead_player(self):
        s, _, _ = self.player(b"Validation")
        packet = self.portal(s, 1202)
        s.player.update(x=451.64, z=3629.45)
        self.assertIsNone(handlers.dispatch("GAME_REPLIES", packet, s))
        s.quest_flags = 30
        for offset, value in ((0x10, 1), (0x14, 88), (0x14, 1203), (0x14, 9999),
                              (0x18, 1), (0x1C, 0xFFFFFFFF), (0x20, 1), (0x24, 1)):
            bad = bytearray(packet)
            struct.pack_into("<I", bad, offset, value)
            self.assertIsNone(handlers.dispatch("GAME_REPLIES", bad, s), (offset, value))
        for change in ({"alive": False}, {"x": 419, "z": 3661}, {"scene": 90}, {"map": 88}, {"x": float("nan")}):
            original = s.player.copy()
            s.player.update(change)
            self.assertIsNone(handlers.dispatch("GAME_REPLIES", packet, s))
            s.player.update(original)
        with patch.object(world, "QUEST_TEST", False):
            self.assertIsNone(handlers.dispatch("GAME_REPLIES", packet, s))
        self.assertEqual(s.checkpoint_map, 89)
        with self.assertRaises(ValueError):
            handlers.dispatch("GAME_REPLIES", packet[:0x24], s)

    def test_player_visibility_movement_return_trip_and_private_drops(self):
        a, inbox_a, _ = self.player(b"Alice")
        b, inbox_b, _ = self.player(b"Bob")
        self.depart(b)
        c, inbox_c, _ = self.player(b"Carol")
        a.drops[123] = object()
        inbox_a.clear(); inbox_b.clear(); inbox_c.clear()
        burst = self.depart(a)
        self.assertEqual([(op, struct.unpack_from("<H", p, 6)[0]) for op, p in ops(inbox_c[-1])], [(0x806, a.uid)])
        self.assertEqual(ops(inbox_b[-1])[0][0], 0x803)
        spawned = [struct.unpack_from("<H", p, 6)[0] for op, p in ops(burst) if op == 0x803]
        self.assertEqual(set(spawned), {b.uid, world.NPC_UID_BASE + 2})
        self.assertFalse(a.drops)
        inbox_b.clear(); inbox_c.clear()
        handlers.dispatch("GAME_REPLIES", movement(a.uid, 330, 3440), a)
        self.assertEqual(ops(inbox_b[-1])[0][0], 0x416)
        self.assertFalse(inbox_c)
        query = build(0x4CA, struct.pack("<II", c.uid, 0), extra=a.uid)
        self.assertEqual(ops(handlers.dispatch("GAME_REPLIES", query, a))[0][0], 0x806)
        burst = self.depart(a, 1203)
        self.assertEqual(a.player["map"], 89)
        self.assertEqual(ops(inbox_b[-1])[0][0], 0x806)
        self.assertEqual(ops(inbox_c[-1])[0][0], 0x803)
        self.assertEqual(a.checkpoint_map, 89)

    def test_foreign_monster_hits_pushes_queries_and_ai_are_isolated(self):
        a, inbox_a, _ = self.player(b"Away")
        b, inbox_b, _ = self.player(b"Home")
        self.depart(a)
        slime = world.UNITS[world.MONSTER_UID_BASE]
        b.player.update(x=slime.x + 1, z=slime.z)
        original = (slime.hp, slime.x, slime.z)
        with sessions.use(a):
            hit = world._client_hit(slime.uid)
        result = handlers.dispatch("GAME_REPLIES", hit, a)
        self.assertEqual(struct.unpack_from("<Hh", ops(result)[0][1], 0x34), (0, 0))
        push = request(0x412, 0x88, a.uid)
        push[16:0x50] = hit[16:0x50]
        struct.pack_into("<f", push, 0x50, 331)
        struct.pack_into("<f", push, 0x6C, 3441)
        handlers.dispatch("GAME_REPLIES", push, a)
        self.assertEqual((slime.hp, slime.x, slime.z), original)
        query = build(0x4CA, struct.pack("<II", slime.uid, 0), extra=a.uid)
        self.assertEqual(ops(handlers.dispatch("GAME_REPLIES", query, a))[0][0], 0x806)
        inbox_a.clear(); inbox_b.clear()
        ai.tick_world(100, [a, b])
        ai.tick_world(101, [a, b])
        self.assertFalse(inbox_a)
        self.assertTrue(inbox_b)
        slime.hp, slime.dead_until = 0, 0
        inbox_a.clear(); inbox_b.clear()
        ai.tick_world(102, [a, b])
        self.assertFalse(inbox_a)
        self.assertTrue(any(op == 0x804 for data in inbox_b for op, _ in ops(data)))

    def test_npc_on_wrong_map_cannot_complete_or_report_talk(self):
        s, _, _ = self.player(b"WrongNpc")
        s.quest_flags = 30
        test_progress.QuestTests.accept(self, s, 5)
        frei = world.UNITS[world.NPC_UID_BASE + 2]
        # Even matching coordinates do not make a foreign NPC nearby.
        s.player.update(x=frei.x, z=frei.z)
        with sessions.use(s):
            self.assertFalse(quests.near_npc(198))
        self.assertIsNone(test_progress.QuestTests.turn_in(self, s, 5))

    def test_abandon_in_camp_keeps_return_portal_available(self):
        s, _, _ = self.player(b"Abandon")
        s.quest_flags = 30
        test_progress.QuestTests.accept(self, s, 5)
        self.depart(s)
        abandon = build(0x48E, struct.pack("<HhHH", 0, 2, 0, 5), extra=s.uid)
        self.assertTrue(handlers.dispatch("GAME_REPLIES", abandon, s))
        self.assertFalse(any(s.quest_slots[0]))
        self.assertTrue(self.depart(s, 1203))

    def test_failed_warp_save_preserves_player_viewers_and_drops(self):
        a, _, _ = self.player(b"SaveFail")
        _, inbox_b, _ = self.player(b"Observer")
        a.quest_flags = 30
        a.player.update(x=451.64, z=3629.45)
        before = a.player.copy()
        a.drops[123] = object()
        inbox_b.clear()
        with patch.object(persistence, "save_progress", side_effect=OSError("disk full")):
            with self.assertRaises(OSError):
                handlers.dispatch("GAME_REPLIES", self.portal(a, 1202), a)
        self.assertEqual(a.player, before)
        self.assertEqual(a.checkpoint_map, 89)
        self.assertIn(123, a.drops)
        self.assertFalse(inbox_b)

    def test_old_saves_and_route_state(self):
        s, _, _ = self.player(b"OldSave")
        char_id = struct.unpack_from("<Q", s.record)[0]
        handlers.disconnect(s)
        path = persistence.progress_path(s.account, char_id)
        saved = json.loads(path.read_text())
        del saved["checkpoint_map"]
        path.write_text(json.dumps(saved))
        s, _, _ = self.reconnect(b"OldSave", char_id)
        self.assertEqual(s.player["map"], 89)
        packet = handlers.dispatch("GAME_REPLIES", build(0x445, extra=s.uid), s)
        self.assertEqual((len(packet), ops(packet)[0][0]), (0x7DC, 0x446))
        self.assertEqual(struct.unpack_from("<I", packet, 0x10)[0], s.player["team"])


if __name__ == "__main__":
    unittest.main()
