---
title: "Maps and dungeons"
---

# Maps and dungeons

What the world looked like and what each dungeon held, from player guides (2018) checked against the client tables in `data/tables/` (`FieldNames.tsv`, `Dungeon.tsv`, `DungeonAdmission.tsv`, `Event_Dungeon.tsv`, `UnitDB.tsv`). Guide screenshots were looked at and described here; none are copied. Sources are listed in [[gameplay/README|Gameplay]].

Confidence tags: **client** = in the client data, **guide** = one guide says so, **guides** = several agree, **image** = read off a screenshot, **guess**.

## 1. The world (Gaia)

- The overworld is called **Gaia**. It is one heart-shaped continent cut into named **lands** (the `FieldName_1..86` entries: End of Earth, Shade Wood, Death Valley, Spider Nest, Crater of Abaddon, ...). Each land is owned by a nation (red = Arslan, blue = Erion, green = Armia) or is **grey** (held by monsters / no nation). *image* — world map screenshots in [strategy guide][g-strat] §"So how do i actually farm" and [noob guide][g-noob] §Dungeons of Gaia.
- In spring 2018 Arslan (red) held the west/north-west half, Erion (blue) the east and south, with a grey band between them (Refuge of old dragon, Long Road, Sunstone Hill, Sunstone gateway, Floor of Twilight, Crater of Abaddon ...). The Nation Information panel counted **Arslan 33 lands / 4 forts, Erion 41 lands / 4 forts, Armia 0 / 0**. *image* [strategy guide][g-strat].
- Each nation also has a separate home area outside Gaia: **Training Camp, Training Ground, Castle** (FieldNames 88–98: three copies, one per nation). New characters start in a training zone. *client + guides* [definitive guide][g-def] §First Steps.
- Inside a land the minimap shows the land's level, its owner legion and its **Safety Factor** (seen values 21, 24). *image* [ES upgrade guide][g-es-upg] §Farm Areas.
- Teleporter NPC (Haley) in the fortress offers: **Castle (10,000 gold), Fortress (6,000 gold), Gaia (free), Abyss (free)**. *image* [noob guide][g-noob] §Dungeons of Gaia.
- **Abyss** is a separate farming area. The ES guide says monsters there stop giving loot once you reach **level 30**; Tow monsters are the target at levels 1–25 and Demon Hunters at 26–29. *guide* [ES upgrade guide][g-es-upg] §Red Passion. FieldNames 5 *Fall of Abyss*, 66 *Earth of Abyss*, 75 *Thunderstorm Ruin – Abyss* are Gaia lands, not this area (*guess*).
- Other client fields not covered by any guide: 99–101 *Corpse incineration*, 102/112 *Death's Rest*, 108/109/111 *The land of Greed*, 110 *Prison*, 114 *The way go to devildom*, 118/119 *Sinking Nest*, 120 *Fortress*, 130 *Room of Core*, 131 *Room of the Fortress Keeper*, 140 *Battle Arena*, 141 *Temple*, 142 *[Lv 9] Dragon Island*. *client*

### Where dungeons appear

- A dungeon portal ("Dimension Gate" / "Connected World") sits in lands owned by **your own nation**; each nation's map shows dungeon icons only on its own lands. *image* (the Arslan and Erion map screenshots show icons on red and blue lands respectively) [strategy guide][g-strat], [noob guide][g-noob].
- **Dungeon tier depends on distance from the nation's forts**: a land's dungeon level rises with the number of cells between that land and the nearest fort of its nation, counted over all forts the nation owns. Lands next to a fort get Chepa Village (Lv 1); far lands get Demon Hell / Thorn's Hell (Lv 7–8). Moving or adding a fort therefore reshapes every dungeon on that nation's side. *guides* [Turkish guide][g-tr] §Kale Yönetimi 2.10, [strategy guide][g-strat] ("the farther from the highest-level fort, the higher the tier").
- The same land can carry different tiers for the two nations (example given: a land that is T8 for red can be T2 for blue if a blue fort is close). *guide* [Turkish guide][g-tr] §2.10.
- Each portal is one instance: **max 5 players inside**; with the "Can not enter" option ticked, nobody else can join until the party leaves, so others must use another portal. *guide* [noob guide][g-noob] §Dungeons of Gaia.
- The fortress also has a portal (bottom-right) that sends you to a dungeon matched to your level. *guide* [noob guide][g-noob].

