---
title: "Progression and economy"
---

# Progression and economy

From the player guides listed in [[gameplay/README|Gameplay]] and their screenshots, checked against `Item_Base`, `Level_Table`, `ExpandSlot` in `data/tables/`. Tags: **client**, **guide(s)**, **image**, **guess**.

## 1. Levels and experience

- **Max level 30.** *guides* [Turkish guide][g-tr] (hero transformation "only at max level 30"), [ES upgrade guide][g-es-upg] (Abyss loot stops at 30); every endgame screenshot shows level 30. Client `Level_Table` has 30 levels, exp 700 at Lv 1 rising to 42,350,740 at Lv 30 *client*.
- Levelling is quest-driven: yellow "?" quests on the map and quest tracker, with **AutoMove** to walk to the objective. Quests are easy; gear has to be farmed to keep up with quest levels. *guides* [definitive guide][g-def] §First Steps, [strategy guide][g-strat] §Actual progression. A video "First steps lvl 1–17" was linked by the definitive guide.
- Example quest chain names: "Group – Border Area Hard Mode" (go to a dungeon, kill its boss, talk to Freya), "Fortress of Ghost" (kill ghosts, collect sculptures), "Occupation of Monster Invasion Area", "Join & Create Legion", "killed boss of Border area No.3". *image*.
- **Fame** and **Rank**: the character sheet shows Fame "81,500 (107,110)" and Rank "Officer [5]"; client `Level_Table` holds fame thresholds and `FameRank` 20 rank names *client + image*.

## 2. Daily / weekly / monthly quests

*image* [noob guide][g-noob] §Dungeons of Gaia (quest window):

- **Daily** (reset **every day 00:00**, once per day): Monster Hunt (**50 monsters → 100,000 EXP + 1 bronze medal**), Kill Player, War of Warmonger, Win in Battle.
- **Weekly** (reset **Monday 00:00**): Monster Hunt (**250 monsters → 10 Dimensional Energy + 1 silver medal**), Doping (craft consumables), Kill Player, War of Warmonger, Win in Battle.
- **Monthly**: Boss Hunt (100 bosses), Doping (make 200 A–S scrolls/tomes/flasks/elixirs), Kill Player (240). *image* [strategy guide][g-strat].
- A progress bar "x / 137" with milestone chests (gold ×2,500 and ×5,000 icons) runs across all of them.
- These "max-level quests" pay **yellow jewels**. *guide* [Turkish guide][g-tr] §Para Birimleri. Client: `NoticeQuest` (51) / `NoticeQuestReward` (6).

## 3. Currencies

| Currency | How you get it | What it buys | Source |
|---|---|---|---|
| **Gold** | Selling loot to NPCs (Faded Passion from Nas Village is the main gold farm), quests, auction | NPC shops, crafting, reinforcing, rune setting, teleport | [Turkish guide][g-tr], [noob guide][g-noob] |
| **Yellow jewel** | Achievements, max-level daily/weekly/monthly quests, buying from players, gacha; 2,000 from a Discord code | Gacha (1:1 with purple), auction house, bag/warehouse expansion | [Turkish guide][g-tr], [noob guide][g-noob] Step 10, [definitive guide][g-def] §Links |
| **Purple jewel** | **Real money only** | Shop Mall, gacha, extra character slot, bag and warehouse space | [Turkish guide][g-tr] |
| **Medals**: Bronze, Silver, Gold, Mithril | PvP by performance (bronze/silver/gold), monster invasions (bronze), daily/weekly quests; Mithril only from Gold/Mithril reward boxes | Athan's medal shop | [Turkish guide][g-tr], [noob guide][g-noob] |
| **Legion gold / ether / fame** | See [[gameplay/classes-and-legions\|legions]] | Legion levels, wages, Civil War bids, War Nexus | [Turkish guide][g-tr] |
| **TP** | Killing monsters inside a war | Towers, TP skills (war only) | see [[gameplay/pvp-and-matches\|PvP]] |

- Auction house shows each price both in gold and in jewels at **1 jewel = 1,000 gold** (49,999 gold listed as 50 jewels). *image + guide* [noob guide][g-noob] Step 10.
- Client currency codes on `Item_Base` (buy currency column): 2 = gold, 10/11/12 = Tier 1/2/3 Time Energy's currency (bronze/silver/gold medal, *guess* from Athan's shop), 17 = Dimensional Energy's (gold paid without the usual multiplier, see §5) *client + guess*.

## 4. Shops

### Wren (Merchant) — prices in gold, *image* [definitive guide][g-def] §Dungeons, [strategy guide][g-strat]

