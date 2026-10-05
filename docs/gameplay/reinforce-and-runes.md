---
title: "Reinforce, tier-up and rune numbers"
---

# Reinforce, tier-up and rune numbers

The costs, caps and rates for reinforcing gear and runes, taken from the official Warmonger patch notes (2018–19) and the tables in their images. The tables are laid out in our own form. Each fact cites its announcement, using the date tag from [[gameplay/patch-history|Patch notes and other sources]] ("WM 0920 image 3" = the third image in the 20 Sep 2018 notes). Client ids and the client cross-checks come from `data/tables/` (see [[spec/data-tables]]). For how the system works in general, see [[gameplay/items-and-crafting|Items and crafting]].

Tags: **client** (in the client data) · **notes** (the patch-note text) · **image** (a table image in the patch notes) · **guide** · **guess**.

## 1. Rune upgrade materials (final, from 20 Sep 2018)

The 20 Sep 2018 patch replaced the crystal-only rune costs with crystals + Red Passion + one fame material per step. The full table is in an image linked from the notes ([WM 0920][wm0920], linked image `fd91f531…png`). **It matches the client's `JewelSocketMake` table exactly for steps +0→+1 … +8→+9.** *image + client*

Rune tiers, read from the client (`JewelSocketMake` group → `Item_Jewel` names, rune items 7002–7211, 10 levels each) *client*:

- **Tier 1**: Attack, Ability Power, Armor, Magic Resist, Health, Mana, HP Regen, MP Regen, Attack Speed (%).
- **Tier 2**: Armor Penetration, Magic Resist Penetration, Life Steal, Spell Vamp, Movement (%), Cooldown Reduction, Critical Strike (%).
- **Tier 3**: Armor Penetration (%), Magic Resist Penetration (%), PvP Attack, PvP Armor, Critical Strike Damage.

Cost of each step (row = level after the upgrade). "nT Red" is the players' tier name for Red Passion grades: 1T = D Fragment (611), 2T = D Piece (612), 3T = C Fragment (613), 4T = C Piece (614), 5T = B Fragment (615), 6T = B Piece (616). Crystals: Blue 700, Yellow 701, Red 702, Black 703. Fame materials: Shining 854, Mysterious 855, Brilliant 856, Amplifying 857.

| Step | Tier 1 rune | Tier 2 rune | Tier 3 rune |
|---|---|---|---|
| +1 | Blue 10, 1T Red 10 | Yellow 10, 3T Red 10, Mysterious 1 | Red 10, 5T Red 15, Brilliant 1 |
| +2 | Blue 15, 1T Red 15 | Yellow 20, 3T Red 15, Mysterious 1 | Red 20, 5T Red 20, Brilliant 1 |
| +3 | Blue 20, 1T Red 20 | Yellow 40, 3T Red 20, Mysterious 1 | Red 40, 5T Red 30, Brilliant 1 |
| +4 | Blue 30, 1T Red 30 | Yellow 60, 3T Red 30, Mysterious 1 | Red 60, 5T Red 40, Brilliant 1 |
| +5 | Blue 60, 1T Red 40, Shining 1 | Yellow 80, 3T Red 40, Mysterious 1 | Black 10, 6T Red 10, Amplifying 1 |
| +6 | Blue 80, 1T Red 50, Shining 1 | Red 10, 4T Red 10, Brilliant 1 | Black 20, 6T Red 15, Amplifying 1 |
| +7 | Blue 100, 1T Red 60, Shining 1 | Red 20, 4T Red 15, Brilliant 1 | Black 40, 6T Red 20, Amplifying 1 |
| +8 | Yellow 10, 2T Red 10, Shining 1 | Red 40, 4T Red 20, Brilliant 1 | Black 60, 6T Red 30, Amplifying 1 |
| +9 | Yellow 20, 2T Red 15, Shining 1 | Red 60, 4T Red 30, Brilliant 1 | Black 80, 6T Red 40, Amplifying 1 |

Source: [WM 0920][wm0920] linked image; the same patch says success chances for rune upgrades were raised overall. *image + notes*. The client table also has a tenth row per rune (at +9) whose cost is never used, because a +9 rune has no next item *client*.