## 2. Border-area (normal/hard) dungeons

The nine "border area" dungeons, in the order of the client's `Dungeon.tsv` rows (127, 121, 128, 122, 123, 125, 124, 126, 129, then 142 ×5).

| Lv | Name (map label) | Field id | Boss (UnitDB id) | Gear tier dropped | Materials named by the guides |
|---|---|---|---|---|---|
| 1 | Chepa Village | 127 | Chepa Sorcerer (870/950) | T1 | Lavender ×4, Peppermint ×4 |
| 1 | Skull Temple (*Temple of the Skull*) | 121 | King Deathhead (672; "Tough" 804) | T1 | Garnet ×4, Red Bloodstone ×4 |
| 2 | Skull Cemetery (*Cemetery of the Skull*) | 128 | Dark Knight Skull (673/809/1205) | T1 | Blue Bloodstone, Topaz, Rosemary, Jasmine ×2 each |
| 3 | Tsunami Lake (*Lake of the tsunami*) | 122 | Tempest Fisher (674/733/1209) | T1 | Topaz, Blue Bloodstone, Rosemary, Jasmine ×2 each |
| 4 | Swamps of Snake Warrior | 123 | Slayer Komodo (675/736/1213) | T1 | Onyx ×4, Borage ×5, Spartium ×3 |
| 5 | Tow Canyon (*Canyon of Tow*) | 125 | War Chief Garon (677/822/1223) | T2 | Emerald ×4, Rosemary ×5, Jasmine ×3 |
| 6 | Ghost Fortress (*Fortress of Ghost*) | 124 | Great Summoner Spectre (676/743/1218) | T2 | Moonstone ×4, Lavender ×3, Peppermint ×5 |
| 7 | Demon Hell (*Hell of Demon*) | 126 | Reviatan Shadow (678/740; "Commander Reviatan" 739) | T2 | Diamond ×4, Spartium ×5, Borage ×3 |
| 8 | Thorn's Hell (*ThornsHell*) | 129 | Akasha (849) | T2 | Emerald ×4, Rosemary ×5, Jasmine ×3 |
| 9 | Dragon Island | 142 | ? | ? | not in any 2018 guide; in client only |

Sources: [dungeons guide][g-dng] (one section per dungeon), repeated in [Turkish guide][g-tr] §Zindanlar; field and unit ids *client*. The older Crush Online guide [Crush basics][g-crush-basics] §Dungeons lists the same nine with the Lv 5/6 names swapped and calls the Lv 7–8 boss "Akasha/Revenant".

Notes per dungeon (from the guide screenshots — boss portraits, minimaps and loot grids, *image*):

- Minimap legend common to all: entry portal in a framed box; a yellow four-arrow marker (probably the boss/exit); green leaf icons = herb gathering points; blue diamond icons = mineral/gem points; pink star icons (from Lv 3 up) = probably elite spawns. Layouts are 3–6 round chambers joined by corridors.
  - Chepa: entry bottom-left, one corridor north splitting west (marker) and north-east; only herb nodes.
  - Skull Temple: S-shaped chain of chambers from the entry (bottom) to the marker (top-left); mineral nodes only.
  - Skull Cemetery: entry bottom-left, loop of chambers, marker on the far east; a large square room at bottom-right.
  - Tsunami Lake: five separate islands; entry bottom-centre, marker top-centre; many pink stars.
  - Swamps: entry top-left, chambers zig-zag to the south-east; marker centre-left; two big blue star icons.
  - Tow Canyon: entry top-left, two columns of chambers; marker top-right; pink stars down the east side.
  - Ghost Fortress: entry top-left, two long lobes; marker centre.
  - Demon Hell: entry top-right; many small islands with pink stars; marker top-left.
  - Thorn's Hell: one large irregular area; entry bottom-centre, marker top-centre.
