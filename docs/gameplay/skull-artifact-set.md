---
title: "Skull artifact set tooltips (Crush Online, Feb 2017)"
---

# Skull artifact set tooltips (Crush Online, Feb 2017)

In-game item tooltips for the **Skull** set and two common artifacts, taken on 26 Feb 2017 (Crush Online era, before the Warmonger rework) and posted in a bug report about the set's 3-piece bonus. The numbers come from two screenshots. Tags: *image* (read off a screenshot), *guide* (forum text), *client* (decoded client table), *guess*.

Sources:

- Forum thread "Skull artifact set 3 piece bonus" (thread 928, 3 posts by one author, 26–28 Feb 2017, one page) [thread][f-928].
- Screenshot A, Earrings of Life + Helmet of Skull [img A][i-a]. Screenshot B, Old Belt + Belt of Skull [img B][i-b]. A third image ([11FtGrL][i-c]) has been removed from imgur and was not archived.
- Screenshot file names in the chat log are `c20170226_131058` / `c20170226_131100`, so they were taken on 26 Feb 2017 at about 13:11 [img A][i-a].

Related pages: [[gameplay/gear-stats]] (Crush Share sheet, EP and SP model), [[gameplay/reinforce-and-runes]] (Warmonger-era set bonuses), [[gameplay/stat-values]], [[gameplay/patch-history]].

## 1. Tooltip layout (Crush Online artifacts)

Each artifact tooltip shows the following, top to bottom *image* [img A][i-a]:

| Field | Meaning |
|---|---|
| Rank badge (letter on the icon: S or A, in different colours) | Item rank. The two items with a yellow S badge show all 5 steps lit; the two with a green S badge show step 5 greyed out. *image*; that the badge sets the number of usable steps is a *guess*. |
| Stars (1–3) | Star grade. |
| Slot name | Helmet, Belt… (Earrings of Life uses the **Helmet** slot). |
| EP Cost | EP the item takes from the wearer's EP budget. Shown **red** when it does not fit. Belt of Skull's 1,500 is red while the wearer's budget shows 14,100 / 15,000 used. *image*; "red = over budget" is a *guess*. |
| Activated SP | SP cost of **one** step. |
| Bound | The item is bound. |
| [Basic Ability] | Stats while worn. |
| [Activated Ability Every Step] | Stats added by each step, steps 1–5. |
| [Set Item n/8] + [Equip Effect 3/5/8] | Set pieces and bonuses (set items only). |
| [Additional Effect] | Extra stats on this copy (random or reinforced, *guess*). The set items show none. |
| Durability | Current durability of this copy. |

- **Activated SP = EP cost ÷ 5** on all four items (1,800→360, 1,500→300, 2,400→480, 900→180) *image* [img A][i-a], [img B][i-b]. This confirms the ÷5 rule that [[gameplay/gear-stats]] §1 only inferred.
- The action bar lists the 8 artifact slots with the SP price of the **next** step, or **Max** when the item is fully stepped. On the screenshot: slots 1–3 Max, 4 = 360, 5 = 370, 6 = 180, 7 = 420, 8 = 315, with **72 SP** in hand *image* [img A][i-a].
- Items have **5 steps** in Feb 2017. Older forum posts give 3 steps at D rank ([[gameplay/gear-stats]] §1), so the number of steps probably grew with rank. *image + guess*

## 2. Skull set (8 pieces)

Set pieces, in tooltip order, and the matching Warmonger client items *image* [img A][i-a]; ids *client* (`Item_Base`, kind 50–57; `SetBounsItem` set 2):

| # | Crush Online name | Slot (`ItemKind`) | Warmonger client item |
|---|---|---|---|
| 1 | Helmet of Skull | Helmet (50) | 3011 Skull's Helmet |
| 2 | Plate of Skull | Armour (51) | 3012 Skull's Armor |
| 3 | Gloves of Skull | Gloves (52) | 3013 Skull's Gloves |
| 4 | Boots of Skull | Shoes (53) | 3014 Skull's Shoes |
| 5 | Necklace of Skull | Necklace (54) | 3015 Skull's Necklace |
| 6 | Belt of Skull | Belt (55) | 3016 Skull's Belt |
| 7 | Bracelet of Skull | Bracelet (56) | 3017 Skull's Bracelet |
| 8 | Ring of Skull | Ring (57) | 3018 Skull's Ring |

### Set bonuses

| Pieces worn | Crush Online bonus (Feb 2017) | `ItemOption` code | Warmonger client (`SetBounsItem` id 2) |
|---|---|---|---|
| 3 | Attack +30 | 1 | Armor +30 (6) |
| 5 | Attack +20, Attack Speed +8 % | 1, 103 | Magic Resist +30 (7) |
| 8 | Attack +20, Life Steal +8 %, Critical Strike +5 % | 1, 41, 109 | Armor +50, Magic Resist +50 |

- Crush Online numbers *image* [img A][i-a], [img B][i-b]. Option codes *client*: the tooltip's own wording ("AttackSpeed(%)", "Life Steal(%)", "Critical Strike +(%)") matches the `ItemOption` names of codes 103, 41 and 109.
- Whether the tiers add up (Attack +70 at 8 pieces) or replace each other is not shown. *guess: they add up*, as with the client's `SetBounsItem` rows, which give each tier its own entry.
- Warmonger replaced the set with a defensive one (Armor/MR). Right column *client* (`SetBounsItem` row 2); see also [[gameplay/reinforce-and-runes]].

