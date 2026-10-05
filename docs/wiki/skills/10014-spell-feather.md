---
title: "Spell Feather"
type: "skill"
id: 10014
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10014", "client: StringAll_Eng SkillComment_10014 (tooltip value tags)"]
name_key: "Skill_10014"
desc_key: "SkillComment_10014"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 9
cost: {"type": 5, "type_name": "MP", "amount": 100}
cooldown: {"ms": 12000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 102, "value": 85, "rate": 0}
  - {"slot": 3, "type": 314, "value": 30016, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 80, "ability_pct": 85, "buffs": [{"buff": 30016, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_MDAM", "value": 85}
visual: 199
icon: {"file": "Skill_Einsel_01.png", "index": 12}
used_by:
  - {"weapon_base": 104, "slot": 1, "items": [11003]}
---
<!-- generated:start -->
<!-- generated-keys: title=41659a type=86a754 id=ef75f7 sources=47ff43 name_key=0fd459 desc_key=8525cf kind=356a19 kind_name=9bc378 target=069ef3 range=0ade7c cost=4e8ae0 cooldown=d1c73e delivery=93a212 effect_kind=da4b92 effects=005da4 damage_or_effect=16a18a tooltip_formula=67f65b visual=2952ae icon=31f51a used_by=166c98 -->
|  |  |
|---|---|
|  | ![Spell Feather](wiki/assets/skills/10014.png) |
| **Skill id** | `10014` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 9 (world units) |
| **Cost** | 100 MP |
| **Cooldown** | 12 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 199 `PCE_Staff_04 Q 마력깃든 깃털` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 12 |

### Tooltip

> [Active] Sends out a Spell Feather that deals `{EF_STATIC 80}``{EF_R_MDAM 85}` damage. Decreases the enemy's Movement Speed by 90 for 2 seconds.

Tooltip formula: **80 + 85% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 85 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/30016-spell-feather-reduced-movement-speed\|Spell Feather : Reduced Movement Speed]] | 100 |

**Reading:** amount **80 + 85% Ability Power**; damage (magic?); applies [[wiki/buffs/30016-spell-feather-reduced-movement-speed|Spell Feather : Reduced Movement Speed]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 104: [[wiki/items/11003-magical-cystal-wand|Magical Cystal Wand]]
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
