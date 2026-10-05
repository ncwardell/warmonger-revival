---
title: "Fire Support"
type: "skill"
id: 4512
status: "partial"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 4512", "client: Skill_TP.cdb row 10", "guide: [[gameplay/pvp-and-matches]] TP skills (team pool; nexus/tower grid)", "image: [[gameplay/events-and-schedules]] §7, WM 1018 image 1 (TP cost / cooldown before → after; after = client)", "notes: [[gameplay/events-and-schedules]] §6 Shaia Legion donations, WM 1128 (Fire Support core at tier 3)", "notes: [[gameplay/crush-patch-notes]] 2017-03-02 and [[gameplay/crush-mechanics]] §6 (CO TP-skill rules; history)"]
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
|  | ![Fire Support](../assets/skills/4512.png) |
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

- TP is one pool for the whole side: when any ally uses a TP skill the pool drops for everyone ([[gameplay/pvp-and-matches]]; [[gameplay/video-fort-war]] §1 TP). TP skills are opened by right-clicking your Nexus or a Tower ([[gameplay/pvp-and-matches]] TP skills). *guide + video*
- Patch history: [WM 1018](https://steamcommunity.com/games/718790/announcements/detail/2403126706515770404) changed its TP cost / cooldown from 2,500 / 180 s to **2,000** / 180 s, which is the client `Skill_TP` value ([[gameplay/events-and-schedules]] §7). *image*
- The legion donation system of [WM 1128](https://steamcommunity.com/games/718790/announcements/detail/2415515408464895311) unlocks a **Fire Support** core at tier 3 (10,000,000 gold, durability 50) ([[gameplay/events-and-schedules]] §6). *notes + image*

## Behaviour

- Crush Online rules (history): changing TP skills during a war was allowed but locked them for 180 s ([[gameplay/crush-patch-notes]] 2017-03-02); strategy skills could not be used on fortress floor 2 ([[gameplay/crush-mechanics]] §6, staff).

## Sources

- Gameplay pages this page draws on: [[gameplay/pvp-and-matches]] TP skills, [[gameplay/events-and-schedules]] §7, [[gameplay/events-and-schedules]] §6, [[gameplay/crush-patch-notes]] 2017-03-02, [[gameplay/crush-mechanics]] §6.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