- Demon Hell's boss is shown as **two** identical figures and Thorn's Hell's as **three** (multi-boss fights). The Remote Bomb TP skill text says that in PvE it "attacks all bosses after attacking the middle boss", which fits. *image* [dungeons guide][g-dng], [strategy guide][g-strat].
- Gear drops are the **named sets** below, and they drop **already reinforced** at a random level: seen from +0 up to **+11** (e.g. "+10 Helmet of Honor", "+11 Guardian Gloves"). Lv 1–4 drop 1-star (T1) items, Lv 5–8 drop 2-star (T2). Sets seen: Life, Honor, Guardian, Spirit, Bandolier, Spell, Mediation, Transcendency, Barrier. *image* [dungeons guide][g-dng].
  - Lv 1 Chepa: Life helmet/armor, Guardian armor/gloves, Spell necklace, Mediation necklace/belt/bracelet/ring (+ Guardian boots per a comment).
  - Lv 1 Skull Temple: Spirit earring/robe/shoes, Bandolier necklace/belt/bracelet, Life bracelet/ring, Spell ring.
  - Lv 2 Cemetery: Honor armor/shoes, Life gloves/shoes/necklace/belt, Transcendency necklace/bracelet, Barrier belt.
  - Lv 3 Tsunami: Guardian helmet/armor, Honor gloves, Transcendency necklace/bracelet/ring, Life bracelet/ring.
  - Lv 4 Swamps: Life helmet/armor, Spirit earring/robe, Honor helmet/armor, Spell necklace/belt, Barrier necklace/belt/bracelet/ring.
  - Lv 5 Tow: Guardian shoes, Spirit shoes, Bandolier belt/bracelet/ring/necklace, Spell bracelet/ring, Life bracelet/ring (T2).
  - Lv 6 Ghost: Guardian helmet/armor, Honor helmet/armor, Life gloves/shoes/necklace/belt, Mediation necklace/belt/ring/bracelet (T2).
  - Lv 7 Demon: Life helmet, Spirit earring/robe, Transcendency belt/necklace/ring/bracelet, Spell belt (T2).
  - Lv 8 Thorn's: Life gloves/necklace/belt, Guardian gloves/shoes, Spirit gloves/shoes, Barrier bracelet/ring (T2).
  - The author notes 2–3 rarer drops per dungeon are missing from the lists. *guide* [dungeons guide][g-dng] §Thanks + comments.
- Decomposing the loot of three (Lv 1–4) or five (Lv 5–8) hard runs gave stacks of Blue/Red Passion fragments (hundreds), Orange Passion, crystals, and alchemy herbs/oils; higher dungeons gave more fragments and Yellow/Red crystals. *image* [dungeons guide][g-dng]. Tags list the alchemy drops: Medical Herb Water, Clown Mushroom, Soft Leather, Ointment of Spirit, Wild Herb, Refined Oil, Dried Flower, Burned Sulphur, Burning Water, Brilliant/Amplifying/Mysterious Core Stone, Blue/Red/Orange Passion fragments.
- Best farming per the ES guide: Red Passion T1 from Lv 1 hard (Chepa/Skull Temple), T2 from Ghost Fortress, T3 from Demon Hell; Blue Passion T2 from Tow Canyon, T3 from Thorn's Hell. *guide* [ES upgrade guide][g-es-upg].

### Entry cost (Dimensional Energy, item 688)

| Dungeon | Normal | Hard (2018 table) | Hard (spring 2018 UI) | Client `DungeonAdmission` normal / hard |
|---|---|---|---|---|
| Chepa Village | 2 | 4 | 4 | 2 / 2 |
| Skull Temple | 3 | 6 | 6 | 3 / 3 |
| Skull Cemetery | 3 | 8 | 3 + 1 bronze Time Energy | 3 / 5 |
| Tsunami Lake | 5 | 10 | 5 + 1 bronze | 5 / 5 |
| Swamps of Snake Warrior | 6 | 13 | 6 + 1 bronze | 6 / 7 |
| Tow Canyon | 7 | 16 | 7 + 2 bronze | 7 / 9 |
| Ghost Fortress | 8 | 20 | 8 + 1 silver (UI showed 8 + 2) | 8 / 12 |
| Demon Hell | 9 | 24 | 9 + 1 silver | 9 / 15 |
| Thorn's Hell | 10 | 29 | 10 + 2 silver | 10 / 19 |
| Dragon Island (142) | – | – | – | 10 / 23 |
| Gollam Hill | 5 | 10 | 10 | 5 / 5 (field 115) |
| Nas Village Entrance | 5 | 10 | 10 | ? |
| Siren Lake | 5 | 10 | 10 | ? |
| Place for Scattered Troops | 5 | 20 | 5 + 3 bronze | ? |
| The Avenue of Spirit | 5 | 20 | 5 + 3 bronze | ? |

