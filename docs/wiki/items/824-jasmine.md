---
title: "Jasmine"
type: "item"
id: 824
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 824", "sheet + guide: [[gameplay/dungeon-drops]] §1, §3 (Crush Share Ore/Herb tab, same lists in the 2018 dungeons guide; sheet Lv 5/6 mapped to client fields 124/125)"]
name_key: "ItemName_824"
kind: 12
kind_name: "Material"
classes: "all"
bind: null
price: {"currency": 2, "currency_name": "Gold", "buy": 20}
cost_pair:
  - {"currency": 2, "amount": 20}
stats: []
icon: {"file": "Items_04.png", "index": 23}
obtained_from:
  - {"how": "gather", "field": 128}
  - {"how": "gather", "field": 122}
  - {"how": "gather", "field": 125}
  - {"how": "gather", "field": 129}
---
<!-- generated:start -->
<!-- generated-keys: title=0cb684 type=d36ca9 id=5fbdc8 sources=846eec name_key=00f0db kind=7b5200 kind_name=59f0ad classes=92d079 bind=2be88c price=80fa96 cost_pair=e76c7b stats=97d170 icon=ee5640 obtained_from=97d170 -->
|  |  |
|---|---|
|  | ![Jasmine](../assets/items/824.png) |
| **Item id** | `824` |
| **Kind** | Material (12) |
| **Classes** | all |
| **Buy price** | 20 Gold |
| **Icon** | `ui/icons/Items_04.png` cell 23 |

### Tooltip

> Can be obtained by gathering.

### Where to get it

Nothing in the client data. Monster drops are server data: add them to the monster's page (`drops:`) or to this page's `obtained_from:`.

### Used for

- Material (× 1) for [[wiki/items/825-jasmine-powder|Jasmine powder]] (recipe 612)
- Material (× 5) for [[wiki/items/872-extracted-jasmine|Extracted Jasmine]] (recipe 626)
- Material (× 1) for [[wiki/items/825-jasmine-powder|Jasmine powder]] (recipe 2412)
- Material (× 5) for [[wiki/items/872-extracted-jasmine|Extracted Jasmine]] (recipe 2426)
<!-- generated:end -->

## Notes

Gathered from ore/herb nodes in Skull Cemetery (128), Tsunami Lake (122), Tow Canyon (125), Thorn's Hell (129) ([[gameplay/dungeon-drops|Dungeon drops]] §1, *sheet + guide*). The 2018 dungeons guide names the same materials per dungeon, with counts per run in [[gameplay/maps-and-dungeons|Maps and dungeons]] §2. Gathering takes about 3 s and is not interrupted by hits ([[gameplay/video-dungeon-run|Nas Village run video]] §5, *video*); the nodes are the client's `Trigger` rows, which match the 2016 minimap ([[gameplay/video-dungeon-run|Nas Village run video]] §5).

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- sheet + guide: [[gameplay/dungeon-drops]] §1, §3 (Crush Share Ore/Herb tab, same lists in the 2018 dungeons guide; sheet Lv 5/6 mapped to client fields 124/125)

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
