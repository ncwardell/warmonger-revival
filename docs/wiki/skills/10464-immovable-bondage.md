---
title: "Immovable bondage"
type: "skill"
id: 10464
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10464", "client: StringAll_Eng SkillComment_10464 (tooltip value tags)"]
name_key: "Skill_10464"
desc_key: "SkillComment_10464"
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
  - {"slot": 2, "type": 101, "value": 85, "rate": 0}
  - {"slot": 3, "type": 314, "value": 30427, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 85, "buffs": [{"buff": 30427, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 85}
visual: 469
icon: {"file": "Skill_Miriam_01.png", "index": 31}
used_by:
  - {"weapon_base": 130, "slot": 3, "items": [16008]}
---
<!-- generated:start -->
<!-- generated-keys: title=bd2e90 type=86a754 id=d6256a sources=caced2 name_key=49a0a4 desc_key=162468 kind=356a19 kind_name=9bc378 target=d1cc1b range=1b6453 area=6d01a6 cost=deac18 cooldown=a93f07 effect_kind=356a19 effects=abf8f7 damage_or_effect=ba8c71 tooltip_formula=de4d81 visual=e3e097 icon=b6460f used_by=885c99 -->
|  |  |
|---|---|
|  | ![Immovable bondage](wiki/assets/skills/10464.png) |
| **Skill id** | `10464` |
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

> [Active] Inflicts `{EF_STATIC 80}``{EF_R_DAM 85}` Damage to nearby enemies and traps them for a certain time.

Tooltip formula: **80 + 85% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 85 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/30427-immovable-bondage-rooted-in-place-for-2-seconds\|Immovable bondage : Rooted in place for 2 seconds]] | 100 |

**Reading:** amount **80 + 85% Attack**; damage (physical?); applies [[wiki/buffs/30427-immovable-bondage-rooted-in-place-for-2-seconds|Immovable bondage : Rooted in place for 2 seconds]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 130: [[wiki/items/16008-magical-hiding-dagger|Magical hiding Dagger]]
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
