---
title: "Furious Charge"
type: "skill"
id: 10000
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10000", "client: StringAll_Eng SkillComment_10000 (tooltip value tags)"]
name_key: "Skill_10000"
desc_key: "SkillComment_10000"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
cost: {"type": 5, "type_name": "MP", "amount": 125}
cooldown: {"ms": 17000, "group": 0}
movement: "dash"
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 70, "rate": 100}
  - {"slot": 2, "type": 101, "value": 75, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 70, "attack_pct": 75}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_DAM", "value": 75}
visual: 99
icon: {"file": "Skill_Dolorece_01.png", "index": 0}
used_by:
  - {"weapon_base": 162, "slot": 1, "items": [21020]}
---
<!-- generated:start -->
<!-- generated-keys: title=9f5ab2 type=86a754 id=8a12a3 sources=32726f name_key=f90b82 desc_key=49cf68 kind=356a19 kind_name=9bc378 target=069ef3 range=902ba3 cost=f67772 cooldown=c9c532 movement=5f1488 effect_kind=356a19 effects=d03d6c damage_or_effect=db0edd tooltip_formula=e37e0c visual=9a79be icon=b75792 used_by=2bae00 -->
|  |  |
|---|---|
|  | ![Furious Charge](wiki/assets/skills/10000.png) |
| **Skill id** | `10000` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Cost** | 125 MP |
| **Cooldown** | 17 s |
| **Movement** | dash |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 99 `PCD_Hammer_01_Q_광포한 돌격` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 0 |

### Tooltip

> [Active] Charge to an enemy, damaging it  with `{EF_STATIC 70}``{EF_R_DAM 75}`.

Tooltip formula: **70 + 75% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 75 | 0 |

**Reading:** amount **70 + 75% Attack**; damage (physical?).

### Used by

- Weapon skill **Q** of WeaponBase 162: [[wiki/items/21020-magical-protect-hammer|Magical Protect Hammer]]
- Nation policy 1 `PolicyName_1` (Policy.cdb, server-only; buff_or_skill)
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
