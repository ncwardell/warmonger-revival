---
title: "Hunting Eye"
type: "skill"
id: 20216
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20216"]
name_key: "Skill_20216"
desc_key: "SkillComment_20216"
kind: 2
kind_name: "passive"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
cost: null
cooldown: null
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 1, "rate": 100}
  - {"slot": 2, "type": 101, "value": 100, "rate": 0}
  - {"slot": 3, "type": 314, "value": 20207, "rate": 100}
  - {"slot": 4, "type": 301, "value": 20214, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 1, "attack_pct": 100, "buffs": [{"buff": 20207, "rate": 100}, {"buff": 20214, "rate": 100}]}
visual: 430
icon: {"file": "Skill_Boss_01.dds", "index": 33}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=64c9d2 type=86a754 id=5c6f19 sources=13de60 name_key=f7e07c desc_key=38c75c kind=da4b92 kind_name=3844d5 target=069ef3 range=902ba3 cost=2be88c cooldown=2be88c effect_kind=356a19 effects=80689a damage_or_effect=cc6ce8 visual=f8c024 icon=2fe3b0 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Hunting Eye](../assets/skills/20216.png) |
| **Skill id** | `20216` |
| **Kind** | passive (2) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 430 `아르타모스_사냥의 눈 평타 이펙트` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 33 |

### Tooltip

> [Passive] When an enemy is hit by a basic attack, the enemy's Defense decreases by 4% for a certain amount of time. (Up to 5 times.)

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 1 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 100 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/20207-hunting-eye-reduced-armor\|Hunting Eye: Reduced armor]] | 100 |
| 4 | 301 | applies buff (variant 301) | [[wiki/buffs/20214-improved-hand-increases-attack-speed\|Improved Hand: Increases attack speed]] | 100 |

**Reading:** amount **1 + 100% Attack**; damage (physical?); applies [[wiki/buffs/20207-hunting-eye-reduced-armor|Hunting Eye: Reduced armor]] (100%); applies [[wiki/buffs/20214-improved-hand-increases-attack-speed|Improved Hand: Increases attack speed]] (100%).
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
