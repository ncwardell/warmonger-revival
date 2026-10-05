---
title: "Blessing of Order"
type: "skill"
id: 5052
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5052", "client: StringAll_Eng SkillComment_5052 (tooltip value tags)"]
name_key: "Skill_5052"
desc_key: "SkillComment_5052"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["self", "ally"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 6
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 317, "value": 10047, "rate": 100}
  - {"slot": 2, "type": 314, "value": 10048, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 10047, "rate": 100}, {"buff": 10048, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 30}
  - {"tag": "EF_R_MDAM", "value": 90}
visual: 173
icon: {"file": "Skill_Einsel_01.png", "index": 22}
used_by:
  - {"weapon_base": 16, "slot": 3, "items": [10015]}
---
<!-- generated:start -->
<!-- generated-keys: title=ef77b5 type=86a754 id=ff4fcd sources=f390ed name_key=8964cc desc_key=623912 kind=356a19 kind_name=9bc378 target=644925 range=c1dfd9 cost=e4e7cf cooldown=e3989d effect_kind=b6589f effects=84d674 damage_or_effect=2ff808 tooltip_formula=194b75 visual=572e20 icon=6b4fc5 used_by=d866e2 -->
|  |  |
|---|---|
|  | ![Blessing of Order](wiki/assets/skills/5052.png) |
| **Skill id** | `5052` |
| **Kind** | active (1) |
| **Target** | unit; self, ally; units: monster, player; up to 1 |
| **Range** | 6 (world units) |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Visual** | skillVisual 173 `PCE_Knife_01_E 시전 (질서의 가호)` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 22 |

### Tooltip

> [Active] Summon a Shield for yourself or an ally, dealing `{EF_STATIC 30}``{EF_R_MDAM 90}` Damage. When the Shield fades, it leaves a blessing that grants 10% Armor and Magic Resistance.

Tooltip formula: **30 + 90% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 317 | applies buff (variant 317) | [[wiki/buffs/10047-blessing-of-order-creates-a-shield-that-absorbs-damage-for-1\|Blessing of Order: Creates a shield that absorbs Damage for 10 seconds]] | 100 |
| 2 | 314 | applies buff (variant 314) | [[wiki/buffs/10048-blessing-of-order-explosion\|Blessing of Order : Explosion]] | 100 |

**Reading:** applies [[wiki/buffs/10047-blessing-of-order-creates-a-shield-that-absorbs-damage-for-1|Blessing of Order: Creates a shield that absorbs Damage for 10 seconds]] (100%); applies [[wiki/buffs/10048-blessing-of-order-explosion|Blessing of Order : Explosion]] (100%).

### Used by

- Weapon skill **E** of WeaponBase 16: [[wiki/items/10015-magical-dash-blade|Magical Dash Blade]]
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
