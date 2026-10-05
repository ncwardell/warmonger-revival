---
title: "Quick Shot"
type: "skill"
id: 10116
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10116", "client: StringAll_Eng SkillComment_10116 (tooltip value tags)"]
name_key: "Skill_10116"
desc_key: "SkillComment_10116"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 8
cost: {"type": 5, "type_name": "MP", "amount": 80}
cooldown: {"ms": 8000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 75, "rate": 100}
  - {"slot": 2, "type": 101, "value": 85, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 75, "attack_pct": 85}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 75}
  - {"tag": "EF_R_DAM", "value": 85}
visual: 249
icon: {"file": "Skill_Dolorece_01.png", "index": 20}
used_by:
  - {"weapon_base": 153, "slot": 1, "items": [21011]}
---
<!-- generated:start -->
<!-- generated-keys: title=c10402 type=86a754 id=ebd0b4 sources=e0ea93 name_key=deb632 desc_key=d5fc89 kind=356a19 kind_name=9bc378 target=069ef3 range=fe5dbb cost=e01d1d cooldown=9ded33 delivery=93a212 effect_kind=356a19 effects=974a50 damage_or_effect=17b953 tooltip_formula=f070eb visual=ee44c6 icon=a792ac used_by=92af4e -->
|  |  |
|---|---|
|  | ![Quick Shot](wiki/assets/skills/10116.png) |
| **Skill id** | `10116` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 8 (world units) |
| **Cost** | 80 MP |
| **Cooldown** | 8 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 249 `PCD_Cannon_02_Q  유탄발사` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 20 |

### Tooltip

> [Active] A single shot that hits the targeted enemy for `{EF_STATIC 75}``{EF_R_DAM 85}` Damage.

Tooltip formula: **75 + 85% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 75 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 85 | 0 |

**Reading:** amount **75 + 85% Attack**; damage (physical?).

### Used by

- Weapon skill **Q** of WeaponBase 153: [[wiki/items/21011-magical-blast-cannon|Magical Blast Cannon]]
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
