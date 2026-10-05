---
title: "Farrell"
type: "npc"
id: 237
status: "stub"
missing: ["x", "z"]
sources: ["client: UnitDB.cdb id 237", "client: Quest.cdb start_npc@18 / c18@2c / objective type 4", "client: Quest.cdb giver/receiver field (map only; no position)"]
name_key: "TitleName_12"
title_key: "UnitName_237"
npc_title: "Blacksmith"
category: 50
class_mask: 2
model: 238
scale: 1.5
functions:
  - {"code": 19, "function": "craft", "label": "Create"}
role: "Blacksmith"
talk_key: "Quest_Talk_Default_Black"
portrait: "ui/NPCProfile/Quest_Reinforce.dds"
quests: {"gives": [16, 111, 112, 113, 114, 120, 761, 762], "receives": [16, 111, 112, 113, 114, 761, 762, 845]}
quest_fields: [120]
map: 120
x: null
z: null
---
<!-- generated:start -->
<!-- generated-keys: title=1ce8ba type=3664ce id=3c3316 sources=c37b02 name_key=e2d294 title_key=5076ed npc_title=5088e1 category=e1822d class_mask=da4b92 model=5b7d26 scale=aa8f28 functions=ba093c role=5088e1 talk_key=971ba2 portrait=d2d345 quests=b30468 quest_fields=6c3da9 map=775bc5 x=2be88c z=2be88c -->
|  |  |
|---|---|
|  | ![Farrell](../assets/npcs/237.png) |
| **Unit id** | `237` |
| **Title** | Blacksmith |
| **Category** | NPC (category 50) |
| **Menu** | Create (`19`) |
| **Stands in** | [[wiki/fields/120-fortress\|Fortress]] (position unknown) |
| **Model** | ObjectList `238`, scale 1.5 |
| **Portrait** | `ui/NPCProfile/Quest_Reinforce.dds` |

### Greeting

> Hi! If you are looking to create a weapon, you've come to the right place.

### Where it stands

No measured position yet. The client's quests put this NPC in [[wiki/fields/120-fortress|Fortress]] (giver/receiver fields, one per nation).

### Quests

- **Gives:** [[wiki/quests/16-farrell-s-request|Farrell's Request]], [[wiki/quests/111-weapon-manufacturing|Weapon manufacturing]], [[wiki/quests/112-weapon-manufacturing|Weapon manufacturing]], [[wiki/quests/113-weapon-manufacturing|Weapon manufacturing]], [[wiki/quests/114-weapon-tier-reinforce|Weapon tier reinforce]], [[wiki/quests/120-enemy-territory|Enemy territory]], [[wiki/quests/761-killed-boss-of-border-area-no-1|killed boss of Border area No.1]], [[wiki/quests/762-killed-boss-of-border-area-no-2|killed boss of Border area No.2]]
- **Takes the turn-in of:** [[wiki/quests/16-farrell-s-request|Farrell's Request]], [[wiki/quests/111-weapon-manufacturing|Weapon manufacturing]], [[wiki/quests/112-weapon-manufacturing|Weapon manufacturing]], [[wiki/quests/113-weapon-manufacturing|Weapon manufacturing]], [[wiki/quests/114-weapon-tier-reinforce|Weapon tier reinforce]], [[wiki/quests/761-killed-boss-of-border-area-no-1|killed boss of Border area No.1]], [[wiki/quests/762-killed-boss-of-border-area-no-2|killed boss of Border area No.2]], [[wiki/quests/845-gather-resourses-at-connected-world|Gather resourses at Connected World]]

### Other units with this name

The client has one unit row per placement or variant: [[wiki/npcs/317-farrell|Farrell (317)]].

### Seen in

- [[gameplay/npc-locations|NPC and point-of-interest locations]] (3. Fortress (field 120))
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
