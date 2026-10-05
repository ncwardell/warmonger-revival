---
title: "Lightning Strike"
type: "skill"
id: 5005
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5005", "client: StringAll_Eng SkillComment_5005 (tooltip value tags)"]
name_key: "Skill_5005"
desc_key: "SkillComment_5005"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 12}
range: 7
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 105}
cooldown: {"ms": 13000, "group": 0}
delivery: {"type": 4, "field_tick": 1.3}
effect_kind: 2
effects:
  - {"slot": 1, "type": 330, "value": 100, "rate": 100}
  - {"slot": 2, "type": 102, "value": 100, "rate": 0}
damage_or_effect: {"kind": "damage (magic?)", "base": 100, "ability_pct": 100}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 100}
  - {"tag": "EF_R_MDAM", "value": 100}
visual: 104
icon: {"file": "Skill_Einsel_01.png", "index": 5}
used_by:
  - {"weapon_base": 2, "slot": 2, "items": [10001]}
---
<!-- generated:start -->
<!-- generated-keys: title=b22690 type=86a754 id=8aba9e sources=450b04 name_key=8a6d06 desc_key=86224c kind=356a19 kind_name=9bc378 target=138a60 range=902ba3 area=6d01a6 cost=d57e66 cooldown=f8ee77 delivery=d66f33 effect_kind=da4b92 effects=e9f59a damage_or_effect=844296 tooltip_formula=a8acf5 visual=78a8ef icon=eb1101 used_by=163ab7 -->
|  |  |
|---|---|
|  | ![Lightning Strike](wiki/assets/skills/5005.png) |
| **Skill id** | `5005` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 12 |
| **Range** | 7 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 105 MP |
| **Cooldown** | 13 s |
| **Delivery** | projectile / SFX (4), tick 1.3 |
| **Effect kind** | damage (magic?) (2) |
| **Visual** | skillVisual 104 `PCE_Staff_02_W_낙뢰` |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 5 |

### Tooltip

> [Active] Thunder strikes in the targeted area that deals `{EF_STATIC 100}``{EF_R_MDAM 100}`damage.

Tooltip formula: **100 + 100% Ability Power** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 100 | 100 |
| 2 | 102 | % of Ability Power (tooltip `EF_R_MDAM`) | 100 | 0 |

**Reading:** amount **100 + 100% Ability Power**; damage (magic?).

### Used by

- Weapon skill **W** of WeaponBase 2: [[wiki/items/10001-magical-thunder-wand|Magical Thunder Wand]]

### Current server

- `server/skills.py` WEAPON_SKILLS puts it on slot W for [[wiki/items/10001-magical-thunder-wand|Magical Thunder Wand]].
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
