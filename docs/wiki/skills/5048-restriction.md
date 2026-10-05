---
title: "Restriction"
type: "skill"
id: 5048
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5048", "client: StringAll_Eng SkillComment_5048 (tooltip value tags)", "notes: [[gameplay/classes-and-legions]] §5 Weapons, WM 0329/0402 (AD to AP)"]
name_key: "Skill_5048"
desc_key: "SkillComment_5048"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 2
cost: {"type": 5, "type_name": "MP", "amount": 110}
cooldown: {"ms": 14000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 301, "value": 10043, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "buffs": [{"buff": 10043, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_MDAM", "value": 90}
visual: 187
icon: {"file": "Skill_Einsel_01.png", "index": 20}
used_by:
  - {"weapon_base": 16, "slot": 1, "items": [10015]}
---
<!-- generated:start -->
<!-- generated-keys: title=a3e44e type=86a754 id=b5e429 sources=abb5b9 name_key=92ec8c desc_key=af42b2 kind=356a19 kind_name=9bc378 target=d99f6c range=da4b92 cost=060055 cooldown=5b7687 effect_kind=da4b92 effects=829f0a damage_or_effect=26e1b2 tooltip_formula=7b1add visual=f67462 icon=b7a24b used_by=c43c42 -->
|  |  |
|---|---|
|  | ![Restriction](../assets/skills/5048.png) |
| **Skill id** | `5048` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 2 (world units) |
| **Cost** | 110 MP |
| **Cooldown** | 14 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 187 `PCE_Knife_01_Q 시전 (빛의속박)` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 20 |

### Tooltip

> [Active] Your next attack deals an additional `{EF_STATIC 70}``{EF_R_MDAM 90}` Damage and holds the target in place for 3 seconds.

Tooltip formula: **70 + 90% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 301 | applies buff (variant 301) | [[wiki/buffs/10043-restriction-your-next-basic-attack-deals-additional-damage\|Restriction : Your next basic attack deals additional damage]] | 100 |

**Reading:** damage (magic?); applies [[wiki/buffs/10043-restriction-your-next-basic-attack-deals-additional-damage|Restriction : Your next basic attack deals additional damage]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 16: [[wiki/items/10015-magical-dash-blade|Magical Dash Blade]]
<!-- generated:end -->

## Notes

- Patch history: [WM 0329](https://steamcommunity.com/games/718790/announcements/detail/2383968106570216224) / [WM 0402](https://steamcommunity.com/games/718790/announcements/detail/2383968106583377018) moved Magical Dash Blade's Q and W scaling from AD to AP; the client tooltips use AP (`EF_R_MDAM`) where they have one. The note names the weapon, not an item id; it is copied to every same-name copy of the skill. ([[gameplay/classes-and-legions]] §5 Weapons). *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/classes-and-legions]] §5 Weapons.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
