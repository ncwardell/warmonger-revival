---
title: "Thunderbolt"
type: "skill"
id: 10004
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10004", "client: StringAll_Eng SkillComment_10004 (tooltip value tags)", "notes: [[gameplay/classes-and-legions]] §5 Weapons, WM 0412 (Q base 70 → 80; matches client)"]
name_key: "Skill_10004"
desc_key: "SkillComment_10004"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 7
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 9.0, "width_or_angle": 2.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 75}
cooldown: {"ms": 7000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 102, "value": 85, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 80, "ability_pct": 85}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_MDAM", "value": 85}
visual: 103
icon: {"file": "Skill_Einsel_01.png", "index": 4}
used_by:
  - {"weapon_base": 102, "slot": 1, "items": [11001]}
---
<!-- generated:start -->
<!-- generated-keys: title=6d3029 type=86a754 id=75186a sources=83cbcf name_key=e72125 desc_key=8cdfe1 kind=356a19 kind_name=9bc378 target=e84f24 range=902ba3 area=b10964 cost=8b4fa7 cooldown=0156ad delivery=93a212 effect_kind=da4b92 effects=40e76d damage_or_effect=bfab1c tooltip_formula=67f65b visual=934385 icon=fc253c used_by=d77be7 -->
|  |  |
|---|---|
|  | ![Thunderbolt](../assets/skills/10004.png) |
| **Skill id** | `10004` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 7 (world units) |
| **Area** | line / rectangle?, radius 9, width/angle 2 (indicator `stick256x512.png`) |
| **Cost** | 75 MP |
| **Cooldown** | 7 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 103 `PCE_Staff_02_Q_광휘의 일격` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 4 |

### Tooltip

> [Active] Blast an enemy unit with `{EF_STATIC 80}``{EF_R_MDAM 85}`.

Tooltip formula: **80 + 85% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 85 | 0 |

**Reading:** amount **80 + 85% Ability Power**; damage (magic?).

### Used by

- Weapon skill **Q** of WeaponBase 102: [[wiki/items/11001-magical-thunder-wand|Magical Thunder Wand]]
- Nation policy 5 `PolicyName_5` (Policy.cdb, server-only; buff_or_skill)
<!-- generated:end -->

## Notes

- Patch history: [WM 0412](https://steamcommunity.com/games/718790/announcements/detail/2394102381817542359) raised Magical Thunder Wand (10001)'s Q AP base 70 → 80; the client tooltip base is 80. ([[gameplay/classes-and-legions]] §5 Weapons). *notes*

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
