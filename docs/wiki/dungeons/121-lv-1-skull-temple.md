---
title: "[Lv 1] Skull Temple"
type: "dungeon"
id: 121
status: "complete"
missing: []
sources: ["client: SceneList.cdb id 121", "client: DungeonAdmission.cdb field 121", "client: Dungeon.cdb", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 121", "notes: [[gameplay/patch-history]] § Dungeons and world, WM 0402 \"dungeon open time 20 → 15 min\" (also [[gameplay/events-and-schedules]] §9); read as the instance timer because the Crush Online timer counted down from 20:00 ([[gameplay/video-dungeon-run]] §5) — patch notes, interpretation inferred", "notes: [[gameplay/patch-history]] § Dungeons and world, WM 0615 unlock level per border area — patch notes"]
manual: ["time_limit_s"]
field: 121
max_users: 5
level: 1
entry_cost:
  - {"mode": "normal", "item": 688, "count": 3}
  - {"mode": "hard", "item": 688, "count": 3}
event: false
shown_rewards: [601, 693, 1930, 2701, 2751]
c17: 2002
image: "UI/FieldImages/1.png"
dungeon_slots:
  - {"group": 0, "slot": 3}
  - {"group": 1, "slot": 3}
  - {"group": 2, "slot": 2}
  - {"group": 2, "slot": 3}
boss: [672, 804]
gear_tier: "T1"
gathering: [802, 812]
time_limit_s: 900
unlock_level: 20
---
<!-- generated:start -->
<!-- generated-keys: title=5cdb46 type=3e3f38 id=8bd795 sources=e3dda6 field=8bd795 max_users=ac3478 level=356a19 entry_cost=3510f5 event=7cb6ef shown_rewards=e8b4f2 c17=2e8c02 image=d7b848 dungeon_slots=068b5b boss=69effa gear_tier=13930c gathering=42ca89 -->
|  |  |
|---|---|
|  | ![(Lv 1) Skull Temple](wiki/assets/dungeons/121.png) |
| **Field** | [[wiki/fields/121-lv-1-skull-temple\|(Lv 1) Skull Temple (field 121)]] |
| **Level** | 1 |
| **Gear tier dropped** | T1 (guides) |
| **Max players** | 5 (SceneList; guides: max 5 per portal) |
| **Event dungeon** | no |
| **Time limit** | 15 min |
| **Banner** | `UI/FieldImages/1.png` |
| **c17 (unknown)** | 2002 |

### Entry cost

| mode | ticket | count |
|---|---|---|
| normal | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 3 |
| hard | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 3 |

`DungeonAdmission` has two {item, count} pairs; reading them as normal / hard mode follows the guides' tables (*inferred*). The 2018 guide numbers differ: [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost]].

### Boss

- [[wiki/monsters/672-king-deathhead|King Deathhead]] (main)
- [[wiki/monsters/804-tough-king-deathhead|Tough King Deathhead]] (other id in the guides' list; *client* variant)

### Rewards shown on the entry panel

What the dungeon window advertises; not a drop table and no rates (*client*). Drop rates go on the monster pages.

[[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/1930-essence-of-darkness|essence of Darkness]], [[wiki/items/2701-deathhead-horn|DeathHead Horn]], [[wiki/items/2751-the-death-head-s-sealed-weapon|The Death Head's Sealed Weapon]]

### Gathering

Nodes placed by `Trigger.cdb` give: [[wiki/items/802-garnet|Garnet]], [[wiki/items/812-red-bloodstone|Red bloodstone]]. Positions on the [[wiki/fields/121-lv-1-skull-temple|field page]].

### Dungeon groups

`Dungeon.cdb` has 3 groups of 15 slots. A slot probably is the tier step a land gets from its distance to the nation's nearest fort (*guess*, from [[gameplay/maps-and-dungeons#Where dungeons appear|Maps and dungeons § Where dungeons appear]]).

Here: group 0 slot 3, group 1 slot 3, group 2 slot 2, group 2 slot 3

### Rules from the guides

Respawn (solo: none; party: about every minute), party loot and the hard-mode rules are in [[gameplay/maps-and-dungeons#Respawn and party rules inside dungeons|Maps and dungeons § Respawn and party rules]]. Materials per run: [[gameplay/dungeon-drops|Dungeon drops]].
<!-- generated:end -->

## Notes

- Boss: [[wiki/monsters/672-king-deathhead|King Deathhead 672]] ("Tough" [[wiki/monsters/804-tough-king-deathhead|804]]; [[wiki/monsters/1501-king-deathhead|1501]] listed by [[gameplay/dungeon-drops]]) (guides + client ids, [[gameplay/maps-and-dungeons]] §2 and [[gameplay/dungeon-drops]] §1).
- Crush Online name: Temple of the Skull (Lv 1) (sheet / forum, [[gameplay/dungeon-drops]] §1, [[gameplay/crush-mechanics]] §9).
- Materials named by the 2018 dungeons guide: Garnet ×4 and Red Bloodstone ×4 (guide, [[gameplay/maps-and-dungeons]] §2). The gathering list in the front matter comes from the client's `Trigger` table.
- Gear: drops T1 named-set gear, already reinforced at a random level (seen +0 to +11). Sets seen in this dungeon: Spirit earring/robe/shoes, Bandolier necklace/belt/bracelet, Life bracelet/ring, Spell ring. The guide's author says 2–3 rarer drops are missing from the list (image + guide, [[gameplay/maps-and-dungeons]] §2).
- Map (from the guide's minimap): S-shaped chain of chambers from the entry (bottom) to the marker (top-left); mineral nodes only (image, [[gameplay/maps-and-dungeons]] §2).
- Unlocks at character level 20 (Warmonger patch 0615, [[gameplay/patch-history]] § Dungeons and world).
- The Spanish upgrade guide names it the best Red Passion T1 farm on hard mode (with Chepa Village) (guide, [[gameplay/maps-and-dungeons]] §2).
- The Crush Online summon scroll for this boss survives in the client as [[wiki/items/2585-the-death-head-s-pipe|The Death Head's Pipe]] (client, [[gameplay/crush-patch-notes]] § 2016-12-15).
- Forum: the Lv 1–2 bosses (Deathhead, Death Knight) could be soloed with base gear and potions; T1/T2 bosses were shielded unless the nation held more than one fort on the channel (forum, [[gameplay/warmonger-forum]] §3). Essence of Darkness "drops from the Tier 1 dungeon boss" (Crush forum, [[gameplay/dungeon-drops]] §1).

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

- Entry cost: the client's `DungeonAdmission` (front matter) asks 3 / 3 Dimensional Energy (normal / hard). The 2018 guide table and Warmonger patch 0726 give 3 / 6, and the spring-2018 UI showed hard = 6 (guides + image, [[gameplay/maps-and-dungeons]] §2; [[gameplay/patch-history]]). The client (final build) is used; the guide numbers are history.
- `time_limit_s` 900 assumes the "dungeon open time" of Warmonger patch 0402 is the instance timer (the Crush Online timer was 20:00, [[gameplay/video-dungeon-run]] §5). No source shows the Warmonger timer on screen.
- The guides do not say which of the boss's unit ids is the normal-mode, hard-mode or field version.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
