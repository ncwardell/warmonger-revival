---
title: "Pyrotechnics"
type: "skill"
id: 5218
status: "stub"
missing: ["damage_or_effect", "cooldown", "cost"]
sources: ["client: Skill_Base.cdb id 5218"]
name_key: "Skill_5218"
desc_key: "SkillComment_5218"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": [], "unit_classes": [], "max_targets": 1}
range: 255
area: {"shape": 1, "shape_name": "circle", "radius": 1.0, "width_or_angle": 1.0}
cost: null
cooldown: null
effect_kind: 0
effects:
  - {"slot": 1, "type": 264, "value": 1, "rate": 0}
damage_or_effect: {}
icon: {"file": "Policy_01.png", "index": 32}
used_by:
  - {"item_use": 1105}
  - {"item_use": 50002}
---
<!-- generated:start -->
<!-- generated-keys: title=38244f type=86a754 id=ec2603 sources=e376d9 name_key=61fa9a desc_key=243811 kind=356a19 kind_name=9bc378 target=e0d9b5 range=3028f5 area=394af4 cost=2be88c cooldown=2be88c effect_kind=b6589f effects=e7ea45 damage_or_effect=bf21a9 icon=130210 used_by=989c4b -->
|  |  |
|---|---|
|  | ![Pyrotechnics](wiki/assets/skills/5218.png) |
| **Skill id** | `5218` |
| **Kind** | active (1) |
| **Target** | ground; -; units: -; up to 1 |
| **Range** | 255 (world units) |
| **Area** | circle, radius 1, width/angle 1 |
| **Icon** | `ui/icons/Policy_01.png` cell 32 |

### Tooltip

> Notify your allies.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 264 | unknown | 1 | 0 |

### Used by

- Cast when [[wiki/items/1105-pyrotechnics|Pyrotechnics]] is used (Item_Base option 210)
- Cast when [[wiki/items/50002-pyrotechnics|Pyrotechnics]] is used (Item_Base option 210)

### Mentioned in

- [[gameplay/progression-and-economy|Progression and economy]] § Wren (Merchant) — prices in gold, *image* (definitive guide)(g-def) §Dungeons, (strategy guide)(g-strat) (line 51): Pyrotechnics · 3,960 · 500 (1105) · 7.92
- [[gameplay/progression-and-economy|Progression and economy]] § Athan (Merits Merchant) — prices in medals, *image* (noob guide)(g-noob) (line 66): Pyrotechnics · 100 (yellow coin currency)
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
