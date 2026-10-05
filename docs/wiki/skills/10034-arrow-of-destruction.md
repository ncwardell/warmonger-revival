---
title: "Arrow of Destruction"
type: "skill"
id: 10034
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10034", "client: StringAll_Eng SkillComment_10034 (tooltip value tags)"]
name_key: "Skill_10034"
desc_key: "SkillComment_10034"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
cost: {"type": 5, "type_name": "MP", "amount": 110}
cooldown: {"ms": 14000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 85, "rate": 100}
  - {"slot": 2, "type": 101, "value": 85, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 85, "attack_pct": 85}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 85}
  - {"tag": "EF_R_DAM", "value": 85}
visual: 185
icon: {"file": "Skill_Miriam_01.png", "index": 2}
used_by:
  - {"weapon_base": 122, "slot": 3, "items": [16000]}
---
<!-- generated:start -->
<!-- generated-keys: title=48c923 type=86a754 id=6f2cdc sources=3af859 name_key=dad1bf desc_key=f87b89 kind=356a19 kind_name=9bc378 target=069ef3 range=902ba3 cost=060055 cooldown=5b7687 delivery=93a212 effect_kind=356a19 effects=08ddcc damage_or_effect=5cb3bd tooltip_formula=86cb38 visual=cfa2ed icon=1f5f1b used_by=bbb9ad -->
|  |  |
|---|---|
|  | ![Arrow of Destruction](../assets/skills/10034.png) |
| **Skill id** | `10034` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Cost** | 110 MP |
| **Cooldown** | 14 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 185 `PCM_Bow_01_E_파멸의 화살` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 2 |

### Tooltip

> [Active] Shoot a penetrating arrow that deals `{EF_STATIC 85}``{EF_R_DAM 85}` Damage to the first target it hits. Additionally the target gets knocked back.

Tooltip formula: **85 + 85% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 85 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 85 | 0 |

**Reading:** amount **85 + 85% Attack**; damage (physical?).

### Used by

- Weapon skill **E** of WeaponBase 122: [[wiki/items/16000-magical-shadow-bow|Magical Shadow Bow]]
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
