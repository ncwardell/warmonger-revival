---
title: "Savior's Gift"
type: "skill"
id: 10281
status: "partial"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 10281", "notes: [[gameplay/classes-and-legions]] §5 Weapons, WM 0412 (range 8 → 6, recovery 6 → 5)"]
name_key: "Skill_10281"
desc_key: "SkillComment_10281"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["self", "party"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 8
area: {"shape": 1, "shape_name": "circle", "radius": 6.0, "width_or_angle": 6.0}
cost: {"type": 5, "type_name": "MP", "amount": 440}
cooldown: {"ms": 80000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 324, "value": 15004, "rate": 100}
damage_or_effect: {}
visual: 366
icon: {"file": "Skill_Einsel_01.png", "index": 11}
used_by:
  - {"weapon_base": 164, "slot": 4, "items": [11002]}
---
<!-- generated:start -->
<!-- generated-keys: title=eee00b type=86a754 id=3f7449 sources=3aa975 name_key=e3321b desc_key=0f89e0 kind=356a19 kind_name=9bc378 target=8871e4 range=fe5dbb area=d82541 cost=15d513 cooldown=dceb3e effect_kind=356a19 effects=4a377e damage_or_effect=bf21a9 visual=b00168 icon=5095da used_by=875f34 -->
|  |  |
|---|---|
|  | ![Savior's Gift](../assets/skills/10281.png) |
| **Skill id** | `10281` |
| **Kind** | active (1) |
| **Target** | ground; self, party; units: monster, player; up to 1 |
| **Range** | 8 (world units) |
| **Area** | circle, radius 6, width/angle 6 |
| **Cost** | 440 MP |
| **Cooldown** | 80 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 366 `시즌1_PCE_Staff_03_R_구원의 선물` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 11 |

### Tooltip

> [Active] Summons a Recovery Zone to a designated location, restoring party members' HP by 5% of their target HP for 6 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 324 | unknown | 15,004 | 100 |

### Used by

- Weapon skill **R** of WeaponBase 164: [[wiki/items/11002-magical-life-wand|Magical Life Wand]]
<!-- generated:end -->

## Notes

- Patch history: [WM 0412](https://steamcommunity.com/games/718790/announcements/detail/2394102381817542359) cut Magical Life Wand (10002)'s R range 8 → 6 and its recovery 6 → 5. The client tooltip restores 5 % (matches) but the client range is still 8. ([[gameplay/classes-and-legions]] §5 Weapons). *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/classes-and-legions]] §5 Weapons.

## Open questions

- Range: WM 0412 says 8 → 6; the client `range` is 8. The client value is kept (client first).

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
