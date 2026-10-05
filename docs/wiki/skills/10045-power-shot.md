---
title: "Power Shot"
type: "skill"
id: 10045
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10045", "client: StringAll_Eng SkillComment_10045 (tooltip value tags)"]
name_key: "Skill_10045"
desc_key: "SkillComment_10045"
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
  - {"slot": 2, "type": 101, "value": 95, "rate": 0}
damage_or_effect: {"kind": "effect kind 10", "base": 70, "attack_pct": 95}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 70}
  - {"tag": "EF_R_DAM", "value": 95}
visual: 193
icon: {"file": "Skill_Miriam_01.png", "index": 5}
used_by:
  - {"weapon_base": 123, "slot": 2, "items": [16001]}
---
<!-- generated:start -->
<!-- generated-keys: title=3339ea type=86a754 id=b19eeb sources=f6927a name_key=34bdfb desc_key=49929b kind=356a19 kind_name=9bc378 target=aa5d92 range=0ade7c cost=7b288b cooldown=e61764 delivery=93a212 effect_kind=b1d578 effects=0846bf damage_or_effect=5e58fa tooltip_formula=a3b220 visual=14bb99 icon=bdb8b8 used_by=3924c8 -->
|  |  |
|---|---|
|  | ![Power Shot](../assets/skills/10045.png) |
| **Skill id** | `10045` |
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

> [Active] You summon all your strength, dealing `{EF_STATIC 70}``{EF_R_DAM 95}` Damage.

Tooltip formula: **70 + 95% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 70 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 95 | 0 |

**Reading:** amount **70 + 95% Attack**; effect kind 10.

### Used by

- Weapon skill **W** of WeaponBase 123: [[wiki/items/16001-magical-sniping-bow|Magical Sniping Bow]]
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
