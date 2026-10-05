---
title: "Thunder bolt"
type: "skill"
id: 5303
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5303", "client: StringAll_Eng SkillComment_5303 (tooltip value tags)"]
name_key: "Skill_5303"
desc_key: "SkillComment_5303"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
cost: {"type": 5, "type_name": "MP", "amount": 110}
cooldown: {"ms": 14000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 102, "value": 70, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 80, "ability_pct": 70}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_MDAM", "value": 70}
visual: 392
icon: {"file": "Skill_Einsel_01.png", "index": 4}
used_by:
  - {"weapon_base": 5, "slot": 1, "items": [10004]}
---
<!-- generated:start -->
<!-- generated-keys: title=46d857 type=86a754 id=656429 sources=760b4d name_key=f1ea09 desc_key=a8d50d kind=356a19 kind_name=9bc378 target=069ef3 range=902ba3 cost=060055 cooldown=5b7687 delivery=93a212 effect_kind=da4b92 effects=7da3e1 damage_or_effect=8faab9 tooltip_formula=343e6f visual=0715d5 icon=fc253c used_by=ee8b07 -->
|  |  |
|---|---|
|  | ![Thunder bolt](../assets/skills/5303.png) |
| **Skill id** | `5303` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Cost** | 110 MP |
| **Cooldown** | 14 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 392 `시즌2_PCE_Staff_01_Q_광휘의 일격` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 4 |

### Tooltip

> [Active] Blast an enemy unit with `{EF_STATIC 80}``{EF_R_MDAM 70}`.

Tooltip formula: **80 + 70% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 70 | 0 |

**Reading:** amount **80 + 70% Ability Power**; damage (magic?).

### Used by

- Weapon skill **Q** of WeaponBase 5: [[wiki/items/10004-tempest-s-magical-wand|Tempest's magical wand]]
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
