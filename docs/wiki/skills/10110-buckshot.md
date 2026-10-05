---
title: "Buckshot"
type: "skill"
id: 10110
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10110", "client: StringAll_Eng SkillComment_10110 (tooltip value tags)"]
name_key: "Skill_10110"
desc_key: "SkillComment_10110"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 12}
range: 10
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 85, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 85}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 85}
visual: 247
icon: {"file": "Skill_Dolorece_01.png", "index": 18}
used_by:
  - {"weapon_base": 163, "slot": 3, "items": [21021]}
---
<!-- generated:start -->
<!-- generated-keys: title=79454d type=86a754 id=089e94 sources=e787d6 name_key=c06fde desc_key=6c5f6a kind=356a19 kind_name=9bc378 target=138a60 range=b1d578 cost=e4e7cf cooldown=e3989d delivery=93a212 effect_kind=356a19 effects=e933c6 damage_or_effect=f00589 tooltip_formula=de4d81 visual=b4ef7d icon=54219d used_by=66c67e -->
|  |  |
|---|---|
|  | ![Buckshot](wiki/assets/skills/10110.png) |
| **Skill id** | `10110` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 12 |
| **Range** | 10 (world units) |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 247 `PCD_Cannon_01_E 산탄 발사` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 18 |

### Tooltip

> [Active] Deals `{EF_STATIC 80}``{EF_R_DAM 85}` Damage to all enemies hit.

Tooltip formula: **80 + 85% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 85 | 0 |

**Reading:** amount **80 + 85% Attack**; damage (physical?).

### Used by

- Weapon skill **E** of WeaponBase 163: [[wiki/items/21021-magical-protect-cannon|Magical Protect Cannon]]
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
