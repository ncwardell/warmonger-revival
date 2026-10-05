---
title: "[Lv 6] Ghost Fortress"
type: "dungeon"
id: 124
status: "complete"
missing: []
sources: ["client: SceneList.cdb id 124", "client: DungeonAdmission.cdb field 124", "client: Dungeon.cdb", "doc: gameplay/maps-and-dungeons § 2. Border-area (normal/hard) dungeons (boss)", "client: Trigger.cdb field 124", "doc: gameplay/video-dungeon-run §5 (Crush Online 2016 video: the instance timer counts down from 20:00)", "notes: [[gameplay/patch-history]] § Dungeons and world, WM 0402 \"dungeon open time 20 → 15 min\" (also [[gameplay/events-and-schedules]] §9); read as the instance timer because the Crush Online timer counted down from 20:00 ([[gameplay/video-dungeon-run]] §5) — patch notes, interpretation inferred", "notes: [[gameplay/patch-history]] § Dungeons and world, WM 0615 unlock level per border area — patch notes"]
manual: ["time_limit_s"]
field: 124
max_users: 5
level: 6
entry_cost:
  - {"mode": "normal", "item": 688, "count": 8}
  - {"mode": "hard", "item": 688, "count": 12}
event: false
shown_rewards: [612, 693, 694, 1934, 2705, 2755]
c17: 2007
image: "UI/FieldImages/6.png"
dungeon_slots:
  - {"group": 0, "slot": 8}
  - {"group": 1, "slot": 8}
  - {"group": 2, "slot": 8}
boss: [676, 743, 1218]
gear_tier: "T2"
gathering: [808, 818, 820]
time_limit_s: 900
unlock_level: 25
---
<!-- generated:start -->
<!-- generated-keys: title=6a2ed2 type=3e3f38 id=f38cfe sources=3e10ee field=f38cfe max_users=ac3478 level=c1dfd9 entry_cost=215a89 event=7cb6ef shown_rewards=51a1e7 c17=aca6d6 image=41ca94 dungeon_slots=e54862 boss=d1729a gear_tier=7b5982 gathering=020cf6 -->
|  |  |
|---|---|
|  | ![(Lv 6) Ghost Fortress](wiki/assets/dungeons/124.png) |
| **Field** | [[wiki/fields/124-lv-6-ghost-fortress\|(Lv 6) Ghost Fortress (field 124)]] |
| **Level** | 6 |
| **Gear tier dropped** | T2 (guides) |
| **Max players** | 5 (SceneList; guides: max 5 per portal) |
| **Event dungeon** | no |
| **Time limit** | 15 min |
| **Banner** | `UI/FieldImages/6.png` |
| **c17 (unknown)** | 2007 |

### Entry cost

| mode | ticket | count |
|---|---|---|
| normal | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 8 |
| hard | [[wiki/items/688-dimensional-energy\|Dimensional energy]] | 12 |

`DungeonAdmission` has two {item, count} pairs; reading them as normal / hard mode follows the guides' tables (*inferred*). The 2018 guide numbers differ: [[gameplay/maps-and-dungeons#Entry cost (Dimensional Energy, item 688)|Maps and dungeons § Entry cost]].

### Boss

