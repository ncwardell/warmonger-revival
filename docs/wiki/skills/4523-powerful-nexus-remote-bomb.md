---
title: "Powerful Nexus Remote Bomb"
type: "skill"
id: 4523
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 4523", "client: Skill_TP.cdb row 16", "guide: [[gameplay/pvp-and-matches]] TP skills (team pool; nexus/tower grid)", "notes: [[gameplay/events-and-schedules]] §6, WM 1107 (effect text) and WM 1128 (donation tier)", "notes: [[gameplay/events-and-schedules]] §6, WM 1107 (damage_or_effect text)", "notes: [[gameplay/crush-patch-notes]] 2017-03-02 and [[gameplay/crush-mechanics]] §6 (CO TP-skill rules; history)"]
manual: ["damage_or_effect"]
name_key: "Skill_4523"
desc_key: "SkillComment_4523"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["player", "structure"], "max_targets": 1}
range: 255
area: {"shape": 1, "shape_name": "circle", "radius": 255.0, "width_or_angle": 255.0}
cost: {"type": 14, "type_name": "TP", "amount": 3000, "from": "Skill_TP"}
cooldown: {"ms": 300000, "group": 0, "from": "Skill_TP"}
effect_kind: 0
effects:
  - {"slot": 1, "type": 463, "value": 14009, "rate": 100}
damage_or_effect: {"text": "Legion-core TP skill: a stronger nexus remote bomb"}
icon: {"file": "Policy_01.png", "index": 26}
used_by: []
tp: {"row": 16, "tp_cost": 3000, "cooldown_s": 300, "need_flags": 388, "c7": 2}
---
<!-- generated:start -->
<!-- generated-keys: title=de88fe type=86a754 id=3238da sources=6a2174 name_key=eb67b9 desc_key=6813c6 kind=356a19 kind_name=9bc378 target=35e077 range=3028f5 area=febbd1 cost=768946 cooldown=82d6c4 effect_kind=b6589f effects=f3d4da damage_or_effect=bf21a9 icon=503286 used_by=97d170 tp=c1f3f3 -->
|  |  |
|---|---|
|  | ![Powerful Nexus Remote Bomb](../assets/skills/4523.png) |
| **Skill id** | `4523` |
| **Kind** | active (1) |
| **Target** | self; self; units: player, structure; up to 1 |
| **Range** | 255 (world units) |
| **Area** | circle, radius 255, width/angle 255 |
| **Cost** | 3,000 TP |
| **Cooldown** | 300 s |
| **TP skill** | 3,000 TP, 300 s cooldown (Skill_TP row 16) |
| **Icon** | `ui/icons/Policy_01.png` cell 26 |

### Tooltip

> Use it to attack the Nexus

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 463 | unknown | 14,009 | 100 |

### Mentioned in

- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § TP skills (line 37): Further client rows not in any guide: I'll be back! (4509), Recovery Shot (4510, 2,500), Fire Support (4512, 2,000), Blind (4514), Create a Portal (4516), Fr...
<!-- generated:end -->

## Notes

- TP is one pool for the whole side: when any ally uses a TP skill the pool drops for everyone ([[gameplay/pvp-and-matches]]; [[gameplay/video-fort-war]] §1 TP). TP skills are opened by right-clicking your Nexus or a Tower ([[gameplay/pvp-and-matches]] TP skills). *guide + video*
- Effect: Legion-core TP skill: a stronger nexus remote bomb. Added in [WM 1107](https://steamcommunity.com/games/718790/announcements/detail/2423394805992652770) as a legion core that enables the TP skill on the land where it is placed ([[gameplay/events-and-schedules]] §6). The Shaia legion donations of [WM 1128](https://steamcommunity.com/games/718790/announcements/detail/2415515408464895311) unlock a Powerful Remote Bomb core at tier 6 (35,000,000 gold). *notes*

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
