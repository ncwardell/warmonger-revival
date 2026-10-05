---
title: "Quick attack"
type: "skill"
id: 20259
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20259"]
name_key: "Skill_20259"
desc_key: "SkillComment_20259"
kind: 2
kind_name: "passive"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 3
cost: null
cooldown: null
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 1, "rate": 100}
  - {"slot": 2, "type": 101, "value": 100, "rate": 0}
  - {"slot": 3, "type": 301, "value": 20256, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 1, "attack_pct": 100, "buffs": [{"buff": 20256, "rate": 100}]}
requirements:
  - {"type": 20257, "a": 2, "b": 0}
visual: 461
icon: {"file": "Skill_Boss_01.dds", "index": 53}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=67e85a type=86a754 id=12a91c sources=b1047e name_key=8c7e87 desc_key=ce84c4 kind=da4b92 kind_name=3844d5 target=069ef3 range=77de68 cost=2be88c cooldown=2be88c effect_kind=356a19 effects=ce6326 damage_or_effect=0fe15e requirements=be0cd2 visual=668f37 icon=e8b5ca used_by=97d170 -->
|  |  |
|---|---|
|  | ![Quick attack](wiki/assets/skills/20259.png) |
| **Skill id** | `20259` |
| **Kind** | passive (2) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 3 (world units) |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 461 `데스헤드_빠른 공격` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 53 |

### Tooltip

> [Passive] A stack is created during a basic attack and your Attack Speed is increased when you reach 5 stacks.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 1 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 100 | 0 |
| 3 | 301 | applies buff (variant 301) | [[wiki/buffs/20256\|Buff 20256]] | 100 |

**Reading:** amount **1 + 100% Attack**; damage (physical?); applies [[wiki/buffs/20256|Buff 20256]] (100%).

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 20257 | 2 | 0 |
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
