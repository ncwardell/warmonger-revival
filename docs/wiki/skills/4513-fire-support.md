---
title: "Fire Support"
type: "skill"
id: 4513
status: "stub"
missing: ["cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 4513"]
name_key: "Skill_4513"
desc_key: "SkillComment_4513"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 10}
range: 8
area: {"shape": 1, "shape_name": "circle", "radius": 8.0, "width_or_angle": 8.0}
cost: null
cooldown: null
effect_kind: 15
effects:
  - {"slot": 1, "type": 131, "value": 10, "rate": 1}
  - {"slot": 2, "type": 314, "value": 4512, "rate": 100}
damage_or_effect: {"kind": "effect kind 15", "stats": [{"code": 131, "value": 10}], "buffs": [{"buff": 4512, "rate": 100}]}
visual: 347
icon: {"file": "Policy_01.png", "index": 43}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=925671 type=86a754 id=59742a sources=110e59 name_key=378901 desc_key=2832bf kind=356a19 kind_name=9bc378 target=9dc90e range=fe5dbb area=950fc9 cost=2be88c cooldown=2be88c effect_kind=f1abd6 effects=5e5352 damage_or_effect=c20b74 visual=1b04f2 icon=913d4f used_by=97d170 -->
|  |  |
|---|---|
|  | ![Fire Support](wiki/assets/skills/4513.png) |
| **Skill id** | `4513` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 10 |
| **Range** | 8 (world units) |
| **Area** | circle, radius 8, width/angle 8 |
| **Effect kind** | ? (15) |
| **Visual** | skillVisual 347 `TP_Support_Shooting_피격` |
| **Icon** | `ui/icons/Policy_01.png` cell 43 |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 131 | stat? Health(%) | 10 | 1 |
| 2 | 314 | applies buff (variant 314) | [[wiki/buffs/4512\|Buff 4512]] | 100 |

**Reading:** effect kind 15; applies [[wiki/buffs/4512|Buff 4512]] (100%).

### Mentioned in

- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § Shaia Legion donations (line 165): 3 · 10,000,000 · 10% · Fire Support · 50
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § 7. TP skill costs (line 181): Fire Support · 2,500 / 180 · 2,000 / 180
- [[gameplay/patch-history|Patch notes and other sources]] § PvP, events, forts (line 36): - TP skill changes (WM 1018): Siege Minion 1000 TP cd 100→60 s, Fortified cd 180→120, Fire Support 2500→2000, I'll be back! 2000→1500, Blind/Portal/Freeze 25...
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
