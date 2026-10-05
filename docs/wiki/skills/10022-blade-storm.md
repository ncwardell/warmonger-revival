---
title: "Blade storm"
type: "skill"
id: 10022
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10022", "client: StringAll_Eng SkillComment_10022 (tooltip value tags)", "notes: [[gameplay/classes-and-legions]] §5 Weapons, WM 0329/0402 (AD to AP)"]
name_key: "Skill_10022"
desc_key: "SkillComment_10022"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 65}
cooldown: {"ms": 5000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 102, "value": 95, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 80, "ability_pct": 95}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_MDAM", "value": 95}
visual: 177
icon: {"file": "Skill_Einsel_01.png", "index": 24}
used_by:
  - {"weapon_base": 118, "slot": 1, "items": [11017]}
---
<!-- generated:start -->
<!-- generated-keys: title=31cd33 type=86a754 id=9e4337 sources=a16c98 name_key=8b4ab5 desc_key=d0bd28 kind=356a19 kind_name=9bc378 target=d1cc1b range=1b6453 area=6d01a6 cost=9fa5fb cooldown=752bf3 effect_kind=da4b92 effects=9f5f2d damage_or_effect=80f374 tooltip_formula=93a825 visual=26e745 icon=e42156 used_by=444d5d -->
|  |  |
|---|---|
|  | ![Blade storm](../assets/skills/10022.png) |
| **Skill id** | `10022` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 65 MP |
| **Cooldown** | 5 s |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 177 `PCE_Knife_02_Q_칼날돌풍` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 24 |

### Tooltip

> [Active] Summons magical Blades that inflict `{EF_STATIC 80}``{EF_R_MDAM 95}` Magic Damage to nearby enemies.

Tooltip formula: **80 + 95% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 95 | 0 |

**Reading:** amount **80 + 95% Ability Power**; damage (magic?).

### Used by

- Weapon skill **Q** of WeaponBase 118: [[wiki/items/11017-magical-wrath-blade|Magical Wrath Blade]]

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 38): Saint · 10017 Magical Wrath Blade (Flying Blade) · 10011 Magical adapted Dual Gun (Dual Gun) · 10001 Magical Thunder Wand (Wand) · 10002 Magical Life Wand (n...
<!-- generated:end -->

## Notes

- Patch history: [WM 0329](https://steamcommunity.com/games/718790/announcements/detail/2383968106570216224) / [WM 0402](https://steamcommunity.com/games/718790/announcements/detail/2383968106583377018) moved Magical Wrath Blade's Q from AD to AP scaling; the client tooltip uses AP. The note names the weapon, not an item id; it is copied to every same-name copy of the skill. ([[gameplay/classes-and-legions]] §5 Weapons). *notes*

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
