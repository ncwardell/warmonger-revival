---
title: "Ankle Aim"
type: "skill"
id: 10102
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10102", "client: StringAll_Eng SkillComment_10102 (tooltip value tags)"]
name_key: "Skill_10102"
desc_key: "SkillComment_10102"
kind: 1
kind_name: "active"
target: {"type": 1, "type_name": "unit", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 7
cost: {"type": 5, "type_name": "MP", "amount": 100}
cooldown: {"ms": 12000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 95, "rate": 0}
  - {"slot": 3, "type": 314, "value": 30084, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 95, "buffs": [{"buff": 30084, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 95}
visual: 240
icon: {"file": "Skill_Einsel_01.png", "index": 16}
used_by:
  - {"weapon_base": 112, "slot": 1, "items": [11011]}
---
<!-- generated:start -->
<!-- generated-keys: title=75557b type=86a754 id=049b27 sources=df5463 name_key=7e3310 desc_key=7b1f0d kind=356a19 kind_name=9bc378 target=069ef3 range=902ba3 cost=4e8ae0 cooldown=d1c73e delivery=93a212 effect_kind=356a19 effects=c5806d damage_or_effect=b94ea0 tooltip_formula=42ecac visual=cae91e icon=3b602b used_by=013b7b -->
|  |  |
|---|---|
|  | ![Ankle Aim](../assets/skills/10102.png) |
| **Skill id** | `10102` |
| **Kind** | active (1) |
| **Target** | unit; enemy; units: monster, player; up to 1 |
| **Range** | 7 (world units) |
| **Cost** | 100 MP |
| **Cooldown** | 12 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 240 `PCE_Gun_01_Q` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 16 |

### Tooltip

> [Active] Firing both pistols at once, dealing `{EF_STATIC 80}``{EF_R_DAM 95}` Damage. Decreases their Movement Speed by 30.

Tooltip formula: **80 + 95% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 95 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/30084-double-time-decrease-movement-speed-by-30\|Double Time : Decrease Movement Speed by 30%]] | 100 |

**Reading:** amount **80 + 95% Attack**; damage (physical?); applies [[wiki/buffs/30084-double-time-decrease-movement-speed-by-30|Double Time : Decrease Movement Speed by 30%]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 112: [[wiki/items/11011-magical-adapted-dual-gun|Magical adapted Dual Gun]]

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