Earlier screenshots fit this table: the PvP Armor rune (tier 3) +0→+1 cost **30 Red Crystals + 15 Red Passion Fragments [B]** in mid-2018 ([blog runas][blog-runas] image, also in the [noob guide][g-noob]), which is the pre-0920 cost. *image*

## 2. Older rune crystal costs (20 Apr 2018)

Before 0920, rune upgrades cost crystals only (plus gold). [WM 0420][wm0420] images 2 and 3 show the crystal kind and count per rune level ("Sanc" 0–9) and rune tier, before and after that patch. *image*

| Level | T1 before | T1 after | T2 before | T2 after | T3 before | T3 after |
|---|---|---|---|---|---|---|
| 0 | Blue 20 | Blue 20 | Yellow 20 | Yellow 20 | Red 20 | Red 30 |
| 1 | Blue 30 | Blue 30 | Yellow 30 | Yellow 30 | Red 30 | Red 40 |
| 2 | Blue 40 | Blue 40 | Yellow 40 | Yellow 40 | Red 40 | Red 60 |
| 3 | Blue 60 | Blue 60 | Yellow 60 | Yellow 60 | Red 60 | Red 80 |
| 4 | Yellow 20 | Blue 80 | Red 20 | Yellow 80 | Black 20 | Black 20 |
| 5 | Yellow 30 | Blue 100 | Red 30 | Red 20 | Black 30 | Black 30 |
| 6 | Yellow 40 | Blue 120 | Red 40 | Red 30 | Black 40 | Black 40 |
| 7 | Yellow 60 | Yellow 20 | Red 60 | Red 40 | Black 60 | Black 60 |
| 8 | Red 40 | Yellow 30 | Black 40 | Red 60 | Black 80 | Black 80 |
| 9 | Red 60 | Yellow 40 | Black 60 | Red 80 | Black 120 | Black 120 |

The notes only say the patch "adjusted the crystal requirements for reinforcement". The tables have ten rows (0–9), which fits runes (+9 max) and not gear (+15), so they are almost certainly **rune** costs. *guess*. [[gameplay/patch-history]] described them as gear reinforce steps. The 1T crafting screen with "1 Tier / 2 Tier / 3 Tier" filters at the Rune Maker is in [WM 0406][wm0406] image 2. *image*

## 3. Rune caps and success rates

- Launch cap **+5** ([WM 0613][wm0613]); **+9** from [WM 0726][wm0726]. *notes*
- Stat at +9 (patch notes): Armor **45**, Mana Regen **102**, Magic Resist **45** ([WM 0412][wm0412]) then **60** ([WM 0420][wm0420]), Ability Power **60**, Attack **45**. Armor Penetration rune +7/+8/+9: 13/16/19 → **12/14/16**. Magic Resist Penetration rune +7/+8/+9: 13/16/19 → 12/13/15 ([WM 0412][wm0412]) → **11/12/13** ([WM 0420][wm0420]). *notes*
  - The client's server-only `Item_Jewel` has different and mostly higher +9 values (for example Attack 120, Ability Power 96, Armor 60, Magic Resist 36, MP Regen 180), so it is a later rebalance or uses another scale. **Use the client table.** *client*
- Fail chance: until 4 Apr 2018, T1 runes could not fail at all because of a bug. From [WM 0404][wm0404], T1 runes get a "really small" fail chance at +8 and +9 only. *notes*
- [WM 0406][wm0406]: success falls slowly with rune level, and the fall starts earlier for rarer runes: rarity 1 from level 6–7, rarity 2 from 5–6, rarity 3 from 4–5. Each level's drop stays in single-digit percent. *notes* (The real percentages were never published; the client has none, so they are server-side.)
- [WM 0920][wm0920]: rune success chances raised overall. *notes*
- From [WM 1107][wm1107], runes are affected by the **PvP stat correction**, including in War of Warmonger. *notes*
- Failure outcome: the blog says a failed rune upgrade usually loses one level ([blog runas][blog-runas]). The 2018 UI warns "destruction of rune in case of failure" unless a sub-material is used ([noob guide][g-noob]). Before the 0406 fix the notes mention a "failure notifier" when supplements are used in rune reinforcement ([WM 0406][wm0406]). *guide + notes*

