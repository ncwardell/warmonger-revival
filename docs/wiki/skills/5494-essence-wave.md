---
title: "Essence Wave"
type: "skill"
id: 5494
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5494", "client: StringAll_Eng SkillComment_5494 (tooltip value tags)", "notes: [[gameplay/classes-and-legions]] §5 Skeleton King's Vision Bow, WM 0110 (cooldown and mana match client)"]
name_key: "Skill_5494"
desc_key: "SkillComment_5494"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 17
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 18.0, "width_or_angle": 3.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 330}
cooldown: {"ms": 55000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 120, "rate": 100}
  - {"slot": 2, "type": 101, "value": 100, "rate": 0}
  - {"slot": 3, "type": 102, "value": 90, "rate": 0}
  - {"slot": 4, "type": 301, "value": 10442, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 120, "attack_pct": 100, "ability_pct": 90, "buffs": [{"buff": 10442, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 120}
  - {"tag": "EF_R_DAM", "value": 100}
  - {"tag": "EF_R_MDAM", "value": 90}
visual: 484
icon: {"file": "Skill_Miriam_01.png", "index": 37}
used_by:
  - {"weapon_base": 86, "slot": 4, "items": [15005]}
---
<!-- generated:start -->
<!-- generated-keys: title=ebf099 type=86a754 id=6c098a sources=9d8139 name_key=a6cf8d desc_key=c6ff7e kind=356a19 kind_name=9bc378 target=e84f24 range=0716d9 area=34415f cost=e10ae0 cooldown=8825ab delivery=93a212 effect_kind=356a19 effects=a380b3 damage_or_effect=6f175a tooltip_formula=ec12cc visual=329a97 icon=2c4899 used_by=11955c -->
|  |  |
|---|---|
|  | ![Essence Wave](wiki/assets/skills/5494.png) |
| **Skill id** | `5494` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 17 (world units) |
| **Area** | line / rectangle?, radius 18, width/angle 3 (indicator `stick256x512.png`) |
| **Cost** | 330 MP |
| **Cooldown** | 55 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 484 `해골왕의 비전 활_정조준 일격` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 37 |

### Tooltip

> [Active] Shoots a large wave of pure energy, inflicting `{EF_STATIC 120}``{EF_R_DAM 100}``{EF_R_MDAM 90}` Damage to all enemies it passes. The stack increases by the number of enemies damaged by energy missiles.

Tooltip formula: **120 + 100% Attack + 90% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 120 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 100 | 0 |
| 3 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 90 | 0 |
| 4 | 301 | applies buff (variant 301) | [[wiki/buffs/10442-vision-explosion-stack\|Vision explosion : Stack]] | 100 |

**Reading:** amount **120 + 100% Attack + 90% Ability Power**; damage (physical?); applies [[wiki/buffs/10442-vision-explosion-stack|Vision explosion : Stack]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 86: [[wiki/items/15005-skeleton-king-s-vision-bow|Skeleton king's Vision Bow]]

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]] § Weapons (line 115): R · Essence Wave · 55 s · 330 · 120 + 1.0 AD + 0.875 AP to all hit; +1 Vision stack per enemy hit
<!-- generated:end -->

## Notes

- [WM 0110](https://steamcommunity.com/games/718790/announcements/detail/2417771014047971842) (text + image 2) introduced Skeleton King's Vision Bow (item 15005) with this R: 55 s cooldown, 330 mana; 120 + 1.0 AD + 0.875 AP to everything hit, +1 Vision stack per enemy hit ([[gameplay/classes-and-legions]] §5). Cooldown and mana match the client exactly. *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/classes-and-legions]] §5 Skeleton King's Vision Bow.

## Open questions

- Multipliers: the patch note's AD/AP factors differ slightly from the client tooltip (the client tooltip has 120 + 100 % AD + 90 % AP); the note may quote values at a different weapon level. Client kept.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
