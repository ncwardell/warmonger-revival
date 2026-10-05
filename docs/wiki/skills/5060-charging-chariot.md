---
title: "Charging Chariot"
type: "skill"
id: 5060
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5060", "client: StringAll_Eng SkillComment_5060 (tooltip value tags)"]
name_key: "Skill_5060"
desc_key: "SkillComment_5060"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
cost: {"type": 5, "type_name": "MP", "amount": 190}
cooldown: {"ms": 30000, "group": 0}
movement: "dash"
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 75, "rate": 100}
  - {"slot": 2, "type": 101, "value": 100, "rate": 0}
  - {"slot": 3, "type": 301, "value": 10053, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 75, "attack_pct": 100, "buffs": [{"buff": 10053, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 75}
  - {"tag": "EF_R_DAM", "value": 100}
visual: 114
icon: {"file": "Skill_Dolorece_01.png", "index": 9}
used_by:
  - {"weapon_base": 44, "slot": 2, "items": [20002]}
---
<!-- generated:start -->
<!-- generated-keys: title=e01132 type=86a754 id=5568a4 sources=b6f52a name_key=9a89f3 desc_key=ee0371 kind=356a19 kind_name=9bc378 target=069ef3 range=902ba3 cost=9b32a5 cooldown=6963fe movement=5f1488 effect_kind=356a19 effects=79d89b damage_or_effect=f13128 tooltip_formula=8dec14 visual=ecb793 icon=aa3f54 used_by=e70b06 -->
|  |  |
|---|---|
|  | ![Charging Chariot](wiki/assets/skills/5060.png) |
| **Skill id** | `5060` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Cost** | 190 MP |
| **Cooldown** | 30 s |
| **Movement** | dash |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 114 `PCD_Hammer_03_W_돌격전차` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 9 |

### Tooltip

> [Active] Charge to an enemy, damaging them with `{EF_STATIC 75}``{EF_R_DAM 100}`. Gain 100 additional Movement Speed for 5 seconds.

Tooltip formula: **75 + 100% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 75 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 100 | 0 |
| 3 | 301 | applies buff (variant 301) | [[wiki/buffs/10053-charging-chariot-additional-100-movement-speed-for-5-seconds\|Charging Chariot : Additional 100 Movement Speed for 5 seconds]] | 100 |

**Reading:** amount **75 + 100% Attack**; damage (physical?); applies [[wiki/buffs/10053-charging-chariot-additional-100-movement-speed-for-5-seconds|Charging Chariot : Additional 100 Movement Speed for 5 seconds]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 44: [[wiki/items/20002-magical-dash-hammer|Magical Dash Hammer]]
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
