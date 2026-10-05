---
title: "Fang of Knives"
type: "skill"
id: 5290
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5290", "client: StringAll_Eng SkillComment_5290 (tooltip value tags)"]
name_key: "Skill_5290"
desc_key: "SkillComment_5290"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 5
area: {"shape": 1, "shape_name": "circle", "radius": 5.0, "width_or_angle": 5.0}
cost: {"type": 5, "type_name": "MP", "amount": 125}
cooldown: {"ms": 17000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 80, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10345, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 80, "attack_pct": 80, "buffs": [{"buff": 10345, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 80}
visual: 375
icon: {"file": "Skill_Miriam_01.png", "index": 26}
used_by:
  - {"weapon_base": 66, "slot": 3, "items": [15009]}
---
<!-- generated:start -->
<!-- generated-keys: title=09def0 type=86a754 id=a5f153 sources=68a236 name_key=e6d557 desc_key=c54e1c kind=356a19 kind_name=9bc378 target=d1cc1b range=ac3478 area=e8b0ea cost=f67772 cooldown=c9c532 effect_kind=da4b92 effects=59debb damage_or_effect=c56dc5 tooltip_formula=4709a0 visual=348763 icon=5f1bf5 used_by=9223cb -->
|  |  |
|---|---|
|  | ![Fang of Knives](../assets/skills/5290.png) |
| **Skill id** | `5290` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 5 (world units) |
| **Area** | circle, radius 5, width/angle 5 |
| **Cost** | 125 MP |
| **Cooldown** | 17 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 375 `시즌1_PCM_Knife_05_E_정면승부` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 26 |

### Tooltip

> [Active] Damages all nearby enemies with `{EF_STATIC 80}``{EF_R_DAM 80}` and decreases their Movement Speed briefly for 20%.

Tooltip formula: **80 + 80% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 80 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10345-fang-of-knives-reduced-movement-speed\|Fang of Knives : Reduced Movement Speed]] | 100 |

**Reading:** amount **80 + 80% Attack**; damage (magic?); applies [[wiki/buffs/10345-fang-of-knives-reduced-movement-speed|Fang of Knives : Reduced Movement Speed]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 66: [[wiki/items/15009-skeleton-king-s-magic-dagger|Skeleton King's Magic Dagger]]
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
