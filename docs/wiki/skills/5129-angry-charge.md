---
title: "Angry Charge"
type: "skill"
id: 5129
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5129", "client: StringAll_Eng SkillComment_5129 (tooltip value tags)"]
name_key: "Skill_5129"
desc_key: "SkillComment_5129"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
cost: {"type": 5, "type_name": "MP", "amount": 120}
cooldown: {"ms": 16000, "group": 0}
movement: "dash"
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 75, "rate": 100}
  - {"slot": 2, "type": 101, "value": 80, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10152, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 75, "attack_pct": 80, "buffs": [{"buff": 10152, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 75}
  - {"tag": "EF_R_DAM", "value": 80}
visual: 268
icon: {"file": "Skill_Dolorece_01.png", "index": 24}
used_by:
  - {"weapon_base": 46, "slot": 1, "items": [20004]}
---
<!-- generated:start -->
<!-- generated-keys: title=66742f type=86a754 id=1a7cb6 sources=d48d25 name_key=d87882 desc_key=e54e3d kind=356a19 kind_name=9bc378 target=069ef3 range=902ba3 cost=deac18 cooldown=a93f07 movement=5f1488 effect_kind=356a19 effects=bd0c4f damage_or_effect=082907 tooltip_formula=74c011 visual=d5f0d9 icon=4c901c used_by=3711bb -->
|  |  |
|---|---|
|  | ![Angry Charge](wiki/assets/skills/5129.png) |
| **Skill id** | `5129` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Cost** | 120 MP |
| **Cooldown** | 16 s |
| **Movement** | dash |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 268 `PCD_Hammer_05_Q_분노의돌진` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 24 |

### Tooltip

> [Active] Charge to an enemy, damaging them with `{EF_STATIC 75}``{EF_R_DAM 80}`.

Tooltip formula: **75 + 80% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 75 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 80 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10152-angry-charge\|Angry Charge]] | 100 |

**Reading:** amount **75 + 80% Attack**; damage (physical?); applies [[wiki/buffs/10152-angry-charge|Angry Charge]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 46: [[wiki/items/20004-skeleton-king-s-magic-hammer|Skeleton King's Magic Hammer]]
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
