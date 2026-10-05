---
title: "Step Back"
type: "skill"
id: 5301
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5301", "client: StringAll_Eng SkillComment_5301 (tooltip value tags)"]
name_key: "Skill_5301"
desc_key: "SkillComment_5301"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 6
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
movement: "dash"
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 70, "rate": 100}
  - {"slot": 2, "type": 102, "value": 70, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10355, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 70, "ability_pct": 70, "buffs": [{"buff": 10355, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_MDAM", "value": 70}
visual: 385
icon: {"file": "Skill_Dolorece_01.png", "index": 30}
used_by:
  - {"weapon_base": 68, "slot": 3, "items": [20014]}
---
<!-- generated:start -->
<!-- generated-keys: title=4e3e91 type=86a754 id=a009b3 sources=e018a3 name_key=f43fa5 desc_key=63d8d6 kind=356a19 kind_name=9bc378 target=aa5d92 range=c1dfd9 cost=e4e7cf cooldown=e3989d movement=5f1488 delivery=93a212 effect_kind=da4b92 effects=814337 damage_or_effect=8e9fea tooltip_formula=7fd566 visual=855679 icon=b534c0 used_by=6ead3a -->
|  |  |
|---|---|
|  | ![Step Back](../assets/skills/5301.png) |
| **Skill id** | `5301` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 1 |
| **Range** | 6 (world units) |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Movement** | dash |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 385 `시즌1_PCD_Cannon_05_E_날랜 백스텝` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 30 |

### Tooltip

> [Active] Launch a missile into the designated direction that deals `{EF_STATIC 70}``{EF_R_MDAM 70}` Damage on impact. You also take a quick step back while firing.

Tooltip formula: **70 + 70% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 70 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10355-quick-step-back-decreased-move-speed\|Quick step back : Decreased Move Speed]] | 100 |

**Reading:** amount **70 + 70% Ability Power**; damage (magic?); applies [[wiki/buffs/10355-quick-step-back-decreased-move-speed|Quick step back : Decreased Move Speed]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 68: [[wiki/items/20014-skeleton-king-s-magic-cannon|Skeleton King's Magic Cannon]]
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
