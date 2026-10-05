---
title: "Blade storm"
type: "skill"
id: 5022
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5022", "client: StringAll_Eng SkillComment_5022 (tooltip value tags)"]
name_key: "Skill_5022"
desc_key: "SkillComment_5022"
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
  - {"slot": 2, "type": 102, "value": 90, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 80, "ability_pct": 90}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_MDAM", "value": 90}
visual: 177
icon: {"file": "Skill_Einsel_01.png", "index": 24}
used_by:
  - {"weapon_base": 18, "slot": 1, "items": [10017]}
---
<!-- generated:start -->
<!-- generated-keys: title=31cd33 type=86a754 id=1e5872 sources=1b88ad name_key=6f0d4f desc_key=0fca3d kind=356a19 kind_name=9bc378 target=d1cc1b range=1b6453 area=6d01a6 cost=9fa5fb cooldown=752bf3 effect_kind=da4b92 effects=fea263 damage_or_effect=f4a963 tooltip_formula=fd41c2 visual=26e745 icon=e42156 used_by=8547fa -->
|  |  |
|---|---|
|  | ![Blade storm](../assets/skills/5022.png) |
| **Skill id** | `5022` |
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

> [Active] Summons magical Blades that inflict `{EF_STATIC 80}``{EF_R_MDAM 90}` Magic Damage to nearby enemies.

Tooltip formula: **80 + 90% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 90 | 0 |

**Reading:** amount **80 + 90% Ability Power**; damage (magic?).

### Used by

- Weapon skill **Q** of WeaponBase 18: [[wiki/items/10017-magical-wrath-blade|Magical Wrath Blade]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot Q for [[wiki/items/10017-magical-wrath-blade|Magical Wrath Blade]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 38): Saint · 10017 Magical Wrath Blade (Flying Blade) · 10011 Magical adapted Dual Gun (Dual Gun) · 10001 Magical Thunder Wand (Wand) · 10002 Magical Life Wand (n...
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
