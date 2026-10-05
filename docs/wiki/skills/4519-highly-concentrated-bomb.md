---
title: "Highly Concentrated Bomb"
type: "skill"
id: 4519
status: "partial"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 4519", "client: Skill_TP.cdb row 14", "guide: [[gameplay/pvp-and-matches]] TP skills (team pool; nexus/tower grid)", "guide: [[gameplay/events-and-schedules]] §6 (extra Skill_TP rows probably core-unlocked; guess)", "notes: [[gameplay/crush-patch-notes]] 2017-03-02 and [[gameplay/crush-mechanics]] §6 (CO TP-skill rules; history)"]
name_key: "Skill_4519"
desc_key: "SkillComment_4519"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["player", "structure"], "max_targets": 1}
range: 255
area: {"shape": 1, "shape_name": "circle", "radius": 255.0, "width_or_angle": 255.0}
cost: {"type": 14, "type_name": "TP", "amount": 10000, "from": "Skill_TP"}
cooldown: {"ms": 180000, "group": 0, "from": "Skill_TP"}
effect_kind: 0
effects:
  - {"slot": 1, "type": 464, "value": 14007, "rate": 100}
damage_or_effect: {}
icon: {"file": "Policy_01.png", "index": 16}
used_by: []
tp: {"row": 14, "tp_cost": 10000, "cooldown_s": 180, "need_flags": 2, "c7": 1}
---
<!-- generated:start -->
<!-- generated-keys: title=31d608 type=86a754 id=2238a0 sources=d702ea name_key=c71dc3 desc_key=c0d564 kind=356a19 kind_name=9bc378 target=35e077 range=3028f5 area=febbd1 cost=593709 cooldown=c44d13 effect_kind=b6589f effects=f8e924 damage_or_effect=bf21a9 icon=51436c used_by=97d170 tp=4534ca -->
|  |  |
|---|---|
|  | ![Highly Concentrated Bomb](../assets/skills/4519.png) |
| **Skill id** | `4519` |
| **Kind** | active (1) |
| **Target** | self; self; units: player, structure; up to 1 |
| **Range** | 255 (world units) |
| **Area** | circle, radius 255, width/angle 255 |
| **Cost** | 10,000 TP |
| **Cooldown** | 180 s |
| **TP skill** | 10,000 TP, 180 s cooldown (Skill_TP row 14) |
| **Icon** | `ui/icons/Policy_01.png` cell 16 |

### Tooltip

> Attack the middle boss and the boss. If there is an Middle boss, attack the middle boss first

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 464 | unknown | 14,007 | 100 |

### Mentioned in

- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § TP skills (line 37): Further client rows not in any guide: I'll be back! (4509), Recovery Shot (4510, 2,500), Fire Support (4512, 2,000), Blind (4514), Create a Portal (4516), Fr...
<!-- generated:end -->

## Notes

- TP is one pool for the whole side: when any ally uses a TP skill the pool drops for everyone ([[gameplay/pvp-and-matches]]; [[gameplay/video-fort-war]] §1 TP). TP skills are opened by right-clicking your Nexus or a Tower ([[gameplay/pvp-and-matches]] TP skills). *guide + video*
- Not in any guide. It is one of the extra `Skill_TP` rows (10,000 TP / 180 s) outside the always-available set, probably unlocked by a legion core ([[gameplay/events-and-schedules]] §6, *client + guess*).

## Behaviour

- Crush Online rules (history): changing TP skills during a war was allowed but locked them for 180 s ([[gameplay/crush-patch-notes]] 2017-03-02); strategy skills could not be used on fortress floor 2 ([[gameplay/crush-mechanics]] §6, staff).

## Sources

- Gameplay pages this page draws on: [[gameplay/pvp-and-matches]] TP skills, [[gameplay/events-and-schedules]] §6, [[gameplay/crush-patch-notes]] 2017-03-02, [[gameplay/crush-mechanics]] §6.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
