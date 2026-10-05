---
title: "Flame armor"
type: "skill"
id: 5271
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5271", "client: StringAll_Eng SkillComment_5271 (tooltip value tags)"]
name_key: "Skill_5271"
desc_key: "SkillComment_5271"
kind: 3
kind_name: "kind 3"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 50}
cooldown: {"ms": 2000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 301, "value": 10335, "rate": 100}
  - {"slot": 2, "type": 321, "value": 10335, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 10335, "rate": 100}, {"buff": 10335, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 30}
requirements:
  - {"type": 10335, "a": 4, "b": 0}
icon: {"file": "Skill_Einsel_01.png", "index": 37}
used_by:
  - {"weapon_base": 6, "slot": 2, "items": [10005]}
---
<!-- generated:start -->
<!-- generated-keys: title=3b8f74 type=86a754 id=a1d3c8 sources=4a7dd8 name_key=0ac93a desc_key=58bb3f kind=77de68 kind_name=78ea43 target=d1cc1b range=1b6453 area=6d01a6 cost=7e5cd4 cooldown=367d78 effect_kind=356a19 effects=b80dd3 damage_or_effect=436184 tooltip_formula=4e7b45 requirements=df8b11 icon=04a3fd used_by=f3a78b -->
|  |  |
|---|---|
|  | ![Flame armor](../assets/skills/5271.png) |
| **Skill id** | `5271` |
| **Kind** | kind 3 (3) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 50 MP |
| **Cooldown** | 2 s |
| **Effect kind** | damage (physical?) (1) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 37 |

### Tooltip

> [Active] Use Mana per second and deal `{EF_STATIC 80}``{EF_R_DAM 30}` Damage to all nearby enemies.

Tooltip formula: **80 + 30% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/10335\|Buff 10335]] | 100 |
| 2 | 321 | applies buff (variant 321) | [[wiki/buffs/10335\|Buff 10335]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/10335|Buff 10335]] (100%); applies [[wiki/buffs/10335|Buff 10335]] (100%).

### Requirements

`Skill_Base` requirement slots (type 1 = needs a buff or item, checked by `FUN_004b981e` / `FUN_004b98ee`; other types not decoded):

| type | a | b |
|---|---|---|
| 10335 | 4 | 0 |

### Used by

- Weapon skill **W** of WeaponBase 6: [[wiki/items/10005-magical-blade-shield-flame|Magical Blade Shield : Flame]]
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
