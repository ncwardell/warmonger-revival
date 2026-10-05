---
title: "Running Wild"
type: "skill"
id: 10057
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10057"]
name_key: "Skill_10057"
desc_key: "SkillComment_10057"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self", "ally"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 5
cost: {"type": 5, "type_name": "MP", "amount": 70}
cooldown: {"ms": 6000, "group": 0}
movement: "dash"
effect_kind: 0
effects:
  - {"slot": 1, "type": 301, "value": 30051, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 30051, "rate": 100}]}
visual: 109
icon: {"file": "Skill_Miriam_01.png", "index": 22}
used_by:
  - {"weapon_base": 128, "slot": 3, "items": [16006]}
---
<!-- generated:start -->
<!-- generated-keys: title=df0f2d type=86a754 id=0a3025 sources=3ec40c name_key=0a8f64 desc_key=93b750 kind=356a19 kind_name=9bc378 target=6bbbc3 range=ac3478 cost=e3dc9b cooldown=e7a8df movement=5f1488 effect_kind=b6589f effects=ebbf8c damage_or_effect=9f1371 visual=a1422e icon=3f3eba used_by=698d86 -->
|  |  |
|---|---|
|  | ![Running Wild](wiki/assets/skills/10057.png) |
| **Skill id** | `10057` |
| **Kind** | active (1) |
| **Target** | ground; self, ally; units: monster, player; up to 1 |
| **Range** | 5 (world units) |
| **Cost** | 70 MP |
| **Cooldown** | 6 s |
| **Movement** | dash |
| **Visual** | skillVisual 109 `PCM_Knife_02_E_야성의 질주` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 22 |

### Tooltip

> [Active] Dash to the targeted location and Gain 100 additional Attack Speed for 5 second.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/30051-running-wild-increased-attack-speed\|Running Wild : Increased Attack Speed]] | 100 |

**Reading:** applies [[wiki/buffs/30051-running-wild-increased-attack-speed|Running Wild : Increased Attack Speed]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 128: [[wiki/items/16006-magical-blood-dagger|Magical Blood Dagger]]
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
