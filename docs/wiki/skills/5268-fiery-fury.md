---
title: "Fiery Fury"
type: "skill"
id: 5268
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5268", "client: StringAll_Eng SkillComment_5268 (tooltip value tags)"]
name_key: "Skill_5268"
desc_key: "SkillComment_5268"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 130}
cooldown: {"ms": 18000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 90, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10332, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 90, "buffs": [{"buff": 10332, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 90}
visual: 388
icon: {"file": "Skill_Einsel_01.png", "index": 38}
used_by:
  - {"weapon_base": 6, "slot": 3, "items": [10005]}
---
<!-- generated:start -->
<!-- generated-keys: title=a04d5d type=86a754 id=8b637c sources=1f58d6 name_key=16c9be desc_key=5a59c4 kind=356a19 kind_name=9bc378 target=d1cc1b range=1b6453 area=6d01a6 cost=58a4ca cooldown=133145 effect_kind=356a19 effects=50c41c damage_or_effect=1bdbec tooltip_formula=0fc93d visual=113077 icon=01ddda used_by=58f2bc -->
|  |  |
|---|---|
|  | ![Fiery Fury](wiki/assets/skills/5268.png) |
| **Skill id** | `5268` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 130 MP |
| **Cooldown** | 18 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 388 `PCE_SwordShd_01_E_불의 격노` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 38 |

### Tooltip

> [Active] Stuns the enemy for 2 seconds and deals `{EF_STATIC 80}``{EF_R_DAM 90}` Damage.

Tooltip formula: **80 + 90% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 90 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10332-fury-of-fire-strun-2-secs\|Fury of fire : Strun (2 Secs)]] | 100 |

**Reading:** amount **80 + 90% Attack**; damage (physical?); applies [[wiki/buffs/10332-fury-of-fire-strun-2-secs|Fury of fire : Strun (2 Secs)]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 6: [[wiki/items/10005-magical-blade-shield-flame|Magical Blade Shield : Flame]]
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
