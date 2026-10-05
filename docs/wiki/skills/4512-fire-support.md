---
title: "Fire Support"
type: "skill"
id: 4512
status: "stub"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 4512", "client: Skill_TP.cdb row 10"]
name_key: "Skill_4512"
desc_key: "SkillComment_4512"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 255
area: {"shape": 1, "shape_name": "circle", "radius": 8.0, "width_or_angle": 8.0}
cost: {"type": 14, "type_name": "TP", "amount": 2000, "from": "Skill_TP"}
cooldown: {"ms": 180000, "group": 0, "from": "Skill_TP"}
effect_kind: 1
effects:
  - {"slot": 1, "type": 324, "value": 10004, "rate": 100}
damage_or_effect: {}
icon: {"file": "Policy_01.png", "index": 43}
used_by: []
tp: {"row": 10, "tp_cost": 2000, "cooldown_s": 180, "need_flags": 396, "c7": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=925671 type=86a754 id=38e2ff sources=1840d4 name_key=02ff76 desc_key=433686 kind=356a19 kind_name=9bc378 target=cacd0a range=3028f5 area=950fc9 cost=03969c cooldown=c44d13 effect_kind=356a19 effects=60b01b damage_or_effect=bf21a9 icon=913d4f used_by=97d170 tp=489443 -->
|  |  |
|---|---|
|  | ![Fire Support](wiki/assets/skills/4512.png) |
| **Skill id** | `4512` |
| **Kind** | active (1) |
| **Target** | ground; self; units: monster, player; up to 1 |
| **Range** | 255 (world units) |
| **Area** | circle, radius 8, width/angle 8 |
| **Cost** | 2,000 TP |
| **Cooldown** | 180 s |
| **Effect kind** | damage (physical?) (1) |
| **TP skill** | 2,000 TP, 180 s cooldown (Skill_TP row 10) |
| **Icon** | `ui/icons/Policy_01.png` cell 43 |

### Tooltip

> Click on a field or Minimap to inflict Damage per second worth 10% of your HP to enemies within a certain radius.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 324 | unknown | 10,004 | 100 |

### Mentioned in

- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § Shaia Legion donations (line 165): 3 · 10,000,000 · 10% · Fire Support · 50
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § 7. TP skill costs (line 181): Fire Support · 2,500 / 180 · 2,000 / 180
- [[gameplay/patch-history|Patch notes and other sources]] § PvP, events, forts (line 36): - TP skill changes (WM 1018): Siege Minion 1000 TP cd 100→60 s, Fortified cd 180→120, Fire Support 2500→2000, I'll be back! 2000→1500, Blind/Portal/Freeze 25...
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