### Bug report: 3-piece bonus far too large

- The forum author says the 3-piece bonus was meant to be roughly **+20 Attack** (the tooltip says +30). On live servers it pushed players to the **1,000 Attack cap** by itself: a Saint with no attack gear reached 1,000 Attack *guide* [thread][f-928] post 1.
- The inspected target in screenshot A (Lv 30 Guardian, nation Erion) shows **Attack 1,000**, AP 58, Armor 531, MR 192, a 969 value under the sword icon (probably attack speed, *guess*) and Move 550 *image* [img A][i-a].
- The author adds that players of every nation were using the bug by 28 Feb 2017 *guide* [thread][f-928] post 3.
- **Server rule:** Attack is capped at **1,000** (the target sits exactly at 1,000). *image + guide*. The replacement server should apply the cap after set bonuses and make sure each set tier is applied **once**.

## 3. Item stats

| Item | Slot | Stars / badge | EP cost | SP per step | Basic | Step 1 | Step 2 | Step 3 | Step 4 | Step 5 | Additional effect | Durability | Src |
|---|---|---|---:|---:|---|---|---|---|---|---|---|---:|---|
| Helmet of Skull | Helmet | ★★★ / green S | 1,800 | 360 | Atk 8, Armor 6 | Atk +10 | Armor +12 | Atk +10 | Armor +12 | Atk +10 (greyed) | – | 43 | [A][i-a] |
| Belt of Skull | Belt | ★★★ / yellow S | 1,500 | 300 | HP 168 | HP +134 | HP +134 | HP +134 | HP +134 | HP +134 | – | 33 | [B][i-b] |
| Earrings of Life | Helmet | ★★★ / yellow S | 2,400 | 480 | AP 5, HP 144 | AP +7 | HP +288 | AP +7 | HP +288 | AP +7 | MR +24, Armor +32 | 70 | [A][i-a] |
| Old Belt | Belt | ★ / green S | 900 | 180 | Armor 4, HP 90 | Armor +5 | HP +180 | Armor +5 | HP +180 | Armor +5 (greyed) | Armor +52 | 73 | [B][i-b] |

All *image*. Steps 3–4 of Belt of Skull are partly hidden behind an on-screen message but read as HP +134, the same as the other steps.

Totals with all 5 steps bought (our arithmetic):

| Item | Full stats (basic + 5 steps) | Full stats with 4 steps (step 5 greyed) |
|---|---|---|
| Helmet of Skull | Atk 38, Armor 30 | Atk 28, Armor 30 |
| Belt of Skull | HP 838 | HP 704 |
| Earrings of Life | AP 26, HP 720 | AP 19, HP 720 |
| Old Belt | Armor 19, HP 450 | Armor 14, HP 450 |

Compared with the Crush Share sheet ([[gameplay/gear-stats]] §2, Nov 2016):

- **Old Belt**: the sheet gives HP 120 / Armor 4 basic and HP 600 / Armor 19 full. Armor matches the tooltip. The tooltip's HP is lower (90 basic, 450 full = 0.75×). *sheet vs image*
- **Earrings of Life**: the sheet gives HP 240 / AP 8 basic and HP 1,200 / AP 41 full. The tooltip is about 0.6× of that (HP 144 / AP 5, full HP 720 / AP 26). *sheet vs image*
- So either HP and AP on artifacts were cut between Nov 2016 and Feb 2017, or the values depend on the copy (rank/stars). *guess*. A replacement server targeting Crush Online should take the Feb 2017 tooltip values as the later ones.
- Neither Skull piece is in the sheet.

## 4. Other numbers on the screenshots

- **EP budget at level 30: 15,000** (artifact panel 14,100 / 15,000) *image* [img A][i-a]. This matches the forum's 15,000-EP builds ([[gameplay/gear-stats]]).
- Map **Long Road**, war in progress: TP 2,324 / 10,000, timer 37:38, three fort icons, Kill / Death / Assist counters *image* [img A][i-a]. See [[gameplay/pvp-and-matches]].
- The viewer is a Lv 30 character with HP 2,988 and MP 1,091. Own stats: Attack 64, AP 390, Armor 429, MR 194, 554 (sword icon), Move 550 *image* [img A][i-a].
- Quest tracker entries: "Battle with Legion members No. 2" (fight alongside 10 legion members, report to **Kelsey**), "Craft Spell Charge [B]" (go to **Farrell**), "[Monthly] Battle Arena" (win 20 arena matches, 6/20 shown), "[Monthly] Kill Player" (240 kills, 80/240 shown) *image* [img A][i-a]. NPCs Kelsey and Farrell are not placed on a map by this source.
- Weapon slots show rank badges **S** and **A** at weapon level **30** *image* [img A][i-a].
- Strategy skill bar: 4 TP skills on Ctrl+1 … Ctrl+4 *image* [img A][i-a].

[f-928]: https://web.archive.org/web/20170302000227/http://www.crush-game.com/forum/threads/skull-artifact-set-3-piece-bonus.928/
[i-a]: https://i.imgur.com/biw1gJI.jpg
[i-b]: https://i.imgur.com/h9eBKr6.jpg
[i-c]: https://i.imgur.com/11FtGrL.jpg
