---
title: "Nexus Remote Bomb"
type: "skill"
id: 4504
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 4504", "client: Skill_TP.cdb row 5", "gameplay: [[gameplay/pvp-and-matches]]", "guide: [[gameplay/pvp-and-matches]] TP skills (team pool; nexus/tower grid)", "image: [[gameplay/pvp-and-matches]] TP skills (2,000 TP / 180 s = client)", "video: [[gameplay/video-fort-war]] §1 TP and §4 (used; one −2,500 reading)", "image: [[gameplay/pvp-and-matches]] TP skills (damage_or_effect text)", "notes: [[gameplay/crush-patch-notes]] 2017-03-02 and [[gameplay/crush-mechanics]] §6 (CO TP-skill rules; history)"]
manual: ["damage_or_effect"]
name_key: "Skill_4504"
desc_key: "SkillComment_4504"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["player", "structure"], "max_targets": 1}
range: 255
area: {"shape": 1, "shape_name": "circle", "radius": 255.0, "width_or_angle": 255.0}
cost: {"type": 14, "type_name": "TP", "amount": 2000, "from": "Skill_TP"}
cooldown: {"ms": 180000, "group": 0, "from": "Skill_TP"}
effect_kind: 0
effects:
  - {"slot": 1, "type": 463, "value": 14006, "rate": 100}
damage_or_effect: {"text": "Attacks the enemy nexus"}
icon: {"file": "Policy_01.png", "index": 16}
used_by: []
tp: {"row": 5, "tp_cost": 2000, "cooldown_s": 180, "need_flags": 388, "c7": 2}
observed:
  - {"tp": 2000, "cooldown_s": 180, "effect": "Attacks the nexus", "source": "gameplay/pvp-and-matches line 33"}
---
<!-- generated:start -->
<!-- generated-keys: title=ec6ddd type=86a754 id=1fa14e sources=94fbc8 name_key=183326 desc_key=b4b7da kind=356a19 kind_name=9bc378 target=35e077 range=3028f5 area=febbd1 cost=03969c cooldown=c44d13 effect_kind=b6589f effects=33bf48 icon=51436c used_by=97d170 tp=780c5b observed=8f8f7a -->
|  |  |
|---|---|
|  | ![Nexus Remote Bomb](wiki/assets/skills/4504.png) |
| **Skill id** | `4504` |
| **Kind** | active (1) |
| **Target** | self; self; units: player, structure; up to 1 |
| **Range** | 255 (world units) |
| **Area** | circle, radius 255, width/angle 255 |
| **Cost** | 2,000 TP |
| **Cooldown** | 180 s |
| **TP skill** | 2,000 TP, 180 s cooldown (Skill_TP row 5) |
| **Icon** | `ui/icons/Policy_01.png` cell 16 |

### Tooltip

> Use it to attack the Nexus

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 463 | unknown | 14,006 | 100 |

### Observed in play

Numbers from the gameplay pages (guides, patch notes, video), not from the client:

| cooldown (s) | mana | TP | effect | source |
|---|---|---|---|---|
| 180 |  | 2000 | Attacks the nexus | [[gameplay/pvp-and-matches]] line 33 |

### Mentioned in

- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § TP skills (line 33): Nexus Remote Bomb (4504) · Tower · 2,000 · 180 s · 2000 / 180 · Attacks the nexus
- [[gameplay/server-rules|Server rules checklist]] § Land war (line 55): - [ ] TP skills and costs per Skill_TP (Shield 1,500/120 s, Remote Bomb 1,500/120 s, Nexus Remote Bomb 2,000/180 s, Siege Minion 1,000, Fortified 2,000 …); S...
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § TP (line 44, at 32:39, 32:35, 2:56, 3:04): Nexus Remote Bomb ("WinterGold set a Nexus Remote Bomb") · −2,500 (2,780 → 280, 32:39 → 32:35) · P2 2:56–3:04 · video at 360p; the client lists Nexus Remote...
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § TP (line 46, at 2:08, 0:00): TP is one pool for the side: it drops when any ally uses a TP skill. Other TP skills used by name: Shield recovery, Siege Minion, Remote Bomb, Nexus Remote B...
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § 4. Timestamped log (line 138, at 1:00, 34:23): P2 1:00 · 34:23 · "Ariel use a Nexus Remote Bomb"
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § 4. Timestamped log (line 141, at 3:04, 32:35): P2 3:04 · 32:35 · "WinterGold set a Nexus Remote Bomb"; TP 2,780 → 280
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § 4. Timestamped log (line 143, at 2:04, 29:32): P3 2:04 · 29:32 · "Zpike use a Nexus Remote Bomb"
<!-- generated:end -->

## Notes

- TP is one pool for the whole side: when any ally uses a TP skill the pool drops for everyone ([[gameplay/pvp-and-matches]]; [[gameplay/video-fort-war]] §1 TP). TP skills are opened by right-clicking your Nexus or a Tower ([[gameplay/pvp-and-matches]] TP skills). *guide + video*
- Effect: attacks the enemy nexus; used from a Tower; 2,000 TP / 180 s in the guide image = client ([[gameplay/pvp-and-matches]] TP skills). *image*
- Used several times in the June 2018 fort war ([[gameplay/video-fort-war]] §4: P2 1:00, P2 3:04, P3 2:04). One use at [P2 2:56–3:04](https://www.youtube.com/watch?v=6_z6CUpZj30&t=176s) dropped the pool 2,780 → 280, i.e. 2,500 TP. *video*

## Behaviour

- Crush Online rules (history): changing TP skills during a war was allowed but locked them for 180 s ([[gameplay/crush-patch-notes]] 2017-03-02); strategy skills could not be used on fortress floor 2 ([[gameplay/crush-mechanics]] §6, staff).

## Sources

- Gameplay pages this page draws on: [[gameplay/pvp-and-matches]] TP skills, [[gameplay/video-fort-war]] §1, §4, [[gameplay/crush-patch-notes]] 2017-03-02, [[gameplay/crush-mechanics]] §6.

## Open questions

- Cost: the video read (360p) shows −2,500 TP for a "Nexus Remote Bomb"; the guide and client say 2,000 (Powerful Remote Bomb costs 2,500). Client kept.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
