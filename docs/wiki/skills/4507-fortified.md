---
title: "Fortified"
type: "skill"
id: 4507
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 4507", "client: Skill_TP.cdb row 7", "gameplay: [[gameplay/pvp-and-matches]]", "guide: [[gameplay/pvp-and-matches]] TP skills (team pool; nexus/tower grid)", "image: [[gameplay/events-and-schedules]] §7, WM 1018 image 1 (TP cost / cooldown before → after; after = client)", "image: [[gameplay/pvp-and-matches]] TP skills (effect text)", "notes: [[gameplay/crush-patch-notes]] 2017-03-02 and [[gameplay/crush-mechanics]] §6 (CO TP-skill rules; history)"]
name_key: "Skill_4507"
desc_key: "SkillComment_4507"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["player", "structure"], "max_targets": 1}
range: 1
area: {"shape": 1, "shape_name": "circle", "radius": 1.0, "width_or_angle": 1.0}
cost: {"type": 14, "type_name": "TP", "amount": 2000, "from": "Skill_TP"}
cooldown: {"ms": 120000, "group": 0, "from": "Skill_TP"}
effect_kind: 0
effects:
  - {"slot": 1, "type": 304, "value": 4507, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 4507, "rate": 100}]}
icon: {"file": "Policy_01.png", "index": 39}
used_by: []
tp: {"row": 7, "tp_cost": 2000, "cooldown_s": 120, "need_flags": 396, "c7": 2}
observed:
  - {"tp": 2000, "cooldown_s": 180, "effect": "Raises attack and defence of all your towers on the map", "source": "gameplay/pvp-and-matches line 35"}
---
<!-- generated:start -->
<!-- generated-keys: title=ce9b19 type=86a754 id=dca5e1 sources=b4bef2 name_key=4b02e9 desc_key=6c8ee0 kind=356a19 kind_name=9bc378 target=35e077 range=356a19 area=394af4 cost=03969c cooldown=d97414 effect_kind=b6589f effects=951aab damage_or_effect=71ac22 icon=30da17 used_by=97d170 tp=4d1a2d observed=95b3c1 -->
|  |  |
|---|---|
|  | ![Fortified](../assets/skills/4507.png) |
| **Skill id** | `4507` |
| **Kind** | active (1) |
| **Target** | self; self; units: player, structure; up to 1 |
| **Range** | 1 (world units) |
| **Area** | circle, radius 1, width/angle 1 |
| **Cost** | 2,000 TP |
| **Cooldown** | 120 s |
| **TP skill** | 2,000 TP, 120 s cooldown (Skill_TP row 7) |
| **Icon** | `ui/icons/Policy_01.png` cell 39 |

### Tooltip

> Increases the offensive and defensive potential of all 
> your towers on the map.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 304 | applies buff (variant 304) | [[wiki/buffs/4507-strengthen-tower\|Strengthen Tower]] | 100 |

**Reading:** applies [[wiki/buffs/4507-strengthen-tower|Strengthen Tower]] (100%).

### Observed in play

Numbers from the gameplay pages (guides, patch notes, video), not from the client:

| cooldown (s) | mana | TP | effect | source |
|---|---|---|---|---|
| 180 |  | 2000 | Raises attack and defence of all your towers on the map | [[gameplay/pvp-and-matches]] line 35 |

### Mentioned in

- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § 7. TP skill costs (line 180): Fortified · 2,000 / 180 · 2,000 / 120
- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § TP skills (line 35): Fortified (4507) · Tower · 2,000 · 180 s · 2000 / 120 · Raises attack and defence of all your towers on the map
<!-- generated:end -->

## Notes

- TP is one pool for the whole side: when any ally uses a TP skill the pool drops for everyone ([[gameplay/pvp-and-matches]]; [[gameplay/video-fort-war]] §1 TP). TP skills are opened by right-clicking your Nexus or a Tower ([[gameplay/pvp-and-matches]] TP skills). *guide + video*
- Patch history: [WM 1018](https://steamcommunity.com/games/718790/announcements/detail/2403126706515770404) changed its TP cost / cooldown from 2,000 / 180 s to 2,000 / **120 s**, which is the client `Skill_TP` value ([[gameplay/events-and-schedules]] §7). *image*
- Effect: raises the attack and defence of all your towers on the map; used from a Tower ([[gameplay/pvp-and-matches]] TP skills; guide image showed 2,000 TP / 180 s, before WM 1018). The client buff [[wiki/buffs/4507-strengthen-tower|4507]] gives +1,000 Attack and +500 Armor. *image*

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