- [[wiki/monsters/676-great-summoner-spectre|Great Summoner Spectre]] (main)
- [[wiki/monsters/743-great-summoner-spectre|Great Summoner Spectre]] (other id in the guides' list; *client* variant)
- [[wiki/monsters/1218-great-summoner-spectre|Great Summoner Spectre]] (other id in the guides' list; *client* variant)

### Rewards shown on the entry panel

What the dungeon window advertises; not a drop table and no rates (*client*). Drop rates go on the monster pages.

[[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/694-gem-stone-yellow|Gem Stone : Yellow]], [[wiki/items/1934-essence-of-earth|Essence of Earth]], [[wiki/items/2705-bone-of-spector|Bone of Spector]], [[wiki/items/2755-the-wizard-spector-s-sealed-weapon|The Wizard Spector's Sealed Weapon]]

### Gathering

Nodes placed by `Trigger.cdb` give: [[wiki/items/808-moonstone|Moonstone]], [[wiki/items/818-lavender|Lavender]], [[wiki/items/820-peppermint|Peppermint]]. Positions on the [[wiki/fields/124-lv-6-ghost-fortress|field page]].

### Dungeon groups

`Dungeon.cdb` has 3 groups of 15 slots. A slot probably is the tier step a land gets from its distance to the nation's nearest fort (*guess*, from [[gameplay/maps-and-dungeons#Where dungeons appear|Maps and dungeons § Where dungeons appear]]).

Here: group 0 slot 8, group 1 slot 8, group 2 slot 8

### Rules from the guides

Respawn (solo: none; party: about every minute), party loot and the hard-mode rules are in [[gameplay/maps-and-dungeons#Respawn and party rules inside dungeons|Maps and dungeons § Respawn and party rules]]. Materials per run: [[gameplay/dungeon-drops|Dungeon drops]].

### Mentioned in

- [[gameplay/crush-mechanics#9. Dungeons, bosses, farming|Crush Online mechanics from the forum § 9. Dungeons, bosses, farming]]
- [[gameplay/precept-shop#3. Example rolled quest (screenshot)|Precept shop and precept quests § 3. Example rolled quest (screenshot)]]
- [[gameplay/video-dungeon-run#Video notes: Nas Village dungeon run (ZonderCoRe)|Video notes: Nas Village dungeon run (ZonderCoRe) § Video notes: Nas Village dungeon run (ZonderCoRe)]]
- [[gameplay/video-dungeon-run#1. Field id and map|Video notes: Nas Village dungeon run (ZonderCoRe) § 1. Field id and map]]
- [[gameplay/video-dungeon-run#5. Gathering in a dungeon (Crush Online, field 124)|Video notes: Nas Village dungeon run (ZonderCoRe) § 5. Gathering in a dungeon (Crush Online, field 124)]]
<!-- generated:end -->

## Notes

- Boss: [[wiki/monsters/676-great-summoner-spectre|Great Summoner Spectre 676]] / [[wiki/monsters/743-great-summoner-spectre|743]] / [[wiki/monsters/1218-great-summoner-spectre|1218]] (guides + client ids, [[gameplay/maps-and-dungeons]] §2 and [[gameplay/dungeon-drops]] §1).
- Crush Online name: Fortress of Ghost, **Lv 5** in Crush Online (the client and the 2018 guides make it Lv 6) (sheet / forum, [[gameplay/dungeon-drops]] §1, [[gameplay/crush-mechanics]] §9).
- Materials named by the 2018 dungeons guide: Moonstone ×4, Lavender ×3 and Peppermint ×5 (guide, [[gameplay/maps-and-dungeons]] §2). The gathering list in the front matter comes from the client's `Trigger` table.
- Gear: drops T2 named-set gear, already reinforced at a random level (seen +0 to +11). Sets seen in this dungeon: Guardian helmet/armor, Honor helmet/armor, Life gloves/shoes/necklace/belt, Mediation necklace/belt/ring/bracelet. The guide's author says 2–3 rarer drops are missing from the list (image + guide, [[gameplay/maps-and-dungeons]] §2).
- Map (from the guide's minimap): entry top-left, two long lobes; marker in the centre (image, [[gameplay/maps-and-dungeons]] §2).
- Unlocks at character level 25 (Warmonger patch 0615, [[gameplay/patch-history]] § Dungeons and world).
- The Spanish upgrade guide names it the best Red Passion T2 farm (guide, [[gameplay/maps-and-dungeons]] §2).
- A Crush Online video (2016) shows the instance timer counting down from 20:00, a gather cast of about 3 s, Moonstone nodes at `Trigger` 12401 and 12404, and Red and Black Ghosts near the entrance. Every minimap node matches a `Trigger` row of field 124, so the node layout did not change between Crush and the final client (video + client, [[gameplay/video-dungeon-run]] §5).

## Behaviour

- Hard mode has more and stronger monsters, better loot and a boss at the end; normal mode is easy (guide, [[gameplay/maps-and-dungeons]] §2).
- Respawn: solo, monsters do not respawn; with 2+ party members in hard mode they do. Guides give the first refill after 3–5 min (3 players) then about every minute, or after 9 min / when the timer shows 10:00 (guides, [[gameplay/maps-and-dungeons]] §2). Warmonger patch 0404: with more than 2 users monsters respawn after 5 min (notes, [[gameplay/patch-history]] § Dungeons and world).
- Time limit: Warmonger patch 0402 cut the dungeon open time from 20 to 15 min (notes, [[gameplay/patch-history]]); in Crush Online, when the timer ran out nothing dropped and the party was teleported out (staff, [[gameplay/crush-mechanics]] §9).
- Loot: in March 2018 only the last hitter got loot; later every living party member who damaged the monster got a drop, and a party raised the drop rate (guides, [[gameplay/maps-and-dungeons]] §2). Crush Online scaled monster count and loot with party size; a solo player got about 1/5 of a full group's loot (player, [[gameplay/crush-mechanics]] §9).
- Max 5 players per portal instance; with "Can not enter" ticked nobody else can join (guide, [[gameplay/maps-and-dungeons]] §1).
- The dungeon tier a land shows depends on its distance from the nation's main fort (guides, [[gameplay/maps-and-dungeons]] §1; [[gameplay/patch-history]] WM 0726).
- In Crush Online (patch 2016-12-15) the dungeon elites dropped a scroll that summoned one extra boss, once per boss (staff, [[gameplay/crush-patch-notes]] § 2016-12-15). The forum says the dungeon boss only exists while the land is monster-invaded (forum, [[gameplay/warmonger-forum]] §3).

## Sources

- [[gameplay/maps-and-dungeons]] §1–2, [[gameplay/dungeon-drops]] §1–2, [[gameplay/patch-history]] § Dungeons and world, [[gameplay/crush-mechanics]] §9 and §12, [[gameplay/crush-patch-notes]] § 2016-12-15, [[gameplay/warmonger-forum]] §3, [[gameplay/video-dungeon-run]] §5

## Open questions

- Entry cost: the client's `DungeonAdmission` (front matter) asks 8 / 12 Dimensional Energy (normal / hard). The 2018 guide table and Warmonger patch 0726 give 8 / 20, and the spring-2018 UI showed hard = 8 + 1 silver (UI showed 8 + 2) (guides + image, [[gameplay/maps-and-dungeons]] §2; [[gameplay/patch-history]]). The client (final build) is used; the guide numbers are history.
- `time_limit_s` 900 assumes the "dungeon open time" of Warmonger patch 0402 is the instance timer (the Crush Online timer was 20:00, [[gameplay/video-dungeon-run]] §5). No source shows the Warmonger timer on screen.
- Conflict: the Crush Online video (2016) shows a 20:00 timer (1200 s, the value the generator wrote); Warmonger patch 0402 (2018) cut it to 15 min, so 900 s is used here and `time_limit_s` is listed in `manual`.
- Level swap: Crush Online had Ghost Fortress at Lv 5 and Tow Canyon at Lv 6; players reported quest markers mixed up between the two ([[gameplay/crush-mechanics]] §9). The client order is used.
- The guides do not say which of the boss's unit ids is the normal-mode, hard-mode or field version.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
