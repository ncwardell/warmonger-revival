---
title: "[Lv 7] Demon Hell"
type: "dungeon"
id: 126
status: "complete"
missing: []
sources: ["client: SceneList.cdb id 126", "client: DungeonAdmission.cdb field 126", "client: Dungeon.cdb", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 126", "notes: [[gameplay/patch-history]] § Dungeons and world, WM 0402 \"dungeon open time 20 → 15 min\" (also [[gameplay/events-and-schedules]] §9); read as the instance timer because the Crush Online timer counted down from 20:00 ([[gameplay/video-dungeon-run]] §5) — patch notes, interpretation inferred", "notes: [[gameplay/patch-history]] § Dungeons and world, WM 0615 unlock level per border area — patch notes"]
manual: ["time_limit_s"]
field: 126
max_users: 5
level: 7
entry_cost:
  - {"mode": "normal", "item": 688, "count": 9}
  - {"mode": "hard", "item": 688, "count": 15}
event: false
shown_rewards: [612, 613, 693, 694, 1935, 2707, 2757]
c17: 2008
image: "UI/FieldImages/7.png"
dungeon_slots:
  - {"group": 0, "slot": 9}
  - {"group": 1, "slot": 9}
  - {"group": 2, "slot": 9}
boss: [678, 740, 739]
gear_tier: "T2"
gathering: [810, 826, 828]
time_limit_s: 900
unlock_level: 26
---
<!-- generated:start -->
<!-- generated-keys: title=12597b type=3e3f38 id=114d4e sources=cef1ec field=114d4e max_users=ac3478 level=902ba3 entry_cost=992c16 event=7cb6ef shown_rewards=d3c68f c17=527dc6 image=168686 dungeon_slots=899470 boss=33e996 gear_tier=7b5982 gathering=a8425a -->
|  |  |
|---|---|
|  | ![(Lv 7) Demon Hell](wiki/assets/dungeons/126.png) |
| **Field** | [[wiki/fields/126-lv-7-demon-hell\|(Lv 7) Demon Hell (field 126)]] |
| **Level** | 7 |
| **Gear tier dropped** | T2 (guides) |
| **Max players** | 5 (SceneList; guides: max 5 per portal) |
| **Event dungeon** | no |
| **Time limit** | 15 min |
| **Banner** | `UI/FieldImages/7.png` |
| **c17 (unknown)** | 2008 |

### Entry cost

| mode | ticket | count |
|---|---|---|
| normal | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 9 |
| hard | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 15 |

`DungeonAdmission` has two {item, count} pairs; reading them as normal / hard mode follows the guides' tables (*inferred*). The 2018 guide numbers differ: [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost]].

### Boss

- [[wiki/monsters/678-reviatan-shadow|Reviatan Shadow]] (main)
- [[wiki/monsters/740-reviatan-shadow|Reviatan Shadow]] (other id in the guides' list; *client* variant)
- [[wiki/monsters/739-commander-reviatan|Commander Reviatan]] (other id in the guides' list; *client* variant)

### Rewards shown on the entry panel

What the dungeon window advertises; not a drop table and no rates (*client*). Drop rates go on the monster pages.

[[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]], [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/694-gem-stone-yellow|Gem Stone : Yellow]], [[wiki/items/1935-essence-of-light|Essence of Light]], [[wiki/items/2707-horn-of-leviathan|Horn of Leviathan]], [[wiki/items/2757-the-devil-commander-leviathan-s-sealed-weapon|The Devil commander Leviathan's Sealed Weapon]]

### Gathering

Nodes placed by `Trigger.cdb` give: [[wiki/items/810-diamond|Diamond]], [[wiki/items/826-borage|Borage]], [[wiki/items/828-spartium|Spartium]]. Positions on the [[wiki/fields/126-lv-7-demon-hell|field page]].

### Dungeon groups

`Dungeon.cdb` has 3 groups of 15 slots. A slot probably is the tier step a land gets from its distance to the nation's nearest fort (*guess*, from [[gameplay/maps-and-dungeons#Where dungeons appear|Maps and dungeons § Where dungeons appear]]).

Here: group 0 slot 9, group 1 slot 9, group 2 slot 9

### Rules from the guides

Respawn (solo: none; party: about every minute), party loot and the hard-mode rules are in [[gameplay/maps-and-dungeons#Respawn and party rules inside dungeons|Maps and dungeons § Respawn and party rules]]. Materials per run: [[gameplay/dungeon-drops|Dungeon drops]].
<!-- generated:end -->

## Notes

- Boss: [[wiki/monsters/678-reviatan-shadow|Reviatan Shadow 678]] / [[wiki/monsters/740-reviatan-shadow|740]] and [[wiki/monsters/739-commander-reviatan|Commander Reviatan 739]] ([[wiki/monsters/972-reviatan|Reviatan 972]] also listed by [[gameplay/dungeon-drops]]) (guides + client ids, [[gameplay/maps-and-dungeons]] §2 and [[gameplay/dungeon-drops]] §1).
- Crush Online name: Hell of Demon (Lv 7), boss "Akasha/Reviathan" (sheet) or "Akasha/Leviathan" (forum) (sheet / forum, [[gameplay/dungeon-drops]] §1, [[gameplay/crush-mechanics]] §9).
- Materials named by the 2018 dungeons guide: Diamond ×4, Spartium ×5 and Borage ×3 (guide, [[gameplay/maps-and-dungeons]] §2). The gathering list in the front matter comes from the client's `Trigger` table.
- Gear: drops T2 named-set gear, already reinforced at a random level (seen +0 to +11). Sets seen in this dungeon: Life helmet, Spirit earring/robe, Transcendency belt/necklace/ring/bracelet, Spell belt. The guide's author says 2–3 rarer drops are missing from the list (image + guide, [[gameplay/maps-and-dungeons]] §2).
- Map (from the guide's minimap): entry top-right; many small islands with pink stars; marker top-left (image, [[gameplay/maps-and-dungeons]] §2).
- Unlocks at character level 26 (Warmonger patch 0615, [[gameplay/patch-history]] § Dungeons and world).
- The Spanish upgrade guide names it the best Red Passion T3 farm (guide, [[gameplay/maps-and-dungeons]] §2).
- The guide shows this boss as **two** identical figures (a multi-boss fight); the PvE text of the Remote Bomb TP skill ("attacks all bosses after attacking the middle boss") fits (image, [[gameplay/maps-and-dungeons]] §2).

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

- Entry cost: the client's `DungeonAdmission` (front matter) asks 9 / 15 Dimensional Energy (normal / hard). The 2018 guide table and Warmonger patch 0726 give 9 / 24, and the spring-2018 UI showed hard = 9 + 1 silver (guides + image, [[gameplay/maps-and-dungeons]] §2; [[gameplay/patch-history]]). The client (final build) is used; the guide numbers are history.
- `time_limit_s` 900 assumes the "dungeon open time" of Warmonger patch 0402 is the instance timer (the Crush Online timer was 20:00, [[gameplay/video-dungeon-run]] §5). No source shows the Warmonger timer on screen.
- The guides do not say which of the boss's unit ids is the normal-mode, hard-mode or field version.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
