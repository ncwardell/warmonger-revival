---
title: "Fortress"
type: "field"
id: 120
status: "complete"
missing: []
sources: ["client: SceneList.cdb id 120", "doc: gameplay/npc-locations §2 (Fortress = ZoneDB 103-105, one per nation)", "client: Teleport_List.cdb field 120", "client: Quest.cdb (quests and objectives in field 120)", "doc: gameplay/npc-locations § 3. Fortress (field 120)"]
name_key: "FieldName_120"
kind: "town"
scene_type: 1
max_users: 100
group: 14
zones: [103, 104, 105]
segments: ["ZP07_06", "ZP08_06", "ZP09_06"]
gates:
  - {"gate": 1901, "x": 0, "z": 0, "to_gate": 0, "to_field": 103, "label": "Land"}
  - {"gate": 1902, "x": 0, "z": 0, "to_gate": 0, "to_field": 105, "label": "Land"}
  - {"gate": 1903, "x": 0, "z": 0, "to_gate": 0, "to_field": 107, "label": "Land"}
connections:
  - {"to": 103, "gate": 1901, "to_gate": null}
  - {"to": 105, "gate": 1902, "to_gate": null}
  - {"to": 107, "gate": 1903, "to_gate": null}
  - {"to": 103, "gate": 1901, "to_gate": 0}
  - {"to": 105, "gate": 1902, "to_gate": 0}
  - {"to": 107, "gate": 1903, "to_gate": 0}
npcs: [99, 200, 204, 205, 207, 208, 210, 212, 213, 214, 217, 237, 242, 323, 324, 206, 211, 218, 300, 303, 311, 322, 304]
monsters: []
spawn_points: []
---
<!-- generated:start -->
<!-- generated-keys: title=3ec720 type=7a94db id=775bc5 sources=600668 name_key=a40dd1 kind=da9544 scene_type=356a19 max_users=310b86 group=fa35e1 zones=3e5d13 segments=b94d6e gates=496ae8 connections=e35a24 npcs=53cd3c monsters=97d170 spawn_points=97d170 -->
|  |  |
|---|---|
|  | ![minimap of zone 103](../assets/zones/103.png) |
| **Field id** | `120` |
| **Kind** | town (SceneList type 1; name *inferred*) |
| **Max users** | 100 (SceneList, column meaning *guessed*) |
| **Region group** | 14 (SceneList last column) |
| **Zones** | [[wiki/zones/103-a-fortress\|A Fortress]], [[wiki/zones/104-b-fortress\|B Fortress]], [[wiki/zones/105-c-fortress\|C Fortress]] |
| **Terrain segments** | `ZP07_06`, `ZP08_06`, `ZP09_06` |
| **Name key** | `FieldName_120` |

### Gates and connections

`Teleport_List` rows of this field. A player sent to a gate id arrives at that gate's position (`server/travel.py`); the gate's own trigger is the portal object a little further out (*client*).

| gate | at (x, z) | leads to | arrives at gate | label |
|---|---|---|---|---|
| 1901 | no position (0, 0) | [[wiki/fields/103-place-for-scattered-troops\|Place for Scattered troops]] | — | Land |
| 1902 | no position (0, 0) | [[wiki/fields/105-place-for-scattered-troops\|Place for Scattered troops]] | — | Land |
| 1903 | no position (0, 0) | [[wiki/fields/107-place-for-scattered-troops\|Place for Scattered troops]] | — | Land |

### NPCs

Positions come from the NPC's own page (`x`, `z`). The client does not place town NPCs; the server spawns them ([[gameplay/npc-locations|NPC locations]] §1).

