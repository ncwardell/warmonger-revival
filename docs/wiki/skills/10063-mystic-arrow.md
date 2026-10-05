---
title: "Mystic Arrow"
type: "skill"
id: 10063
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10063", "client: StringAll_Eng SkillComment_10063 (tooltip value tags)"]
name_key: "Skill_10063"
desc_key: "SkillComment_10063"
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
  - {"slot": 2, "type": 101, "value": 95, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 80, "attack_pct": 95}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_DAM", "value": 95}
visual: 76
icon: {"file": "Skill_Miriam_01.png", "index": 8}
used_by:
  - {"weapon_base": 124, "slot": 1, "items": [16002]}
---
<!-- generated:start -->
<!-- generated-keys: title=c57537 type=86a754 id=c1412d sources=0cee7d name_key=113a2c desc_key=63b715 kind=356a19 kind_name=9bc378 target=aa5d92 range=b1d578 area=2a66b8 cost=9fa5fb cooldown=752bf3 delivery=93a212 effect_kind=356a19 effects=d84d69 damage_or_effect=d4c414 tooltip_formula=42ecac visual=d54ad0 icon=a11afc used_by=b2d281 -->
|  |  |
|---|---|
|  | ![Mystic Arrow](../assets/skills/10063.png) |
| **Skill id** | `10063` |
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

> [Active] Shoots an energy arrow that deals `{EF_STATIC 80}``{EF_R_DAM 95}` Damage.

Tooltip formula: **80 + 95% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 95 | 0 |

**Reading:** amount **80 + 95% Attack**; damage (physical?).

### Used by

- Weapon skill **Q** of WeaponBase 124: [[wiki/items/16002-magical-vision-bow|Magical Vision Bow]]

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
