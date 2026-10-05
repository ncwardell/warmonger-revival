---
title: "Power Shot"
type: "skill"
id: 5045
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5045", "client: StringAll_Eng SkillComment_5045 (tooltip value tags)"]
name_key: "Skill_5045"
desc_key: "SkillComment_5045"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 9
cost: {"type": 5, "type_name": "MP", "amount": 60}
cooldown: {"ms": 4000, "group": 0}
delivery: {"type": 1, "field_tick": 0.0}
effect_kind: 10
effects:
  - {"slot": 1, "type": 330, "value": 70, "rate": 100}
  - {"slot": 2, "type": 101, "value": 90, "rate": 0}
damage_or_effect: {"kind": "effect kind 10", "base": 70, "attack_pct": 90}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_DAM", "value": 90}
visual: 193
icon: {"file": "Skill_Miriam_01.png", "index": 5}
used_by:
  - {"weapon_base": 23, "slot": 2, "items": [15001]}
---
<!-- generated:start -->
<!-- generated-keys: title=3339ea type=86a754 id=9c9e16 sources=f5374f name_key=02e14b desc_key=228437 kind=356a19 kind_name=9bc378 target=aa5d92 range=0ade7c cost=7b288b cooldown=e61764 delivery=93a212 effect_kind=b1d578 effects=867c43 damage_or_effect=9cf909 tooltip_formula=e73004 visual=14bb99 icon=bdb8b8 used_by=3bbc3d -->
|  |  |
|---|---|
|  | ![Power Shot](../assets/skills/5045.png) |
| **Skill id** | `5045` |
| **Kind** | active (1) |
| **Target** | ground; enemy; units: monster, player; up to 1 |
| **Range** | 9 (world units) |
| **Cost** | 60 MP |
| **Cooldown** | 4 s |
| **Delivery** | projectile / SFX |
| **Effect kind** | ? (10) |
| **Visual** | skillVisual 193 `PCM_Bow_02_W 팽팽한 시위` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 5 |

### Tooltip

> [Active] You summon all your strength, dealing `{EF_STATIC 70}``{EF_R_DAM 90}` Damage.

Tooltip formula: **70 + 90% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 90 | 0 |

**Reading:** amount **70 + 90% Attack**; effect kind 10.

### Used by

- Weapon skill **W** of WeaponBase 23: [[wiki/items/15001-magical-sniping-bow|Magical Sniping Bow]]
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
