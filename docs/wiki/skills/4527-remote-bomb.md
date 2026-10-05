---
title: "Remote Bomb"
type: "skill"
id: 4527
status: "stub"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 4527", "client: Skill_TP.cdb row 3", "gameplay: [[gameplay/pvp-and-matches]]"]
name_key: "Skill_4527"
desc_key: "SkillComment_4527"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["player", "structure"], "max_targets": 1}
range: 255
area: {"shape": 1, "shape_name": "circle", "radius": 255.0, "width_or_angle": 255.0}
cost: {"type": 14, "type_name": "TP", "amount": 1500, "from": "Skill_TP"}
cooldown: {"ms": 120000, "group": 0, "from": "Skill_TP"}
effect_kind: 0
effects:
  - {"slot": 1, "type": 464, "value": 14011, "rate": 100}
damage_or_effect: {}
icon: {"file": "Policy_01.png", "index": 15}
used_by: []
tp: {"row": 3, "tp_cost": 1500, "cooldown_s": 120, "need_flags": 388, "c7": 1}
observed:
  - {"tp": 1500, "cooldown_s": 120, "effect": "PvP: hits enemy towers, then the nexus once the attacking towers are gone. PvE: hits every boss after the middle one", "source": "gameplay/pvp-and-matches line 32"}
---
<!-- generated:start -->
<!-- generated-keys: title=06ceac type=86a754 id=2023e0 sources=dd81f9 name_key=2dc197 desc_key=808bd8 kind=356a19 kind_name=9bc378 target=35e077 range=3028f5 area=febbd1 cost=4e6c0e cooldown=d97414 effect_kind=b6589f effects=21a7fc damage_or_effect=bf21a9 icon=413f00 used_by=97d170 tp=defae4 observed=fbb03a -->
|  |  |
|---|---|
|  | ![Remote Bomb](../assets/skills/4527.png) |
| **Skill id** | `4527` |
| **Kind** | active (1) |
| **Target** | self; self; units: player, structure; up to 1 |
| **Range** | 255 (world units) |
| **Area** | circle, radius 255, width/angle 255 |
| **Cost** | 1,500 TP |
| **Cooldown** | 120 s |
| **TP skill** | 1,500 TP, 120 s cooldown (Skill_TP row 3) |
| **Icon** | `ui/icons/Policy_01.png` cell 15 |

### Tooltip

> Attack enemy objects. If there is an enemy attack tower, attack the tower first.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 464 | unknown | 14,011 | 100 |

### Observed in play

Numbers from the gameplay pages (guides, patch notes, video), not from the client:

| cooldown (s) | mana | TP | effect | source |
|---|---|---|---|---|
| 120 |  | 1500 | PvP: hits enemy towers, then the nexus once the attacking towers are gone. PvE: hits every boss after the middle one | [[gameplay/pvp-and-matches]] line 32 |

### Mentioned in

- [[gameplay/maps-and-dungeons|Maps and dungeons]] § 2. Border-area (normal/hard) dungeons (line 60): - Demon Hell's boss is shown as two identical figures and Thorn's Hell's as three (multi-boss fights). The Remote Bomb TP skill text says that in PvE it "att...
- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § TP skills (line 32): Remote Bomb (4502/4527) · Nexus · 1,500 · 120 s · 1500 / 120 · PvP: hits enemy towers, then the nexus once the attacking towers are gone. PvE: hits every bos...
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § TP (line 43, at 37:19, 2:32): Remote Bomb · −1,500 (3,050 → 1,550, 37:19) · P1 2:32 · video, matches Skill_TP 1,500
<!-- generated:end -->

## Notes

<!-- hand-written: add what you know, with a source -->

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
