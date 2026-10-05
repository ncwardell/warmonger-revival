---
title: "I'll be back!"
type: "skill"
id: 4509
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 4509", "client: Skill_TP.cdb row 8"]
name_key: "Skill_4509"
desc_key: "SkillComment_4509"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self", "ally"], "unit_classes": ["player", "structure"], "max_targets": 1}
range: 255
area: {"shape": 1, "shape_name": "circle", "radius": 255.0, "width_or_angle": 255.0}
cost: {"type": 14, "type_name": "TP", "amount": 1500, "from": "Skill_TP"}
cooldown: {"ms": 120000, "group": 0, "from": "Skill_TP"}
effect_kind: 0
effects:
  - {"slot": 1, "type": 460, "value": 4509, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 4509, "rate": 100}]}
icon: {"file": "Policy_01.png", "index": 45}
used_by: []
tp: {"row": 8, "tp_cost": 1500, "cooldown_s": 120, "need_flags": 0, "c7": 1}
---
<!-- generated:start -->
<!-- generated-keys: title=211a26 type=86a754 id=27e5a2 sources=ed5ef6 name_key=7983b4 desc_key=5880d1 kind=356a19 kind_name=9bc378 target=d97d2d range=3028f5 area=febbd1 cost=4e6c0e cooldown=d97414 effect_kind=b6589f effects=e2b3fa damage_or_effect=b57969 icon=78d8c9 used_by=97d170 tp=354a45 -->
|  |  |
|---|---|
|  | ![I'll be back!](../assets/skills/4509.png) |
| **Skill id** | `4509` |
| **Kind** | active (1) |
| **Target** | self; self, ally; units: player, structure; up to 1 |
| **Range** | 255 (world units) |
| **Area** | circle, radius 255, width/angle 255 |
| **Cost** | 1,500 TP |
| **Cooldown** | 120 s |
| **TP skill** | 1,500 TP, 120 s cooldown (Skill_TP row 8) |
| **Icon** | `ui/icons/Policy_01.png` cell 45 |

### Tooltip

> Resurrect dead allies immediately.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 460 | applies buff (variant 460) | [[wiki/buffs/4509\|Buff 4509]] | 100 |

**Reading:** applies [[wiki/buffs/4509|Buff 4509]] (100%).

### Mentioned in

- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § 7. TP skill costs (line 182): I'll be back! · 2,000 / 180 · 1,500 / 120
- [[gameplay/patch-history|Patch notes and other sources]] § PvP, events, forts (line 36): - TP skill changes (WM 1018): Siege Minion 1000 TP cd 100→60 s, Fortified cd 180→120, Fire Support 2500→2000, I'll be back! 2000→1500, Blind/Portal/Freeze 25...
- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § TP skills (line 37): Further client rows not in any guide: I'll be back! (4509), Recovery Shot (4510, 2,500), Fire Support (4512, 2,000), Blind (4514), Create a Portal (4516), Fr...
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
