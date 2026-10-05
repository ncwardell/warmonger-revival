---
title: "Items, upgrades and crafting"
---

# Items, upgrades and crafting

From the player guides listed in [[gameplay/README|Gameplay]] and their screenshots, checked against `Item_Base`, `Item_Make`, `ItemSancMet` in `data/tables/`. Tags: **client**, **guide(s)**, **image**, **guess**.

## 1. Gear tiers and reinforcement

- Every weapon and gear piece has a **tier (T1–T3, shown as stars)** and a **reinforce level +0…+15** per tier. Max is **T3+15**. *guides* [definitive guide][g-def] §Upgrade your gears, [ES upgrade guide][g-es-upg] §Introducción.
- **Red Passion** reinforces **weapons** (and is used for runes); **Blue Passion** reinforces **gear** (helmet, armour, gloves, shoes, necklace, belt, bracelet, ring). *guides*; item tooltips say "Reinforcement Materials of Weapon / of Item" *image*.
- Passion grades: Fragment and Piece for each of D, C, B, A, S (`Item_Base` 601–640: Blue, Red, Orange, Violet). Players called **D Fragment "T1", D Piece "T2", C Fragment "T3"**, so "Red Passion T6" = B Piece (*guess* by extension). *guide* [strategy guide][g-strat] §farm; *client*.
- Material used per tier: T1 +0→+15 uses the T1 passion, T2 uses T2, T3 uses T3; amounts grow each level. *guides*.
- Reinforcing (+N → +N+1) **never fails** and costs gold + passion. Seen costs (*image*):
  - T1 helmet +0→+1: **1,000 gold + 2 Blue Passion Fragments [D]**; stats Armor 40→44, MR 20→23, +10 HP. [noob guide][g-noob].
  - T1 wand +0→+1: **1,000 gold + 3 Red Passion Fragments [D]**; Attack 80→82, AP 100→108. [definitive guide][g-def].
  - T3 dagger +14→+15: **4,000 gold + 56 Red Passion** (C Fragment icon); Attack 580→590. [strategy guide][g-strat].
  - The server-side table is `ItemSancMet` (gold + 6 steps × 5 {material, count}) *client*.
