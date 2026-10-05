---
title: "Mystic Arrow"
type: "skill"
id: 5491
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5491", "client: StringAll_Eng SkillComment_5491 (tooltip value tags)", "notes: [[gameplay/classes-and-legions]] §5 Skeleton King's Vision Bow, WM 0110 (cooldown and mana match client)"]
name_key: "Skill_5491"
desc_key: "SkillComment_5491"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 10
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 11.0, "width_or_angle": 2.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 75}
cooldown: {"ms": 5000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 85, "rate": 100}
  - {"slot": 2, "type": 101, "value": 85, "rate": 0}
  - {"slot": 3, "type": 102, "value": 65, "rate": 0}
  - {"slot": 4, "type": 301, "value": 10443, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 85, "attack_pct": 85, "ability_pct": 65, "buffs": [{"buff": 10443, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 85}
  - {"tag": "EF_R_DAM", "value": 80}
  - {"tag": "EF_R_MDAM", "value": 65}
visual: 481
icon: {"file": "Skill_Miriam_01.png", "index": 34}
used_by:
  - {"weapon_base": 86, "slot": 1, "items": [15005]}
---
<!-- generated:start -->
<!-- generated-keys: title=c57537 type=86a754 id=f85931 sources=48cb19 name_key=1ed5a9 desc_key=a0e6c7 kind=356a19 kind_name=9bc378 target=aa5d92 range=b1d578 area=2a66b8 cost=8b4fa7 cooldown=752bf3 delivery=93a212 effect_kind=356a19 effects=4bd619 damage_or_effect=194b1b tooltip_formula=9636b4 visual=2978e0 icon=744c36 used_by=8115b7 -->
|  |  |
|---|---|
|  | ![Mystic Arrow](../assets/skills/5491.png) |
| **Skill id** | `5491` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 1 |
| **Range** | 10 (world units) |
| **Area** | line / rectangle?, radius 11, width/angle 2 (indicator `stick256x512.png`) |
| **Cost** | 75 MP |
| **Cooldown** | 5 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 481 `해골왕의 비젼 활_신비한 화살` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 34 |

### Tooltip

> [Active]Shoots an energy arrow that deals `{EF_STATIC 85}``{EF_R_DAM 80}``{EF_R_MDAM 65}` Damage. When Mistic Arrow hits an enemy, your attack speed is increased 20% for 6 sec.

Tooltip formula: **85 + 80% Attack + 65% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 85 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 85 | 0 |
| 3 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 65 | 0 |
| 4 | 301 | applies buff (variant 301) | [[wiki/buffs/10443-mystic-arrow-increased-attack-speed\|Mystic Arrow : Increased Attack Speed]] | 100 |

**Reading:** amount **85 + 85% Attack + 65% Ability Power**; damage (physical?); applies [[wiki/buffs/10443-mystic-arrow-increased-attack-speed|Mystic Arrow : Increased Attack Speed]] (100%).

> [!warning] The tooltip (85 + 80% Attack + 65% Ability Power) and the effect slots (85 + 85% Attack + 65% Ability Power) disagree; one of them was out of date in the shipped client.

### Used by

- Weapon skill **Q** of WeaponBase 86: [[wiki/items/15005-skeleton-king-s-vision-bow|Skeleton king's Vision Bow]]

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]] § Weapons (line 112): Q · Mystic Arrow · 5 s · 75 · 85 + 0.8 AD + 0.625 AP; on hit, attack speed up for 6 s
<!-- generated:end -->

## Notes

- [WM 0110](https://steamcommunity.com/games/718790/announcements/detail/2417771014047971842) (text + image 2) introduced Skeleton King's Vision Bow (item 15005) with this Q: 5 s cooldown, 75 mana; 85 + 0.8 AD + 0.625 AP, and attack speed up for 6 s on hit ([[gameplay/classes-and-legions]] §5). Cooldown and mana match the client exactly. *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/classes-and-legions]] §5 Skeleton King's Vision Bow.

## Open questions

- Multipliers: the patch note's AD/AP factors differ slightly from the client tooltip (the client tooltip has 85 + 80 % AD + 65 % AP); the note may quote values at a different weapon level. Client kept.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
