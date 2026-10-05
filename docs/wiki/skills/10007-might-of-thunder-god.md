---
title: "Might of Thunder God"
type: "skill"
id: 10007
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10007", "client: StringAll_Eng SkillComment_10007 (tooltip value tags)", "notes: [[gameplay/classes-and-legions]] §5 Weapons, WM 0412 (cooldown 70 → 60 s, note says E)"]
name_key: "Skill_10007"
desc_key: "SkillComment_10007"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 12}
range: 7
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 390}
cooldown: {"ms": 60000, "group": 0}
delivery: {"type": 4, "field_tick": 0.9}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 130, "rate": 100}
  - {"slot": 2, "type": 102, "value": 125, "rate": 0}
  - {"slot": 3, "type": 314, "value": 30007, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 130, "ability_pct": 125, "buffs": [{"buff": 30007, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 130}
  - {"tag": "EF_R_MDAM", "value": 125}
visual: 106
icon: {"file": "Skill_Einsel_01.png", "index": 7}
used_by:
  - {"weapon_base": 102, "slot": 4, "items": [11001]}
---
<!-- generated:start -->
<!-- generated-keys: title=bf802b type=86a754 id=24896e sources=9deb0b name_key=197d69 desc_key=76c252 kind=356a19 kind_name=9bc378 target=138a60 range=902ba3 area=6d01a6 cost=ff5a60 cooldown=7d0c8c delivery=4fe5f3 effect_kind=da4b92 effects=6e3ecc damage_or_effect=2d4b9e tooltip_formula=ce2c0c visual=7224f9 icon=62f758 used_by=06e165 -->
|  |  |
|---|---|
|  | ![Might of Thunder God](wiki/assets/skills/10007.png) |
| **Skill id** | `10007` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 12 |
| **Range** | 7 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 390 MP |
| **Cooldown** | 60 s |
| **Delivery** | projectile / SFX (4), tick 0.9 |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 106 `PCE_Staff_02_R_뇌전 작렬` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 7 |

### Tooltip

> [Active] Thunderbolts fall down at the targeted area, inflicting `{EF_STATIC 130}``{EF_R_MDAM 125}` damage. All targets that are hit are stunned for 2 seconds.

Tooltip formula: **130 + 125% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 130 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 125 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/30007-might-of-the-thunder-god-stunned-for-2-seconds\|Might of the Thunder God : Stunned for 2 seconds]] | 100 |

**Reading:** amount **130 + 125% Ability Power**; damage (magic?); applies [[wiki/buffs/30007-might-of-the-thunder-god-stunned-for-2-seconds|Might of the Thunder God : Stunned for 2 seconds]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 102: [[wiki/items/11001-magical-thunder-wand|Magical Thunder Wand]]
- Nation policy 8 `PolicyName_8` (Policy.cdb, server-only; buff_or_skill)
<!-- generated:end -->

## Notes

- Patch history: [WM 0412](https://steamcommunity.com/games/718790/announcements/detail/2394102381817542359) cut a Magical Thunder Wand cooldown 70 → 60 s. The note calls it the "E", but in the client the 60 s skill is this R. ([[gameplay/classes-and-legions]] §5 Weapons). *notes*

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
