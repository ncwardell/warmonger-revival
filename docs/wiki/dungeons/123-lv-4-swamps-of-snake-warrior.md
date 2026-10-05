---
title: "[Lv 4] Swamps of Snake Warrior"
type: "dungeon"
id: 123
status: "complete"
missing: []
sources: ["client: SceneList.cdb id 123", "client: DungeonAdmission.cdb field 123", "client: Dungeon.cdb", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 123", "notes: [[gameplay/patch-history]] § Dungeons and world, WM 0402 \"dungeon open time 20 → 15 min\" (also [[gameplay/events-and-schedules]] §9); read as the instance timer because the Crush Online timer counted down from 20:00 ([[gameplay/video-dungeon-run]] §5) — patch notes, interpretation inferred", "notes: [[gameplay/patch-history]] § Dungeons and world, WM 0615 unlock level per border area — patch notes"]
manual: ["time_limit_s"]
field: 123
max_users: 5
level: 4
entry_cost:
  - {"mode": "normal", "item": 688, "count": 6}
  - {"mode": "hard", "item": 688, "count": 7}
event: false
shown_rewards: [612, 602, 693, 1932, 2704, 2754]
c17: 2005
image: "UI/FieldImages/4.png"
dungeon_slots:
  - {"group": 0, "slot": 6}
  - {"group": 1, "slot": 6}
  - {"group": 2, "slot": 6}
boss: [675, 736, 1213]
gear_tier: "T1"
gathering: [816, 826, 828]
time_limit_s: 900
unlock_level: 23
---
<!-- generated:start -->
<!-- generated-keys: title=e5603a type=3e3f38 id=40bd00 sources=c58ebc field=40bd00 max_users=ac3478 level=1b6453 entry_cost=00381f event=7cb6ef shown_rewards=65b1ed c17=23a053 image=936313 dungeon_slots=679f34 boss=9798c5 gear_tier=13930c gathering=f3c467 -->
|  |  |
|---|---|
|  | ![(Lv 4) Swamps of Snake Warrior](wiki/assets/dungeons/123.png) |
| **Field** | [[wiki/fields/123-lv-4-swamps-of-snake-warrior\|(Lv 4) Swamps of Snake Warrior (field 123)]] |
| **Level** | 4 |
| **Gear tier dropped** | T1 (guides) |
| **Max players** | 5 (SceneList; guides: max 5 per portal) |
| **Event dungeon** | no |
| **Time limit** | 15 min |
| **Banner** | `UI/FieldImages/4.png` |
| **c17 (unknown)** | 2005 |

### Entry cost

| mode | ticket | count |
|---|---|---|
| normal | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 6 |
| hard | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 7 |

`DungeonAdmission` has two {item, count} pairs; reading them as normal / hard mode follows the guides' tables (*inferred*). The 2018 guide numbers differ: [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost]].

### Boss

- [[wiki/monsters/675-slayer-komodo|Slayer Komodo]] (main)
- [[wiki/monsters/736-slayer-komodo|Slayer Komodo]] (other id in the guides' list; *client* variant)
- [[wiki/monsters/1213-slayer-komodo|Slayer Komodo]] (other id in the guides' list; *client* variant)

### Rewards shown on the entry panel

What the dungeon window advertises; not a drop table and no rates (*client*). Drop rates go on the monster pages.

[[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]], [[wiki/items/602-blue-passion-piece-d|Blue Passion Piece (D)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/1932-essence-of-fire|Essence of Fire]], [[wiki/items/2704-horn-of-komodo|Horn of Komodo]], [[wiki/items/2754-the-slayer-komodo-s-sealed-weapon|The Slayer Komodo's Sealed Weapon]]

### Gathering

Nodes placed by `Trigger.cdb` give: [[wiki/items/816-onyx|Onyx]], [[wiki/items/826-borage|Borage]], [[wiki/items/828-spartium|Spartium]]. Positions on the [[wiki/fields/123-lv-4-swamps-of-snake-warrior|field page]].

### Dungeon groups

`Dungeon.cdb` has 3 groups of 15 slots. A slot probably is the tier step a land gets from its distance to the nation's nearest fort (*guess*, from [[gameplay/maps-and-dungeons#Where dungeons appear|Maps and dungeons § Where dungeons appear]]).

Here: group 0 slot 6, group 1 slot 6, group 2 slot 6

### Rules from the guides

Respawn (solo: none; party: about every minute), party loot and the hard-mode rules are in [[gameplay/maps-and-dungeons#Respawn and party rules inside dungeons|Maps and dungeons § Respawn and party rules]]. Materials per run: [[gameplay/dungeon-drops|Dungeon drops]].
<!-- generated:end -->

## Notes

- Boss: [[wiki/monsters/675-slayer-komodo|Slayer Komodo 675]] / [[wiki/monsters/736-slayer-komodo|736]] / [[wiki/monsters/1213-slayer-komodo|1213]] (guides + client ids, [[gameplay/maps-and-dungeons]] §2 and [[gameplay/dungeon-drops]] §1).
- Crush Online name: Swamps of the Snake Warrior (Lv 4) (sheet / forum, [[gameplay/dungeon-drops]] §1, [[gameplay/crush-mechanics]] §9).
- Materials named by the 2018 dungeons guide: Onyx ×4, Borage ×5 and Spartium ×3 (guide, [[gameplay/maps-and-dungeons]] §2). The gathering list in the front matter comes from the client's `Trigger` table.
- Gear: drops T1 named-set gear, already reinforced at a random level (seen +0 to +11). Sets seen in this dungeon: Life helmet/armor, Spirit earring/robe, Honor helmet/armor, Spell necklace/belt, Barrier necklace/belt/bracelet/ring. The guide's author says 2–3 rarer drops are missing from the list (image + guide, [[gameplay/maps-and-dungeons]] §2).
- Map (from the guide's minimap): entry top-left, chambers zig-zag to the south-east; marker centre-left; two big blue star icons (image, [[gameplay/maps-and-dungeons]] §2).
- Unlocks at character level 23 (Warmonger patch 0615, [[gameplay/patch-history]] § Dungeons and world).
- The Crush Online summon scroll for this boss survives in the client as [[wiki/items/2588-the-slayer-komodo-s-pipe|The Slayer Komodo's Pipe]] (client, [[gameplay/crush-patch-notes]] § 2016-12-15).

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

- Entry cost: the client's `DungeonAdmission` (front matter) asks 6 / 7 Dimensional Energy (normal / hard). The 2018 guide table and Warmonger patch 0726 give 6 / 13, and the spring-2018 UI showed hard = 6 + 1 bronze (guides + image, [[gameplay/maps-and-dungeons]] §2; [[gameplay/patch-history]]). The client (final build) is used; the guide numbers are history.
- `time_limit_s` 900 assumes the "dungeon open time" of Warmonger patch 0402 is the instance timer (the Crush Online timer was 20:00, [[gameplay/video-dungeon-run]] §5). No source shows the Warmonger timer on screen.
- The guides do not say which of the boss's unit ids is the normal-mode, hard-mode or field version.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
