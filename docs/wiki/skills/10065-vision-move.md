---
title: "Vision Move"
type: "skill"
id: 10065
status: "partial"
missing: ["damage_or_effect"]
sources: ["client: Skill_Base.cdb id 10065", "notes: [[gameplay/classes-and-legions]] §5 (describes the 5493 copy only)"]
name_key: "Skill_10065"
desc_key: "SkillComment_10065"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["ally", "enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 10
area: {"shape": 1, "shape_name": "circle", "radius": 1.0, "width_or_angle": 0.0}
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
movement: "blink / teleport"
effect_kind: 2
effects: []
damage_or_effect: {}
visual: 79
icon: {"file": "Skill_Miriam_01.png", "index": 10}
used_by:
  - {"weapon_base": 124, "slot": 3, "items": [16002]}
---
<!-- generated:start -->
<!-- generated-keys: title=be7862 type=86a754 id=cf6a3f sources=6749cd name_key=3fd887 desc_key=e06142 kind=356a19 kind_name=9bc378 target=c9e051 range=b1d578 area=3b02d8 cost=e4e7cf cooldown=e3989d movement=953fcf effect_kind=da4b92 effects=97d170 damage_or_effect=bf21a9 visual=b74f5e icon=ad8fbf used_by=d5239d -->
|  |  |
|---|---|
|  | ![Vision Move](../assets/skills/10065.png) |
| **Skill id** | `10065` |
| **Kind** | active (1) |
| **Target** | ground; ally, enemy; units: monster, player; up to 1 |
| **Range** | 10 (world units) |
| **Area** | circle, radius 1, width/angle 0 |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Movement** | blink / teleport |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 79 `PCM_Bow_03_E_비전 이동` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 10 |

### Tooltip

> [Active] Teleport to the designated location.

### Used by

- Weapon skill **E** of WeaponBase 124: [[wiki/items/16002-magical-vision-bow|Magical Vision Bow]]

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]] § Weapons (line 114): E · Vision Move · 15 s · 125 · teleport to target point
<!-- generated:end -->

## Notes

- A skill of the same name on Skeleton King's Vision Bow ([[wiki/skills/5493-vision-move|5493]]) is described in [WM 0110](https://steamcommunity.com/games/718790/announcements/detail/2417771014047971842) as a teleport to the target point ([[gameplay/classes-and-legions]] §5). This copy's own effect is not described in any source. *notes (other copy)*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/classes-and-legions]] §5.

## Open questions

- Effect not filled: no source describes this copy; the client tooltip and 5493 suggest the same teleport.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
