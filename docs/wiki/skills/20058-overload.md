---
title: "Overload"
type: "skill"
id: 20058
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20058"]
name_key: "Skill_5194"
desc_key: "SkillComment_5194"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 4, "type_name": "HP %", "amount": 13}
cooldown: {"ms": 120000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 301, "value": 20059, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 20059, "rate": 100}]}
visual: 332
icon: {"file": "Skill_Boss_01.dds", "index": 7}
used_by:
  - {"weapon_base": 70, "slot": 8, "items": [8001, 8501]}
---
<!-- generated:start -->
<!-- generated-keys: title=702564 type=86a754 id=638177 sources=576d9b name_key=8cf4dd desc_key=4b4148 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=2f3f9b cooldown=a7242f effect_kind=b6589f effects=177a18 damage_or_effect=e74c67 visual=ef2afd icon=914e85 used_by=495531 -->
|  |  |
|---|---|
|  | ![Overload](../assets/skills/20058.png) |
| **Skill id** | `20058` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 13 HP % |
| **Cooldown** | 120 s |
| **Visual** | skillVisual 332 `수호신장_변신스킬_08_마력의 폭주` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 7 |

### Tooltip

> [Active] You gain increased Movement Speed, Armor and Magic Resistance. You are immune to all abilities. Lasts 10 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/20059-overload-increased-movement-speed-armor-magic-resistance-and\|Overload : Increased Movement Speed, Armor, Magic Resistance and immune to abilities.]] | 100 |

**Reading:** applies [[wiki/buffs/20059-overload-increased-movement-speed-armor-magic-resistance-and|Overload : Increased Movement Speed, Armor, Magic Resistance and immune to abilities.]] (100%).

### Used by

- Weapon skill **hero set 4** of WeaponBase 70: [[wiki/items/8001-guardian|Guardian]], [[wiki/items/8501-crystal-guardian|Crystal : Guardian]]
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
