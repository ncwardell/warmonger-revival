---
title: "Backstab"
type: "skill"
id: 5461
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5461", "client: StringAll_Eng SkillComment_5461 (tooltip value tags)"]
name_key: "Skill_5461"
desc_key: "SkillComment_5461"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 20000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 301, "value": 10421, "rate": 100}
  - {"slot": 2, "type": 301, "value": 10422, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 10421, "rate": 100}, {"buff": 10422, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 10}
  - {"tag": "EF_R_DAM", "value": 100}
visual: 466
icon: {"file": "Skill_Miriam_01.png", "index": 29}
used_by:
  - {"weapon_base": 30, "slot": 1, "items": [15008]}
---
<!-- generated:start -->
<!-- generated-keys: title=982e1b type=86a754 id=8a7117 sources=40e687 name_key=0afbae desc_key=4a7da3 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=e4e7cf cooldown=628d31 effect_kind=356a19 effects=f083dd damage_or_effect=71ee17 tooltip_formula=e38d4c visual=cf2f32 icon=c0fb59 used_by=7cad31 -->
|  |  |
|---|---|
|  | ![Backstab](wiki/assets/skills/5461.png) |
| **Skill id** | `5461` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 115 MP |
| **Cooldown** | 20 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 466 `마력의 은신 대거_은신술_시전` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 29 |

### Tooltip

> [Active] Your Movement Speed is increased. Inflicts `{EF_STATIC 10}``{EF_R_DAM 100}` Damage during a basic attack. Reduces Movement Speed of all hit targets.

Tooltip formula: **10 + 100% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/10421-backstab-increase-movement-speed\|Backstab : Increase movement speed]] | 100 |
| 2 | 301 | applies buff (variant 301) | [[wiki/buffs/10422-backstab-your-basic-attacks-deal-additional-damage\|Backstab : Your basic Attacks deal additional damage]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/10421-backstab-increase-movement-speed|Backstab : Increase movement speed]] (100%); applies [[wiki/buffs/10422-backstab-your-basic-attacks-deal-additional-damage|Backstab : Your basic Attacks deal additional damage]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 30: [[wiki/items/15008-magical-hiding-dagger|Magical hiding Dagger]]

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]] § Weapons (line 97): 0420 · Magical Hiding Dagger (15008) · Q cooldown 15 → 19 s, W 20 → 25 s (client: Backstab 20 s, Deception 25 s)
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
