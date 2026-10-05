---
title: "Water column"
type: "skill"
id: 20304
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20304", "client: StringAll_Eng SkillComment_20304 (tooltip value tags)"]
name_key: "Skill_20304"
desc_key: "SkillComment_20304"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 6
area: {"shape": 1, "shape_name": "circle", "radius": 5.0, "width_or_angle": 5.0}
cost: {"type": 5, "type_name": "MP", "amount": 50}
cooldown: {"ms": 2000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 60, "rate": 100}
  - {"slot": 2, "type": 102, "value": 20, "rate": 0}
  - {"slot": 3, "type": 133, "value": 5, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 60, "ability_pct": 20, "stats": [{"code": 133, "value": 5}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 60}
  - {"tag": "EF_R_MDAM", "value": 20}
  - {"tag": "EF_R_MAXMANA", "value": 5}
visual: 446
icon: {"file": "Skill_Boss_01.dds", "index": 40}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=78605e type=86a754 id=4698db sources=a4ec7e name_key=7dcbc3 desc_key=258752 kind=356a19 kind_name=9bc378 target=d1cc1b range=c1dfd9 area=e8b0ea cost=7e5cd4 cooldown=367d78 effect_kind=da4b92 effects=9bb3a3 damage_or_effect=cdfdd5 tooltip_formula=389900 visual=5a9295 icon=2eeddb used_by=97d170 -->
|  |  |
|---|---|
|  | ![Water column](wiki/assets/skills/20304.png) |
| **Skill id** | `20304` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 6 (world units) |
| **Area** | circle, radius 5, width/angle 5 |
| **Cost** | 50 MP |
| **Cooldown** | 2 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 446 `피셔_물기둥` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 40 |

### Tooltip

> [Active] Consumes Mana per second, and deals Magic Damage to enemies around you `{EF_STATIC 60}``{EF_R_MDAM 20}``{EF_R_MAXMANA 5}` continuously.

Tooltip formula: **60 + 20% Ability Power + 5% max Mana** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 60 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 20 | 0 |
| 3 | 133 | stat? Mana(%) | 5 | 0 |

**Reading:** amount **60 + 20% Ability Power**; damage (magic?).
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
