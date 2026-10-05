---
title: "Immovable bondage"
type: "skill"
id: 5464
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5464", "client: StringAll_Eng SkillComment_5464 (tooltip value tags)"]
name_key: "Skill_5464"
desc_key: "SkillComment_5464"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 120}
cooldown: {"ms": 16000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 80, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10427, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 80, "buffs": [{"buff": 10427, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 80}
visual: 469
icon: {"file": "Skill_Miriam_01.png", "index": 31}
used_by:
  - {"weapon_base": 30, "slot": 3, "items": [15008]}
---
<!-- generated:start -->
<!-- generated-keys: title=bd2e90 type=86a754 id=feba5b sources=66a8b6 name_key=dcbd67 desc_key=1461d3 kind=356a19 kind_name=9bc378 target=d1cc1b range=1b6453 area=6d01a6 cost=deac18 cooldown=a93f07 effect_kind=356a19 effects=4205e0 damage_or_effect=a72026 tooltip_formula=4709a0 visual=e3e097 icon=b6460f used_by=751340 -->
|  |  |
|---|---|
|  | ![Immovable bondage](../assets/skills/5464.png) |
| **Skill id** | `5464` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 120 MP |
| **Cooldown** | 16 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 469 `마력의 은신 대거_지면가르기` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 31 |

### Tooltip

> [Active] Inflicts `{EF_STATIC 80}``{EF_R_DAM 80}` Damage to nearby enemies and traps them for a certain time.

Tooltip formula: **80 + 80% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 80 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10427-immovable-bondage-rooted-in-place-for-2-seconds\|Immovable bondage : Rooted in place for 2 seconds]] | 100 |

**Reading:** amount **80 + 80% Attack**; damage (physical?); applies [[wiki/buffs/10427-immovable-bondage-rooted-in-place-for-2-seconds|Immovable bondage : Rooted in place for 2 seconds]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 30: [[wiki/items/15008-magical-hiding-dagger|Magical hiding Dagger]]
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
