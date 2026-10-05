---
title: "Fury of fire"
type: "skill"
id: 19953
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 19953", "client: StringAll_Eng SkillComment_19953 (tooltip value tags)"]
name_key: "Skill_19953"
desc_key: "SkillComment_19953"
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
  - {"slot": 3, "type": 314, "value": 19954, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 90, "buffs": [{"buff": 19954, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 90}
visual: 404
icon: {"file": "Skill_Einsel_01.png", "index": 38}
used_by:
  - {"weapon_base": 74, "slot": 3, "items": [8005, 8505]}
---
<!-- generated:start -->
<!-- generated-keys: title=087e2d type=86a754 id=abe6a4 sources=13b7c1 name_key=1e1107 desc_key=7abe33 kind=356a19 kind_name=9bc378 target=d1cc1b range=1b6453 area=6d01a6 cost=58a4ca cooldown=133145 effect_kind=356a19 effects=5065a9 damage_or_effect=4f893d tooltip_formula=0fc93d visual=c35a9f icon=01ddda used_by=1f5802 -->
|  |  |
|---|---|
|  | ![Fury of fire](../assets/skills/19953.png) |
| **Skill id** | `19953` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 130 MP |
| **Cooldown** | 18 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 404 `모리온_불의 격노` |
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
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/19954-fury-of-fire-stun-2-secs\|Fury of fire : Stun (2 Secs)]] | 100 |

**Reading:** amount **80 + 90% Attack**; damage (physical?); applies [[wiki/buffs/19954-fury-of-fire-stun-2-secs|Fury of fire : Stun (2 Secs)]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 74: [[wiki/items/8005-morion|Morion]], [[wiki/items/8505-crystal-morion|Crystal : Morion]]
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
