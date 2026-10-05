---
title: "Thunderbolt"
type: "skill"
id: 5004
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5004", "client: StringAll_Eng SkillComment_5004 (tooltip value tags)"]
name_key: "Skill_5004"
desc_key: "SkillComment_5004"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 5}
range: 7
area: {"shape": 2, "shape_name": "line / rectangle?", "radius": 9.0, "width_or_angle": 2.0, "indicator": "stick256x512.png"}
cost: {"type": 5, "type_name": "MP", "amount": 75}
cooldown: {"ms": 7000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 80, "rate": 100}
  - {"slot": 2, "type": 102, "value": 80, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 80, "ability_pct": 80}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 80}
  - {"tag": "EF_R_MDAM", "value": 80}
visual: 103
icon: {"file": "Skill_Einsel_01.png", "index": 4}
used_by:
  - {"weapon_base": 2, "slot": 1, "items": [10001]}
---
<!-- generated:start -->
<!-- generated-keys: title=6d3029 type=86a754 id=3aca06 sources=c3f9a4 name_key=2b68ef desc_key=a8aa35 kind=356a19 kind_name=9bc378 target=e84f24 range=902ba3 area=b10964 cost=8b4fa7 cooldown=0156ad delivery=93a212 effect_kind=da4b92 effects=8a20a8 damage_or_effect=bf1784 tooltip_formula=c2e772 visual=934385 icon=fc253c used_by=79b415 -->
|  |  |
|---|---|
|  | ![Thunderbolt](../assets/skills/5004.png) |
| **Skill id** | `5004` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 5 |
| **Range** | 7 (world units) |
| **Area** | line / rectangle?, radius 9, width/angle 2 (indicator `stick256x512.png`) |
| **Cost** | 75 MP |
| **Cooldown** | 7 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 103 `PCE_Staff_02_Q_광휘의 일격` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 4 |

### Tooltip

> [Active] Blast an enemy unit with `{EF_STATIC 80}``{EF_R_MDAM 80}`.

Tooltip formula: **80 + 80% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 80 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 80 | 0 |

**Reading:** amount **80 + 80% Ability Power**; damage (magic?).

### Used by

- Weapon skill **Q** of WeaponBase 2: [[wiki/items/10001-magical-thunder-wand|Magical Thunder Wand]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot Q for [[wiki/items/10001-magical-thunder-wand|Magical Thunder Wand]].
- `server/world.py` deals a flat `SKILL_DAMAGE` (45 × 0.75–1.25) for every skill; nothing above is used yet.
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
