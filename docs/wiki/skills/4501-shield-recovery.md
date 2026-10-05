---
title: "Shield recovery"
type: "skill"
id: 4501
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 4501", "client: Skill_TP.cdb row 2", "gameplay: [[gameplay/pvp-and-matches]]"]
name_key: "Skill_4501"
desc_key: "SkillComment_4501"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["player", "structure"], "max_targets": 1}
range: 1
area: {"shape": 1, "shape_name": "circle", "radius": 1.0, "width_or_angle": 1.0}
cost: {"type": 14, "type_name": "TP", "amount": 1500, "from": "Skill_TP"}
cooldown: {"ms": 120000, "group": 0, "from": "Skill_TP"}
effect_kind: 33
effects:
  - {"slot": 1, "type": 131, "value": 80, "rate": 1}
damage_or_effect: {"kind": "restore MP", "stats": [{"code": 131, "value": 80}]}
visual: 400
icon: {"file": "Policy_01.png", "index": 17}
used_by: []
tp: {"row": 2, "tp_cost": 1500, "cooldown_s": 120, "need_flags": 396, "c7": 2}
observed:
  - {"tp": 1500, "cooldown_s": 120, "effect": "Gives the nexus a shield (restores shield, not HP)", "source": "gameplay/pvp-and-matches line 31"}
---
<!-- generated:start -->
<!-- generated-keys: title=c2efe5 type=86a754 id=5d7311 sources=1c757b name_key=5fc8cd desc_key=1446c8 kind=356a19 kind_name=9bc378 target=35e077 range=356a19 area=394af4 cost=4e6c0e cooldown=d97414 effect_kind=b6692e effects=4bd0ad damage_or_effect=301909 visual=ab7f7b icon=6a165d used_by=97d170 tp=8d34e0 observed=7b34e1 -->
|  |  |
|---|---|
|  | ![Shield recovery](wiki/assets/skills/4501.png) |
| **Skill id** | `4501` |
| **Kind** | active (1) |
| **Target** | self; self; units: player, structure; up to 1 |
| **Range** | 1 (world units) |
| **Area** | circle, radius 1, width/angle 1 |
| **Cost** | 1,500 TP |
| **Cooldown** | 120 s |
| **Effect kind** | restore MP (33) |
| **Visual** | skillVisual 400 `TP스킬_타워 쉴드회복` |
| **TP skill** | 1,500 TP, 120 s cooldown (Skill_TP row 2) |
| **Icon** | `ui/icons/Policy_01.png` cell 17 |

### Tooltip

> If you use it, you will create a Tower shield.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 131 | stat? Health(%) | 80 | 1 |

**Reading:** restore MP.

### Observed in play

Numbers from the gameplay pages (guides, patch notes, video), not from the client:

| cooldown (s) | mana | TP | effect | source |
|---|---|---|---|---|
| 120 |  | 1500 | Gives the nexus a shield (restores shield, not HP) | [[gameplay/pvp-and-matches]] line 31 |

### Mentioned in

- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § 5. Forts and sieges (line 115): Shield recovery time · 3 h · WM 0705
- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § TP skills (line 31): Shield recovery (4500/4501) · Nexus, Tower · 1,500 · 120 s · 1500 / 120 · Gives the nexus a shield (restores shield, not HP)
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § TP (line 46, at 2:08, 0:00): TP is one pool for the side: it drops when any ally uses a TP skill. Other TP skills used by name: Shield recovery, Siege Minion, Remote Bomb, Nexus Remote B...
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § 4. Timestamped log (line 140, at 2:08, 33:31): P2 2:08 · 33:31 · "Zpike set a Shield recovery"
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
