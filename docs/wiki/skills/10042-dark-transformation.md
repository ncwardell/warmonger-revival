---
title: "Dark Transformation"
type: "skill"
id: 10042
status: "stub"
missing: ["cost"]
sources: ["client: Skill_Base.cdb id 10042"]
name_key: "Skill_10042"
desc_key: "SkillComment_10042"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 3
cost: null
cooldown: {"ms": 2000, "group": 0}
effect_kind: 31
effects:
  - {"slot": 1, "type": 131, "value": 4, "rate": 0}
damage_or_effect: {"kind": "heal HP", "stats": [{"code": 131, "value": 4}]}
icon: null
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=128bcd type=86a754 id=22cdd7 sources=965a9a name_key=e6082d desc_key=a80afe kind=356a19 kind_name=9bc378 target=d99f6c range=77de68 cost=2be88c cooldown=367d78 effect_kind=632667 effects=64b278 damage_or_effect=88271d icon=2be88c used_by=97d170 -->
|  |  |
|---|---|
| **Skill id** | `10042` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 3 (world units) |
| **Cooldown** | 2 s |
| **Effect kind** | heal HP (31) |

### Tooltip

> -

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 131 | stat? Health(%) | 4 | 0 |

**Reading:** heal HP.

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 47): Dark Transformation · 60 s · 340 · More HP regeneration and movement speed for 10 s
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Steps (line 27, at 1:38, 3:20, 3:15): 1. Character creation 1:38–3:20. The nation is chosen first (Arslan). Then the class: Guardian, Saint, Punisher, each with a weapon picked from the class's l...
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
