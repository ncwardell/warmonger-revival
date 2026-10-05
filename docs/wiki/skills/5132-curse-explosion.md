---
title: "Curse Explosion"
type: "skill"
id: 5132
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5132", "client: StringAll_Eng SkillComment_5132 (tooltip value tags)"]
name_key: "Skill_5132"
desc_key: "SkillComment_5132"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 7}
range: 7
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 10.0, "width_or_angle": 4.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 415}
cooldown: {"ms": 75000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 110, "rate": 100}
  - {"slot": 2, "type": 102, "value": 90, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10155, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 110, "ability_pct": 90, "buffs": [{"buff": 10155, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 110}
  - {"tag": "EF_R_MDAM", "value": 90}
visual: 271
icon: {"file": "Skill_Dolorece_01.png", "index": 27}
used_by:
  - {"weapon_base": 46, "slot": 4, "items": [20004]}
---
<!-- generated:start -->
<!-- generated-keys: title=8a0810 type=86a754 id=5a8824 sources=4033e7 name_key=064659 desc_key=ff2bed kind=356a19 kind_name=9bc378 target=7056fd range=902ba3 area=bade13 cost=d55bc7 cooldown=cf1f8c delivery=93a212 effect_kind=da4b92 effects=4a087b damage_or_effect=7b305f tooltip_formula=6fe718 visual=ef7de0 icon=f19f25 used_by=101f1c -->
|  |  |
|---|---|
|  | ![Curse Explosion](../assets/skills/5132.png) |
| **Skill id** | `5132` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 7 |
| **Range** | 7 (world units) |
| **Area** | line / rectangle?, radius 10, width/angle 4 (indicator `stick256x512.png`) |
| **Cost** | 415 MP |
| **Cooldown** | 75 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 271 `PCD_Hammer_05_R_저주의폭발` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 27 |

### Tooltip

> [Active] Sends out an explosion that deals `{EF_STATIC 110}``{EF_R_MDAM 90}` Damage. Stuns every target in the area for 2 seconds.

Tooltip formula: **110 + 90% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 110 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 90 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10155-curse-explosion-stuns-all-enemies-for-2-seconds\|Curse Explosion : Stuns all enemies for 2 seconds]] | 100 |

**Reading:** amount **110 + 90% Ability Power**; damage (magic?); applies [[wiki/buffs/10155-curse-explosion-stuns-all-enemies-for-2-seconds|Curse Explosion : Stuns all enemies for 2 seconds]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 46: [[wiki/items/20004-skeleton-king-s-magic-hammer|Skeleton King's Magic Hammer]]
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
