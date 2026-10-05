---
title: "Rapid Reload"
type: "skill"
id: 10103
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10103", "client: StringAll_Eng SkillComment_10103 (tooltip value tags)"]
name_key: "Skill_10103"
desc_key: "SkillComment_10103"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["self"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 1
cost: {"type": 5, "type_name": "MP", "amount": 115}
cooldown: {"ms": 15000, "group": 0}
effect_kind: 0
effects:
  - {"slot": 1, "type": 314, "value": 30085, "rate": 100}
  - {"slot": 2, "type": 301, "value": 30140, "rate": 100}
damage_or_effect: {"buffs": [{"buff": 30085, "rate": 100}, {"buff": 30140, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 10}
  - {"tag": "EF_R_DAM", "value": 125}
visual: 241
icon: {"file": "Skill_Einsel_01.png", "index": 17}
used_by:
  - {"weapon_base": 112, "slot": 2, "items": [11011]}
---
<!-- generated:start -->
<!-- generated-keys: title=590afc type=86a754 id=a5f419 sources=9e2051 name_key=f337b3 desc_key=9bad85 kind=356a19 kind_name=9bc378 target=d99f6c range=356a19 cost=e4e7cf cooldown=e3989d effect_kind=b6589f effects=3a7bd3 damage_or_effect=320ef9 tooltip_formula=d317c6 visual=9ffd1a icon=7c2320 used_by=fee542 -->
|  |  |
|---|---|
|  | ![Rapid Reload](wiki/assets/skills/10103.png) |
| **Skill id** | `10103` |
| **Kind** | active (1) |
| **Target** | self; self; units: monster, player; up to 1 |
| **Range** | 1 (world units) |
| **Cost** | 115 MP |
| **Cooldown** | 15 s |
| **Visual** | skillVisual 241 `PCE_Gun_01_W` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 17 |

### Tooltip

> [Active] Gain 40% Attack and Movement Speed. Your basic Attacks deal an additional `{EF_STATIC 10}``{EF_R_DAM 125}` Damage for 4 seconds.

Tooltip formula: **10 + 125% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 314 | applies buff (variant 314) | [[wiki/buffs/30085-rapid-reload-gain-improved-attack-and-movement-speed\|Rapid Reload : Gain improved Attack and Movement Speed]] | 100 |
| 2 | 301 | applies buff (variant 301) | [[wiki/buffs/30140-quick-reload-your-next-basic-attacks-deal-area-damage\|Quick Reload : Your next basic Attacks deal area damage]] | 100 |

**Reading:** applies [[wiki/buffs/30085-rapid-reload-gain-improved-attack-and-movement-speed|Rapid Reload : Gain improved Attack and Movement Speed]] (100%); applies [[wiki/buffs/30140-quick-reload-your-next-basic-attacks-deal-area-damage|Quick Reload : Your next basic Attacks deal area damage]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 112: [[wiki/items/11011-magical-adapted-dual-gun|Magical adapted Dual Gun]]
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
