---
title: "Recovery shot"
type: "skill"
id: 4511
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 4511"]
name_key: "Skill_4511"
desc_key: "SkillComment_4511"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "ally"], "unit_classes": ["monster", "player"], "max_targets": 7}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 8.0, "width_or_angle": 8.0}
cost: null
cooldown: null
effect_kind: 31
effects:
  - {"slot": 1, "type": 131, "value": 5, "rate": 1}
damage_or_effect: {"kind": "heal HP", "stats": [{"code": 131, "value": 5}]}
visual: 349
icon: {"file": "Policy_01.png", "index": 40}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=a9c523 type=86a754 id=87ee54 sources=4d83db name_key=504e38 desc_key=e7c717 kind=356a19 kind_name=9bc378 target=e77383 range=1b6453 area=950fc9 cost=2be88c cooldown=2be88c effect_kind=632667 effects=9223b3 damage_or_effect=9e6559 visual=3341b1 icon=14510d used_by=97d170 -->
|  |  |
|---|---|
|  | ![Recovery shot](wiki/assets/skills/4511.png) |
| **Skill id** | `4511` |
| **Kind** | active (1) |
| **Target** | self; self, ally; units: monster, player; up to 7 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 8, width/angle 8 |
| **Effect kind** | heal HP (31) |
| **Visual** | skillVisual 349 `TP_Recovery_shot_피격` |
| **Icon** | `ui/icons/Policy_01.png` cell 40 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 131 | stat? Health(%) | 5 | 1 |

**Reading:** heal HP.

### Mentioned in

- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § Shaia Legion donations (line 164): 2 · 6,000,000 · 10% · Recovery Shot · 50
- [[gameplay/server-rules|Server rules checklist]] § PvP, events, forts (line 153): - [ ] Shaia Legion donations: 200,000 gold/day per player (+1 donation per 100 jewels); 7 weekly tiers 3/6/10/15/25/35/45 M gold → Shaia +10/10/10/20/20/20/3...
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
