---
title: "Crystal Wave"
type: "skill"
id: 5017
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5017", "client: StringAll_Eng SkillComment_5017 (tooltip value tags)", "notes: [[gameplay/classes-and-legions]] §5 Weapons, WM 0412 (R slow 2 → 4 s; matches client tooltip)"]
name_key: "Skill_5017"
desc_key: "SkillComment_5017"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 7
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 11.0, "width_or_angle": 4.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 340}
cooldown: {"ms": 60000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 120, "rate": 100}
  - {"slot": 2, "type": 102, "value": 120, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10020, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 120, "ability_pct": 120, "buffs": [{"buff": 10020, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 120}
  - {"tag": "EF_R_MDAM", "value": 120}
visual: 202
icon: {"file": "Skill_Einsel_01.png", "index": 15}
used_by:
  - {"weapon_base": 4, "slot": 4, "items": [10003]}
---
<!-- generated:start -->
<!-- generated-keys: title=1c8d34 type=86a754 id=d3ca45 sources=5c4873 name_key=6ccb5a desc_key=9cc80e kind=356a19 kind_name=9bc378 target=e84f24 range=902ba3 area=73f973 cost=9e049c cooldown=7d0c8c delivery=93a212 effect_kind=da4b92 effects=892f7e damage_or_effect=8810df tooltip_formula=bb1008 visual=1e7b95 icon=29c012 used_by=e652a6 -->
|  |  |
|---|---|
|  | ![Crystal Wave](wiki/assets/skills/5017.png) |
| **Skill id** | `5017` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 7 (world units) |
| **Area** | line / rectangle?, radius 11, width/angle 4 (indicator `stick256x512.png`) |
| **Cost** | 340 MP |
| **Cooldown** | 60 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 202 `PCE_Staff_04 R 수정가시 지대` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 15 |

### Tooltip

> [Active] Sends out a wave that deals `{EF_STATIC 120}``{EF_R_MDAM 120}` damage to everyone in its path. Decreases the Movement Speed of all targets hit by 150 for 4 seconds.

Tooltip formula: **120 + 120% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 120 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 120 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10020-wave-of-crystals-reduced-movement-speed\|Wave of Crystals : Reduced Movement Speed]] | 100 |

**Reading:** amount **120 + 120% Ability Power**; damage (magic?); applies [[wiki/buffs/10020-wave-of-crystals-reduced-movement-speed|Wave of Crystals : Reduced Movement Speed]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 4: [[wiki/items/10003-magical-cystal-wand|Magical Cystal Wand]]
<!-- generated:end -->

## Notes

- Patch history: [WM 0412](https://steamcommunity.com/games/718790/announcements/detail/2394102381817542359) lengthened Magical Crystal Wand's R slow 2 → 4 s; the client tooltip says 4 seconds. The note names the weapon, not an item id; it is copied to every same-name copy of the skill. ([[gameplay/classes-and-legions]] §5 Weapons). *notes*

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
