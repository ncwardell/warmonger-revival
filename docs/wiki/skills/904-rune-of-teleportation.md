---
title: "Rune of Teleportation"
type: "skill"
id: 904
status: "stub"
missing: ["damage_or_effect", "cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 904"]
name_key: "Skill_800"
desc_key: "SkillComment_800"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 100
cost: null
cooldown: null
effect_kind: 2
effects:
  - {"slot": 1, "type": 328, "value": 10001, "rate": 0}
damage_or_effect: {}
visual: 266
icon: {"file": "Skill_MagicScholar_17.png", "index": 0}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=4c68c5 type=86a754 id=6f2c73 sources=7142cf name_key=2d8c2e desc_key=916ec7 kind=356a19 kind_name=9bc378 target=cacd0a range=310b86 cost=2be88c cooldown=2be88c effect_kind=da4b92 effects=1a2747 damage_or_effect=bf21a9 visual=45cbe1 icon=826275 used_by=97d170 -->
|  |  |
|---|---|
| **Skill id** | `904` |
| **Kind** | active (1) |
| **Target** | ground; self; units: monster, player; up to 1 |
| **Range** | 100 (world units) |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 266 `공간이동` |
| **Icon** | `ui/icons/Skill_MagicScholar_17.png` cell 0 |

### Tooltip

> Teleport

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 328 | summon? (unknown) | 10,001 | 0 |
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
