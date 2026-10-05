---
title: "Flare"
type: "skill"
id: 5213
status: "stub"
missing: ["damage_or_effect", "cost"]
sources: ["client: Skill_Base.cdb id 5213"]
name_key: "Skill_5213"
desc_key: "SkillComment_5213"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 255
cost: null
cooldown: {"ms": 5000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 324, "value": 10002, "rate": 0}
damage_or_effect: {}
visual: 350
icon: {"file": "Policy_01.png", "index": 33}
used_by:
  - {"item_use": 2909}
---
<!-- generated:start -->
<!-- generated-keys: title=67d2a6 type=86a754 id=fc6d7e sources=0c2cb1 name_key=65638b desc_key=f60a71 kind=356a19 kind_name=9bc378 target=cacd0a range=3028f5 cost=2be88c cooldown=752bf3 effect_kind=da4b92 effects=ac0355 damage_or_effect=bf21a9 visual=89a1c1 icon=d4b33d used_by=72c4c6 -->
|  |  |
|---|---|
|  | ![Flare](wiki/assets/skills/5213.png) |
| **Skill id** | `5213` |
| **Kind** | active (1) |
| **Target** | ground; self; units: monster, player; up to 1 |
| **Range** | 255 (world units) |
| **Cooldown** | 5 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 350 `TP_Flare` |
| **Icon** | `ui/icons/Policy_01.png` cell 33 |

### Tooltip

> Reveal the targeted area temporarily.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 324 | unknown | 10,002 | 0 |

### Used by

- Cast when [[wiki/items/2909-flare|Flare]] is used (Item_Base option 210)
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
