---
title: "[Lv 8] Thorn's Hell"
type: "dungeon"
id: 129
status: "complete"
missing: []
sources: ["client: SceneList.cdb id 129", "client: DungeonAdmission.cdb field 129", "client: Dungeon.cdb", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 129", "notes: [[gameplay/patch-history]] § Dungeons and world, WM 0402 \"dungeon open time 20 → 15 min\" (also [[gameplay/events-and-schedules]] §9); read as the instance timer because the Crush Online timer counted down from 20:00 ([[gameplay/video-dungeon-run]] §5) — patch notes, interpretation inferred", "notes: [[gameplay/patch-history]] § Dungeons and world, WM 0615 unlock level per border area — patch notes"]
field: 129
max_users: 5
level: 8
entry_cost:
  - {"mode": "normal", "item": 688, "count": 10}
  - {"mode": "hard", "item": 688, "count": 19}
event: false
shown_rewards: [602, 603, 693, 694, 695, 1932, 2708, 2758]
c17: 2009
image: "UI/FieldImages/8.png"
dungeon_slots:
  - {"group": 0, "slot": 10}
  - {"group": 1, "slot": 10}
  - {"group": 2, "slot": 10}
boss: [849]
gear_tier: "T2"
gathering: [806, 822, 824]
time_limit_s: 900
unlock_level: 27
---
<!-- generated:start -->
<!-- generated-keys: title=0bf214 type=3e3f38 id=8b7471 sources=f70cd9 field=8b7471 max_users=ac3478 level=fe5dbb entry_cost=3f4f04 event=7cb6ef shown_rewards=342901 c17=7263d6 image=6fb519 dungeon_slots=9a35e1 boss=f97f7d gear_tier=7b5982 gathering=0cbe10 time_limit_s=2be88c -->
|  |  |
|---|---|
|  | ![(Lv 8) Thorn's Hell](../assets/dungeons/129.png) |
| **Field** | [[wiki/fields/129-lv-8-thorn-s-hell\|(Lv 8) Thorn's Hell (field 129)]] |
| **Level** | 8 |
| **Gear tier dropped** | T2 (guides) |
| **Max players** | 5 (SceneList; guides: max 5 per portal) |
| **Event dungeon** | no |
| **Banner** | `UI/FieldImages/8.png` |
| **c17 (unknown)** | 2009 |

### Entry cost

| mode | ticket | count |
|---|---|---|
| normal | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 10 |
| hard | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 19 |

`DungeonAdmission` has two {item, count} pairs; reading them as normal / hard mode follows the guides' tables (*inferred*). The 2018 guide numbers differ: [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost]].

### Boss

- [[wiki/monsters/849-akasha|Akasha]] (main)

### Rewards shown on the entry panel

What the dungeon window advertises; not a drop table and no rates (*client*). Drop rates go on the monster pages.

[[wiki/items/602-blue-passion-piece-d|Blue Passion Piece (D)]], [[wiki/items/603-blue-passion-fragments-c|Blue Passion Fragments (C)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/694-gem-stone-yellow|Gem Stone : Yellow]], [[wiki/items/695-gem-stone-red|Gem Stone : Red]], [[wiki/items/1932-essence-of-fire|Essence of Fire]], [[wiki/items/2708-horn-of-akasha|Horn of Akasha]], [[wiki/items/2758-the-arch-devil-akasha-s-sealed-weapon|The Arch devil Akasha's Sealed Weapon]]

### Gathering

Nodes placed by `Trigger.cdb` give: [[wiki/items/806-emerald|Emerald]], [[wiki/items/822-rosemary|Rosemary]], [[wiki/items/824-jasmine|Jasmine]]. Positions on the [[wiki/fields/129-lv-8-thorn-s-hell|field page]].

### Dungeon groups

`Dungeon.cdb` has 3 groups of 15 slots. A slot probably is the tier step a land gets from its distance to the nation's nearest fort (*guess*, from [[gameplay/maps-and-dungeons#Where dungeons appear|Maps and dungeons § Where dungeons appear]]).

Here: group 0 slot 10, group 1 slot 10, group 2 slot 10

### Rules from the guides

Respawn (solo: none; party: about every minute), party loot and the hard-mode rules are in [[gameplay/maps-and-dungeons#Respawn and party rules inside dungeons|Maps and dungeons § Respawn and party rules]]. Materials per run: [[gameplay/dungeon-drops|Dungeon drops]].
<!-- generated:end -->

## Notes

- Boss: [[wiki/monsters/849-akasha|Akasha 849]] (guides + client ids, [[gameplay/maps-and-dungeons]] §2 and [[gameplay/dungeon-drops]] §1).
- Crush Online name: Thorns Hell (Lv 8), boss "Akasha/Reviathan" (sheet) or "Akasha/Revenant" (Crush basics guide) (sheet / forum, [[gameplay/dungeon-drops]] §1, [[gameplay/crush-mechanics]] §9).
- Materials named by the 2018 dungeons guide: Emerald ×4, Rosemary ×5 and Jasmine ×3 (guide, [[gameplay/maps-and-dungeons]] §2). The gathering list in the front matter comes from the client's `Trigger` table.
- Gear: drops T2 named-set gear, already reinforced at a random level (seen +0 to +11). Sets seen in this dungeon: Life gloves/necklace/belt, Guardian gloves/shoes, Spirit gloves/shoes, Barrier bracelet/ring. The guide's author says 2–3 rarer drops are missing from the list (image + guide, [[gameplay/maps-and-dungeons]] §2).
- Map (from the guide's minimap): one large irregular area; entry bottom-centre, marker top-centre (image, [[gameplay/maps-and-dungeons]] §2).
- Unlocks at character level 27 (Warmonger patch 0615, [[gameplay/patch-history]] § Dungeons and world).
- The Spanish upgrade guide names it the best Blue Passion T3 farm (guide, [[gameplay/maps-and-dungeons]] §2).
- The guide shows this boss as **three** figures (a multi-boss fight) (image, [[gameplay/maps-and-dungeons]] §2). A Lords of the Land screenshot shows this dungeon on the minimap during a grey-land war (image, [[gameplay/lords-of-the-land]] §5).

## Behaviour

- Hard mode has more and stronger monsters, better loot and a boss at the end; normal mode is easy (guide, [[gameplay/maps-and-dungeons]] §2).
- Respawn: solo, monsters do not respawn; with 2+ party members in hard mode they do. Guides give the first refill after 3–5 min (3 players) then about every minute, or after 9 min / when the timer shows 10:00 (guides, [[gameplay/maps-and-dungeons]] §2). Warmonger patch 0404: with more than 2 users monsters respawn after 5 min (notes, [[gameplay/patch-history]] § Dungeons and world).
- Time limit: Warmonger patch 0402 cut the dungeon open time from 20 to 15 min (notes, [[gameplay/patch-history]]); in Crush Online, when the timer ran out nothing dropped and the party was teleported out (staff, [[gameplay/crush-mechanics]] §9).
- Loot: in March 2018 only the last hitter got loot; later every living party member who damaged the monster got a drop, and a party raised the drop rate (guides, [[gameplay/maps-and-dungeons]] §2). Crush Online scaled monster count and loot with party size; a solo player got about 1/5 of a full group's loot (player, [[gameplay/crush-mechanics]] §9).
- Max 5 players per portal instance; with "Can not enter" ticked nobody else can join (guide, [[gameplay/maps-and-dungeons]] §1).
- The dungeon tier a land shows depends on its distance from the nation's main fort (guides, [[gameplay/maps-and-dungeons]] §1; [[gameplay/patch-history]] WM 0726).
- In Crush Online (patch 2016-12-15) the dungeon elites dropped a scroll that summoned one extra boss, once per boss (staff, [[gameplay/crush-patch-notes]] § 2016-12-15). The forum says the dungeon boss only exists while the land is monster-invaded (forum, [[gameplay/warmonger-forum]] §3).

## Sources

- [[gameplay/maps-and-dungeons]] §1–2, [[gameplay/dungeon-drops]] §1–2, [[gameplay/patch-history]] § Dungeons and world, [[gameplay/crush-mechanics]] §9 and §12, [[gameplay/crush-patch-notes]] § 2016-12-15, [[gameplay/warmonger-forum]] §3

## Open questions

- Entry cost: the client's `DungeonAdmission` (front matter) asks 10 / 19 Dimensional Energy (normal / hard). The 2018 guide table and Warmonger patch 0726 give 10 / 29, and the spring-2018 UI showed hard = 10 + 2 silver (guides + image, [[gameplay/maps-and-dungeons]] §2; [[gameplay/patch-history]]). The client (final build) is used; the guide numbers are history.
- `time_limit_s` 900 assumes the "dungeon open time" of Warmonger patch 0402 is the instance timer (the Crush Online timer was 20:00, [[gameplay/video-dungeon-run]] §5). No source shows the Warmonger timer on screen.
- The guides do not say which of the boss's unit ids is the normal-mode, hard-mode or field version.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