- **Tier-up** (T1+15 → T2+0, T2+15 → T3+0) needs: the item at +15, **a second identical item also at +15 of the same tier** (consumed; sockets don't matter, keep the one with more sockets), plus Blue + Red + **Orange Passion** and gold. *guides* [definitive guide][g-def], [ES upgrade guide][g-es-upg].
  - Seen: T2+15 "Fame knight Shoes" → T3: **40,000 gold, copy item, 80 Blue, 80 Red, 8 Orange, 8 of a superior material**; tier-up to T3 of superior/fame gear **can fail** and the UI warns "destruction of material in case of failure". Normal tier-ups are described as never failing. *image* [strategy guide][g-strat].
  - Stats after tier-up of that shoe: Armor 110→120, MR 90→100, HP 280 = (no change), Move +26% (no change).
- Weapons at T1 always start from a crafted base; base stats per tier are the same within a weapon family. *guide*.

### Gear stat table at T3+15 (normal sets)

From the [ES gear guide][g-es-gear] §Equipo (*image*, same table re-posted in [Turkish guide][g-tr] §Zırh, which states the values are at **T3+15**). Armor / Magic Resist / Health / Mana / Movement:

| Slot | Guardian | Life | Honor | Spirit |
|---|---|---|---|---|
| Helmet | 240/175/920/75/9% | 100/50/40/805/10% | 240/175/470/85/13% | 195/220/–/540/11% (Spirit Earring) |
| Armor | 287/131/1290/–/9% | 102/51/1415/20/10% | 197/221/1090/–/13% | 152/266/360/470/11% (Robe) |
| Gloves | 240/130/–/510/9% | 100/50/1295/20/20% | 195/175/–/500/13% | 150/220/470/45/11% |
| Shoes | 195/85/255/–/18% | 100/50/40/500/10% | 150/130/280/–/26% | 105/175/290/–/22% |

Accessories (Attack / AP / Armor / MR / Health / HP regen / Mana / MP regen / Attack speed):

| Set | Necklace | Belt | Bracelet | Ring |
|---|---|---|---|---|
| Spell | AP 210, HP 690, HPR 57 | same | same | same |
| Life | Atk 220, HP 1140, HPR 57 | same | same | same |
| Mediation | AP 325, HP 440, MP 460 | AP 280, … | AP 460, … | AP 415, … |
| Transcendency | AP 215, MP 636, MPR 53 | AP 170 | AP 350 | AP 305 |
| Bandolier | Atk 415, HP 740, AS 5% | Atk 460 | Atk 325 | Atk 280 |
| Barrier | Atk 355, HP 965, HPR 10 | Atk 310 | Atk 220 | Atk 175 |
| Courage | Armor 300, MR 150, HP 945 | Armor 345, MR 105, HP 945 | Armor 210, MR 240, MP 610 | Armor 165, MR 285, MP 610 |
| Rise | Armor 155, MR 295, HP 945 | Armor 110, MR 340, HP 945 | Armor 290, MR 160, MP 610 | Armor 245, MR 205, MP 610 |

("same"/"…" = the other columns as in the necklace row.) **Courage and Rise are craft-only** (Odin), never dropped. *guide comments* [dungeons guide][g-dng]. A fuller list was on **warwiki.net** (linked from the definitive guide §Gear List; site gone). Superior/fame items also exist ("Fame knight" set, "Belt of Rise [Equip]").

## 2. Sockets and runes

- Each gear piece has **1–3 rune sockets**, rolled **when the item is created** (crafted or dropped); sockets can never be added later and **carry over on tier-up**. So players re-craft/re-farm until they get 3 sockets before upgrading. One player spent 2,000+ Blue crystals and still got 2 sockets. *guides* [noob guide][g-noob] Step 4, [ES gear guide][g-es-gear] §Ranuras, guide comments.
- Runes are crafted at **Alan (Rune Maker)** and upgraded / set / removed at **Casta (Rune Manager)**. Runes exist in T1–T3 (fort Rune mastery needed for T2/T3). *guides* [definitive guide][g-def] §Runes.
- Each rune type fits only specific sockets, e.g. Attack rune "first/second/third slot: all"; **Life Steal rune: second slot, Armor/Gloves/Bracelet only**; **PvP Armor rune: third slot, Helmet/Armor/Gloves/Shoes**. Runes are bound and **cannot be sold**. Rune stats apply only while the item is equipped. *image* [noob guide][g-noob], [definitive guide][g-def].
- Rune list (T1 tab): Attack, Ability Power, Armor, Magic Resist, Health, Mana, Health Regeneration, Mana Regeneration, Attack Speed(%), Armor Penetration, …; also Life Steal, Cooldown Reduction, PvP Attack, PvP Armor. *image*.
- Crafting an Attack rune (T1): **10 Blue Crystals + 1 red gem material + 7,500 gold → Attack +5**. *image* [noob guide][g-noob].
- **Setting a rune costs 5,000 gold** (and removing one also costs gold). *image + guide* [noob guide][g-noob].
- Rune reinforcement: max **+9**; it **can fail**. Guides say a failed upgrade usually **drops the rune one level**; the UI at +4→+5 says "**destruction of rune in case of failure**" and has an optional **sub-material** slot (protection). Cost seen: +4→+5 Life Steal: **5,000 gold + 20 + 10 materials**. +4 Life Steal = **5% life steal**. PvP Armor rune +0 = PvP Armor 1, +1 = 2; upgrading it used **30 Red Crystals + 15 Red Passion Fragments [B]**. *guides + image* [definitive guide][g-def] §Runes, [noob guide][g-noob].
- Materials: dungeon herbs/minerals, **Crystal: Blue** (T1 runes), **Yellow** (higher), **Red** (top); Red Passion throughout, up to "Red Passion T6" for PvP Attack runes. *guides*.

## 3. Crafting

NPCs: **Farrell** (weapons, passion conversion), **Odin** (gear), **Alan** (runes), **Owen** (alchemy), **Paraman** (superior Skeleton King's weapons). Materials sold by **Cassia**. *guides + image*.

- Crafting window: filters by type/class; shows needed materials (up to 3), gold cost, "Auto Create" (repeat) and, for superior items, "**There is a chance to fail in creating this item**". *image*.
- Normal gear from Odin: **10–30 Blue Crystals per piece** (e.g. Ring of Spell: 10 Blue Crystals + 15,000 gold). *guide + image* [ES gear guide][g-es-gear], [noob guide][g-noob].
- Normal weapons from Farrell: **3 or 5** of a medal-bought material (2 bronze medals each at Athan) + **50 / 70 / 100 crystals** (from decomposing gemstones). *guide* [ES gear guide][g-es-gear] §Armas.
- Superior weapons (Skeleton King's Magic Dagger/Gun/Hammer/Cannon): **150,000 gold + 3 materials**, can fail, need fort Weapon mastery 3. Stats: Attack +140, AP +60, range +200. *image* [strategy guide][g-strat].
- **Passion conversion** at Farrell (both directions). Client `Item_Make` rows 801–827 (*client*), where the column after `c21` is the **output count** and the next one the **gold cost** (the README labels these `c22`/`c23`):
  - up: 200 D Fragment → 100 D Piece (2,500 g); 200 D Piece → 65 C Fragment (5,000 g); 200 C Fragment → 50 C Piece (10,000 g); Orange: 20 D Frag → 10 D Piece (25,000 g); 20 D Piece → 6 C Frag (50,000 g).
  - down: 60 D Piece → 100 D Frag (2,500 g); 40 C Frag → 100 D Piece; 30 C Piece → 100 C Frag; Orange 12 D Piece → 20 D Frag; 8 C Frag → 20 D Piece.
  - Guides confirm "60 × T2 → 100 × T1" and "20 Orange T1 → 10 T2". The in-game screenshots show **7,500 and 37,500 gold**, i.e. the client costs **× 1.5** at that fort. *image* [ES upgrade guide][g-es-upg].
- **Decomposition**: a hammer tool in the inventory. Left-click the hammer, then click the item. Decomposing gear/weapons gives **Orange Passion** (higher tier/star → higher chance) and fragments; decomposing **gemstones** gives crystals. Auto-decomposition modes: **Not use / Gemstone / below 1 tier / below 2 tier / below 3 tier**, with a durability-like gauge (58,966 / 64,000). Auto-decomposition hammers [D]/[C]/[B]/[A] (`Item_Base` 945–949). *guides + image* [strategy guide][g-strat], [noob guide][g-noob] Step 5.1.
- Crush Online (2016) differed: weapons had a weapon level up to 30 fed by **Spell Stones** (ranks D–SS, a stone must be ≥ the weapon's rank), then rank-ups with a red reinforcement stone that cost 1 durability; gear had **EP cost** and **SP** steps; a **Magic Crafting Stone** (48,000 gold) re-rolled an artifact's two random "additional effects". *guides* [Crush basics][g-crush-basics], [Crush stats][g-crush-stats]. Random add-on values per roll: Attack 2/4/8, Armor 4/8/12, Resist 3/6/9, Health 10/20/30, HP regen 4/8/12, Mana 5/10/15, MP regen 2/4/6 (low/med/high); two rolls of the same stat show as one line; each rank-up adds a fixed step (e.g. single Armor +8, Attack +4 per rank). Probably legacy, kept for reference.

## 4. Alchemy (consumables)

- Five consumable families: **Potions, Scrolls, Tomes, Elixirs, Flasks**, each in grades **D, C, B, A, S**. Higher grade = better stats; **S needs fort Alchemy mastery 3** (A needs 2). *guides* [definitive guide][g-def] §Alchemy, [buffs guide][g-buff], client `FortMastery`.
- **One active buff per family** (one Scroll, one Tome, one Elixir, one Flask); using another of the same family replaces it and resets the timer. HP and MP potions can run together. *guide* [buffs guide][g-buff] §3.
- Recipe pattern: **container** (e.g. Empty Scroll B from Cassia) + **primary** (a gem powder made at Owen from dungeon gems, e.g. Garnet → Garnet Powder) + **secondary** (dungeon drop, e.g. Medical Herb Water). Example: Scroll of the Warrior = attack damage, Scroll of the Magician = ability power. *guide* [buffs guide][g-buff] §2.
- Owen's tabs: Potion, Scroll, Tome, Elixir, Flask, Dye; Ore (Worked, Decomposition); Plants (Extraction, Decompose). Powders: Garnet, Bloodstone, Emerald, Moonstone, Diamond, Red Bloodstone, Topaz, Peppermint, … (10 per craft). *image* [noob guide][g-noob].
- Potion of Mana [C]: 100 per craft from 100 empty flasks + 3 Blue crystal-like items + **1,500 gold**; restores **150 MP over 16 s**. *image*.
- Tome of Critical: [S] **+20% crit chance for 5 min**, [C] **+5% for 5 min**. *image* [definitive guide][g-def].
- Health is not regenerated much passively; players must carry potions. *guide* [Crush basics][g-crush-basics].

## 5. Where gear comes from

1. Dungeon drops (sets per dungeon in [[gameplay/maps-and-dungeons|Maps and dungeons]]), already reinforced at a random +level.
2. Crafting (Farrell / Odin / Paraman), sockets rolled at creation.
3. Cash/jewel **gacha** (tier 1–3 items, see [[gameplay/progression-and-economy|Progression and economy]]).
4. Medal-bought materials for weapons and superior sets (Athan).

## 6. Inventory and storage

- Bag tabs ("Item" ×2), equipment column with 2 weapon slots + 10 gear slots, gold and jewel balances shown at the bottom. Warehouse (Kaysa), legion warehouse, mail (items can be traded by mail). Bag/warehouse/character slots expand with jewels. *image + guides*. Client: `ExpandSlot` (18 steps).

[g-dng]: https://steamcommunity.com/sharedfiles/filedetails/?id=1344219430
[g-noob]: https://steamcommunity.com/sharedfiles/filedetails/?id=1345368744
[g-buff]: https://steamcommunity.com/sharedfiles/filedetails/?id=1354427871
[g-es-gear]: https://steamcommunity.com/sharedfiles/filedetails/?id=1431688611
[g-es-upg]: https://steamcommunity.com/sharedfiles/filedetails/?id=1431875497
[g-def]: https://steamcommunity.com/sharedfiles/filedetails/?id=1459948573
[g-strat]: https://steamcommunity.com/sharedfiles/filedetails/?id=1460486971
[g-tr]: https://steamcommunity.com/sharedfiles/filedetails/?id=1460533609
[g-crush-basics]: https://steamcommunity.com/sharedfiles/filedetails/?id=780459080
[g-crush-stats]: https://steamcommunity.com/sharedfiles/filedetails/?id=814958862
