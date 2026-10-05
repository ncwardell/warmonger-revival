---
title: "Ankle Aim"
type: "skill"
id: 5102
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5102", "client: StringAll_Eng SkillComment_5102 (tooltip value tags)"]
name_key: "Skill_5102"
desc_key: "SkillComment_5102"
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
  - {"slot": 2, "type": 101, "value": 90, "rate": 0}
  - {"slot": 3, "type": 314, "value": 10084, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 90, "buffs": [{"buff": 10084, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 90}
visual: 240
icon: {"file": "Skill_Einsel_01.png", "index": 16}
used_by:
  - {"weapon_base": 12, "slot": 1, "items": [10011]}
---
<!-- generated:start -->
<!-- generated-keys: title=75557b type=86a754 id=0519a3 sources=02907f name_key=8085c6 desc_key=5a2160 kind=356a19 kind_name=9bc378 target=069ef3 range=902ba3 cost=4e8ae0 cooldown=d1c73e delivery=93a212 effect_kind=356a19 effects=7bbbe3 damage_or_effect=4163a5 tooltip_formula=0fc93d visual=cae91e icon=3b602b used_by=aae6a5 -->
|  |  |
|---|---|
|  | ![Ankle Aim](wiki/assets/skills/5102.png) |
| **Skill id** | `5102` |
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

> [Active] Firing both pistols at once, dealing `{EF_STATIC 80}``{EF_R_DAM 90}` Damage. Decreases their Movement Speed by 30.

Tooltip formula: **80 + 90% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 90 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/10084-double-time-decrease-movement-speed-by-30\|Double Time : Decrease Movement Speed by 30%]] | 100 |

**Reading:** amount **80 + 90% Attack**; damage (physical?); applies [[wiki/buffs/10084-double-time-decrease-movement-speed-by-30|Double Time : Decrease Movement Speed by 30%]] (100%).

### Used by

- Weapon skill **Q** of WeaponBase 12: [[wiki/items/10011-magical-adapted-dual-gun|Magical adapted Dual Gun]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot Q for [[wiki/items/10011-magical-adapted-dual-gun|Magical adapted Dual Gun]].
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
