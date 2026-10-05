---
title: "Dark Knight Skull Transformation"
type: "skill"
id: 20001
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20001"]
name_key: "Skill_20001"
desc_key: "SkillComment_20001"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 6, "type_name": "EXP", "amount": 0}
cooldown: {"ms": 120000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 331, "value": 20001, "rate": 100}
  - {"slot": 2, "type": 301, "value": 20020, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 20001, "rate": 100}, {"buff": 20020, "rate": 100}]}
visual: 178
icon: {"file": "Items_20.png", "index": 19}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=1ba7e6 type=86a754 id=8a91c6 sources=25fdbf name_key=ab0d3b desc_key=aa753c kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=b1d441 cooldown=a7242f effect_kind=da4b92 effects=46ffaf damage_or_effect=e21297 visual=25293f icon=a71171 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Dark Knight Skull Transformation](wiki/assets/skills/20001.png) |
| **Skill id** | `20001` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 0 EXP |
| **Cooldown** | 120 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 178 `PCE_Knife_02_W_순풍의 날개` |
| **Icon** | `ui/icons/Items_20.png` cell 19 |

### Tooltip

> [Active] Dark knight Skull transformation. 
> Consumes EXP when transforming.

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