Sources: 2018 table *image* in [ES definitive guide][g-def-es] §Dungeons ("how much energy per dungeon"); spring UI *image* [dungeons guide][g-dng] headers and [noob guide][g-noob] portal screenshots; event dungeon costs [ES upgrade guide][g-es-upg] §Dungeon Especiales and [Turkish guide][g-tr]. The ES definitive guide says Time Energy was later dropped from hard-mode entry. The client file is the final build and differs again, so **the server should read the client file** and treat the guide numbers as history.

- Dimensional Energy is sold by **Wren** in every fortress for **5,500 gold** (Item_Base base price 5,000). *guides + image* [definitive guide][g-def] §Dungeons.
- Hard mode: more and stronger monsters, better loot, a boss at the end. Normal mode is easy and has no boss emphasis. *guide* [noob guide][g-noob].
- The strategy guide says "event dungeons always cost 10" energy (an earlier value). *guide* [strategy guide][g-strat].

### Respawn and party rules inside dungeons

- **Solo: monsters do not respawn.** With 2+ party members in a hard dungeon they do. *guides* [ES definitive guide][g-def-es] §Dungeons, [Turkish guide][g-tr] §Parti ganimeti.
- With 3 players: after the room is cleared, the first respawn takes **3–5 minutes**, then **every 1 minute**. *guide* [ES definitive guide][g-def-es].
- Turkish guide: respawn starts after **9 minutes**, faster with more players in the party and in the dungeon. Strategy guide: respawn starts when the timer shows **10:00 remaining**. *guides* (the dungeon has a countdown timer). [Turkish guide][g-tr], [strategy guide][g-strat].
- Loot: early patch (March 2018) — **only the last hitter gets the loot**. Later — **every party member who damaged the monster and is alive gets a drop**, and a party raises drop rate. *guides* [noob guide][g-noob] §Dungeons of Gaia, [Turkish guide][g-tr] §Parti ganimeti, [ES definitive guide][g-def-es].

## 3. Event / special dungeons

These pop up on random lands of either nation on a schedule; the map's Dungeon tab lists the active ones and the land they are on. *guides* [ES upgrade guide][g-es-upg] §Dungeon Especiales, [Turkish guide][g-tr] §Haritalar.

| Name | Client field | Seen on lands | Drops (guides) |
|---|---|---|---|
| The Avenue of Spirit | 113, 116 | Skywing Yard | Orange Passion T1, Yellow + Red crystals, T2 Red/Blue Passion |
| Place for Scattered Troops | 103–107 | End of Earth | Orange Passion T1, Yellow + Blue crystals, T2 Red/Blue, T1 Blue Passion |
| Gollam Hill (*Hill of Gollam*) | 115 | End of Earth | Red Bloodstone, Diamond, Garnet, Topaz |
| Siren Lake | – (134/135?) | Thornsbush peak | Blue Bloodstone, Emerald, Moonstone, Onyx |
| Nas Village (Entrance) | – (134/135?) | Skywing Yard, Sunstone gateway | Blue/Yellow/Red/Black crystals and Faded Passion Pattern (vendor trash worth gold) |

