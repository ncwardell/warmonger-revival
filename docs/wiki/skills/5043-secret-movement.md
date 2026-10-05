---
title: "Secret Movement"
type: "skill"
id: 5043
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5043", "client: StringAll_Eng SkillComment_5043 (tooltip value tags)"]
name_key: "Skill_5043"
desc_key: "SkillComment_5043"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 301, "value": 10039, "rate": 100}
  - {"slot": 2, "type": 301, "value": 10040, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 10039, "rate": 100}, {"buff": 10040, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 10}
  - {"tag": "EF_R_DAM", "value": 100}
visual: 194
icon: {"file": "Skill_Miriam_01.png", "index": 4}
used_by:
  - {"weapon_base": 23, "slot": 1, "items": [15001]}
---
<!-- generated:start -->
<!-- generated-keys: title=12d4a7 type=86a754 id=7b46e1 sources=5a1fc5 name_key=9f9334 desc_key=3611c5 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=e4e7cf cooldown=e3989d effect_kind=356a19 effects=eafd27 damage_or_effect=46965f tooltip_formula=e38d4c visual=2a79f1 icon=a12d2b used_by=18e7f1 -->
|  |  |
|---|---|
|  | ![Secret Movement](../assets/skills/5043.png) |
| **Skill id** | `5043` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 194 `PCM_Bow_02_Q 은밀한 움직임` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 4 |

### Tooltip

> [Active] You gain Stealth and move more swiftly. When you choose to attack while hidden, your next basic attack deals `{EF_STATIC 10}``{EF_R_DAM 100}` more damage . The bonus damage is increased by 3% of the targets maximum HP.

Tooltip formula: **10 + 100% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/10039-secret-movement-increases-movement-speed\|Secret Movement: Increases Movement Speed]] | 100 |
| 2 | 301 | applies buff (variant 301) | [[wiki/buffs/10040-secret-movement-your-next-basic-attack-will-deal-additional\|Secret Movement : Your next basic attack will deal additional damage]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/10039-secret-movement-increases-movement-speed|Secret Movement: Increases Movement Speed]] (100%); applies [[wiki/buffs/10040-secret-movement-your-next-basic-attack-will-deal-additional|Secret Movement : Your next basic attack will deal additional damage]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 23: [[wiki/items/15001-magical-sniping-bow|Magical Sniping Bow]]
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
