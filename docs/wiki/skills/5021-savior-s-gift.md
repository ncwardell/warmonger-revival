---
title: "Savior's Gift"
type: "skill"
id: 5021
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5021", "client: StringAll_Eng SkillComment_5021 (tooltip value tags)"]
name_key: "Skill_5021"
desc_key: "SkillComment_5021"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "party"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 1
area: {"shape": 1, "shape_name": "circle", "radius": 8.0, "width_or_angle": 8.0}
cost: {"type": 5, "type_name": "MP", "amount": 490}
cooldown: {"ms": 90000, "group": 0}
effect_kind: 31
effects:
  - {"slot": 1, "type": 131, "value": 10, "rate": 1}
  - {"slot": 2, "type": 102, "value": 30, "rate": 0}
damage_or_effect: {"kind": "heal HP", "stats": [{"code": 131, "value": 10}], "ability_pct": 30}
tooltip_formula:
  - {"tag": "EF_R_MDAM", "value": 30}
visual: 208
icon: {"file": "Skill_Einsel_01.png", "index": 11}
used_by:
  - {"weapon_base": 3, "slot": 4, "items": [30002]}
---
<!-- generated:start -->
<!-- generated-keys: title=eee00b type=86a754 id=7093f6 sources=690012 name_key=1d2740 desc_key=70c376 kind=356a19 kind_name=9bc378 target=55b685 range=356a19 area=950fc9 cost=cb4f2a cooldown=bc9744 effect_kind=632667 effects=008304 damage_or_effect=c50c3b tooltip_formula=2bf440 visual=baab34 icon=5095da used_by=c3ffec -->
|  |  |
|---|---|
|  | ![Savior's Gift](../assets/skills/5021.png) |
| **Skill id** | `5021` |
| **Kind** | active (1) |
| **Target** | self; self, party; units: monster, player; up to 5 |
| **Range** | 1 (world units) |
| **Area** | circle, radius 8, width/angle 8 |
| **Cost** | 490 MP |
| **Cooldown** | 90 s |
| **Effect kind** | heal HP (31) |
| **Visual** | skillVisual 208 `PCE_Staff_03_R_구원의 선물` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 11 |

### Tooltip

> [Active] Heals all party nearby with 10% of their missing HP plus and additional `{EF_R_MDAM 30}`.

Tooltip formula: **30% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 131 | stat? Health(%) | 10 | 1 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 30 | 0 |

**Reading:** amount **30% Ability Power**; heal HP.

### Used by

- Weapon skill **R** of WeaponBase 3: [[wiki/items/30002-magical-life-wand|Magical Life Wand]]
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
