---
title: "Step Back"
type: "skill"
id: 5136
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5136", "client: StringAll_Eng SkillComment_5136 (tooltip value tags)"]
name_key: "Skill_5136"
desc_key: "SkillComment_5136"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 6
cost: {"type": 5, "type_name": "MP", "amount": 140}
cooldown: {"ms": 20000, "group": 0}
movement: "dash"
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 70, "rate": 100}
  - {"slot": 2, "type": 101, "value": 50, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10160, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 70, "attack_pct": 50, "buffs": [{"buff": 10160, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_DAM", "value": 50}
visual: 278
icon: {"file": "Skill_Dolorece_01.png", "index": 30}
used_by:
  - {"weapon_base": 56, "slot": 3, "items": [40014]}
---
<!-- generated:start -->
<!-- generated-keys: title=4e3e91 type=86a754 id=dfd71b sources=27af1f name_key=b04740 desc_key=4fa5c6 kind=356a19 kind_name=9bc378 target=aa5d92 range=c1dfd9 cost=911ade cooldown=628d31 movement=5f1488 delivery=93a212 effect_kind=356a19 effects=d3096d damage_or_effect=16c1dd tooltip_formula=5fe65c visual=68b519 icon=b534c0 used_by=94f28a -->
|  |  |
|---|---|
|  | ![Step Back](wiki/assets/skills/5136.png) |
| **Skill id** | `5136` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 1 |
| **Range** | 6 (world units) |
| **Cost** | 140 MP |
| **Cooldown** | 20 s |
| **Movement** | dash |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 278 `PCD_Cannon_05_E_날랜 백스텝` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 30 |

### Tooltip

> [Active] Launch a missile into the designated direction that deals `{EF_STATIC 70}``{EF_R_DAM 50}` Damage on impact. You also take a quick step back while firing.

Tooltip formula: **70 + 50% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 50 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10160-quick-step-back-decreases-attack-speed\|Quick Step Back: Decreases Attack Speed]] | 100 |

**Reading:** amount **70 + 50% Attack**; damage (physical?); applies [[wiki/buffs/10160-quick-step-back-decreases-attack-speed|Quick Step Back: Decreases Attack Speed]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 56: [[wiki/items/40014-skeleton-king-s-magic-cannon|Skeleton King's Magic Cannon]]
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
