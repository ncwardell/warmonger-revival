---
title: "Guardian Transformation"
type: "skill"
id: 20099
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20099"]
name_key: "Skill_20099"
desc_key: "SkillComment_20099"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 20, "type_name": "cost type 20 (unknown)", "amount": 0}
cooldown: {"ms": 120000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 331, "value": 20051, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 20051, "rate": 100}]}
visual: 178
icon: {"file": "Items_20.png", "index": 41}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=fc4784 type=86a754 id=d5aa4f sources=b66cb9 name_key=9d1f40 desc_key=53e04d kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=68d2b6 cooldown=a7242f effect_kind=da4b92 effects=1adc0c damage_or_effect=4574be visual=25293f icon=af683f used_by=97d170 -->
|  |  |
|---|---|
|  | ![Guardian Transformation](../assets/skills/20099.png) |
| **Skill id** | `20099` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 0 cost type 20 (unknown) |
| **Cooldown** | 120 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 178 `PCE_Knife_02_W_순풍의 날개` |
| **Icon** | `ui/icons/Items_20.png` cell 41 |

### Tooltip

> [Active] Guardian transformation. 
> Consumes durability when transforming.
> When all durability is exhausted, the item is destroyed.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 331 | transform: applies buff | [[wiki/buffs/20051\|Buff 20051]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/20051|Buff 20051]] (100%).
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
