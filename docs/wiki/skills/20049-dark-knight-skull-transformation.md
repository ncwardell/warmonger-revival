---
title: "Dark Knight Skull Transformation"
type: "skill"
id: 20049
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20049"]
name_key: "Skill_20049"
desc_key: "SkillComment_20049"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 20, "type_name": "cost type 20 (unknown)", "amount": 0}
cooldown: {"ms": 120000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 331, "value": 20001, "rate": 100}
  - {"slot": 2, "type": 301, "value": 20020, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 20001, "rate": 100}, {"buff": 20020, "rate": 100}]}
visual: 178
icon: {"file": "Items_20.png", "index": 40}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=1ba7e6 type=86a754 id=b2e9e9 sources=656696 name_key=a977e0 desc_key=ba51ca kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=68d2b6 cooldown=a7242f effect_kind=da4b92 effects=46ffaf damage_or_effect=e21297 visual=25293f icon=6f1b64 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Dark Knight Skull Transformation](wiki/assets/skills/20049.png) |
| **Skill id** | `20049` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 0 cost type 20 (unknown) |
| **Cooldown** | 120 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 178 `PCE_Knife_02_W_순풍의 날개` |
| **Icon** | `ui/icons/Items_20.png` cell 40 |

### Tooltip

> [Active] Dark knight Skull transformation. 
> Consumes durability when transforming.
> When all durability is exhausted, the item is destroyed.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 331 | transform: applies buff | [[wiki/buffs/20001\|Buff 20001]] | 100 |
| 2 | 301 | applies buff (variant 301) | [[wiki/buffs/20020-immortal-body-recovering-for-300-seconds\|Immortal Body : Recovering for 300 seconds]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/20001|Buff 20001]] (100%); applies [[wiki/buffs/20020-immortal-body-recovering-for-300-seconds|Immortal Body : Recovering for 300 seconds]] (100%).
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
