"""Wiki data and the quest 5 -> 6 -> 7 journey, using isolated character saves."""
import copy
import pathlib
import struct
import tempfile
import unittest
from unittest.mock import patch

import gamedata
import handlers
import maps
import persistence
import quests
import sessions
import travel
import world
from proto import build
from test_multiplayer import ops
from test_progress import GameTestCase, QuestTests
import loot


class WikiDefinitionTests(unittest.TestCase):
    def test_wiki_quests_work_without_extracted_tables(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(
                quests.paths, "SETTING", pathlib.Path(directory)):
            definitions = quests.definitions()
        self.assertLessEqual(set(range(1, 8)), set(definitions))
        self.assertTrue(set(definitions).isdisjoint(quests.SKIPPED))
        self.assertEqual(definitions[7]["bit"], 99)
        self.assertEqual([r[2] for r in definitions[7]["rewards"] if r[:2] == (1, 11)], [400, 408])
        self.assertEqual(definitions[6]["prerequisite"], 5)
        self.assertTrue(definitions[6]["auto_accept"])

    @unittest.skipUnless((quests.paths.SETTING / "Quest.cdb").exists(), "requires owned Quest.cdb")
    def test_existing_quests_match_owned_client_values(self):
        definitions = quests.definitions()
        for row in quests.rows("Quest.cdb"):
            qid = int(row[0])
            if qid not in (1, 2, 3, 4, 5, 7):
                continue
            q = definitions[qid]
            self.assertEqual(q["bit"], int(row[5]))
            self.assertEqual(q["maps"], tuple(map(int, row[7:10])))
            self.assertEqual(q["receiver_maps"], tuple(map(int, row[14:17])))
            self.assertEqual(q["giver"], int(row[10]))
            self.assertEqual(q["receiver"], int(row[17]))
            self.assertEqual(q["stages"], tuple(map(int, row[51:56])))
            # Non-counter report rows can contain irrelevant target fields.
            expected = [tuple(map(int, row[i:i + 5])) for i in range(56, 111, 11)]
            self.assertEqual([o for o in q["objectives"] if o[0]], [o for o in expected if o[0]])
            expected = [tuple(map(int, row[i:i + 4])) for i in range(111, 141, 6)]
            self.assertEqual(q["rewards"], [r for r in expected if r[0]])

    def test_wiki_errors_fail_instead_of_disabling_quests_silently(self):
        read = gamedata.pages
        def changed(kind):
            pages = read(kind)
            if kind == "quests":
                pages = copy.deepcopy(pages)
                pages[7]["rewards"][1]["type"] = 99
            return pages
        with patch.object(gamedata, "pages", side_effect=changed), self.assertRaisesRegex(ValueError, "quest 7: reward"):
            quests.definitions()
        with tempfile.TemporaryDirectory() as directory, \
                patch.object(gamedata, "WIKI", pathlib.Path(directory)), patch.dict(gamedata._PAGES, clear=True):
            with self.assertRaisesRegex(ValueError, "expected one wiki/quests"):
                quests.definitions()

    def test_unsupported_quests_are_skipped_with_a_reason(self):
        definitions = quests.definitions()
        self.assertIn(10, quests.SKIPPED)  # given by the Scout gadget, not an NPC
        self.assertNotIn(10, definitions)
        for reason in quests.SKIPPED.values():
            self.assertTrue(reason)


class FortressQuestTests(GameTestCase):
    """Quests beyond the tutorial, using wiki NPCs placed in the Fortress (120)."""

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

    def at(self, s, unit_id):
        unit = next(u for u in world.UNITS.values() if u.unit_id == unit_id)
        s.player.update(map=unit.map_id, scene=unit.scene, x=unit.x, z=unit.z)

    def talk(self, s, qid, npc):
        report = build(0x492, struct.pack("<HHHhi", 0, qid, npc, 0, 4), extra=s.uid)
        return handlers.dispatch("GAME_REPLIES", report, s)

    def test_level_gate_then_talk_completes_with_rewards(self):
        s, _, _ = self.player(b"Fortress")
        self.at(s, 200)  # Freya gives quest 13 ("level 10+")
        self.assertIsNone(QuestTests.accept(self, s, 13))
        s.level = 10
        self.assertTrue(QuestTests.accept(self, s, 13))
        self.assertIsNone(self.talk(s, 13, 212))  # Cassia is not in reach yet
        self.at(s, 212)
        gold = s.loot["gold"]
        self.assertTrue(self.talk(s, 13, 212))
        self.assertTrue(s.quest_flags & (1 << 12))
        self.assertEqual(s.loot["gold"], gold + 30000)
        with sessions.use(s):
            self.assertEqual(loot.held(834), 100)
        self.assertIsNone(QuestTests.accept(self, s, 13))  # done once

    def test_class_limits_and_class_rewards(self):
        page = copy.deepcopy(gamedata.pages("quests")[13])
        page["classes"] = ["Punisher", "Guardian"]
        page["rewards"].append({"type": 1, "item": 601, "count": 1, "pick": "class", "class": "Saint"})
        page["rewards"].append({"type": 1, "item": 402, "count": 1, "pick": "class", "class": "Punisher"})
        q = quests.compile_quest(13, page)
        self.assertEqual(q["classes"], {4, 5})
        s, _, _ = self.player(b"Saint")  # class 1
        s.level = 10
        self.at(s, 200)
        with patch.dict(quests.DEFINITIONS, {13: q}):
            self.assertIsNone(QuestTests.accept(self, s, 13))
            q["classes"] = None
            self.assertTrue(QuestTests.accept(self, s, 13))
            self.at(s, 212)
            with sessions.use(s):
                held = loot.held(601)
            self.assertTrue(self.talk(s, 13, 212))
            with sessions.use(s):
                self.assertEqual(loot.held(601), held + 16)  # 15 fixed + the Saint's own
                self.assertEqual(loot.held(402), 0)  # the Punisher's reward is withheld
        page["rewards"][-1]["class"] = "Valkyrie"
        with self.assertRaises(quests.Unsupported):
            quests.compile_quest(13, page)

    def test_client_only_objectives_are_never_completed(self):
        self.assertIn("objectives_client", quests.SKIPPED[691])
        s, _, _ = self.player(b"Client")
        s.quest_flags |= 1 << 22
        with sessions.use(s):
            self.assertFalse(quests.start_automatic())


class ChepaQuestTests(GameTestCase):
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
        p = patch.object(quests, "DEFINITIONS", quests.definitions())
        p.start()
        self.addCleanup(p.stop)

    def near(self, s, template):
        unit = next(u for u in world.UNITS.values() if u.unit_id == template)
        s.player.update(x=unit.x, z=unit.z)

    def slot(self, s, qid):
        return next(i for i, r in enumerate(s.quest_slots) if struct.unpack_from("<H", r)[0] == qid)

    def accept(self, s, qid):
        return handlers.dispatch("GAME_REPLIES", build(0x48E, struct.pack("<HhHH", 0, 1, 0, qid), extra=s.uid), s)

    def turn_in(self, s, qid, choice=0, slot=None):
        slot = self.slot(s, qid) if slot is None else slot
        return handlers.dispatch("GAME_REPLIES", build(0x48F, struct.pack("<HHhH", qid, slot, choice, 0), extra=s.uid), s)

    def depart(self, s, destination):
        (anchor, *_), *_ = maps.route(destination, s.player["map"])
        s.player["x"], s.player["z"] = anchor
        return handlers.dispatch("GAME_REPLIES", build(0x44E, struct.pack("<IIIIII", 0, destination, 0, 0, 0, 0), extra=s.uid), s)

    def talk(self, s, qid, npc):
        return handlers.dispatch("GAME_REPLIES", build(0x492, struct.pack("<HHHhi", self.slot(s, qid), qid, npc, 0, 4), extra=s.uid), s)

    def ready_seven(self, account):
        s, inbox, _ = self.player(account)
        s.quest_flags = (1 << 4) | (1 << 5) | (1 << 6)
        self.near(s, 201)
        self.assertTrue(self.accept(s, 7))
        for template in (710, 711):
            officer = next(u for u in world.UNITS.values() if u.unit_id == template)
            officer.hp, officer.dead_until = 1, None
            s.player.update(x=officer.x + 1, z=officer.z)
            with sessions.use(s):
                packet = world._client_hit(officer.uid)
            handlers.dispatch("GAME_REPLIES", packet, s)
        self.assertEqual(s.quest_slots[self.slot(s, 7)][2], 2)
        self.assertTrue(self.depart(s, 1202))
        self.near(s, 198)
        return s, inbox

    def test_letter_followup_and_officers_journey_survives_reconnect(self):
        s, inbox, _ = self.player(b"Journey")
        other, other_inbox, _ = self.player(b"Observer")
        s.quest_flags = 30
        self.near(s, 201)
        self.assertIsNone(self.accept(s, 7))
        self.assertTrue(self.accept(s, 5))
        self.assertTrue(self.depart(s, 1202))
        self.near(s, 198)
        result = self.turn_in(s, 5)
        updates = [p for op, p in ops(result) if op == 0x491]
        self.assertEqual([p[0x11] for p in updates], [1, 0])
        self.assertEqual(struct.unpack_from("<H", updates[1], 0x44)[0], 6)
        self.assertEqual(s.quest_slots[self.slot(s, 6)][2], 0)
        self.assertEqual(s.quest_flags, 62)
        self.assertIsNone(self.talk(s, 6, 201))
        s.player["x"] += 50
        self.assertIsNone(self.talk(s, 6, 198))
        self.near(s, 198)
        self.assertTrue(self.talk(s, 6, 198))
        self.assertEqual(s.quest_flags, 126)
        self.assertTrue(self.depart(s, 1203))
        self.near(s, 201)
        self.assertTrue(self.accept(s, 7))
        # A client report cannot manufacture a server-authoritative kill.
        forged = build(0x492, struct.pack("<HHHhi", self.slot(s, 7), 7, 710, 0, 1), extra=s.uid)
        self.assertIsNone(handlers.dispatch("GAME_REPLIES", forged, s))
        self.assertEqual(s.quest_slots[self.slot(s, 7)][2], 0)
        for template in (710, 711):
            officer = next(u for u in world.UNITS.values() if u.unit_id == template)
            officer.hp, officer.dead_until = 1, None
            s.player.update(x=officer.x + 1, z=officer.z)
            with sessions.use(s):
                packet = world._client_hit(officer.uid)
            handlers.dispatch("GAME_REPLIES", packet, s)
            if template == 710:
                char_id = struct.unpack_from("<Q", s.record)[0]
                handlers.disconnect(s)
                s, _, _ = self.reconnect(b"Journey", char_id)
                self.assertEqual(s.quest_slots[self.slot(s, 7)][8:10], b"\1\0")
        self.assertIsNone(self.turn_in(s, 7))  # wrong map/NPC
        self.assertTrue(self.depart(s, 1202))
        self.near(s, 198)
        before_xp = s.experience
        self.assertTrue(self.turn_in(s, 7, 1))
        self.assertEqual(s.experience, before_xp + 10010)
        self.assertIn(408, s.inventory["bag"])
        self.assertNotIn(400, s.inventory["bag"])
        self.assertEqual(s.inventory["count"][s.inventory["bag"].index(906)], 10)
        saved = persistence.read_progress(s.account, s.record)
        self.assertTrue(saved["quest_flags"] & (1 << 99))
        self.assertIsNone(self.turn_in(s, 7, 1, slot=0))
        self.assertEqual(s.experience, before_xp + 10010)
        self.assertFalse(any(map(any, other.quest_slots)))
        self.assertNotIn(0x491, [op for data in other_inbox for op, _ in ops(data)])

    def test_choice_validation_and_full_bag_are_atomic(self):
        s, _ = self.ready_seven(b"Rewards")
        before = copy.deepcopy(s.inventory), s.experience, s.quest_flags
        for choice in (-1, 2, 32767):
            self.assertIsNone(self.turn_in(s, 7, choice))
            self.assertEqual((s.inventory, s.experience, s.quest_flags), before)
        s.inventory.update(bag=[692] * 70, count=[1] * 70)
        s.inventory["bag"][0] = 0  # room for a ring, but not also the scrolls
        before = copy.deepcopy(s.inventory), s.experience, s.quest_flags
        self.assertIn(0x41B, [op for op, _ in ops(self.turn_in(s, 7, 0))])
        self.assertEqual((s.inventory, s.experience, s.quest_flags), before)
        self.assertEqual(s.quest_slots[self.slot(s, 7)][2], 2)
        s.inventory["bag"][1] = 0
        self.assertTrue(self.turn_in(s, 7, 0))
        self.assertIn(400, s.inventory["bag"])
        self.assertNotIn(408, s.inventory["bag"])

    def test_automatic_assignment_is_gated_and_restores_old_saves(self):
        s, inbox, _ = self.player(b"Auto")
        self.assertIsNone(self.accept(s, 6))
        handlers.tick()
        self.assertFalse(any(map(any, s.quest_slots)))
        s.quest_flags = 62
        handlers.tick()  # wrong map
        self.assertFalse(any(map(any, s.quest_slots)))
        self.depart(s, 1202)
        # Full slots must not be replaced while the automatic quest waits.
        occupied = struct.pack("<H", 7) + bytes(22)
        s.quest_slots = [occupied] * 15
        handlers.tick()
        self.assertEqual(s.quest_slots, [occupied] * 15)
        s.quest_slots = [bytes(24)] * 15
        char_id = struct.unpack_from("<Q", s.record)[0]
        handlers.disconnect(s)
        s, _, _ = self.reconnect(b"Auto", char_id)
        resumed = []
        s.send = resumed.append
        handlers.tick()
        handlers.tick()
        self.assertEqual(s.quest_slots[self.slot(s, 6)][2], 0)
        self.assertEqual([op for data in resumed for op, _ in ops(data)].count(0x491), 1)
        saved = persistence.read_progress(s.account, s.record)
        self.assertEqual(saved["quest_slots"], [r.hex() for r in s.quest_slots])
        # A dead player cannot receive or finish a new objective.
        s.quest_slots = [bytes(24)] * 15
        s.player["alive"] = False
        with sessions.use(s):
            self.assertFalse(quests.start_automatic())


if __name__ == "__main__":
    unittest.main()
