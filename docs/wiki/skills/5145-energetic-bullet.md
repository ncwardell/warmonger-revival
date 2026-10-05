---
title: "Energetic Bullet"
type: "skill"
id: 5145
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5145", "client: StringAll_Eng SkillComment_5145 (tooltip value tags)"]
name_key: "Skill_5145"
desc_key: "SkillComment_5145"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 9
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 10.0, "width_or_angle": 2.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 120}
cooldown: {"ms": 16000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 75, "rate": 100}
  - {"slot": 2, "type": 101, "value": 80, "rate": 0}
  - {"slot": 3, "type": 301, "value": 10170, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 75, "attack_pct": 80, "buffs": [{"buff": 10170, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 75}
  - {"tag": "EF_R_DAM", "value": 80}
visual: 288
icon: {"file": "Skill_Einsel_01.png", "index": 28}
used_by:
  - {"weapon_base": 15, "slot": 1, "items": [10014]}
---
<!-- generated:start -->
<!-- generated-keys: title=41cc51 type=86a754 id=ee45e1 sources=700f08 name_key=1aa93c desc_key=5d60ab kind=356a19 kind_name=9bc378 target=e84f24 range=0ade7c area=728214 cost=deac18 cooldown=a93f07 delivery=93a212 effect_kind=356a19 effects=87f999 damage_or_effect=a1ff01 tooltip_formula=74c011 visual=b70706 icon=721c7c used_by=0564fd -->
|  |  |
|---|---|
|  | ![Energetic Bullet](../assets/skills/5145.png) |
| **Skill id** | `5145` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 9 (world units) |
| **Area** | line / rectangle?, radius 10, width/angle 2 (indicator `stick256x512.png`) |
| **Cost** | 120 MP |
| **Cooldown** | 16 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 288 `PCE_Gun_05_Q_암흑탄` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 28 |

### Tooltip

> [Active] A bullet that deals `{EF_STATIC 75}``{EF_R_DAM 80}` damage on impact. After a successful hit you empower your next basic attack to deal an additional 3% of the enemy's current health as bonus damage.

Tooltip formula: **75 + 80% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 75 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 80 | 0 |
| 3 | 301 | applies buff (variant 301) | [[wiki/buffs/10170-energetic-bullet-your-next-basic-attack-deals-additional-dam\|Energetic Bullet : Your next basic attack deals additional damage]] | 100 |

**Reading:** amount **75 + 80% Attack**; damage (physical?); applies [[wiki/buffs/10170-energetic-bullet-your-next-basic-attack-deals-additional-dam|Energetic Bullet : Your next basic attack deals additional damage]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 15: [[wiki/items/10014-skeleton-king-s-magic-gun|Skeleton king's Magic Gun]]
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
