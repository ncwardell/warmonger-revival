---
title: "Consumables and clickables"
---

# Consumables and clickables

"Clickables" is the players' word for the buff consumables you drag onto the hotbar: **Potions, Scrolls, Tomes, Elixirs and Flasks**, plus a few odd ones (drop and EXP boosters, transform scrolls). This page lists every one the final client knows: its item id, buff id, values, duration, which buffs block each other, the recipe and where the inputs come from. It is the server's reference for using items (opt type 301 = "apply buff") and for Owen's alchemy crafting. Related: [[items-and-crafting]] §4 (guide facts), [[potion-regen]] (how potion ticks paid out), [[stat-values]] (Crush-era buff values), [[npc-locations]] (where the NPCs stand).

Sources and tags:
- *client* = decoded client tables `Item_Base`, `Skill_Buff`, `Item_Make`, `Npc_Carry`, `UnitDB`, `FortMastery` and the English string table (`ItemComment_<id>` tooltips). See [[spec/data-tables]].
- *guide* = fissehans, ["Using the crafting materials to your advantage - the quick buffs"](https://steamcommunity.com/sharedfiles/filedetails/?id=1354427871) (Steam guide, 6 Apr 2018), [buffs guide].
- *image* = screenshots already extracted into [[items-and-crafting]].

> [!warning] The "Overview of clickables" sheet is gone
> The guide's §4 links a Google sheet, ["Overview of clickables"](https://docs.google.com/spreadsheets/d/1YbxB8PadeAi5r0xCW5kde9RrhEViUtw4LxoMDmYhmS0/edit?usp=sharing). On 2026-10-05 every URL form (`/edit`, `/htmlview`, `/pubhtml`, `/export?format=csv`, `/gviz`) returned **HTTP 410 Gone**, and Wayback has no copy (CDX lookup on the id prefix found nothing). So its tab list could not be read. The guide says the sheet was "an easy overview for gathering and crafting" ([buffs guide]). This page rebuilds that overview from the client, which holds the same recipe data and is the final build.

## 1. Rules that apply to every clickable

| Rule | Value | Source |
|---|---|---|
| Duration field unit | `Skill_Buff` duration is in **200 ms ticks**, not ms. Proof: 1500 → the tooltips' "5 minutes"; 18000 → "1 hour" (Drop Chance Potion); 3000 → "10 minutes" (Time energy); 10 → skill tooltips' "2 seconds"; 50 → "10 seconds" | *client* `Skill_Buff` duration column against `ItemComment_704…759`, `ItemComment_764`, `ItemComment_689`, `SkillBuff_10007`, `SkillBuff_10010` |
| Scroll / Tome / Elixir / Flask duration | **5 min** (1500 ticks) for every grade | *client*, matches *image* "Tome of Critical +20% for 5 min" ([[items-and-crafting]]) |
| Potion duration | buff 85 ticks = **17 s**; the tooltip says **16 s** (likely 16 regen ticks after the first) | *client* `Skill_Buff` 2050–2072, `ItemComment_883…897` |
| One active per family | Using another clickable of the same family replaces the old buff and restarts the timer. Potions are not in a family, so HP and MP potions run together | *guide* [buffs guide] §3; *client*: the family is the `Skill_Buff` group column (table below) |
| Craft success | **100%** for every alchemy recipe (powders, potions, scrolls, tomes, elixirs, flasks, dyes) | *client* `Item_Make` success column |
| Craft gold | `Item_Make` column after the output count (README `c23`) is the **gold cost**, before the fort price rate. One screenshot shows Potion of Mana [C] at 1,500 gold against the client's 1,000, the same ×1.5 seen in passion conversion | *client* + *image* ([[items-and-crafting]] §3–4) |
| A and S grades | Need the fort's **A Grade Alchemy** / **S Grade Alchemy** mastery; the tooltips name Owen as the NPC. `FortMastery` rows 22 Alchemy, 23 A grade, 24 S grade, cost column 10,000,000 / 20,000,000 / 50,000,000 (unit unknown) | *client* `FortMastery`, `FortMasteryComment_22/23`; *guide* [definitive guide](https://steamcommunity.com/sharedfiles/filedetails/?id=1459948573) |

Exclusive families (`Skill_Buff` group column) *client*:

| Group id | Family | Members |
|---|---|---|
| 2077 | Scroll (damage) | Warrior, Magician, Armor PNT, Magic PNT |
| 2085 | Tome (utility) | Attack SPD, Cooldown, Patience, Critical |
| 2109 | Elixir (health) | Health, Vampirism, Tenacity |
| 2113 | Flask (mana) | Mana, Devour, Tenacity |
| 2135 | Time energy | Tier 1–3 drop/EXP boosters |
| 2034 | Drop chance | Drop Chance Potion |
| 1150 | Transform | Golem, Demon, Slime, Jack |
| 0 | none (stack freely) | all HP / MP / Omni potions |

> [!note] Scroll or Tome?
> The item names and the buff names disagree. Item 704 is "Scroll of the Warrior" but its buff 2077 is "Tome of the Warrior"; item 712 "Tome of Attack SPD" uses buff 2085 "Scroll of Attack Speed". The crafting UI files recipes by the **item** name: Warrior, Magician and PNT under the Scroll filter (mask bit 2), and Attack SPD, Cooldown, Patience and Critical under Tome (bit 4) *client* `Item_Make` filter column. The guide uses the item names too ([buffs guide] §1). Use the item names. Buff 2129 ("Flask of Tenacity [A]") is a client typo for [C].

## 2. Buff clickables: values per grade

Item ids run C, B, A, S in order; buff ids likewise. Values are what `Skill_Buff` applies (stat codes from `ItemOption`), and they match the English tooltips word for word *client*.

| Family | Item | Item ids C/B/A/S | Buff ids | Effect C / B / A / S |
|---|---|---|---|---|
| Scroll | Scroll of the Warrior | 704–707 | 2077–2080 | Attack +32 / 64 / 96 / **160** |
| Scroll | Scroll of the Magician | 708–711 | 2081–2084 | Ability Power +24 / 48 / 72 / **120** |
| Scroll | Scroll of Armor PNT | 728–731 | 2101–2104 | Armor penetration +2 / 4 / 6 / 8 |
| Scroll | Scroll of Magic PNT | 732–735 | 2105–2108 | Magic penetration +2 / 4 / 6 / 8 |
| Tome | Tome of Attack SPD | 712–715 | 2085–2088 | Attack speed (opt 16) +10 / 20 / 30 / 40 |
| Tome | Tome of Cooldown | 716–719 | 2089–2092 | Cooldown reduction 3 / 6 / 9 / 12% |
| Tome | Tome of Patience | 720–723 | 2093–2096 | Area damage taken −5 / 10 / 15 / 20% (opt 270) |
| Tome | Tome of Critical | 724–727 | 2097–2100 | Crit chance +5 / 10 / 15 / 20% |
| Elixir | Elixir of Health | 736–739 | 2109–2112 | HP regen +2 / 4 / 6 / 8 and max HP +100 / 200 / 300 / 400 |
| Elixir | Elixir of Vampirism | 744–747 | 2117–2120 | Life steal per hit 3 / 6 / 9 / 12 and max HP +100 / 200 / 300 / 400 |
| Elixir | Elixir of Tenacity | 752–755 | 2125–2128 | Life steal per hit 3 / 6 / 9 / 12 and Tenacity +10 / 20 / 30 / 40 |
| Flask | Flask of Mana | 740–743 | 2113–2116 | MP regen +2 / 4 / 6 / 8 and max MP +50 / 100 / 150 / 200 |
| Flask | Flask of Devour | 748–751 | 2121–2124 | Mana steal per hit 2 / 4 / 6 / 8 and max MP +50 / 100 / 150 / 200 |
| Flask | Flask of Tenacity | 756–759 | 2129–2132 | Mana steal per hit 2 / 4 / 6 / 8 and Tenacity +10 / 20 / 30 / 40 |

Steps are linear (C = 1 step, S = 4), except Warrior and Magician, where S is 5 steps. The Crush-era player sheet had different S values for some of these ([[stat-values]] §Sheet3). There is no **D** grade of any buff clickable; D exists only for potions. *client*

Base prices (gold, before the shop rate): C grade 50–70; B 7–11; A 10–15; S 17–24 *client* `Item_Base` buy price. The C-grade price is the shop price at **Lewellyn**; B/A/S are only crafted, so their price is just a sell value.

## 3. Potions and other clickables

HP, MP and Omni potions are covered in full in [[potion-regen]] (ids 883–897, buffs 2050–2072, regen per second × 16 s). Tooltip totals *client* `ItemComment_883…897`:

| Grade | HP potion total | MP potion total | Omni (HP + MP) |
|---|---|---|---|
| D | 400 | 100 | 200 + 50 |
| C | 600 | 150 | 300 + 60 |
| B | 800 | 200 | 400 + 80 |
| A | 1,000 | 250 | 500 + 100 |
| S | 1,200 | 300 | 600 + 120 |

Other clickables *client* (`Item_Base`, `Skill_Buff`, tooltips):

| Item id | Item | Buff | Effect | Duration | Bought with |
|---|---|---|---|---|---|
| 764 | Drop Chance Potion | 2134 | Item drop chance +40% (opt 273) | 1 h (18000) | gold 10 base; in `Npc_Carry` list 401 |
| 689 / 690 / 691 | Tier 1 / 2 / 3 : Time energy | 2135 / 2136 / 2137 | Drop chance **and** EXP +10 / 20 / 30% (opts 273, 271) | 10 min (3000) | currency 10 / 11 / 12, price 1 (medal currencies, *guess*) |
| 880 / 881 / 882 | Potion of Brisk [A] / [B] / [C] | – (opt 503) | +2,000 / 1,000 / 500 Soul Points, usable only during a war | instant | Merits merchant, currency 12 / 11 / 10 |
| 760 / 761 / 762 | Scroll of Transform: Golem / Demon / Slime | 1150 / 1152 / 910 | Turn into unit 613 / 741 / 627 | 5 min | 1,000 gold base (kind 19) |
| 763 | Scroll of Transform: Jack | 1155 | Turn into unit 2000 (pumpkin) | 5 min | 10 gold base (event item, *guess*) |
| 2598 / 2599 | Potion of Health [Quest] / Tome of Cooldown [Quest] | 2062 / 2091 | Same as Health [A] / Cooldown [A] | 17 s / 5 min | quest recipes 749 / 599 |

## 4. Recipes (Owen, Red Union)

Every clickable is made at **Owen**. The fortress Owen (unit 214) has the full list (`Item_Make` category 1). The Training Camp Owen (unit 337, craft list 8 in `UnitDB`) has a shorter list (category 8): **only B-grade** scrolls, tomes, elixirs and flasks, and **only C and B potions** *client*. The Training Camp also has its own Odin (list 6 = copy of category 0) and passion converter (category 7: 220 instead of 200 fragments, a worse rate) *client*.

### 4.1 Buff clickables

Pattern *client*, confirmed for the Warrior scroll by the [buffs guide] §2: **1 container + primary powder + secondary material → 10 clickables**, 100% success.

| Grade | Container | Primary powder | Secondary | Gold (base) | Output | Level? |
|---|---|---|---|---|---|---|
| B | Empty Scroll/Flask [B] ×1 | ×20 | ×1 | 600 | 10 | 24 |
| A | Empty Scroll/Flask [A] ×1 | ×30 | ×2 | 900 | 10 | 25 |
| S | Empty Scroll/Flask [S] ×1 | ×40 | ×3 | 1,200 | 10 | 30 |

"Level?" is `Item_Make` column `c24`, which reads like a required character level (*guess*). There are **no C-grade recipes** for buff clickables. C grade is bought from Lewellyn. *client*

| Item | Recipe rows B/A/S (fort) | Training Camp row (B) | Container | Primary | Secondary |
|---|---|---|---|---|---|
| Scroll of the Warrior | 501–503 | 2301 | Empty Scroll | Garnet powder (803) | Medical herb water (848) |
| Scroll of the Magician | 504–506 | 2302 | Empty Scroll | Bloodstone powder (805) | Clown mushroom (841) |
| Tome of Attack SPD | 507–509 | 2303 | Empty Scroll | Lavender powder (819) | Burned sulphur (842) |
| Tome of Cooldown | 510–512 | 2304 | Empty Scroll | Peppermint powder (821) | Burning water (849) |
| Tome of Patience | 513–515 | 2305 | Empty Scroll | Rosemary powder (823) | Soft leather (840) |
| Tome of Critical | 516–518 | 2306 | Empty Scroll | Red bloodstone powder (813) | Ointment of Spirit (838) |
| **(no result)**, likely Scroll of Armor PNT | 519–521 | 2307 | Empty Scroll | Topaz powder (815) | Burned sulphur (842) |
| **(no result)**, likely Scroll of Magic PNT | 522–524 | 2308 | Empty Scroll | Jasmine powder (825) | Burning water (849) |
| Elixir of Health | 525–527 | 2309 | Empty Flask | Lavender powder (819) | Dried flower (844) |
| Flask of Mana | 528–530 | 2310 | Empty Flask | Peppermint powder (821) | Dried flower (844) |
| Elixir of Vampirism | 531–533 | 2311 | Empty Flask | Rosemary powder (823) | Wild herb (839) |
| Flask of Devour | 534–536 | 2312 | Empty Flask | Jasmine powder (825) | Wild herb (839) |
| Elixir of Tenacity | 537–539 | 2313 | Empty Flask | Borage powder (827) | Refined oil (850) |
| Flask of Tenacity | 540–542 | 2314 | Empty Flask | Spartium powder (829) | Refined oil (850) |

> [!note] Penetration scrolls cannot be crafted in this client
> Rows 519–524 and 2307–2308 have the Scroll filter and full inputs but result item **0**. The only Scrolls without a recipe are Armor PNT (728–731) and Magic PNT (732–735), and the rows sit in the same order, so a server should map Topaz → Armor PNT and Jasmine → Magic PNT (*guess*). Lewellyn does not sell their C grade either. So on the live server these scrolls were probably unobtainable, or came only as drops.

### 4.2 Potions

**100 Empty Flasks of the same grade + Crystals → 100 potions**, 100% success *client* `Item_Make` 701–712 (Training Camp 2501–2506). The *image* in [[items-and-crafting]] (Mana [C]: 100 flasks + 3 Blue → 100, 1,500 gold) matches row 705 at the ×1.5 fort rate.

| Grade | Flask | Crystal | HP potion | MP potion | Omni potion | Gold (base) | Level? |
|---|---|---|---|---|---|---|---|
| C | Empty Flask [C] (834) | Blue (700) | ×2 | ×3 | ×4 | 1,000 | 5 |
| B | Empty Flask [B] (835) | Yellow (701) | ×2 | ×3 | ×4 | 2,000 | 20 |
| A | Empty Flask [A] (836) | Red (702) | ×2 | ×3 | ×4 | 3,000 | 25 |
| S | Empty Flask [S] (837) | Black (703) | ×2 | ×3 | ×4 | 4,000 | 30 |

D potions (883, 884, 893) have no recipe. Wren sells D HP and MP potions (shop 281/287/291) *client*.

### 4.3 Powders

**1 raw gem or herb → 10 powder**, 50 gold base, 100%, at both Owens (rows 601–614 / 2401–2414) *client*; the guide's "10 per craft" agrees ([[items-and-crafting]] §4). The Ore/Plants tabs also make **Worked** gems and **Extracted** herbs (5 raw → 1, 3,000 gold, rows 620–628 / 2415–2428). Extracts plus 5 Worked oil (846) make dyes (rows 751–756, 2601–2620; 5 per craft, 1,000 gold) *client*.

| Raw (id, base gold) | Powder (id) | Used for |
|---|---|---|
| Garnet (802, 20) | 803 | Warrior |
| Blue bloodstone (804, 20) | 805 | Magician |
| Red bloodstone (812, 20) | 813 | Critical |
| Topaz (814, 30) | 815 | (Armor PNT, unmapped) |
| Lavender (818, 30) | 819 | Attack SPD, Elixir of Health |
| Peppermint (820, 30) | 821 | Cooldown, Flask of Mana |
| Rosemary (822, 20) | 823 | Patience, Vampirism |
| Jasmine (824, 20) | 825 | Devour, (Magic PNT, unmapped) |
| Borage (826, 10) | 827 | Elixir of Tenacity |
| Spartium (828, 10) | 829 | Flask of Tenacity |
| Emerald 806, Moonstone 808, Diamond 810, Onyx 816 | 807, 809, 811, 817 | no clickable recipe uses them |

Where the raw gems and herbs drop by dungeon: [[dungeon-drops]].

## 5. Where the inputs come from

| Input | Source | Base price (gold) |
|---|---|---|
| Empty Scroll [C]/[B]/[A]/[S] (830–833) | **Cassia**, material merchant, fortress (shop 286) *client*; "NE in Fortress" *guide* [buffs guide] §2 | 50 / 60 / 80 / 100 |
| Empty Flask [C]/[B]/[A]/[S] (834–837) | Cassia (shop 286) | 80 / 100 / 150 / 200 |
| Worked oil (846, for dyes) | Cassia (shop 286) | 100 |
| Secondaries: Ointment of Spirit 838, Wild herb 839, Soft leather 840, Clown mushroom 841, Burned sulphur 842, Dried flower 844, Medical herb water 848, Burning water 849, Refined oil 850 | Dungeon mob drops, not sold anywhere *guide* [buffs guide] §2, [[maps-and-dungeons]]. In the client they appear only in `Npc_Carry` lists 73–113, which are flagged as non-shop lists (probably drop pools, *guess*); each list leans on one secondary (73 Wild herb, 77 Medical herb water, 81 Soft leather, 85 Dried flower, 89 Refined oil, 93 Ointment of Spirit, 97 Burned sulphur, 101 Burning water, 113 Clown mushroom) | 50 each (sell value) |
| Crystals Blue / Yellow / Red / Black (700–703) | Decomposing Gem Stones 693–696 ([[items-and-crafting]] §3); Athan (unit 207, shop 283) also sells Blue and Yellow *client* | 10 / 20 / 40 / 80 |
| C-grade Scrolls/Tomes/Elixirs/Flasks | **Lewellyn**, scroll merchant (shop 282: fortress unit 205, Training Camp unit 315, unit 316). Sells 704, 708, 712, 716, 720, 724, 736, 740, 744, 748, 752, 756 *client* | 50–70 |

Highland wool 843, Snow flower 845, Frozen tear 847 and Grassland seed 851 are alchemy-type materials that no recipe uses; only `Quest` rows refer to most of them *client*.

NPC positions (Owen 214/337, Cassia 212, Lewellyn 205/315, Wren 204/238): [[npc-locations]].

## 6. Progression hooks

- The monthly **Doping** achievement asks for 200 crafted A–S scrolls, tomes, flasks or elixirs ([[progression-and-economy]]).
- Item 2599 Tome of Cooldown [Quest] and 2598 Potion of Health [Quest] are crafted from quest-only copies of the inputs (2593–2597, bind on pickup), recipes 599 and 749, which name quests 48 "Doping Create" and 47 "Create Potion" in the last column *client*. These are the alchemy tutorial quests.

[buffs guide]: https://steamcommunity.com/sharedfiles/filedetails/?id=1354427871
