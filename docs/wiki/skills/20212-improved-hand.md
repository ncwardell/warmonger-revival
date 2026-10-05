---
title: "Improved Hand"
type: "skill"
id: 20212
status: "stub"
missing: ["cooldown"]
sources: ["client: Skill_Base.cdb id 20212"]
name_key: "Skill_20212"
desc_key: "SkillComment_20212"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
area: {"shape": 1, "shape_name": "circle", "radius": 7.0, "width_or_angle": 7.0}
cost: {"type": 5, "type_name": "MP", "amount": 40}
cooldown: null
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 1, "rate": 100}
  - {"slot": 2, "type": 101, "value": 100, "rate": 0}
  - {"slot": 3, "type": 301, "value": 20214, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 1, "attack_pct": 100, "buffs": [{"buff": 20214, "rate": 100}]}
icon: {"file": "Skill_Boss_01.dds", "index": 37}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=412779 type=86a754 id=f9214d sources=a15266 name_key=fee00d desc_key=425979 kind=356a19 kind_name=9bc378 target=ad4b90 range=902ba3 area=1bac4b cost=2e28a4 cooldown=2be88c effect_kind=356a19 effects=d7877d damage_or_effect=92dfc9 icon=e79476 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Improved Hand](wiki/assets/skills/20212.png) |
| **Skill id** | `20212` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Area** | circle, radius 7, width/angle 7 |
| **Cost** | 40 MP |
| **Effect kind** | damage (physical?) (1) |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 37 |

### Tooltip

> [Passive] When attacked by a basic attack, your Attack Speed increases by 3% for a certain amount of time. (Up to 5 times can be nested)

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 1 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 100 | 0 |
| 3 | 301 | applies buff (variant 301) | [[wiki/buffs/20214-improved-hand-increases-attack-speed\|Improved Hand: Increases attack speed]] | 100 |

**Reading:** amount **1 + 100% Attack**; damage (physical?); applies [[wiki/buffs/20214-improved-hand-increases-attack-speed|Improved Hand: Increases attack speed]] (100%).
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
