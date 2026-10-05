---
title: "Careful Attack"
type: "skill"
id: 5302
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5302", "client: StringAll_Eng SkillComment_5302 (tooltip value tags)", "notes: [[gameplay/classes-and-legions]] §5 Weapons, WM 0712 (Q/R AP → AD + AP; matches this row)"]
name_key: "Skill_5302"
desc_key: "SkillComment_5302"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 20
cost: {"type": 5, "type_name": "MP", "amount": 390}
cooldown: {"ms": 70000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 200, "rate": 100}
  - {"slot": 2, "type": 101, "value": 110, "rate": 0}
  - {"slot": 3, "type": 102, "value": 90, "rate": 100}
  - {"slot": 4, "type": 314, "value": 10356, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 200, "attack_pct": 110, "ability_pct": 90, "buffs": [{"buff": 10356, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 200}
  - {"tag": "EF_R_DAM", "value": 110}
  - {"tag": "EF_R_MDAM", "value": 90}
visual: 386
icon: {"file": "Skill_Dolorece_01.png", "index": 31}
used_by:
  - {"weapon_base": 68, "slot": 4, "items": [20014]}
---
<!-- generated:start -->
<!-- generated-keys: title=ac4ac9 type=86a754 id=496e12 sources=1a6d46 name_key=6030b4 desc_key=964346 kind=356a19 kind_name=9bc378 target=069ef3 range=91032a cost=ff5a60 cooldown=ad2ac8 delivery=93a212 effect_kind=da4b92 effects=f4b2a9 damage_or_effect=8eadc3 tooltip_formula=a0e324 visual=295df4 icon=14a444 used_by=5924e5 -->
|  |  |
|---|---|
|  | ![Careful Attack](../assets/skills/5302.png) |
| **Skill id** | `5302` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 20 (world units) |
| **Cost** | 390 MP |
| **Cooldown** | 70 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 386 `시즌1_PCD_Cannon_05_R_신중한 일격` |
| **Icon** | `ui/icons/Skill_Dolorece_01.png` cell 31 |

### Tooltip

> [Active] Shoot amagic missile and deal `{EF_STATIC 200}``{EF_R_DAM 110}``{EF_R_MDAM 90}` Magic Damage, stunning the enemy.

Tooltip formula: **200 + 110% Attack + 90% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 200 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 110 | 0 |
| 3 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 90 | 100 |
| 4 | 314 | applies buff (variant 314) | [[wiki/buffs/10356-careful-attack-stunned-for-3-seconds\|Careful Attack : Stunned for 3 seconds]] | 100 |

**Reading:** amount **200 + 110% Attack + 90% Ability Power**; damage (magic?); applies [[wiki/buffs/10356-careful-attack-stunned-for-3-seconds|Careful Attack : Stunned for 3 seconds]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 68: [[wiki/items/20014-skeleton-king-s-magic-cannon|Skeleton King's Magic Cannon]]
<!-- generated:end -->

## Notes

- Patch history: [WM 0712](https://steamcommunity.com/games/718790/announcements/detail/2838841185432966428) changed Skeleton King's Magic Cannon's Q and R from AP to AD + AP scaling (and weapon growth AD +10 → +8, AP +2). This copy (item 20014) has both AD and AP in its client tooltip. ([[gameplay/classes-and-legions]] §5 Weapons). *notes*

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