## 4. Gear reinforce and tier-up

- **Failure penalty** ([WM 0412][wm0412]): before, a failed upgrade destroyed the item. After, the item **drops one level** (+3 → +2) and the materials are used up. **Reinforcing Adjuvants** (item 1100) prevent the drop. *notes*
- [WM 0406][wm0406]: gear success rates fall slowly with **tier and rarity**, and the fall starts at a lower tier for rarer items. Also fixed a bug that stopped gear upgrading past T2. *notes*
- **Rainbow Reinforcing Stone** (items 641–646, weapon/gear pairs) only works on items of its own rarity, e.g. a Rare weapon needs a Rare Rainbow stone ([WM 0420][wm0420]). *notes + client*
- A notice now appears before combining or reinforcing two items of different rarities ([WM 0621][wm0621]). *notes*
- **Max tier**: T3 at launch ([WM 0613][wm0613]). The data was extended to "Tier 6" during Early Access ([WM 0511][wm0511]), and **T4+15** went live in [WM 0920][wm0920]. T4 needs Brilliant Passion as well as Orange Passion. *notes*. The client's `ItemSancMet` has six material steps per row, which fits six planned tiers. *client*
- Orange/Brilliant Passion per tier, [WM 0920][wm0920] image 2 (row = the tier the item is at; *guess*: these are the tier-up extras on top of the copy item, Blue/Red Passion and gold). *image*

| Item | From | Normal: Material 1 | Normal: Material 2 | Superior: Material 1 | Superior: Material 2 |
|---|---|---|---|---|---|
| Normal weapon | 1T | 1T Orange ×1 | – | 1T Orange ×2 | Shining ×1 |
| Normal weapon | 2T | 2T Orange ×2 | (count 1, no item shown) | 2T Orange ×4 | Shining ×3 |
| Normal weapon | 3T | 3T Orange ×3 | Brilliant ×1 | 3T Orange ×8 | Brilliant ×2 |
| Normal gear | 1T | 1T Orange ×1 | – | 1T Orange ×2 | – |
| Normal gear | 2T | 2T Orange ×2 | – | 2T Orange ×4 | (count 1, no item shown) |
| Normal gear | 3T | 3T Orange ×3 | Brilliant ×1 | 3T Orange ×8 | Brilliant ×1 |
| Named weapon | 1T | 2T Orange ×4 | Shining ×5 | 2T Orange ×8 | Shining ×10 |
| Named weapon | 2T | 3T Orange ×5 | Shining ×10 | 3T Orange ×10 | Shining ×20 |
| Named weapon | 3T | 4T Orange ×6 | Brilliant ×2 | 4T Orange ×12 | Brilliant ×3 |
| Named gear | 1T | 2T Orange ×4 | – | 2T Orange ×8 | – |
| Named gear | 2T | 3T Orange ×5 | – | 3T Orange ×10 | – |
| Named gear | 3T | 4T Orange ×6 | Brilliant ×1 | 4T Orange ×12 | Brilliant ×2 |

"Named" probably means the boss and fame sets (*guess*). Orange Passion grades follow the same 1T–6T naming as Red (Orange items 621–627). The client's `ItemSancMet` rows 101–113 put Brilliant Passion at the third step, which fits this table, but the counts are not laid out the same way. **Read the client table for the real per-level costs.** *client*

- Seen in game (mid-2018, [blog mejorar][blog-mejorar] image, also [definitive guide][g-def]): T1 Magical Crystal Wand +0→+1 = **1,000 gold + 3 Red Passion Fragments [D]**; Attack 80→82, AP 100→108, range 750 unchanged. *image*
- **Crafting with yellow jewels** ([WM 0824][wm0824]): normal gear and T1 runes can be crafted with yellow jewels standing in for missing materials. The jewel cost scales with the missing material count. *notes*
- Crafted gear ([WM 0726][wm0726]) and crafted weapons ([WM 0920][wm0920]) have a small chance to come out **superior**; superior weapons also drop from the Weapon Gacha. *notes*
- Decomposition output raised slightly ([WM 0420][wm0420]); decomposition price lowered ([WM 0328][wm0328]). *notes*

