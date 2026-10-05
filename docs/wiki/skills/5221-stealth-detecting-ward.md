---
title: "Stealth Detecting Ward"
type: "skill"
id: 5221
status: "stub"
missing: ["damage_or_effect", "cost"]
sources: ["client: Skill_Base.cdb id 5221"]
name_key: "Skill_5221"
desc_key: "SkillComment_5221"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 15
cost: null
cooldown: {"ms": 10000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 324, "value": 13005, "rate": 100}
damage_or_effect: {}
icon: {"file": "Policy_01.png", "index": 38}
used_by:
  - {"item_use": 2911}
---
<!-- generated:start -->
<!-- generated-keys: title=bbbaf8 type=86a754 id=25b04c sources=b7dc3e name_key=5a06df desc_key=75e80f kind=356a19 kind_name=9bc378 target=cacd0a range=f1abd6 cost=2be88c cooldown=4aa5a5 effect_kind=da4b92 effects=78e46a damage_or_effect=bf21a9 icon=8066dc used_by=7fa1aa -->
|  |  |
|---|---|
|  | ![Stealth Detecting Ward](../assets/skills/5221.png) |
| **Skill id** | `5221` |
| **Kind** | active (1) |
| **Target** | ground; self; units: monster, player; up to 1 |
| **Range** | 15 (world units) |
| **Cooldown** | 10 s |
| **Effect kind** | damage (magic?) (2) |
| **Icon** | `ui/icons/Policy_01.png` cell 38 |

### Tooltip

> Places a ward that also detects hidden enemies in the surrounding area.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 324 | unknown | 13,005 | 100 |

### Used by

- Cast when [[wiki/items/2911-pinkward|Pinkward]] is used (Item_Base option 210)

### Mentioned in

- [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]] § 7. Consumables touched by patches (line 143): Flare / Ward / Stealth-detecting Ward (2909–2911, Wren) · ward lasts 90 s · WM 0809 notes + client
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
