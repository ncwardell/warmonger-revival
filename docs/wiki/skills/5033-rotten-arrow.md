---
title: "Rotten Arrow"
type: "skill"
id: 5033
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5033", "client: StringAll_Eng SkillComment_5033 (tooltip value tags)"]
name_key: "Skill_5033"
desc_key: "SkillComment_5033"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 80, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10030, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 80, "buffs": [{"buff": 10030, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 80}
visual: 184
icon: {"file": "Skill_Miriam_01.png", "index": 1}
used_by:
  - {"weapon_base": 22, "slot": 2, "items": [15000]}
---
<!-- generated:start -->
<!-- generated-keys: title=a39ed8 type=86a754 id=5eeadd sources=ff8a2c name_key=efbb29 desc_key=f89521 kind=356a19 kind_name=9bc378 target=069ef3 range=902ba3 cost=e4e7cf cooldown=e3989d delivery=93a212 effect_kind=356a19 effects=a1126c damage_or_effect=064680 tooltip_formula=4709a0 visual=bcf814 icon=a498d1 used_by=e7ba6e -->
|  |  |
|---|---|
|  | ![Rotten Arrow](../assets/skills/5033.png) |
| **Skill id** | `5033` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 184 `PCM_Bow_01_W_부패의 손길` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 1 |

### Tooltip

> [Active] Shoot a poisonous arrow that inflicts `{EF_STATIC 80}``{EF_R_DAM 80}` Damage for 4 seconds.

Tooltip formula: **80 + 80% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 80 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10030-rotten-arrow-damage-over-time\|Rotten Arrow: Damage over time]] | 100 |

**Reading:** amount **80 + 80% Attack**; damage (physical?); applies [[wiki/buffs/10030-rotten-arrow-damage-over-time|Rotten Arrow: Damage over time]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 22: [[wiki/items/15000-magical-shadow-bow|Magical Shadow Bow]]
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
