---
title: "Powerful Remote Bomb"
type: "skill"
id: 4525
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 4525", "client: Skill_TP.cdb row 17", "guide: [[gameplay/pvp-and-matches]] TP skills (team pool; nexus/tower grid)", "notes: [[gameplay/events-and-schedules]] §6, WM 1107 (effect text) and WM 1128 (donation tier)", "notes: [[gameplay/events-and-schedules]] §6, WM 1107 (damage_or_effect text)", "notes: [[gameplay/crush-patch-notes]] 2017-03-02 and [[gameplay/crush-mechanics]] §6 (CO TP-skill rules; history)"]
manual: ["damage_or_effect"]
name_key: "Skill_4525"
desc_key: "SkillComment_4525"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["player", "structure"], "max_targets": 1}
range: 255
area: {"shape": 1, "shape_name": "circle", "radius": 255.0, "width_or_angle": 255.0}
cost: {"type": 14, "type_name": "TP", "amount": 2500, "from": "Skill_TP"}
cooldown: {"ms": 240000, "group": 0, "from": "Skill_TP"}
effect_kind: 0
effects:
  - {"slot": 1, "type": 464, "value": 14010, "rate": 100}
damage_or_effect: {"text": "Legion-core TP skill. PvP: hits the nexus after all enemy attack towers are destroyed. PvE: hits all bosses after the middle one"}
icon: {"file": "Policy_01.png", "index": 25}
used_by: []
tp: {"row": 17, "tp_cost": 2500, "cooldown_s": 240, "need_flags": 388, "c7": 1}
---
<!-- generated:start -->
<!-- generated-keys: title=6452b6 type=86a754 id=bfbb1e sources=ab9b53 name_key=18792e desc_key=6337cd kind=356a19 kind_name=9bc378 target=35e077 range=3028f5 area=febbd1 cost=a7b37a cooldown=11dbc8 effect_kind=b6589f effects=bfb8d8 icon=b5c79c used_by=97d170 tp=826528 -->
|  |  |
|---|---|
|  | ![Powerful Remote Bomb](wiki/assets/skills/4525.png) |
| **Skill id** | `4525` |
| **Kind** | active (1) |
| **Target** | self; self; units: player, structure; up to 1 |
| **Range** | 255 (world units) |
| **Area** | circle, radius 255, width/angle 255 |
| **Cost** | 2,500 TP |
| **Cooldown** | 240 s |
| **TP skill** | 2,500 TP, 240 s cooldown (Skill_TP row 17) |
| **Icon** | `ui/icons/Policy_01.png` cell 25 |

### Tooltip

> Attack enemy objects. If there is an enemy attack tower, attack the tower first.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 464 | unknown | 14,010 | 100 |

### Mentioned in

- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § Shaia Legion donations (line 168): 6 · 35,000,000 · 20% · Powerful Remote Bomb · 50
- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § TP skills (line 37): Further client rows not in any guide: I'll be back! (4509), Recovery Shot (4510, 2,500), Fire Support (4512, 2,000), Blind (4514), Create a Portal (4516), Fr...
- [[gameplay/server-rules|Server rules checklist]] § PvP, events, forts (line 153): - [ ] Shaia Legion donations: 200,000 gold/day per player (+1 donation per 100 jewels); 7 weekly tiers 3/6/10/15/25/35/45 M gold → Shaia +10/10/10/20/20/20/3...
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § TP (line 44, at 32:39, 32:35, 2:56, 3:04): Nexus Remote Bomb ("WinterGold set a Nexus Remote Bomb") · −2,500 (2,780 → 280, 32:39 → 32:35) · P2 2:56–3:04 · video at 360p; the client lists Nexus Remote...
<!-- generated:end -->

## Notes

- TP is one pool for the whole side: when any ally uses a TP skill the pool drops for everyone ([[gameplay/pvp-and-matches]]; [[gameplay/video-fort-war]] §1 TP). TP skills are opened by right-clicking your Nexus or a Tower ([[gameplay/pvp-and-matches]] TP skills). *guide + video*
- Effect: Legion-core TP skill. PvP: hits the nexus after all enemy attack towers are destroyed. PvE: hits all bosses after the middle one. Added in [WM 1107](https://steamcommunity.com/games/718790/announcements/detail/2423394805992652770) as a legion core that enables the TP skill on the land where it is placed ([[gameplay/events-and-schedules]] §6). The Shaia legion donations of [WM 1128](https://steamcommunity.com/games/718790/announcements/detail/2415515408464895311) unlock a Powerful Remote Bomb core at tier 6 (35,000,000 gold). *notes*

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
