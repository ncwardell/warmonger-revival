---
title: "Siege Minion"
type: "skill"
id: 4506
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 4506", "client: Skill_TP.cdb row 6", "gameplay: [[gameplay/pvp-and-matches]]", "guide: [[gameplay/pvp-and-matches]] TP skills (team pool; nexus/tower grid)", "guide: [[gameplay/pvp-and-matches]] TP skills (effect text)", "notes: [[gameplay/events-and-schedules]] §7, WM 0511 and WM 1018 (cooldown 100 → 60 s)", "guide: [[gameplay/crush-mechanics]] §6 (CO: 500 TP; history)", "video: [[gameplay/video-fort-war]] §1, §4, P1 2:08 (−1,000 TP)", "image: [[gameplay/pvp-and-matches]] TP skills (damage_or_effect text; client tooltip agrees)", "notes: [[gameplay/crush-patch-notes]] 2017-03-02 and [[gameplay/crush-mechanics]] §6 (CO TP-skill rules; history)"]
manual: ["damage_or_effect"]
name_key: "Skill_4506"
desc_key: "SkillComment_4506"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": [], "max_targets": 1}
range: 1
area: {"shape": 1, "shape_name": "circle", "radius": 1.0, "width_or_angle": 1.0}
cost: {"type": 14, "type_name": "TP", "amount": 1000, "from": "Skill_TP"}
cooldown: {"ms": 60000, "group": 0, "from": "Skill_TP"}
effect_kind: 0
effects:
  - {"slot": 1, "type": 449, "value": 13008, "rate": 1}
damage_or_effect: {"text": "Summons a weak tanking siege minion; field war only"}
icon: {"file": "Policy_01.png", "index": 35}
used_by: []
tp: {"row": 6, "tp_cost": 1000, "cooldown_s": 60, "need_flags": 392, "c7": 1}
observed:
  - {"tp": 1000, "cooldown_s": 100, "effect": "Summons a weak tanking minion; field war only", "source": "gameplay/pvp-and-matches line 34"}
---
<!-- generated:start -->
<!-- generated-keys: title=f5b5ca type=86a754 id=40951c sources=5b7fa0 name_key=718a6a desc_key=c8b4e8 kind=356a19 kind_name=9bc378 target=ae67d6 range=356a19 area=394af4 cost=f53c41 cooldown=c18e3b effect_kind=b6589f effects=51e4dc icon=35d1e3 used_by=97d170 tp=15871a observed=680686 -->
|  |  |
|---|---|
|  | ![Siege Minion](wiki/assets/skills/4506.png) |
| **Skill id** | `4506` |
| **Kind** | active (1) |
| **Target** | self; self; units: -; up to 1 |
| **Range** | 1 (world units) |
| **Area** | circle, radius 1, width/angle 1 |
| **Cost** | 1,000 TP |
| **Cooldown** | 60 s |
| **TP skill** | 1,000 TP, 60 s cooldown (Skill_TP row 6) |
| **Icon** | `ui/icons/Policy_01.png` cell 35 |

### Tooltip

> Summon a Siege minion to aid you in battle.
> You only can use this skill in Field War.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 449 | unknown | 13,008 | 1 |

### Observed in play

Numbers from the gameplay pages (guides, patch notes, video), not from the client:

| cooldown (s) | mana | TP | effect | source |
|---|---|---|---|---|
| 100 |  | 1000 | Summons a weak tanking minion; field war only | [[gameplay/pvp-and-matches]] line 34 |

### Mentioned in

- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 6. War, territories, TP, safety (line 106): Strategy (TP) panel · goes to the first players to enter the war (up to 3 holders); can be passed on, often bugged. Siege Minion costs 500 TP in that panel ·...
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § 7. TP skill costs (line 179): Siege Minion · 1,000 / 100 · 1,000 / 60 (ability raised)
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § 7. TP skill costs (line 187): Matches the client Skill_TP client. The always-available nexus skills on a war land are Shield (refills the nexus shield, not HP), Bomb (hits a standing towe...
- [[gameplay/patch-history|Patch notes and other sources]] § PvP, events, forts (line 36): - TP skill changes (WM 1018): Siege Minion 1000 TP cd 100→60 s, Fortified cd 180→120, Fire Support 2500→2000, I'll be back! 2000→1500, Blind/Portal/Freeze 25...
- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § TP skills (line 34): Siege Minion (4506) · Nexus · 1,000 · 100 s · 1000 / 60 · Summons a weak tanking minion; field war only
- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § TP skills (line 37): Further client rows not in any guide: I'll be back! (4509), Recovery Shot (4510, 2,500), Fire Support (4512, 2,000), Blind (4514), Create a Portal (4516), Fr...
- [[gameplay/server-rules|Server rules checklist]] § Land war (line 55): - [ ] TP skills and costs per Skill_TP (Shield 1,500/120 s, Remote Bomb 1,500/120 s, Nexus Remote Bomb 2,000/180 s, Siege Minion 1,000, Fortified 2,000 …); S...
- [[gameplay/sources|Sources and gaps]] § 8. Forum threads not yet mined (line 128): Archived and reachable, with numbers, but not cited anywhere in the wiki yet: current-fort-placement-and-balance.260, inventory-slots-price-increase.78, sieg...
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § TP (line 42, at 37:43, 2:08): Siege Minion placed · −1,000 (5,550 → 4,550, 37:43) · P1 2:08 · video, matches Skill_TP 1,000
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § TP (line 46, at 2:08, 0:00): TP is one pool for the side: it drops when any ally uses a TP skill. Other TP skills used by name: Shield recovery, Siege Minion, Remote Bomb, Nexus Remote B...
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § 4. Timestamped log (line 139, at 1:36, 34:03): P2 1:36 · 34:03 · "MISZA set a Siege Minion"
- [[gameplay/warmonger-forum|Warmonger forum (2018)]] § 9. Threads listed on index pages but never archived (line 143): The section indexes name threads whose pages exist in no capture on either domain. They would have filled gaps 1–4 in gameplay/sources §9: List of all Grin...
<!-- generated:end -->

## Notes

- TP is one pool for the whole side: when any ally uses a TP skill the pool drops for everyone ([[gameplay/pvp-and-matches]]; [[gameplay/video-fort-war]] §1 TP). TP skills are opened by right-clicking your Nexus or a Tower ([[gameplay/pvp-and-matches]] TP skills). *guide + video*
- Effect: summons a weak minion that tanks for you; **field war only** (guide image and the client tooltip) ([[gameplay/pvp-and-matches]] TP skills). *image + client*
- Patch history: made a basic (always available) TP skill and strengthened in [WM 0511](https://steamcommunity.com/games/718790/announcements/detail/3822871998312896536); cooldown 100 → **60 s** with its ability raised in [WM 1018](https://steamcommunity.com/games/718790/announcements/detail/2403126706515770404) ([[gameplay/events-and-schedules]] §7). The client has 60 s. In Crush Online the Strategy panel listed Siege Minion at 500 TP ([[gameplay/crush-mechanics]] §6). *notes*
- Seen in play: "MISZA set a Siege Minion" and a 1,000 TP drop (5,550 → 4,550) in [[gameplay/video-fort-war]] §1, §4 ([P1 2:08](https://www.youtube.com/watch?v=XoSM3RbZon0&t=128s)). *video*

## Behaviour

- Crush Online rules (history): changing TP skills during a war was allowed but locked them for 180 s ([[gameplay/crush-patch-notes]] 2017-03-02); strategy skills could not be used on fortress floor 2 ([[gameplay/crush-mechanics]] §6, staff).

## Sources

- Gameplay pages this page draws on: [[gameplay/pvp-and-matches]] TP skills, [[gameplay/events-and-schedules]] §7, [[gameplay/crush-mechanics]] §6, [[gameplay/video-fort-war]] §1, §4, [[gameplay/crush-patch-notes]] 2017-03-02.

## Open questions

- The guide image shows a 100 s cooldown (before WM 1018); the client and WM 1018 say 60 s. Client kept. Crush Online's 500 TP is history.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
