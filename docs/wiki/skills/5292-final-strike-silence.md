---
title: "Final Strike : Silence"
type: "skill"
id: 5292
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5292", "client: StringAll_Eng SkillComment_5292 (tooltip value tags)"]
name_key: "Skill_5292"
desc_key: "SkillComment_5292"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 7}
range: 5
area: {"shape": 1, "shape_name": "circle", "radius": 5.0, "width_or_angle": 5.0}
cost: {"type": 5, "type_name": "MP", "amount": 390}
cooldown: {"ms": 70000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 100, "rate": 100}
  - {"slot": 2, "type": 102, "value": 90, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10348, "rate": 100}
  - {"slot": 4, "type": 302, "value": 10346, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 100, "ability_pct": 90, "buffs": [{"buff": 10348, "rate": 100}, {"buff": 10346, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 100}
  - {"tag": "EF_R_MDAM", "value": 90}
visual: 377
icon: {"file": "Skill_Miriam_01.png", "index": 28}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=fdc0e3 type=86a754 id=9bb397 sources=3c6b0b name_key=448a04 desc_key=8f692f kind=356a19 kind_name=9bc378 target=6ca14a range=ac3478 area=e8b0ea cost=ff5a60 cooldown=ad2ac8 effect_kind=da4b92 effects=2279ea damage_or_effect=149e73 tooltip_formula=8510b3 visual=be4d97 icon=70aa6a used_by=97d170 -->
|  |  |
|---|---|
|  | ![Final Strike : Silence](wiki/assets/skills/5292.png) |
| **Skill id** | `5292` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 7 |
| **Range** | 5 (world units) |
| **Area** | circle, radius 5, width/angle 5 |
| **Cost** | 390 MP |
| **Cooldown** | 70 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 377 `시즌1_PCM_Knife_05_R_최후의 한방_침묵` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 28 |

### Tooltip

> [Active] Deals `{EF_STATIC 100}``{EF_R_MDAM 90}` Damage and silences nearby enemies. When used, your Shield will disappear.

Tooltip formula: **100 + 90% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 100 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 90 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10348-final-strikes-silenced-for-2-second\|Final Strikes : Silenced for 2 second.]] | 100 |
| 4 | 302 | applies buff (variant 302) | [[wiki/buffs/10346-final-strikes-creates-a-absorvs-damage-for-10-seconds\|Final Strikes : Creates a absorvs damage for 10 seconds]] | 100 |

**Reading:** amount **100 + 90% Ability Power**; damage (magic?); applies [[wiki/buffs/10348-final-strikes-silenced-for-2-second|Final Strikes : Silenced for 2 second.]] (100%); applies [[wiki/buffs/10346-final-strikes-creates-a-absorvs-damage-for-10-seconds|Final Strikes : Creates a absorvs damage for 10 seconds]] (100%).
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
