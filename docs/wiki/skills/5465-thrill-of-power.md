---
title: "Thrill of Power"
type: "skill"
id: 5465
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5465"]
name_key: "Skill_5465"
desc_key: "SkillComment_5465"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 5, "type_name": "MP", "amount": 390}
cooldown: {"ms": 70000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 301, "value": 10425, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 10425, "rate": 100}]}
visual: 470
icon: {"file": "Skill_Miriam_01.png", "index": 32}
used_by:
  - {"weapon_base": 30, "slot": 4, "items": [15008]}
---
<!-- generated:start -->
<!-- generated-keys: title=d9423c type=86a754 id=03de34 sources=3e4122 name_key=14bddd desc_key=bc3dd2 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=ff5a60 cooldown=ad2ac8 effect_kind=356a19 effects=96f66e damage_or_effect=24180c visual=264c3f icon=bf4234 used_by=e73926 -->
|  |  |
|---|---|
|  | ![Thrill of Power](../assets/skills/5465.png) |
| **Skill id** | `5465` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 390 MP |
| **Cooldown** | 70 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 470 `마력의 은신 대거_급소노리기` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 32 |

### Tooltip

> [Active] Your Critical Strike Damage increases significantly.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/10425-the-thrill-of-power-critical-damage-increase\|The thrill of power : Critical Damage Increase]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/10425-the-thrill-of-power-critical-damage-increase|The thrill of power : Critical Damage Increase]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 30: [[wiki/items/15008-magical-hiding-dagger|Magical hiding Dagger]]
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
