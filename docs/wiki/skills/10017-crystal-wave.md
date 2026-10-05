---
title: "Crystal Wave"
type: "skill"
id: 10017
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10017", "client: StringAll_Eng SkillComment_10017 (tooltip value tags)"]
name_key: "Skill_10017"
desc_key: "SkillComment_10017"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 7
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 11.0, "width_or_angle": 4.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 340}
cooldown: {"ms": 60000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 120, "rate": 100}
  - {"slot": 2, "type": 102, "value": 125, "rate": 0}
  - {"slot": 3, "type": 314, "value": 30020, "rate": 100}
damage_or_effect: {"kind": "damage (magic?)", "base": 120, "ability_pct": 125, "buffs": [{"buff": 30020, "rate": 100}]}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 120}
  - {"tag": "EF_R_MDAM", "value": 125}
visual: 202
icon: {"file": "Skill_Einsel_01.png", "index": 15}
used_by:
  - {"weapon_base": 104, "slot": 4, "items": [11003]}
---
<!-- generated:start -->
<!-- generated-keys: title=1c8d34 type=86a754 id=4cc58c sources=c912ec name_key=766893 desc_key=1606cf kind=356a19 kind_name=9bc378 target=e84f24 range=902ba3 area=73f973 cost=9e049c cooldown=7d0c8c delivery=93a212 effect_kind=da4b92 effects=0246c1 damage_or_effect=56fd33 tooltip_formula=fec5dc visual=1e7b95 icon=29c012 used_by=431c69 -->
|  |  |
|---|---|
|  | ![Crystal Wave](../assets/skills/10017.png) |
| **Skill id** | `10017` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 7 (world units) |
| **Area** | line / rectangle?, radius 11, width/angle 4 (indicator `stick256x512.png`) |
| **Cost** | 340 MP |
| **Cooldown** | 60 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 202 `PCE_Staff_04 R 수정가시 지대` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 15 |

### Tooltip

> [Active] Sends out a wave that deals `{EF_STATIC 120}``{EF_R_MDAM 125}` damage to everyone in its path. Decreases the Movement Speed of all targets hit by 150 for 4 seconds.

Tooltip formula: **120 + 125% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 120 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 125 | 0 |
| 3 | 314 | applies buff (variant 314) | [[wiki/buffs/30020-wave-of-crystals-reduced-movement-speed\|Wave of Crystals : Reduced Movement Speed]] | 100 |

**Reading:** amount **120 + 125% Ability Power**; damage (magic?); applies [[wiki/buffs/30020-wave-of-crystals-reduced-movement-speed|Wave of Crystals : Reduced Movement Speed]] (100%).

### Used by

- Weapon skill **R** of WeaponBase 104: [[wiki/items/11003-magical-cystal-wand|Magical Cystal Wand]]

### Current server

- `server/skills.py` line 203: `assert skills_of(10017) == (5022, 5023, 5024, 5025)`
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
