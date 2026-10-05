---
title: "Assassination"
type: "skill"
id: 5140
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5140"]
name_key: "Skill_5140"
desc_key: "SkillComment_5140"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["ally", "enemy"], "unit_classes": ["monster", "player"], "max_targets": 2}
range: 7
cost: {"type": 5, "type_name": "MP", "amount": 150}
cooldown: {"ms": 22000, "group": 0}
movement: "blink / teleport"
effect_kind: 1
effects:
  - {"slot": 1, "type": 301, "value": 10169, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 10169, "rate": 100}]}
visual: 281
icon: {"file": "Skill_Miriam_01.png", "index": 25}
used_by:
  - {"weapon_base": 31, "slot": 2, "items": [35009]}
---
<!-- generated:start -->
<!-- generated-keys: title=073578 type=86a754 id=5fb78c sources=ed6c0f name_key=a33d23 desc_key=018b59 kind=356a19 kind_name=9bc378 target=53cfaf range=902ba3 cost=95c2ed cooldown=ba8361 movement=953fcf effect_kind=356a19 effects=56e4bf damage_or_effect=96cb24 visual=d8502b icon=d212e9 used_by=12c142 -->
|  |  |
|---|---|
|  | ![Assassination](wiki/assets/skills/5140.png) |
| **Skill id** | `5140` |
| **Kind** | active (1) |
| **Target** | unit; ally, enemy; units: monster, player; up to 2 |
| **Range** | 7 (world units) |
| **Cost** | 150 MP |
| **Cooldown** | 22 s |
| **Movement** | blink / teleport |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 281 `PCM_Knife_05_W_암살` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 25 |

### Tooltip

> [Active] [Active] Enemy :Enemy: Quickly access the target. The first attack then deals 150% of the damage and silences the enemy. ally: quickly access  to ally.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/10169-assassination-active\|Assassination : Active]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/10169-assassination-active|Assassination : Active]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 31: [[wiki/items/35009-skeleton-king-s-magic-dagger|Skeleton King's Magic Dagger]]
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
