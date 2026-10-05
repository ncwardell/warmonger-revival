---
title: "Assassination"
type: "skill"
id: 5289
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5289"]
name_key: "Skill_5289"
desc_key: "SkillComment_5289"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["ally", "enemy"], "unit_classes": ["monster", "player"], "max_targets": 2}
range: 7
cost: {"type": 5, "type_name": "MP", "amount": 100}
cooldown: {"ms": 12000, "group": 0}
movement: "blink / teleport"
effect_kind: 1
effects:
  - {"slot": 1, "type": 301, "value": 10343, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 10343, "rate": 100}]}
visual: 374
icon: {"file": "Skill_Miriam_01.png", "index": 25}
used_by:
  - {"weapon_base": 66, "slot": 2, "items": [15009]}
---
<!-- generated:start -->
<!-- generated-keys: title=073578 type=86a754 id=c9ca1d sources=c63e98 name_key=c94ba5 desc_key=7a4971 kind=356a19 kind_name=9bc378 target=53cfaf range=902ba3 cost=4e8ae0 cooldown=d1c73e movement=953fcf effect_kind=356a19 effects=64e0da damage_or_effect=65e64a visual=4a0e88 icon=d212e9 used_by=e338f9 -->
|  |  |
|---|---|
|  | ![Assassination](wiki/assets/skills/5289.png) |
| **Skill id** | `5289` |
| **Kind** | active (1) |
| **Target** | unit; ally, enemy; units: monster, player; up to 2 |
| **Range** | 7 (world units) |
| **Cost** | 100 MP |
| **Cooldown** | 12 s |
| **Movement** | blink / teleport |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 374 `시즌1_PCM_Knife_05_W_암살` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 25 |

### Tooltip

> [Active] Enemy : Quickly access the target. The first attack thereafter takes on 150 % of the damage. ally: quickly access  to ally.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/10343-assassination-active\|Assassination : Active]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/10343-assassination-active|Assassination : Active]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 66: [[wiki/items/15009-skeleton-king-s-magic-dagger|Skeleton King's Magic Dagger]]
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
