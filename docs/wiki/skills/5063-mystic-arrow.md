---
title: "Mystic Arrow"
type: "skill"
id: 5063
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5063", "client: StringAll_Eng SkillComment_5063 (tooltip value tags)"]
name_key: "Skill_5063"
desc_key: "SkillComment_5063"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 10
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 11.0, "width_or_angle": 2.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 65}
cooldown: {"ms": 5000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 101, "value": 90, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 90}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 90}
visual: 76
icon: {"file": "Skill_Miriam_01.png", "index": 8}
used_by:
  - {"weapon_base": 24, "slot": 1, "items": [15002]}
---
<!-- generated:start -->
<!-- generated-keys: title=c57537 type=86a754 id=476714 sources=e83543 name_key=e6f206 desc_key=fe72b1 kind=356a19 kind_name=9bc378 target=aa5d92 range=b1d578 area=2a66b8 cost=9fa5fb cooldown=752bf3 delivery=93a212 effect_kind=356a19 effects=db4d14 damage_or_effect=75d6a2 tooltip_formula=0fc93d visual=d54ad0 icon=a11afc used_by=4f4baf -->
|  |  |
|---|---|
|  | ![Mystic Arrow](wiki/assets/skills/5063.png) |
| **Skill id** | `5063` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 1 |
| **Range** | 10 (world units) |
| **Area** | line / rectangle?, radius 11, width/angle 2 (indicator `stick256x512.png`) |
| **Cost** | 65 MP |
| **Cooldown** | 5 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 76 `PCM_Bow_03_Q_신비한화살` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 8 |

### Tooltip

> [Active] Shoots an energy arrow that deals `{EF_STATIC 80}``{EF_R_DAM 90}` Damage.

Tooltip formula: **80 + 90% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 90 | 0 |

**Reading:** amount **80 + 90% Attack**; damage (physical?).

### Used by

- Weapon skill **Q** of WeaponBase 24: [[wiki/items/15002-magical-vision-bow|Magical Vision Bow]]

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]] § Weapons (line 112): Q · Mystic Arrow · 5 s · 75 · 85 + 0.8 AD + 0.625 AP; on hit, attack speed up for 6 s
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