- Nas Village is "the best place for crystals" and for gold (sell the Faded drops). *guides* [strategy guide][g-strat], [Turkish guide][g-tr] §Para Birimleri.
- Client `Event_Dungeon.tsv` has five schedule rows: target fields 132 (*Death's Rest (Passion)*), 115 (Gollam), 133 (*Sinking Nest (Crystal)*) for 180 minutes, and 134/135 for 80 minutes, with hour-like values 12/21/24. *client*. The "(Passion)" and "(Crystal)" suffixes match the Avenue/Scattered Troops (passion) and Nas (crystal) roles, so 132/133 may be later versions of them (*guess*).

## 4. Grey (monster) lands and invasions

- **Grey lands** are neutral lands overrun by monsters. Monster level there sets the farm: **Lv 7 grey land → Red Passion T2/T3, Lv 8 → Blue Passion T2/T3**. *guides* [definitive guide][g-def] §Upgrade your gears.
- A grey zone **resets every 40 minutes unless its boss is killed**; killing the boss ends the grey zone and the land turns to the killer's nation colour. *guide* [ES upgrade guide][g-es-upg] §Farm Areas.
- **Making a land grey**: only on enemy-owned land. Enter the enemy land (starting a war), then leave it — abandoning counts as losing that war and lowers the land's **Safety Factor by about 5**. Repeat (3–5 times) until it reaches **0**; then wait and the land becomes a **Monster Invasion** land. *guides* [ES upgrade guide][g-es-upg], [Turkish guide][g-tr] §Monster Invasion Land.
- Monster invasions show as **purple skulls** on the map; clearing them gives legion fame and **bronze medals**. *guide* [Turkish guide][g-tr] §1.1, §Para Birimleri.
- A quest "Occupation of Monster Invasion Area" has the steps: go to the invasion area → build a tower → build all towers and win. *image* [noob guide][g-noob].
- To conquer an NPC (grey) land: kill its boss **or** reach **10,000 TP**. *guide* [Crush basics][g-crush-basics] §Wars.
- "Holy Things" (a blue triangle icon on a land, e.g. Spirit's Refuge) can be farmed like a T7/T8 grey land while it is grey; it gives red or blue T3 fragments depending on the holy thing. *image + guide* [strategy guide][g-strat]. See also the Holy Gift event in [[gameplay/classes-and-legions|Classes, nations and legions]].

## 5. Fortress layout (town)

All from screenshots (*image*) in [noob guide][g-noob], [strategy guide][g-strat], [definitive guide][g-def], [ES gear guide][g-es-gear], [Crush basics][g-crush-basics]:

- **Wren** (Merchant) — top-right stairs: potions, scrolls (Return, Gaia, Castle), Dimensional Energy, auto-decomposition hammers, Pyrotechnics, Magic Crafting Stone (Crush era).
- **Cassia** (Material Merchant) — north-east: empty containers (Empty Scroll B, flasks).
- **Llewellyn** (Scroll Merchant).
- **Farrell** (Blacksmith) — weapons and Passion conversion; **Odin** (Member of Blue Union) next to him — armour/accessories; **Owen** (Member of Red Union) — alchemy (potions, scrolls, tomes, elixirs, flasks, powders).
- **Alan** (Rune Maker) and **Casta** (Rune Manager) — left of the smiths, by the diamond icon on the minimap.
- **Athan** (Merits Merchant) — medal shop, in the middle of the fortress opposite the auction house.
- **Paraman** (Blacksmith of Legend) — superior "Skeleton King's" weapons.
- Auction House manager **Cathy**, **Mail box**, **Kaysa** (Warehouse Manager), **Haley** (Teleporter), **Hadrian** (fort donations, top-left), **Kesley** (legion quest giver), **Freya** (quest giver).
- The fort minimap shows a castle icon, smith icons, the rune diamond, a red banner and a blue portal at the bottom.

[g-dng]: https://steamcommunity.com/sharedfiles/filedetails/?id=1344219430
[g-noob]: https://steamcommunity.com/sharedfiles/filedetails/?id=1345368744
[g-es-gear]: https://steamcommunity.com/sharedfiles/filedetails/?id=1431688611
[g-es-upg]: https://steamcommunity.com/sharedfiles/filedetails/?id=1431875497
[g-def-es]: https://steamcommunity.com/sharedfiles/filedetails/?id=1459898274
[g-def]: https://steamcommunity.com/sharedfiles/filedetails/?id=1459948573
[g-strat]: https://steamcommunity.com/sharedfiles/filedetails/?id=1460486971
[g-tr]: https://steamcommunity.com/sharedfiles/filedetails/?id=1460533609
[g-crush-basics]: https://steamcommunity.com/sharedfiles/filedetails/?id=780459080
