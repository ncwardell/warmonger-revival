---
title: "Shield recovery"
type: "skill"
id: 4500
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 4500", "client: Skill_TP.cdb row 1", "gameplay: [[gameplay/pvp-and-matches]]", "guide: [[gameplay/pvp-and-matches]] TP skills (team pool; nexus/tower grid)", "guide: [[gameplay/events-and-schedules]] §7 (Shield refills the nexus shield, not HP)", "video: [[gameplay/video-fort-war]] §4, P2 2:08 (used in play)", "notes: [[gameplay/crush-patch-notes]] 2017-03-02 and [[gameplay/crush-mechanics]] §6 (CO TP-skill rules; history)"]
name_key: "Skill_4500"
desc_key: "SkillComment_4500"
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
visual: 399
icon: {"file": "Policy_01.png", "index": 17}
used_by: []
tp: {"row": 1, "tp_cost": 1500, "cooldown_s": 120, "need_flags": 396, "c7": 1}
observed:
  - {"tp": 1500, "cooldown_s": 120, "effect": "Gives the nexus a shield (restores shield, not HP)", "source": "gameplay/pvp-and-matches line 31"}
---
<!-- generated:start -->
<!-- generated-keys: title=c2efe5 type=86a754 id=97a87b sources=b1debe name_key=0d3844 desc_key=0e5347 kind=356a19 kind_name=9bc378 target=35e077 range=356a19 area=394af4 cost=4e6c0e cooldown=d97414 effect_kind=b6692e effects=4bd0ad damage_or_effect=301909 visual=9ed4f2 icon=6a165d used_by=97d170 tp=f3685c observed=7b34e1 -->
|  |  |
|---|---|
|  | ![Shield recovery](../assets/skills/4500.png) |
| **Skill id** | `4500` |
| **Kind** | active (1) |
| **Target** | self; self; units: player, structure; up to 1 |
| **Range** | 1 (world units) |
| **Area** | circle, radius 1, width/angle 1 |
| **Cost** | 1,500 TP |
| **Cooldown** | 120 s |
| **Effect kind** | restore MP (33) |
| **Visual** | skillVisual 399 `TP스킬_넥서스 쉴드 회복` |
| **TP skill** | 1,500 TP, 120 s cooldown (Skill_TP row 1) |
| **Icon** | `ui/icons/Policy_01.png` cell 17 |

### Tooltip

> If you use it, you will create a Nexus shield.

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

- TP is one pool for the whole side: when any ally uses a TP skill the pool drops for everyone ([[gameplay/pvp-and-matches]]; [[gameplay/video-fort-war]] §1 TP). TP skills are opened by right-clicking your Nexus or a Tower ([[gameplay/pvp-and-matches]] TP skills). *guide + video*
- Gives the nexus a shield: it refills the shield, not HP. Usable from the Nexus or a Tower; 1,500 TP and 120 s in the guide image, the same as the client ([[gameplay/pvp-and-matches]]; [[gameplay/events-and-schedules]] §7). One of the always-available skills on an attack/defence land. *image + guide*
- Used in the June 2018 fort war ("Zpike set a Shield recovery", [[gameplay/video-fort-war]] §4, [P2 2:08](https://www.youtube.com/watch?v=6_z6CUpZj30&t=128s)). *video*

## Behaviour

- Crush Online rules (history): changing TP skills during a war was allowed but locked them for 180 s ([[gameplay/crush-patch-notes]] 2017-03-02); strategy skills could not be used on fortress floor 2 ([[gameplay/crush-mechanics]] §6, staff).

## Sources

- Gameplay pages this page draws on: [[gameplay/pvp-and-matches]] TP skills, [[gameplay/events-and-schedules]] §7, [[gameplay/video-fort-war]] §1, §4, [[gameplay/crush-patch-notes]] 2017-03-02, [[gameplay/crush-mechanics]] §6.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
