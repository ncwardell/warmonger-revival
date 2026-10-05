---
title: "[Lv 5] Tow Canyon"
type: "dungeon"
id: 125
status: "complete"
missing: []
sources: ["client: SceneList.cdb id 125", "client: DungeonAdmission.cdb field 125", "client: Dungeon.cdb", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 125", "notes: [[gameplay/patch-history]] § Dungeons and world, WM 0402 \"dungeon open time 20 → 15 min\" (also [[gameplay/events-and-schedules]] §9); read as the instance timer because the Crush Online timer counted down from 20:00 ([[gameplay/video-dungeon-run]] §5) — patch notes, interpretation inferred", "notes: [[gameplay/patch-history]] § Dungeons and world, WM 0615 unlock level per border area — patch notes"]
manual: ["time_limit_s"]
field: 125
max_users: 5
level: 5
entry_cost:
  - {"mode": "normal", "item": 688, "count": 7}
  - {"mode": "hard", "item": 688, "count": 9}
event: false
shown_rewards: [602, 693, 1935, 2706, 2756]
c17: 2006
image: "UI/FieldImages/5.png"
dungeon_slots:
  - {"group": 0, "slot": 7}
  - {"group": 1, "slot": 7}
  - {"group": 2, "slot": 7}
boss: [677, 822, 1223]
gear_tier: "T2"
gathering: [806, 822, 824]
time_limit_s: 900
unlock_level: 24
---
<!-- generated:start -->
<!-- generated-keys: title=0f8440 type=3e3f38 id=0ca927 sources=024730 field=0ca927 max_users=ac3478 level=ac3478 entry_cost=11406a event=7cb6ef shown_rewards=3a1a59 c17=1938b7 image=fe7704 dungeon_slots=01fff0 boss=6d768e gear_tier=7b5982 gathering=0cbe10 -->
|  |  |
|---|---|
|  | ![(Lv 5) Tow Canyon](wiki/assets/dungeons/125.png) |
| **Field** | [[wiki/fields/125-lv-5-tow-canyon\|(Lv 5) Tow Canyon (field 125)]] |
| **Level** | 5 |
| **Gear tier dropped** | T2 (guides) |
| **Max players** | 5 (SceneList; guides: max 5 per portal) |
| **Event dungeon** | no |
| **Time limit** | 15 min |
| **Banner** | `UI/FieldImages/5.png` |
| **c17 (unknown)** | 2006 |

### Entry cost

| mode | ticket | count |
|---|---|---|
| normal | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 7 |
| hard | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 9 |

`DungeonAdmission` has two {item, count} pairs; reading them as normal / hard mode follows the guides' tables (*inferred*). The 2018 guide numbers differ: [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost]].

### Boss

- [[wiki/monsters/677-war-chief-garon|War Chief Garon]] (main)
- [[wiki/monsters/822-war-chief-garon|War Chief Garon]] (other id in the guides' list; *client* variant)
- [[wiki/monsters/1223-war-chief-garon|War Chief Garon]] (other id in the guides' list; *client* variant)

### Rewards shown on the entry panel

What the dungeon window advertises; not a drop table and no rates (*client*). Drop rates go on the monster pages.

[[wiki/items/602-blue-passion-piece-d|Blue Passion Piece (D)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/1935-essence-of-light|Essence of Light]], [[wiki/items/2706-horn-of-garon|Horn of Garon]], [[wiki/items/2756-the-war-hammer-garon-s-sealed-weapon|The War hammer Garon's Sealed Weapon]]

### Gathering

Nodes placed by `Trigger.cdb` give: [[wiki/items/806-emerald|Emerald]], [[wiki/items/822-rosemary|Rosemary]], [[wiki/items/824-jasmine|Jasmine]]. Positions on the [[wiki/fields/125-lv-5-tow-canyon|field page]].

### Dungeon groups

`Dungeon.cdb` has 3 groups of 15 slots. A slot probably is the tier step a land gets from its distance to the nation's nearest fort (*guess*, from [[gameplay/maps-and-dungeons#Where dungeons appear|Maps and dungeons § Where dungeons appear]]).

Here: group 0 slot 7, group 1 slot 7, group 2 slot 7

### Rules from the guides

Respawn (solo: none; party: about every minute), party loot and the hard-mode rules are in [[gameplay/maps-and-dungeons#Respawn and party rules inside dungeons|Maps and dungeons § Respawn and party rules]]. Materials per run: [[gameplay/dungeon-drops|Dungeon drops]].

### Mentioned in

- [[gameplay/crush-mechanics#9. Dungeons, bosses, farming|Crush Online mechanics from the forum § 9. Dungeons, bosses, farming]]
<!-- generated:end -->

## Notes

- Boss: [[wiki/monsters/677-war-chief-garon|War Chief Garon 677]] / [[wiki/monsters/822-war-chief-garon|822]] / [[wiki/monsters/1223-war-chief-garon|1223]] (guides + client ids, [[gameplay/maps-and-dungeons]] §2 and [[gameplay/dungeon-drops]] §1).
- Crush Online name: Canyon of Tow, **Lv 6** in Crush Online (the client and the 2018 guides make it Lv 5) (sheet / forum, [[gameplay/dungeon-drops]] §1, [[gameplay/crush-mechanics]] §9).
- Materials named by the 2018 dungeons guide: Emerald ×4, Rosemary ×5 and Jasmine ×3 (guide, [[gameplay/maps-and-dungeons]] §2). The gathering list in the front matter comes from the client's `Trigger` table.
- Gear: drops T2 named-set gear, already reinforced at a random level (seen +0 to +11). Sets seen in this dungeon: Guardian shoes, Spirit shoes, Bandolier belt/bracelet/ring/necklace, Spell bracelet/ring, Life bracelet/ring. The guide's author says 2–3 rarer drops are missing from the list (image + guide, [[gameplay/maps-and-dungeons]] §2).
- Map (from the guide's minimap): entry top-left, two columns of chambers; marker top-right; pink stars down the east side (image, [[gameplay/maps-and-dungeons]] §2).
- Unlocks at character level 24 (Warmonger patch 0615, [[gameplay/patch-history]] § Dungeons and world).
- The Spanish upgrade guide names it the best Blue Passion T2 farm (guide, [[gameplay/maps-and-dungeons]] §2).

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

- Entry cost: the client's `DungeonAdmission` (front matter) asks 7 / 9 Dimensional Energy (normal / hard). The 2018 guide table and Warmonger patch 0726 give 7 / 16, and the spring-2018 UI showed hard = 7 + 2 bronze (guides + image, [[gameplay/maps-and-dungeons]] §2; [[gameplay/patch-history]]). The client (final build) is used; the guide numbers are history.
- `time_limit_s` 900 assumes the "dungeon open time" of Warmonger patch 0402 is the instance timer (the Crush Online timer was 20:00, [[gameplay/video-dungeon-run]] §5). No source shows the Warmonger timer on screen.
- Level swap: Crush Online had Ghost Fortress at Lv 5 and Tow Canyon at Lv 6; players reported quest markers mixed up between the two ([[gameplay/crush-mechanics]] §9). The client order is used.
- The guides do not say which of the boss's unit ids is the normal-mode, hard-mode or field version.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
