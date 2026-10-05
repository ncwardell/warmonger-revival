---
title: "Freeze"
type: "skill"
id: 4518
status: "partial"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 4518", "client: Skill_TP.cdb row 13", "guide: [[gameplay/pvp-and-matches]] TP skills (team pool; nexus/tower grid)", "image: [[gameplay/events-and-schedules]] §7, WM 1018 image 1 (TP cost / cooldown before → after; after = client)", "notes: [[gameplay/crush-patch-notes]] 2017-03-02 and [[gameplay/crush-mechanics]] §6 (CO TP-skill rules; history)"]
name_key: "Skill_4517"
desc_key: "SkillComment_4517"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self"], "unit_classes": ["player"], "max_targets": 1}
range: 255
area: {"shape": 1, "shape_name": "circle", "radius": 8.0, "width_or_angle": 8.0}
cost: {"type": 14, "type_name": "TP", "amount": 1500, "from": "Skill_TP"}
cooldown: {"ms": 120000, "group": 0, "from": "Skill_TP"}
effect_kind: 1
effects:
  - {"slot": 1, "type": 324, "value": 10005, "rate": 100}
damage_or_effect: {}
visual: 357
icon: {"file": "Policy_01.png", "index": 44}
used_by: []
tp: {"row": 13, "tp_cost": 1500, "cooldown_s": 120, "need_flags": 396, "c7": 1}
---
<!-- generated:start -->
<!-- generated-keys: title=903854 type=86a754 id=d1d139 sources=f1b1f8 name_key=b9ea03 desc_key=4ec9b8 kind=356a19 kind_name=9bc378 target=d5ca9d range=3028f5 area=950fc9 cost=4e6c0e cooldown=d97414 effect_kind=356a19 effects=539d98 damage_or_effect=bf21a9 visual=869700 icon=897d76 used_by=97d170 tp=4c8e23 -->
|  |  |
|---|---|
|  | ![Freeze](../assets/skills/4518.png) |
| **Skill id** | `4518` |
| **Kind** | active (1) |
| **Target** | ground; self; units: player; up to 1 |
| **Range** | 255 (world units) |
| **Area** | circle, radius 8, width/angle 8 |
| **Cost** | 1,500 TP |
| **Cooldown** | 120 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 357 `TP스킬_얼음 땡` |
| **TP skill** | 1,500 TP, 120 s cooldown (Skill_TP row 13) |
| **Icon** | `ui/icons/Policy_01.png` cell 44 |

### Tooltip

> Freezes friends and foes alike for 4 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 324 | unknown | 10,005 | 100 |

### Mentioned in

- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § 7. TP skill costs (line 185): Freeze · 2,500 / 120 · 1,500 / 120
- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § TP skills (line 37): Further client rows not in any guide: I'll be back! (4509), Recovery Shot (4510, 2,500), Fire Support (4512, 2,000), Blind (4514), Create a Portal (4516), Fr...
<!-- generated:end -->

## Notes

- TP is one pool for the whole side: when any ally uses a TP skill the pool drops for everyone ([[gameplay/pvp-and-matches]]; [[gameplay/video-fort-war]] §1 TP). TP skills are opened by right-clicking your Nexus or a Tower ([[gameplay/pvp-and-matches]] TP skills). *guide + video*
- Patch history: [WM 1018](https://steamcommunity.com/games/718790/announcements/detail/2403126706515770404) changed its TP cost / cooldown from 2,500 / 120 s to **1,500** / 120 s, which is the client `Skill_TP` value ([[gameplay/events-and-schedules]] §7). *image*

## Behaviour

- Crush Online rules (history): changing TP skills during a war was allowed but locked them for 180 s ([[gameplay/crush-patch-notes]] 2017-03-02); strategy skills could not be used on fortress floor 2 ([[gameplay/crush-mechanics]] §6, staff).

## Sources

- Gameplay pages this page draws on: [[gameplay/pvp-and-matches]] TP skills, [[gameplay/events-and-schedules]] §7, [[gameplay/crush-patch-notes]] 2017-03-02, [[gameplay/crush-mechanics]] §6.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
