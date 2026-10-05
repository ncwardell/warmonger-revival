---
title: "Rune of Teleportation"
type: "skill"
id: 800
status: "stub"
missing: ["damage_or_effect", "cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 800"]
name_key: "Skill_800"
desc_key: "SkillComment_800"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["ally", "enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 10
area: {"shape": 1, "shape_name": "circle", "radius": 1.0, "width_or_angle": 0.0}
cost: null
cooldown: null
movement: "blink / teleport"
effect_kind: 2
effects: []
damage_or_effect: {}
visual: 266
icon: {"file": "Skill_MagicScholar_17.png", "index": 0}
used_by:
  - {"item_use": 899}
  - {"item_use": 902}
  - {"item_use": 2903}
  - {"item_use": 50000}
---
<!-- generated:start -->
<!-- generated-keys: title=4c68c5 type=86a754 id=290a52 sources=4a3386 name_key=2d8c2e desc_key=916ec7 kind=356a19 kind_name=9bc378 target=c9e051 range=b1d578 area=3b02d8 cost=2be88c cooldown=2be88c movement=953fcf effect_kind=da4b92 effects=97d170 damage_or_effect=bf21a9 visual=45cbe1 icon=826275 used_by=8a87a9 -->
|  |  |
|---|---|
| **Skill id** | `800` |
| **Kind** | active (1) |
| **Target** | ground; ally, enemy; units: monster, player; up to 1 |
| **Range** | 10 (world units) |
| **Area** | circle, radius 1, width/angle 0 |
| **Movement** | blink / teleport |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 266 `공간이동` |
| **Icon** | `ui/icons/Skill_MagicScholar_17.png` cell 0 |

### Tooltip

> Teleport

### Used by

- Cast when [[wiki/items/899-use-test-2|Use Test 2]] is used (Item_Base option 210)
- Cast when [[wiki/items/902-teleport|Teleport]] is used (Item_Base option 210)
- Cast when [[wiki/items/2903-teleport|Teleport]] is used (Item_Base option 210)
- Cast when [[wiki/items/50000-teleport|Teleport]] is used (Item_Base option 210)
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
