---
title: "[Lv 3] Tsunami Lake"
type: "dungeon"
id: 122
status: "complete"
missing: []
sources: ["client: SceneList.cdb id 122", "client: DungeonAdmission.cdb field 122", "client: Dungeon.cdb", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 122", "notes: [[gameplay/patch-history]] § Dungeons and world, WM 0402 \"dungeon open time 20 → 15 min\" (also [[gameplay/events-and-schedules]] §9); read as the instance timer because the Crush Online timer counted down from 20:00 ([[gameplay/video-dungeon-run]] §5) — patch notes, interpretation inferred", "notes: [[gameplay/patch-history]] § Dungeons and world, WM 0615 unlock level per border area — patch notes"]
field: 122
max_users: 5
level: 3
entry_cost:
  - {"mode": "normal", "item": 688, "count": 5}
  - {"mode": "hard", "item": 688, "count": 5}
event: false
shown_rewards: [612, 602, 693, 1933, 2703, 2753]
c17: 2004
image: "UI/FieldImages/3.png"
dungeon_slots:
  - {"group": 0, "slot": 5}
  - {"group": 1, "slot": 5}
  - {"group": 2, "slot": 5}
boss: [674, 733, 1209]
gear_tier: "T1"
gathering: [814, 804, 822, 824]
time_limit_s: 900
unlock_level: 22
---
<!-- generated:start -->
<!-- generated-keys: title=a1b133 type=3e3f38 id=05a8ea sources=462a80 field=05a8ea max_users=ac3478 level=77de68 entry_cost=6dc8ea event=7cb6ef shown_rewards=8750e7 c17=667e62 image=2f6ead dungeon_slots=d63727 boss=a4d2f8 gear_tier=13930c gathering=83d28e time_limit_s=2be88c -->
|  |  |
|---|---|
|  | ![(Lv 3) Tsunami Lake](../assets/dungeons/122.png) |
| **Field** | [[wiki/fields/122-lv-3-tsunami-lake\|(Lv 3) Tsunami Lake (field 122)]] |
| **Level** | 3 |
| **Gear tier dropped** | T1 (guides) |
| **Max players** | 5 (SceneList; guides: max 5 per portal) |
| **Event dungeon** | no |
| **Banner** | `UI/FieldImages/3.png` |
| **c17 (unknown)** | 2004 |

### Entry cost

| mode | ticket | count |
|---|---|---|
| normal | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 5 |
| hard | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 5 |

`DungeonAdmission` has two {item, count} pairs; reading them as normal / hard mode follows the guides' tables (*inferred*). The 2018 guide numbers differ: [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost]].

### Boss

- [[wiki/monsters/674-tempest-fisher|Tempest Fisher]] (main)
- [[wiki/monsters/733-tempest-fisher|Tempest Fisher]] (other id in the guides' list; *client* variant)
- [[wiki/monsters/1209-tempest-fisher|Tempest Fisher]] (other id in the guides' list; *client* variant)

### Rewards shown on the entry panel

What the dungeon window advertises; not a drop table and no rates (*client*). Drop rates go on the monster pages.

[[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]], [[wiki/items/602-blue-passion-piece-d|Blue Passion Piece (D)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/1933-essence-of-water|Essence of Water]], [[wiki/items/2703-fin-of-fisher|Fin of Fisher]], [[wiki/items/2753-the-tempest-fisher-s-sealed-weapon|The Tempest Fisher's Sealed Weapon]]

### Gathering

Nodes placed by `Trigger.cdb` give: [[wiki/items/814-topaz|Topaz]], [[wiki/items/804-blue-bloodstone|Blue bloodstone]], [[wiki/items/822-rosemary|Rosemary]], [[wiki/items/824-jasmine|Jasmine]]. Positions on the [[wiki/fields/122-lv-3-tsunami-lake|field page]].

### Dungeon groups

`Dungeon.cdb` has 3 groups of 15 slots. A slot probably is the tier step a land gets from its distance to the nation's nearest fort (*guess*, from [[gameplay/maps-and-dungeons#Where dungeons appear|Maps and dungeons § Where dungeons appear]]).

Here: group 0 slot 5, group 1 slot 5, group 2 slot 5

### Rules from the guides

Respawn (solo: none; party: about every minute), party loot and the hard-mode rules are in [[gameplay/maps-and-dungeons#Respawn and party rules inside dungeons|Maps and dungeons § Respawn and party rules]]. Materials per run: [[gameplay/dungeon-drops|Dungeon drops]].
<!-- generated:end -->

## Notes

- Boss: [[wiki/monsters/674-tempest-fisher|Tempest Fisher 674]] / [[wiki/monsters/733-tempest-fisher|733]] / [[wiki/monsters/1209-tempest-fisher|1209]] (guides + client ids, [[gameplay/maps-and-dungeons]] §2 and [[gameplay/dungeon-drops]] §1).
- Crush Online name: Lake of the tsunami (Lv 3) (sheet / forum, [[gameplay/dungeon-drops]] §1, [[gameplay/crush-mechanics]] §9).
- Materials named by the 2018 dungeons guide: Topaz, Blue Bloodstone, Rosemary and Jasmine ×2 each (guide, [[gameplay/maps-and-dungeons]] §2). The gathering list in the front matter comes from the client's `Trigger` table.
- Gear: drops T1 named-set gear, already reinforced at a random level (seen +0 to +11). Sets seen in this dungeon: Guardian helmet/armor, Honor gloves, Transcendency necklace/bracelet/ring, Life bracelet/ring. The guide's author says 2–3 rarer drops are missing from the list (image + guide, [[gameplay/maps-and-dungeons]] §2).
- Map (from the guide's minimap): five separate islands; entry bottom-centre, marker top-centre; many pink stars (probably elite spawns) (image, [[gameplay/maps-and-dungeons]] §2).
- Unlocks at character level 22 (Warmonger patch 0615, [[gameplay/patch-history]] § Dungeons and world).
- The Crush Online summon scroll for this boss survives in the client as [[wiki/items/2587-the-tempest-fisher-s-pipe|The Tempest Fisher's Pipe]] (client, [[gameplay/crush-patch-notes]] § 2016-12-15).

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

- Entry cost: the client's `DungeonAdmission` (front matter) asks 5 / 5 Dimensional Energy (normal / hard). The 2018 guide table and Warmonger patch 0726 give 5 / 10, and the spring-2018 UI showed hard = 5 + 1 bronze (guides + image, [[gameplay/maps-and-dungeons]] §2; [[gameplay/patch-history]]). The client (final build) is used; the guide numbers are history.
- `time_limit_s` 900 assumes the "dungeon open time" of Warmonger patch 0402 is the instance timer (the Crush Online timer was 20:00, [[gameplay/video-dungeon-run]] §5). No source shows the Warmonger timer on screen.
- The guides do not say which of the boss's unit ids is the normal-mode, hard-mode or field version.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
