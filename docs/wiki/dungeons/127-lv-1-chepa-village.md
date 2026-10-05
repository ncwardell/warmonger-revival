---
title: "[Lv 1] Chepa Village"
type: "dungeon"
id: 127
status: "complete"
missing: []
sources: ["client: SceneList.cdb id 127", "client: DungeonAdmission.cdb field 127", "client: Dungeon.cdb", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 127", "notes: [[gameplay/patch-history]] § Dungeons and world, WM 0402 \"dungeon open time 20 → 15 min\" (also [[gameplay/events-and-schedules]] §9); read as the instance timer because the Crush Online timer counted down from 20:00 ([[gameplay/video-dungeon-run]] §5) — patch notes, interpretation inferred", "notes: [[gameplay/patch-history]] § Dungeons and world, WM 0615 unlock level per border area — patch notes"]
field: 127
max_users: 5
level: 1
entry_cost:
  - {"mode": "normal", "item": 688, "count": 2}
  - {"mode": "hard", "item": 688, "count": 2}
event: false
shown_rewards: [611, 601, 693, 1931, 2709, 2759]
c17: 2001
image: "UI/FieldImages/0.png"
dungeon_slots:
  - {"group": 0, "slot": 1}
  - {"group": 0, "slot": 2}
  - {"group": 1, "slot": 1}
  - {"group": 1, "slot": 2}
  - {"group": 2, "slot": 1}
boss: [870, 950]
gear_tier: "T1"
gathering: [818, 820]
time_limit_s: 900
unlock_level: 0
---
<!-- generated:start -->
<!-- generated-keys: title=a46136 type=3e3f38 id=008451 sources=e5a418 field=008451 max_users=ac3478 level=356a19 entry_cost=6d13a2 event=7cb6ef shown_rewards=82c08d c17=9195f8 image=c57209 dungeon_slots=969ce3 boss=00cb4f gear_tier=13930c gathering=3a8b4c time_limit_s=2be88c -->
|  |  |
|---|---|
|  | ![(Lv 1) Chepa Village](../assets/dungeons/127.png) |
| **Field** | [[wiki/fields/127-lv-1-chepa-village\|(Lv 1) Chepa Village (field 127)]] |
| **Level** | 1 |
| **Gear tier dropped** | T1 (guides) |
| **Max players** | 5 (SceneList; guides: max 5 per portal) |
| **Event dungeon** | no |
| **Banner** | `UI/FieldImages/0.png` |
| **c17 (unknown)** | 2001 |

### Entry cost

| mode | ticket | count |
|---|---|---|
| normal | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 2 |
| hard | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 2 |

`DungeonAdmission` has two {item, count} pairs; reading them as normal / hard mode follows the guides' tables (*inferred*). The 2018 guide numbers differ: [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost]].

### Boss

- [[wiki/monsters/870-chepa-sorcerer|Chepa Sorcerer]] (main)
- [[wiki/monsters/950-chepa-sorcerer|Chepa Sorcerer]] (other id in the guides' list; *client* variant)

### Rewards shown on the entry panel

What the dungeon window advertises; not a drop table and no rates (*client*). Drop rates go on the monster pages.

[[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]], [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/1931-essence-of-wind|Essence of Wind]], [[wiki/items/2709-drop-of-chepa-sorcerer|Drop of Chepa Sorcerer]], [[wiki/items/2759-the-chepa-sorcerer-s-sealed-weapon|The Chepa Sorcerer's Sealed Weapon]]

### Gathering

Nodes placed by `Trigger.cdb` give: [[wiki/items/818-lavender|Lavender]], [[wiki/items/820-peppermint|Peppermint]]. Positions on the [[wiki/fields/127-lv-1-chepa-village|field page]].

### Dungeon groups

`Dungeon.cdb` has 3 groups of 15 slots. A slot probably is the tier step a land gets from its distance to the nation's nearest fort (*guess*, from [[gameplay/maps-and-dungeons#Where dungeons appear|Maps and dungeons § Where dungeons appear]]).

Here: group 0 slot 1, group 0 slot 2, group 1 slot 1, group 1 slot 2, group 2 slot 1

### Rules from the guides

Respawn (solo: none; party: about every minute), party loot and the hard-mode rules are in [[gameplay/maps-and-dungeons#Respawn and party rules inside dungeons|Maps and dungeons § Respawn and party rules]]. Materials per run: [[gameplay/dungeon-drops|Dungeon drops]].
<!-- generated:end -->

## Notes

- Boss: [[wiki/monsters/870-chepa-sorcerer|Chepa Sorcerer 870]] / [[wiki/monsters/950-chepa-sorcerer|950]] (guides + client ids, [[gameplay/maps-and-dungeons]] §2 and [[gameplay/dungeon-drops]] §1).
- Crush Online name: Chepa Village (Lv 1) (sheet / forum, [[gameplay/dungeon-drops]] §1, [[gameplay/crush-mechanics]] §9).
- Materials named by the 2018 dungeons guide: Lavender ×4 and Peppermint ×4 (guide, [[gameplay/maps-and-dungeons]] §2). The gathering list in the front matter comes from the client's `Trigger` table.
- Gear: drops T1 named-set gear, already reinforced at a random level (seen +0 to +11). Sets seen in this dungeon: Life helmet/armor, Guardian armor/gloves, Spell necklace, Mediation necklace/belt/bracelet/ring (plus Guardian boots per a comment). The guide's author says 2–3 rarer drops are missing from the list (image + guide, [[gameplay/maps-and-dungeons]] §2).
- Map (from the guide's minimap): entry bottom-left; one corridor north splitting west (to the marker) and north-east; herb nodes only (image, [[gameplay/maps-and-dungeons]] §2).
- Unlocks at character level 0 (Warmonger patch 0615, [[gameplay/patch-history]] § Dungeons and world).
- The Spanish upgrade guide names it the best Red Passion T1 farm on hard mode (with Skull Temple) (guide, [[gameplay/maps-and-dungeons]] §2).
- The Crush Online summon scroll for this boss survives in the client as [[wiki/items/2589-the-chepa-sorcerer-s-pipe|The Chepa Sorcerer's Pipe]] (client, [[gameplay/crush-patch-notes]] § 2016-12-15).

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

- Entry cost: the client's `DungeonAdmission` (front matter) asks 2 / 2 Dimensional Energy (normal / hard). The 2018 guide table and Warmonger patch 0726 give 2 / 4, and the spring-2018 UI showed hard = 4 (guides + image, [[gameplay/maps-and-dungeons]] §2; [[gameplay/patch-history]]). The client (final build) is used; the guide numbers are history.
- `time_limit_s` 900 assumes the "dungeon open time" of Warmonger patch 0402 is the instance timer (the Crush Online timer was 20:00, [[gameplay/video-dungeon-run]] §5). No source shows the Warmonger timer on screen.
- The guides do not say which of the boss's unit ids is the normal-mode, hard-mode or field version.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
