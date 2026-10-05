---
title: "Capture Weakness"
type: "skill"
id: 20208
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20208", "client: StringAll_Eng SkillComment_20208 (tooltip value tags)"]
name_key: "Skill_20208"
desc_key: "SkillComment_20208"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 8
cost: {"type": 5, "type_name": "MP", "amount": 75}
cooldown: {"ms": 7000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 80, "rate": 0}
  - {"slot": 3, "type": 314, "value": 20209, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 80, "buffs": [{"buff": 20209, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 80}
visual: 435
icon: {"file": "Skill_Boss_01.dds", "index": 35}
used_by:
  - {"weapon_base": 73, "slot": 5, "items": [8004, 8504]}
---
<!-- generated:start -->
<!-- generated-keys: title=24df62 type=86a754 id=b4863e sources=82add5 name_key=8c1d9a desc_key=273bb4 kind=356a19 kind_name=9bc378 target=069ef3 range=fe5dbb cost=8b4fa7 cooldown=0156ad delivery=93a212 effect_kind=356a19 effects=bf32e7 damage_or_effect=6b45df tooltip_formula=4709a0 visual=784ef0 icon=48d69c used_by=314d29 -->
|  |  |
|---|---|
|  | ![Capture Weakness](../assets/skills/20208.png) |
| **Skill id** | `20208` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 8 (world units) |
| **Cost** | 75 MP |
| **Cooldown** | 7 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 435 `아르타모스_약점 포착` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 35 |

### Tooltip

> [Active] Gives `{EF_STATIC 80}``{EF_R_DAM 80}` Physical Damage to the specified target and reduces Movement Speed for 3 seconds.

Tooltip formula: **80 + 80% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 80 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/20209-capture-weakness-reduced-movement-speed\|Capture Weakness: Reduced Movement Speed]] | 100 |

**Reading:** amount **80 + 80% Attack**; damage (physical?); applies [[wiki/buffs/20209-capture-weakness-reduced-movement-speed|Capture Weakness: Reduced Movement Speed]] (100%).

### Used by

- Weapon skill **hero set 1** of WeaponBase 73: [[wiki/items/8004-artamos|Artamos]], [[wiki/items/8504-crystal-artamos|Crystal : Artamos]]
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
