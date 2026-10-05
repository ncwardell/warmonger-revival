---
title: "Reviving Breath"
type: "skill"
id: 5019
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5019", "client: StringAll_Eng SkillComment_5019 (tooltip value tags)"]
name_key: "Skill_5019"
desc_key: "SkillComment_5019"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["self", "ally"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 8
cost: {"type": 5, "type_name": "MP", "amount": 140}
cooldown: {"ms": 20000, "group": 0}
effect_kind: 31
effects:
  - {"slot": 1, "type": 330, "value": 85, "rate": 100}
  - {"slot": 2, "type": 102, "value": 70, "rate": 0}
damage_or_effect: {"kind": "heal HP", "base": 85, "ability_pct": 70}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 85}
  - {"tag": "EF_R_MDAM", "value": 70}
visual: 209
icon: {"file": "Skill_Einsel_01.png", "index": 9}
used_by:
  - {"weapon_base": 3, "slot": 2, "items": [30002]}
---
<!-- generated:start -->
<!-- generated-keys: title=53e6e2 type=86a754 id=ad1e57 sources=6c25dd name_key=c8e7fd desc_key=77b7d9 kind=356a19 kind_name=9bc378 target=644925 range=fe5dbb cost=911ade cooldown=628d31 effect_kind=632667 effects=7a470e damage_or_effect=1c4cc1 tooltip_formula=705953 visual=acfdd1 icon=aaa141 used_by=26374f -->
|  |  |
|---|---|
|  | ![Reviving Breath](wiki/assets/skills/5019.png) |
| **Skill id** | `5019` |
| **Kind** | active (1) |
| **Target** | unit; self, ally; units: monster, player; up to 1 |
| **Range** | 8 (world units) |
| **Cost** | 140 MP |
| **Cooldown** | 20 s |
| **Effect kind** | heal HP (31) |
| **Visual** | skillVisual 209 `PCE_Staff_03_W_소생의 숨결` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 9 |

### Tooltip

> [Active] Heals your target with `{EF_STATIC 85}``{EF_R_MDAM 70}`

Tooltip formula: **85 + 70% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 85 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 70 | 0 |

**Reading:** amount **85 + 70% Ability Power**; heal HP.

### Used by

- Weapon skill **W** of WeaponBase 3: [[wiki/items/30002-magical-life-wand|Magical Life Wand]]
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
