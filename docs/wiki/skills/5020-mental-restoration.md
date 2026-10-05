---
title: "Mental Restoration"
type: "skill"
id: 5020
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5020", "client: StringAll_Eng SkillComment_5020 (tooltip value tags)"]
name_key: "Skill_5020"
desc_key: "SkillComment_5020"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["ally"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 8
cost: {"type": 5, "type_name": "MP", "amount": 130}
cooldown: {"ms": 18000, "group": 0}
effect_kind: 33
effects:
  - {"slot": 1, "type": 330, "value": 85, "rate": 100}
  - {"slot": 2, "type": 102, "value": 70, "rate": 0}
damage_or_effect: {"kind": "restore MP", "base": 85, "ability_pct": 70}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 85}
  - {"tag": "EF_R_MDAM", "value": 70}
visual: 210
icon: {"file": "Skill_Einsel_01.png", "index": 10}
used_by:
  - {"weapon_base": 3, "slot": 3, "items": [30002]}
---
<!-- generated:start -->
<!-- generated-keys: title=1b80c5 type=86a754 id=6b35a9 sources=a2c625 name_key=fe26f1 desc_key=5a6ed4 kind=356a19 kind_name=9bc378 target=8b0de6 range=fe5dbb cost=58a4ca cooldown=133145 effect_kind=b6692e effects=7a470e damage_or_effect=885781 tooltip_formula=705953 visual=135deb icon=3e4948 used_by=2ca8b9 -->
|  |  |
|---|---|
|  | ![Mental Restoration](wiki/assets/skills/5020.png) |
| **Skill id** | `5020` |
| **Kind** | active (1) |
| **Target** | unit; ally; units: monster, player; up to 1 |
| **Range** | 8 (world units) |
| **Cost** | 130 MP |
| **Cooldown** | 18 s |
| **Effect kind** | restore MP (33) |
| **Visual** | skillVisual 210 `PCE_Staff_03_E_정기의 물결` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 10 |

### Tooltip

> [Active] Restores `{EF_STATIC 85}``{EF_R_MDAM 70}` Mana on your target.

Tooltip formula: **85 + 70% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 85 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 70 | 0 |

**Reading:** amount **85 + 70% Ability Power**; restore MP.

### Used by

- Weapon skill **E** of WeaponBase 3: [[wiki/items/30002-magical-life-wand|Magical Life Wand]]
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
