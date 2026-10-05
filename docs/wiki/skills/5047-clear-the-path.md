---
title: "Clear the Path"
type: "skill"
id: 5047
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5047", "client: StringAll_Eng SkillComment_5047 (tooltip value tags)"]
name_key: "Skill_5047"
desc_key: "SkillComment_5047"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 17
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 18.0, "width_or_angle": 4.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 340}
cooldown: {"ms": 60000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 120, "rate": 100}
  - {"slot": 2, "type": 101, "value": 90, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 120, "attack_pct": 90}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 120}
  - {"tag": "EF_R_DAM", "value": 90}
visual: 196
icon: {"file": "Skill_Miriam_01.png", "index": 7}
used_by:
  - {"weapon_base": 23, "slot": 4, "items": [15001]}
---
<!-- generated:start -->
<!-- generated-keys: title=483d7a type=86a754 id=60fb73 sources=35f615 name_key=01f91c desc_key=640dc9 kind=356a19 kind_name=9bc378 target=e84f24 range=0716d9 area=eebd23 cost=9e049c cooldown=7d0c8c delivery=93a212 effect_kind=356a19 effects=7c3a79 damage_or_effect=95e4bf tooltip_formula=b062e9 visual=4dea1d icon=8148c0 used_by=ed1e57 -->
|  |  |
|---|---|
|  | ![Clear the Path](../assets/skills/5047.png) |
| **Skill id** | `5047` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 17 (world units) |
| **Area** | line / rectangle?, radius 18, width/angle 4 (indicator `stick256x512.png`) |
| **Cost** | 340 MP |
| **Cooldown** | 60 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 196 `PCM_Bow_02_R 냉혹한 저격` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 7 |

### Tooltip

> [Active] Shoots a large arrow that deals `{EF_STATIC 120}``{EF_R_DAM 90}` Damage to all enemies in its path.

Tooltip formula: **120 + 90% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 120 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 90 | 0 |

**Reading:** amount **120 + 90% Attack**; damage (physical?).

### Used by

- Weapon skill **R** of WeaponBase 23: [[wiki/items/15001-magical-sniping-bow|Magical Sniping Bow]]
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