## 5. Medal prices of the fame materials

| Item (client id) | Price | Source |
|---|---|---|
| Brilliant Passion (856) | 5 silver **or** 1 gold medal | [WM 0920][wm0920] *notes*; client buy currency 11 (silver) × 5 *client* |
| Amplifying Passion (857) | 5 silver **or** 3 gold medals | [WM 0920][wm0920] *notes*; client currency 12 × 5 *client* |
| Shining Passion (854) | 2 (client currency 10) | client; the noob guide shows 2 silver |
| Mysterious Passion (855) | 5 (client currency 10) | client; the noob guide shows 5 bronze |
| Costumes (medal price) | gold 50 → **10**, silver 50 → **25** | [WM 0920][wm0920] *notes* |
| Fame shop (Mertris): Gem Stone Blue / Yellow | **10 / 50 fame** (accumulated fame, later called "Contribution") | [WM 0712][wm0712], [WM 0920][wm0920] *notes* |

## 6. Boss and fame set bonuses

[WM 0809][wm0809] (text). Every bonus takes effect at **3 / 5 / 8 pieces** (client `SetBounsItem`, 8 pieces per set). After that patch:

| Set (client set id, items) | 3 pieces | 5 pieces | 8 pieces |
|---|---|---|---|
| Death Head (1, 3001–) | Attack 30 | Attack 40, Crit Damage 20 | Attack 60, Crit Chance 40% |
| Skull (2, 3011–) | Armor 30 | Magic Resist 30 | Armor 50, MR 50 |
| Fisher (3, 3021–) | AP 30 | AP 40, MR Pen 20 | AP 60, MR Pen 30 |
| Komodo (4, 3031–) | Attack 30 | Attack 40, Attack Speed 20 | Attack 60, Life Steal 30% |
| Spector (5, 3041–) | AP 30 | AP 40, CDR 10 | AP 60, CDR 10 |
| Garon (6, 3051–) | Health 300 | Health 400, HP Regen 50 | Health 600, HP Regen 70 |
| Fame Knight (7, 3501–) | Attack 30 | Attack 40, Attack Speed 20 | Attack 60, PvP Attack 30 |
| Fame Warrior (8, 3511–) | Armor 30 | MR 30 | Armor 40, PvP Armor 30 (client also MR 40) |

- Before 0809 each value was 10 lower (e.g. Death Head 20/30/50; Garon Health 200/300/500, Regen 30/50; CDR 5/5). *notes*
- **The client matches the post-0809 values.** *client*. [WM 1018][wm1018] later raised "boss set ability" by 5–10%; the client does not show that rise.
- **Leviathan set** (client set 9, items 3061–), added [WM 0920][wm0920] for Saint/AP builds; its bonuses are only in the client. *notes + client*
- Boss-set essences: Darkness, Wind, Fire, Water, Earth, Light (items 1930–1935). Fort Guardians drop them at a very small chance ([WM 0809][wm0809]), more often from [WM 0920][wm0920]. In the client's `DungeonAdmission` each border dungeon lists one essence among its shown rewards (Chepa → Wind, Skull Temple and Cemetery → Darkness, Tsunami → Water, Swamps → Fire, Tow → Light, Ghost → Earth, Demon Hell → Light, Thorn's Hell → Fire; Dragon Island → all six). *client*

## 7. Consumables touched by patches

