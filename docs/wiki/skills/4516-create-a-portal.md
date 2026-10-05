---
title: "Create a Portal"
type: "skill"
id: 4516
status: "stub"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 4516", "client: Skill_TP.cdb row 12"]
name_key: "Skill_4516"
desc_key: "SkillComment_4516"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self", "ally"], "unit_classes": [], "max_targets": 1}
range: 22
cost: {"type": 14, "type_name": "TP", "amount": 1500, "from": "Skill_TP"}
cooldown: {"ms": 120000, "group": 0, "from": "Skill_TP"}
effect_kind: 0
effects:
  - {"slot": 1, "type": 451, "value": 13010, "rate": 1}
damage_or_effect: {}
icon: {"file": "Policy_01.png", "index": 42}
used_by: []
tp: {"row": 12, "tp_cost": 1500, "cooldown_s": 120, "need_flags": 396, "c7": 1}
---
<!-- generated:start -->
<!-- generated-keys: title=35c199 type=86a754 id=121de4 sources=adc187 name_key=0835b8 desc_key=9d71d9 kind=356a19 kind_name=9bc378 target=f49bfe range=12c6fc cost=4e6c0e cooldown=d97414 effect_kind=b6589f effects=2f335a damage_or_effect=bf21a9 icon=7af3ea used_by=97d170 tp=2abebb -->
|  |  |
|---|---|
|  | ![Create a Portal](../assets/skills/4516.png) |
| **Skill id** | `4516` |
| **Kind** | active (1) |
| **Target** | ground; self, ally; units: -; up to 1 |
| **Range** | 22 (world units) |
| **Cost** | 1,500 TP |
| **Cooldown** | 120 s |
| **TP skill** | 1,500 TP, 120 s cooldown (Skill_TP row 12) |
| **Icon** | `ui/icons/Policy_01.png` cell 42 |

### Tooltip

> Summon a portal in the field..

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 451 | unknown | 13,010 | 1 |

### Mentioned in

- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § 7. TP skill costs (line 184): Create a Portal · 2,500 / 120 · 1,500 / 120
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
