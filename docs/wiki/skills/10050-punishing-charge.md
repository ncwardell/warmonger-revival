---
title: "Punishing Charge"
type: "skill"
id: 10050
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10050"]
name_key: "Skill_10050"
desc_key: "SkillComment_10050"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self", "ally"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 8.0, "width_or_angle": 1.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 120}
cooldown: {"ms": 16000, "group": 0}
movement: "dash"
effect_kind: 0
effects:
  - {"slot": 1, "type": 301, "value": 30045, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 30045, "rate": 100}]}
requirements:
  - {"type": 30045, "a": 5, "b": 10051}
visual: 171
icon: {"file": "Skill_Einsel_01.png", "index": 21}
used_by:
  - {"weapon_base": 116, "slot": 2, "items": [11015]}
---
<!-- generated:start -->
<!-- generated-keys: title=92808c type=86a754 id=9d798b sources=05e117 name_key=47723e desc_key=9e4a44 kind=356a19 kind_name=9bc378 target=6bbbc3 range=902ba3 area=fbbe31 cost=deac18 cooldown=a93f07 movement=5f1488 effect_kind=b6589f effects=c73b9d damage_or_effect=891017 requirements=fe4bfa visual=94940e icon=83e0e4 used_by=80ddcc -->
|  |  |
|---|---|
|  | ![Punishing Charge](../assets/skills/10050.png) |
| **Skill id** | `10050` |
| **Kind** | active (1) |
| **Target** | ground; self, ally; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Area** | line / rectangle?, radius 8, width/angle 1 (indicator `stick256x512.png`) |
| **Cost** | 120 MP |
| **Cooldown** | 16 s |
| **Movement** | dash |
| **Visual** | skillVisual 171 `PCE_Knife_01_W 돌진 (형벌의 인장: 돌진)` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 21 |

### Tooltip

> [Active] Charge to the designated area, enabling you to use Punishing Stomp.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/30045-punishing-charge-you-are-able-to-use-punishing-stomp-now\|Punishing Charge : You are able to use Punishing Stomp now]] | 100 |

**Reading:** applies [[wiki/buffs/30045-punishing-charge-you-are-able-to-use-punishing-stomp-now|Punishing Charge : You are able to use Punishing Stomp now]] (100%).

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 30045 | 5 | 10051 |

### Used by

- Weapon skill **W** of WeaponBase 116: [[wiki/items/11015-magical-dash-blade|Magical Dash Blade]]
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
