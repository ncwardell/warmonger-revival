---
title: "Water strike"
type: "skill"
id: 20157
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 20157", "client: StringAll_Eng SkillComment_20157 (tooltip value tags)"]
name_key: "Skill_20157"
desc_key: "SkillComment_20157"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 3
cost: {"type": 5, "type_name": "MP", "amount": 85}
cooldown: {"ms": 9000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 70, "rate": 100}
  - {"slot": 2, "type": 101, "value": 60, "rate": 0}
  - {"slot": 3, "type": 314, "value": 20160, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 70, "attack_pct": 60, "buffs": [{"buff": 20160, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_DAM", "value": 60}
visual: 426
icon: {"file": "Skill_Boss_01.dds", "index": 27}
used_by:
  - {"weapon_base": 72, "slot": 5, "items": [8003, 8503]}
---
<!-- generated:start -->
<!-- generated-keys: title=d37e41 type=86a754 id=1484ff sources=a9ee29 name_key=a8d6da desc_key=f90f8a kind=356a19 kind_name=9bc378 target=069ef3 range=77de68 cost=4921ef cooldown=db479b delivery=93a212 effect_kind=da4b92 effects=328e6c damage_or_effect=ca9af7 tooltip_formula=d90a2a visual=62866a icon=e71b04 used_by=889fc9 -->
|  |  |
|---|---|
|  | ![Water strike](wiki/assets/skills/20157.png) |
| **Skill id** | `20157` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 3 (world units) |
| **Cost** | 85 MP |
| **Cooldown** | 9 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 426 `사라스바티_물의 타격` |
| **Icon** | `ui/icons/Skill_Boss_01.dds` cell 27 |

### Tooltip

> [Active]Deals damage to selected enemies by `{EF_STATIC 70}``{EF_R_DAM 60}`.

Tooltip formula: **70 + 60% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 60 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/20160\|Buff 20160]] | 100 |

**Reading:** amount **70 + 60% Attack**; damage (magic?); applies [[wiki/buffs/20160|Buff 20160]] (100%).

### Used by

- Weapon skill **hero set 1** of WeaponBase 72: [[wiki/items/8003-sarasvati|Sarasvati]], [[wiki/items/8503-crystal-sarasvati|Crystal : Sarasvati]]
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