| Item | Shown price | `Item_Base` buy price | Ratio |
|---|---|---|---|
| Potion of Health [D] / Mana [D] | 79 | 10 (883/884) | 7.9 |
| Scroll: Return / Gaia | 79 | 10 (911/912; or 80 if it is 906/909) | 7.9 (or ~1) |
| Scroll: Castle | 19,800 | 2,500 (908) | 7.92 |
| Dimensional energy | 5,500 | 5,000 (688) | 1.1 |
| Auto decomposition hammer D / C / B / A | 158,400 / 285,120 / 1,346,400 / 3,960,000 | 20,000 / 36,000 / 170,000 / 500,000 | 7.92 |
| Pyrotechnics | 3,960 | 500 (1105) | 7.92 |

So in that fortress (spring 2018) **gold-priced items cost 7.92 × base** and Dimensional Energy **1.1 × base**. 7.92 = 7.2 × 1.1 fits a global multiplier plus a **10% fort tax** (*guess*; the fort tax itself is a *guide* fact). Selling: Faded Passion fragments (base 50) sold for **315 each** and pieces (base 100) for **630** = **6.3 × base** *image* [noob guide][g-noob]. Crush Online's shop (2016) showed potions/scrolls at 96, Castle 24,000, Nexus Return 480, Magic Crafting Stone 48,000 (× 9.6) [Crush stats][g-crush-stats]. The server sends the multipliers in packet 0x452 ([[spec/group01]]).

### Athan (Merits Merchant) — prices in medals, *image* [noob guide][g-noob]

| Item | Price |
|---|---|
| Shining Passion | 2 silver |
| Mysterious Passion | 5 bronze |
| Brilliant Passion | 5 silver |
| Amplifying Passion | 5 bronze |
| [Bronze] / [Silver] / [Gold] / [Mithril] Medal Reward Box | 4 bronze / 3 silver / 2 gold / 1 mithril |
| Random box of dye (×3 kinds) | 3 bronze/silver |
| Tier 1 / 2 / 3 Time Energy | 1 bronze / 1 silver / 1 gold |
| Pyrotechnics | 100 (yellow coin currency) |
| Life saviour | 1,000 (yellow coin currency) |

The weapon materials bought here cost **2 bronze medals** each (ES gear guide) and Time Energy was needed for hard-mode dungeons until it was removed. [ES gear guide][g-es-gear], [ES definitive guide][g-def-es].

### Teleporter (Haley)

Castle **10,000 gold**, Fortress **6,000 gold**, Gaia and Abyss free. *image* [noob guide][g-noob].

## 5. Auction house, mail, storage

- Auction house in every fortress; **5% commission** charged when registering (50,000 → 2,500), listings last **6 days**. *guide + image* [noob guide][g-noob] Step 9.
- Trading between players by **mailbox**. *guide*.
- Storage: personal warehouse (Kaysa), legion warehouse. Bag, warehouse and character slots expand with jewels. *guides*; client `ExpandSlot`.

## 6. Gacha and cash shop

- **Free gacha every 12 hours** ("Daily" card), giving items of **tier 1–3**. The definitive guide says it gives **10 rewards** (equipment, weapons, hero pieces, yellow jewels). *image + guide* [noob guide][g-noob], [definitive guide][g-def] §Tip.
- Paid gacha cards: **Artifact 1,000**, **Weapon 2,000**, **Innocence 2,000** jewels, and a second row of the same three at **10,000** each (multi-draw, *guess*). Payable with purple or yellow jewels. *image + guide* [noob guide][g-noob] Step "Cash-shop gacha", [Turkish guide][g-tr]. "Innocence" pulls hero pieces (`ItemKind` 18 Innocence, 36 Innocence Piece) *client*.
- Gacha gear was described as tiny stat boosts, not pay-to-win. *guide* [noob guide][g-noob].
- **Shop Mall** (purple jewels only): convenience items such as **+5% drop rate** and premium dye. *guide* [Turkish guide][g-tr].
- Client: `PrimiumShop` (57), `Gacha_00..06` pools (no odds — server side), `RandomBox` *client*.

## 7. Achievements

Categories and point totals: **Normal 1,100, War 2,530, Battle 935, Repute 1,100, Creation 1,430, Explore 1,650 — total 8,745**. Each achievement pays yellow jewels (e.g. "Jewel Collector" ×10, "Monsters" ×3, "Bosses" ×3). *image* [noob guide][g-noob] Step 10. Client: `Achievement_Base` (32 rows).

[g-noob]: https://steamcommunity.com/sharedfiles/filedetails/?id=1345368744
[g-es-gear]: https://steamcommunity.com/sharedfiles/filedetails/?id=1431688611
[g-es-upg]: https://steamcommunity.com/sharedfiles/filedetails/?id=1431875497
[g-def-es]: https://steamcommunity.com/sharedfiles/filedetails/?id=1459898274
[g-def]: https://steamcommunity.com/sharedfiles/filedetails/?id=1459948573
[g-strat]: https://steamcommunity.com/sharedfiles/filedetails/?id=1460486971
[g-tr]: https://steamcommunity.com/sharedfiles/filedetails/?id=1460533609
[g-crush-stats]: https://steamcommunity.com/sharedfiles/filedetails/?id=814958862
