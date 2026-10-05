---
title: "Furious Charge"
type: "skill"
id: 5000
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5000", "client: StringAll_Eng SkillComment_5000 (tooltip value tags)"]
name_key: "Skill_5000"
desc_key: "SkillComment_5000"
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
  - {"slot": 2, "type": 101, "value": 70, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 70, "attack_pct": 70}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_DAM", "value": 70}
visual: 99
icon: {"file": "Skill_Dolorece_01.png", "index": 0}
used_by:
  - {"weapon_base": 62, "slot": 1, "items": [20020]}
---
<!-- generated:start -->
<!-- generated-keys: title=9f5ab2 type=86a754 id=f8237d sources=e20da3 name_key=d0fd74 desc_key=607e3a kind=356a19 kind_name=9bc378 target=069ef3 range=902ba3 cost=f67772 cooldown=c9c532 movement=5f1488 effect_kind=356a19 effects=6c7a8d damage_or_effect=f8bea5 tooltip_formula=63cff8 visual=9a79be icon=b75792 used_by=e3404d -->
|  |  |
|---|---|
|  | ![Furious Charge](wiki/assets/skills/5000.png) |
| **Skill id** | `5000` |
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

> [Active] Charge to an enemy, damaging it  with `{EF_STATIC 70}``{EF_R_DAM 70}`.

Tooltip formula: **70 + 70% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 70 | 0 |

**Reading:** amount **70 + 70% Attack**; damage (physical?).

### Used by

- Weapon skill **Q** of WeaponBase 62: [[wiki/items/20020-magical-protect-hammer|Magical Protect Hammer]]
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
