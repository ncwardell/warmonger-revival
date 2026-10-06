"""NPC shop buy, sell and buyback against the committed wiki shop pages."""
import struct
import unittest
from unittest.mock import patch

import handlers
import persistence
import shops
import world
from test_multiplayer import ops, request
import test_progress


class ShopTests(test_progress.GameTestCase):
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

    def npc(self, unit_id):
        return next(u for u in world.UNITS.values() if u.unit_id == unit_id)

    def at_wren(self, gold=1000):
        """A player standing at the Training Camp Wren (238, shop 287)."""
        s, _, burst = self.player(b"Buyer")
        wren = self.npc(238)
        s.player.update(map=88, scene=88, x=wren.x, z=wren.z)
        s.loot["gold"] = gold
        return s, wren, burst

    def buy(self, s, npc, index, code, quantity=1):
        packet = request(0x430, 0x1C, s.uid)
        struct.pack_into("<HHHHI", packet, 0x10, npc.uid, index, quantity, code, 1)
        return handlers.dispatch("GAME_REPLIES", packet, s)

    def sell(self, s, npc, slot, code, quantity=1):
        packet = request(0x431, 0x1C, s.uid)
        packet[0x10], packet[0x11] = 1, slot
        struct.pack_into("<HHHI", packet, 0x12, npc.uid, code, quantity, 1)
        return handlers.dispatch("GAME_REPLIES", packet, s)

    def message(self, reply):
        (op, body), = ops(reply)
        self.assertEqual(op, 0x41B)
        return struct.unpack_from("<I", body, 0x10)[0]

    def test_enter_world_sends_wiki_price_rates(self):
        _, _, burst = self.at_wren()
        rates = [body for op, body in ops(burst) if op == 0x452]
        self.assertEqual([struct.unpack_from("<IIi", b, 0x10) for b in rates], [(720, 700, 0)])

    def test_buy_charges_the_client_price_and_saves(self):
        s, wren, _ = self.at_wren()
        reply = self.buy(s, wren, 0, 883, 3)  # Potion of Health [D]: 79 gold each
        self.assertEqual([op for op, _ in ops(reply)], [0x428, 0x427])
        self.assertEqual(s.loot["gold"], 1000 - 3 * 79)
        slot = s.inventory["bag"].index(883)
        self.assertEqual(s.inventory["count"][slot], 3)
        saved = persistence.read_progress(s.account, s.record)
        self.assertEqual(saved["gold"], 763)

    def test_buy_refusals_leave_gold_and_bag_unchanged(self):
        s, wren, _ = self.at_wren()
        before = (s.loot["gold"], list(s.inventory["bag"]))
        for index, code, quantity in ((0, 884, 1), (4, 883, 1), (0, 883, 0), (0, 883, 100)):
            self.assertIsNone(self.buy(s, wren, index, code, quantity), (index, code, quantity))
        self.assertIsNone(self.buy(s, self.npc(335), 0, 883))  # Odin: a craft list, no shop menu
        for change in ({"x": wren.x + 20}, {"map": 89, "scene": 89}, {"alive": False}):
            original = s.player.copy()
            s.player.update(change)
            self.assertIsNone(self.buy(s, wren, 0, 883), change)
            s.player.update(original)
        self.assertEqual(self.message(self.buy(s, wren, 3, 945)), shops.MSG_NOT_ENOUGH_MONEY)
        s.inventory["bag"][:] = [1] * len(s.inventory["bag"])
        self.assertEqual(self.message(self.buy(s, wren, 0, 883)), 36)
        s.inventory["bag"][:] = before[1]
        self.assertEqual((s.loot["gold"], s.inventory["bag"]), before)

    def test_sell_and_buy_back(self):
        s, wren, _ = self.at_wren()
        self.buy(s, wren, 0, 883, 3)
        slot = s.inventory["bag"].index(883)
        reply = self.sell(s, wren, slot, 883, 2)
        self.assertEqual([op for op, _ in ops(reply)], [0x427, 0x428])
        self.assertEqual((s.loot["gold"], s.inventory["count"][slot]), (763 + 2 * 63, 1))
        self.assertIsNone(self.sell(s, wren, slot, 883, 2))  # only one left
        listing = handlers.dispatch("GAME_REPLIES", request(0x4B7, 0x18, s.uid), s)
        (op, body), = ops(listing)
        self.assertEqual((op, len(body)), (0x4B8, 0x114))
        self.assertEqual(struct.unpack_from("<IHxxB", body, 0x10), (0, 883, 2))
        back = request(0x4B9, 0x28, s.uid)
        body = bytearray(back)
        body[0x18:0x28] = listing[0x14:0x24]
        wrong = bytearray(body)
        wrong[0x1C] = 3
        self.assertIsNone(handlers.dispatch("GAME_REPLIES", bytes(wrong), s))
        reply = handlers.dispatch("GAME_REPLIES", bytes(body), s)
        self.assertEqual([op for op, _ in ops(reply)], [0x428, 0x427, 0x4B8])
        self.assertEqual((s.loot["gold"], s.inventory["count"][slot]), (889 - 2 * 79, 3))
        self.assertFalse(s.buyback)

    def test_sell_refuses_quest_items(self):
        s, wren, _ = self.at_wren()
        s.inventory["bag"][5], s.inventory["count"][5] = 2565, 1  # a Quest-kind item
        self.assertEqual(self.message(self.sell(s, wren, 5, 2565)), shops.MSG_QUEST_ITEM)
        self.assertEqual(s.inventory["bag"][5], 2565)


if __name__ == "__main__":
    unittest.main()