| Item (client id) | Value | Source |
|---|---|---|
| Elixir of Health C/B/A/S (736–739) | HP Regen 1/2/3/4 → **2/4/6/8** (max HP +100/200/300/400 in client) | [WM 0124][wm0124] *notes*; client buffs 2109–2112 match *client* |
| Flask of Mana C/B/A/S (740–743) | MP Regen 1/2/3/4 → **2/4/6/8** (max MP +50…+200 in client) | [WM 0124][wm0124]; client buffs 2113–2116 match |
| Tier 1/2/3 Time Energy (689–691) | from 0726: drop rate and EXP **+10/20/30% for 10 min** | [WM 0726][wm0726] image 3; client buffs 2135–2137 match |
| Drop Chance Potion (764) | **+40% drop for 1 h** (WM); in Crush Online +20% for 1 h, 500 jewels or 10 for 4,500 | [WM 0726][wm0726] image 3, [CO 1222][co1222]; client buff 2134 = 40% |
| Tome of Critical [S] / [C] | +20% / +5% crit chance, 5 min | [blog alquimia][blog-alq] image *image* |
| Scrolls of Armor/MR Penetration | removed from the game | [WM 0420][wm0420] *notes* |
| Transformation scroll | 3 → **5 min** | [WM 0503][wm0503] *notes* |
| Mystical Potion → "Blessing of Shaia" (905) | out-of-combat move speed +150, mana +200; only one active, no stacking | [WM 0705][wm0705], [WM 0802][wm0802] *notes* |
| Flare / Ward / Stealth-detecting Ward (2909–2911, Wren) | ward lasts **90 s** | [WM 0809][wm0809] *notes + client* |
| Shaia Stone (1012) | EXP 200,000 → **100,000**; package 1,000 → **2,000 jewels**; not usable in a war | [WM 0615][wm0615], [WM 0621][wm0621]; client value 100,000 *client* |

Buff durations in client `Skill_Buff` (`duration_ms` column) use a 200 ms unit: 3000 = 10 min, 18000 = 1 h, 1500 = 5 min. *client + guess*

[wm0328]: https://steamcommunity.com/games/718790/announcements/detail/2365953485470992984
[wm0404]: https://steamcommunity.com/games/718790/announcements/detail/2394101748794304355
[wm0406]: https://steamcommunity.com/games/718790/announcements/detail/2394101748802019191
[wm0412]: https://steamcommunity.com/games/718790/announcements/detail/2394102381817542359
[wm0420]: https://steamcommunity.com/games/718790/announcements/detail/2758894130315567397
[wm0503]: https://steamcommunity.com/games/718790/announcements/detail/2394104285094559240
[wm0511]: https://steamcommunity.com/games/718790/announcements/detail/3822871998312896536
[wm0613]: https://steamcommunity.com/games/718790/announcements/detail/2431262783620368792
[wm0615]: https://steamcommunity.com/games/718790/announcements/detail/2842216343262999426
[wm0621]: https://steamcommunity.com/games/718790/announcements/detail/2499943313629707204
[wm0705]: https://steamcommunity.com/games/718790/announcements/detail/2499943313680174373
[wm0712]: https://steamcommunity.com/games/718790/announcements/detail/2838841185432966428
[wm0726]: https://steamcommunity.com/games/718790/announcements/detail/2462791699369817744
[wm0802]: https://steamcommunity.com/games/718790/announcements/detail/2451533424634152745
[wm0809]: https://steamcommunity.com/games/718790/announcements/detail/2454911758739952435
[wm0824]: https://steamcommunity.com/games/718790/announcements/detail/2444779293804741322
[wm0920]: https://steamcommunity.com/games/718790/announcements/detail/2450411965551395652
[wm1018]: https://steamcommunity.com/games/718790/announcements/detail/2403126706515770404
[wm1107]: https://steamcommunity.com/games/718790/announcements/detail/2423394805992652770
[wm0124]: https://steamcommunity.com/games/718790/announcements/detail/2425653583381829617
[co1222]: https://steamcommunity.com/games/475630/announcements/detail/4249665521684532740
[blog-runas]: https://guia-warmonger.blogspot.com/p/runas.html
[blog-mejorar]: https://guia-warmonger.blogspot.com/p/mejorar-tu-equipo.html
[blog-alq]: https://guia-warmonger.blogspot.com/p/alquimia.html
[g-noob]: https://steamcommunity.com/sharedfiles/filedetails/?id=1345368744
[g-def]: https://steamcommunity.com/sharedfiles/filedetails/?id=1459948573
