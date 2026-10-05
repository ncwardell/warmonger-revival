---
title: "Punishing Stomp"
type: "skill"
id: 10051
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10051", "client: StringAll_Eng SkillComment_10051 (tooltip value tags)"]
name_key: "Skill_10051"
desc_key: "SkillComment_10051"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 5
area: {"shape": 1, "shape_name": "circle", "radius": 5.0, "width_or_angle": 0.0}
cost: {"type": 5, "type_name": "MP", "amount": 45}
cooldown: {"ms": 1000, "group": 0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 102, "value": 85, "rate": 0}
  - {"slot": 3, "type": 314, "value": 30046, "rate": 100}
  - {"slot": 4, "type": 305, "value": 30045, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 80, "ability_pct": 85, "buffs": [{"buff": 30046, "rate": 100}, {"buff": 30045, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_MDAM", "value": 85}
weapon_type: 2
visual: 172
icon: {"file": "Skill_Einsel_01.png", "index": 21}
used_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=deb569 type=86a754 id=f87c3c sources=965bb0 name_key=e2291c desc_key=5e6767 kind=356a19 kind_name=9bc378 target=d1cc1b range=ac3478 area=500aa4 cost=077e82 cooldown=4a6a0b effect_kind=da4b92 effects=9f4c43 damage_or_effect=73e5d9 tooltip_formula=67f65b weapon_type=da4b92 visual=c1aa04 icon=83e0e4 used_by=97d170 -->
|  |  |
|---|---|
|  | ![Punishing Stomp](wiki/assets/skills/10051.png) |
| **Skill id** | `10051` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 5 |
| **Range** | 5 (world units) |
| **Area** | circle, radius 5, width/angle 0 |
| **Cost** | 45 MP |
| **Cooldown** | 1 s |
| **Effect kind** | damage (magic?) (2) |
| **Needs weapon type** | 2 |
| **Visual** | skillVisual 172 `PCE_Knife_01_W 침묵폭발 (형벌의 인장 : 침묵)` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 21 |

### Tooltip

> [Active] Deals `{EF_STATIC 80}``{EF_R_MDAM 85}` Damage and silences all enemies in the surrounding area for 2 seconds.

Tooltip formula: **80 + 85% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 85 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/30046-punishing-stomp-silenced-for-2-seconds\|Punishing Stomp : Silenced for 2 seconds]] | 100 |
| 4 | 305 | applies buff (variant 305) | [[wiki/buffs/30045-punishing-charge-you-are-able-to-use-punishing-stomp-now\|Punishing Charge : You are able to use Punishing Stomp now]] | 100 |

**Reading:** amount **80 + 85% Ability Power**; damage (magic?); applies [[wiki/buffs/30046-punishing-stomp-silenced-for-2-seconds|Punishing Stomp : Silenced for 2 seconds]] (100%); applies [[wiki/buffs/30045-punishing-charge-you-are-able-to-use-punishing-stomp-now|Punishing Charge : You are able to use Punishing Stomp now]] (100%).
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