| NPC | unit | position | why it is listed |
|---|---|---|---|
| Dimension Gate | 99 |  | quests [[wiki/quests/15-repel-the-skeleton-invasion\|15]], [[wiki/quests/16-farrell-s-request\|16]], [[wiki/quests/22-repel-the-black-skeleton-invasion\|22]], [[wiki/quests/30-chepa-village\|30]], [[wiki/quests/32-swamps-of-snake-warrior\|32]] … |
| [[wiki/npcs/200-freya\|Freya]] | 200 | 1906.6, 1641 | quests [[wiki/quests/12-an-urgent-message\|12]], [[wiki/quests/13-battle-preparations\|13]], [[wiki/quests/14-battle-preparations\|14]], [[wiki/quests/15-repel-the-skeleton-invasion\|15]], [[wiki/quests/17-support-the-abyss-expedition\|17]] …; [[gameplay/npc-locations#3. Fortress (field 120)\|NPC locations § 3. Fortress (field 120)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/204-wren\|Wren]] | 204 | 1983.2, 1709.8 | quests [[wiki/quests/26-border-area-normal-mode\|26]], [[wiki/quests/102-wren-s-sister-wren\|102]], [[wiki/quests/727-the-necessary-materials\|727]], [[wiki/quests/740-tow-canyon\|740]], [[wiki/quests/785-the-strange-flowers-in-the-lake\|785]] …; [[gameplay/npc-locations#3. Fortress (field 120)\|NPC locations § 3. Fortress (field 120)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/205-lewellyn\|Lewellyn]] | 205 | 1987, 1712.4 | quests [[wiki/quests/119-monster-area-wars\|119]], [[wiki/quests/724-find-lost-item\|724]], [[wiki/quests/733-weapon-appropriation\|733]], [[wiki/quests/737-ghost-fortress\|737]], [[wiki/quests/1011-skull-cemetery-hunting\|1011]] …; [[gameplay/npc-locations#3. Fortress (field 120)\|NPC locations § 3. Fortress (field 120)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/207-athan\|Athan]] | 207 | 1910.6, 1666.7 | quests [[wiki/quests/714-buy-time-energy\|714]], [[wiki/quests/1101-the-land-of-greed-kill-monster\|1101]], [[wiki/quests/1102-the-avenue-of-spirit-kill-monster\|1102]], [[wiki/quests/1103-the-way-go-to-devildom-kill-monster\|1103]]; [[gameplay/npc-locations#3. Fortress (field 120)\|NPC locations § 3. Fortress (field 120)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/208-bell-thain\|Bell Thain]] | 208 | 1917, 1746 | quests [[wiki/quests/48-doping-create\|48]], [[wiki/quests/49-war-objects\|49]], [[wiki/quests/50-war-winning-means\|50]], [[wiki/quests/51-war-winning-means\|51]], [[wiki/quests/53-safety-factor-management\|53]]; [[gameplay/npc-locations#3. Fortress (field 120)\|NPC locations § 3. Fortress (field 120)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/210-kesley\|Kesley]] | 210 | 1879.9, 1679.4 | quests [[wiki/quests/29-kesley-s-disgrace\|29]], [[wiki/quests/105-kesley-s-disgrace\|105]], [[wiki/quests/117-lords-of-the-land\|117]], [[wiki/quests/732-fisher-s-scales\|732]], [[wiki/quests/745-gathering-plant-and-ore\|745]] …; [[gameplay/npc-locations#3. Fortress (field 120)\|NPC locations § 3. Fortress (field 120)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/212-cassia\|Cassia]] | 212 | 1990.7, 1716.1 | quests [[wiki/quests/13-battle-preparations\|13]]; [[gameplay/npc-locations#3. Fortress (field 120)\|NPC locations § 3. Fortress (field 120)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/213-odin\|Odin]] | 213 | 1991.9, 1703.6 | quests [[wiki/quests/110-gear-manufacturing\|110]], [[wiki/quests/726-gathering-plant-and-ore\|726]], [[wiki/quests/728-gathering-plant-and-ore\|728]], [[wiki/quests/730-gathering-plant-and-ore\|730]], [[wiki/quests/734-gathering-plant-and-ore\|734]] …; [[gameplay/npc-locations#3. Fortress (field 120)\|NPC locations § 3. Fortress (field 120)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/214-owen\|Owen]] | 214 | 1998.9, 1709 | quests [[wiki/quests/14-battle-preparations\|14]], [[wiki/quests/47-create-potion\|47]], [[wiki/quests/48-doping-create\|48]], [[wiki/quests/108-hunting-ghosts-spirit-avenue\|108]], [[wiki/quests/725-collecting-material\|725]] …; [[gameplay/npc-locations#3. Fortress (field 120)\|NPC locations § 3. Fortress (field 120)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/217-haley\|Haley]] | 217 | 1927.6, 1616.4 | quests [[wiki/quests/104-delivering-punishment\|104]]; [[gameplay/npc-locations#3. Fortress (field 120)\|NPC locations § 3. Fortress (field 120)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/237-farrell\|Farrell]] | 237 |  | quests [[wiki/quests/16-farrell-s-request\|16]], [[wiki/quests/111-weapon-manufacturing\|111]], [[wiki/quests/112-weapon-manufacturing\|112]], [[wiki/quests/113-weapon-manufacturing\|113]], [[wiki/quests/114-weapon-tier-reinforce\|114]] …; NPC page (`map` / `positions`) |
| [[wiki/npcs/242-raon\|Raon]] | 242 |  | quests [[wiki/quests/705-legion-how-to-use-add-on\|705]], [[wiki/quests/774-highly-concentrated-bomb-create\|774]], [[wiki/quests/775-highly-concentrated-bomb-create\|775]], [[wiki/quests/776-highly-concentrated-bomb-create\|776]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/323-alan\|Alan]] | 323 | 1939, 1704.9 | quests [[wiki/quests/121-create-rune\|121]], [[wiki/quests/697-create-rune\|697]]; [[gameplay/npc-locations#3. Fortress (field 120)\|NPC locations § 3. Fortress (field 120)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/324-casta\|Casta]] | 324 | 1942.8, 1704.1 | quests [[wiki/quests/122-rune-equipment\|122]], [[wiki/quests/123-rune-reinforcement\|123]], [[wiki/quests/698-rune-equipment\|698]], [[wiki/quests/699-rune-reinforcement\|699]], [[wiki/quests/1516-item-equip-or-release-rune\|1516]]; [[gameplay/npc-locations#3. Fortress (field 120)\|NPC locations § 3. Fortress (field 120)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/206-ashley\|Ashley]] | 206 | 1888.5, 1704.5 | [[gameplay/npc-locations#3. Fortress (field 120)\|NPC locations § 3. Fortress (field 120)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/211-hadrian\|Hadrian]] | 211 | 1841, 1712 | [[gameplay/npc-locations#3. Fortress (field 120)\|NPC locations § 3. Fortress (field 120)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/218-mail-box\|Mail box]] | 218 | 1928, 1642 | [[gameplay/npc-locations#3. Fortress (field 120)\|NPC locations § 3. Fortress (field 120)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/300-kaysa\|Kaysa]] | 300 | 1924.8, 1657 | [[gameplay/npc-locations#3. Fortress (field 120)\|NPC locations § 3. Fortress (field 120)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/303-cathy\|Cathy]] | 303 | 1924.8, 1666.7 | [[gameplay/npc-locations#3. Fortress (field 120)\|NPC locations § 3. Fortress (field 120)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/311-fortress-portal\|Fortress Portal]] | 311 | 1981, 1561 | [[gameplay/npc-locations#3. Fortress (field 120)\|NPC locations § 3. Fortress (field 120)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/322-paraman\|Paraman]] | 322 | 1959.5, 1699.5 | [[gameplay/npc-locations#3. Fortress (field 120)\|NPC locations § 3. Fortress (field 120)]]; NPC page (`map` / `positions`) |
| [[wiki/npcs/304-fergus\|Fergus]] | 304 |  | NPC page (`map` / `positions`) |

### Monsters

None known yet.

### Spawn points

Monster spawn positions are not in the client data (`map.jpk` has no spawn files; [[spec/monsters|Monsters]]). Add them to the monster's page (`spawns:` with `field`, `x`, `z`) or here as `spawn_points:` (`unit`, `x`, `z`, `count`, `radius`, `respawn_s`).

### Quests in this field

[[wiki/quests/12-an-urgent-message|An urgent message]], [[wiki/quests/13-battle-preparations|Battle preparations]], [[wiki/quests/14-battle-preparations|Battle preparations]], [[wiki/quests/15-repel-the-skeleton-invasion|Repel the Skeleton Invasion]], [[wiki/quests/16-farrell-s-request|Farrell's Request]], [[wiki/quests/17-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/21-group-ancient-ghosts|(Group) Ancient Ghosts]], [[wiki/quests/22-repel-the-black-skeleton-invasion|Repel the Black Skeleton Invasion]], [[wiki/quests/23-stepping-up-your-game|Stepping up your game]], [[wiki/quests/24-stepping-up-your-game|Stepping up your game]], [[wiki/quests/25-stepping-up-your-game|Stepping up your game]], [[wiki/quests/26-border-area-normal-mode|Border Area Normal Mode]], [[wiki/quests/29-kesley-s-disgrace|Kesley's Disgrace]], [[wiki/quests/30-chepa-village|Chepa Village]], [[wiki/quests/32-swamps-of-snake-warrior|Swamps of Snake Warrior]], [[wiki/quests/33-ghost-fortress|Ghost Fortress]], [[wiki/quests/34-tow-canyon|Tow Canyon]], [[wiki/quests/35-demon-hell|Demon Hell]], [[wiki/quests/36-thorn-s-hell|Thorn's Hell]], [[wiki/quests/37-call-tempest|Call Tempest]], [[wiki/quests/41-innocence-s-recovery-operation|Innocence's recovery operation]], [[wiki/quests/44-innocence-report|Innocence report]], [[wiki/quests/47-create-potion|Create Potion]], [[wiki/quests/48-doping-create|Doping Create]], [[wiki/quests/49-war-objects|War - Objects]], [[wiki/quests/50-war-winning-means|War - Winning means]], [[wiki/quests/51-war-winning-means|War - Winning means]], [[wiki/quests/53-safety-factor-management|Safety factor Management]], [[wiki/quests/104-delivering-punishment|Delivering Punishment]], [[wiki/quests/105-kesley-s-disgrace|Kesley's Disgrace]], [[wiki/quests/108-hunting-ghosts-spirit-avenue|Hunting Ghosts (Spirit Avenue)]], [[wiki/quests/109-for-the-honor|For the honor]], [[wiki/quests/110-gear-manufacturing|Gear manufacturing]], [[wiki/quests/111-weapon-manufacturing|Weapon manufacturing]], [[wiki/quests/112-weapon-manufacturing|Weapon manufacturing]], [[wiki/quests/113-weapon-manufacturing|Weapon manufacturing]], [[wiki/quests/114-weapon-tier-reinforce|Weapon tier reinforce]], [[wiki/quests/117-lords-of-the-land|Lords of the Land]], [[wiki/quests/119-monster-area-wars|Monster area wars]], [[wiki/quests/120-enemy-territory|Enemy territory]] and 70 more

### Navmesh

Segments covered by this field's zones (256 × 256 units each). Check a point with `tools/navmesh.py check x z` ([[spec/navmesh|Navmesh]]).

| segment | navmesh (.nav) | terrain (.zp) |
|---|---|---|
| ZP07_06 | yes | yes |
| ZP08_06 | yes | yes |
| ZP09_06 | yes | yes |

### Mentioned in

- [[gameplay/lords-of-the-land#4. The quest chain (NPC Kelsey)|Lords of the Land buff and quest § 4. The quest chain (NPC Kelsey)]]
- [[gameplay/npc-locations#3. Fortress (field 120)|NPC and point-of-interest locations § 3. Fortress (field 120)]]
- [[gameplay/video-character-creation-and-tutorial#Training Camp (field 92) and back|Video notes: character creation and tutorial (ZonderCoRe, June 2018) § Training Camp (field 92) and back]] — at [21:10](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1270s)
- [[gameplay/video-fort-war#Siege result screen (defeat)|Video notes: fortress war series (ZonderCoRe) § Siege result screen (defeat)]] — at [8:00](https://www.youtube.com/watch?v=JPd7TCu-44o&t=480s)
- [[gameplay/video-tutorial-walkthrough#Steps|Video notes: tutorial walkthrough (Bravely Forward 2) § Steps]] — at [32:55](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1975s)
- [[gameplay/README|Gameplay]] (by name)
- [[gameplay/abyss-map|Abyss map and portal graph]] (by name)
- [[gameplay/arena-ranking-rewards|Battle Arena monthly ranking rewards]] (by name)
- [[gameplay/classes-and-legions|Classes, nations and legions]] (by name)
- [[gameplay/consumables|Consumables and clickables]] (by name)
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] (by name)
- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]] (by name)
- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]] (by name)
<!-- generated:end -->

## Notes

<!-- hand-written: add what you know, with a source -->

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
