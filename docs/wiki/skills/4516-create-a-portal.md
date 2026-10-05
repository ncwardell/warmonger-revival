---
title: "Create a Portal"
type: "skill"
id: 4516
status: "partial"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 4516", "client: Skill_TP.cdb row 12", "guide: [[gameplay/pvp-and-matches]] TP skills (team pool; nexus/tower grid)", "image: [[gameplay/events-and-schedules]] §7, WM 1018 image 1 (TP cost / cooldown before → after; after = client)", "guide: [[gameplay/crush-mechanics]] §6 (CO portal bug)", "guide: [[gameplay/warmonger-forum]] §6 (Revive + Portal pair)", "notes: [[gameplay/crush-patch-notes]] 2017-03-02 and [[gameplay/crush-mechanics]] §6 (CO TP-skill rules; history)"]
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

- TP is one pool for the whole side: when any ally uses a TP skill the pool drops for everyone ([[gameplay/pvp-and-matches]]; [[gameplay/video-fort-war]] §1 TP). TP skills are opened by right-clicking your Nexus or a Tower ([[gameplay/pvp-and-matches]] TP skills). *guide + video*
- Patch history: [WM 1018](https://steamcommunity.com/games/718790/announcements/detail/2403126706515770404) changed its TP cost / cooldown from 2,500 / 120 s to **1,500** / 120 s, which is the client `Skill_TP` value ([[gameplay/events-and-schedules]] §7). *image*
- Crush Online bug: destroying an enemy portal set your own TP to 0 until the next TP gain ([[gameplay/crush-mechanics]] §6). Players named "Revive + Portal" a strong TP-skill pair ([[gameplay/warmonger-forum]] §6). *player*

## Behaviour

- Crush Online rules (history): changing TP skills during a war was allowed but locked them for 180 s ([[gameplay/crush-patch-notes]] 2017-03-02); strategy skills could not be used on fortress floor 2 ([[gameplay/crush-mechanics]] §6, staff).

## Sources

- Gameplay pages this page draws on: [[gameplay/pvp-and-matches]] TP skills, [[gameplay/events-and-schedules]] §7, [[gameplay/crush-mechanics]] §6, [[gameplay/warmonger-forum]] §6, [[gameplay/crush-patch-notes]] 2017-03-02.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
