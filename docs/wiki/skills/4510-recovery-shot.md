---
title: "Recovery Shot"
type: "skill"
id: 4510
status: "stub"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 4510", "client: Skill_TP.cdb row 9"]
name_key: "Skill_4510"
desc_key: "SkillComment_4510"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 255
area: {"shape": 1, "shape_name": "circle", "radius": 8.0, "width_or_angle": 8.0}
cost: {"type": 14, "type_name": "TP", "amount": 2500, "from": "Skill_TP"}
cooldown: {"ms": 180000, "group": 0, "from": "Skill_TP"}
effect_kind: 1
effects:
  - {"slot": 1, "type": 324, "value": 10003, "rate": 100}
damage_or_effect: {}
icon: {"file": "Policy_01.png", "index": 40}
used_by: []
tp: {"row": 9, "tp_cost": 2500, "cooldown_s": 180, "need_flags": 396, "c7": 1}
---
<!-- generated:start -->
<!-- generated-keys: title=29fa99 type=86a754 id=244abb sources=91a361 name_key=145372 desc_key=a9b08e kind=356a19 kind_name=9bc378 target=cacd0a range=3028f5 area=950fc9 cost=a7b37a cooldown=c44d13 effect_kind=356a19 effects=eb8dad damage_or_effect=bf21a9 icon=14510d used_by=97d170 tp=e24286 -->
|  |  |
|---|---|
|  | ![Recovery Shot](wiki/assets/skills/4510.png) |
| **Skill id** | `4510` |
| **Kind** | active (1) |
| **Target** | ground; self; units: monster, player; up to 1 |
| **Range** | 255 (world units) |
| **Area** | circle, radius 8, width/angle 8 |
| **Cost** | 2,500 TP |
| **Cooldown** | 180 s |
| **Effect kind** | damage (physical?) (1) |
| **TP skill** | 2,500 TP, 180 s cooldown (Skill_TP row 9) |
| **Icon** | `ui/icons/Policy_01.png` cell 40 |

### Tooltip

> Restores HP of nearby allies.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 324 | unknown | 10,003 | 100 |

### Mentioned in

- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § Shaia Legion donations (line 164): 2 · 6,000,000 · 10% · Recovery Shot · 50
- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § TP skills (line 37): Further client rows not in any guide: I'll be back! (4509), Recovery Shot (4510, 2,500), Fire Support (4512, 2,000), Blind (4514), Create a Portal (4516), Fr...
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
