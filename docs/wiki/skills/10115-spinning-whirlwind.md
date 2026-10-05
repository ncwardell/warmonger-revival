---
title: "Spinning Whirlwind"
type: "skill"
id: 10115
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10115", "client: StringAll_Eng SkillComment_10115 (tooltip value tags)"]
name_key: "Skill_10115"
desc_key: "SkillComment_10115"
kind: 1
kind_name: "active"
target: {"type": 3, "type_name": "self", "relation": ["enemy"], "unit_classes": ["monster", "player"], "max_targets": 10}
range: 4
area: {"shape": 1, "shape_name": "circle", "radius": 4.0, "width_or_angle": 4.0}
cost: {"type": 5, "type_name": "MP", "amount": 340}
cooldown: {"ms": 60000, "group": 0}
effect_kind: 1
effects:
  - {"slot": 1, "type": 330, "value": 100, "rate": 100}
  - {"slot": 2, "type": 101, "value": 95, "rate": 0}
damage_or_effect: {"kind": "damage (physical?)", "base": 100, "attack_pct": 95}
tooltip_formula:
  - {"tag": "EF_STATIC", "value": 100}
  - {"tag": "EF_R_DAM", "value": 95}
visual: 256
icon: {"file": "Skill_Miriam_01.png", "index": 15}
used_by:
  - {"weapon_base": 126, "slot": 4, "items": [16004]}
---
<!-- generated:start -->
<!-- generated-keys: title=e25c22 type=86a754 id=500681 sources=c8be1a name_key=52e1b9 desc_key=2999a0 kind=356a19 kind_name=9bc378 target=9dc90e range=1b6453 area=6d01a6 cost=9e049c cooldown=7d0c8c effect_kind=356a19 effects=8945ee damage_or_effect=5f4268 tooltip_formula=64d6b8 visual=dd7c1a icon=1b8eb2 used_by=faa9d2 -->
|  |  |
|---|---|
|  | ![Spinning Whirlwind](../assets/skills/10115.png) |
| **Skill id** | `10115` |
| **Kind** | active (1) |
| **Target** | self; enemy; units: monster, player; up to 10 |
| **Range** | 4 (world units) |
| **Area** | circle, radius 4, width/angle 4 |
| **Cost** | 340 MP |
| **Cooldown** | 60 s |
| **Effect kind** | damage (physical?) (1) |
| **Visual** | skillVisual 256 `PCM_Bow_04_R 회전회오리` |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 15 |

### Tooltip

> [Active] Deals `{EF_STATIC 100}``{EF_R_DAM 95}` Damage to all enemies around you.

Tooltip formula: **100 + 95% Attack** (the client fills these in from the caster's stats).

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 330 | base amount (tooltip `EF_STATIC`) | 100 | 100 |
| 2 | 101 | % of Attack (tooltip `EF_R_DAM`) | 95 | 0 |

**Reading:** amount **100 + 95% Attack**; damage (physical?).

### Used by

- Weapon skill **R** of WeaponBase 126: [[wiki/items/16004-magical-frost-bow|Magical Frost Bow]]

### Mentioned in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 1. Character creation (line 37): Punisher · 15007 Magical judge Dagger (Dagger) · 15004 Magical Frost Bow (Bow) · 29: Shadow Hurl, Shadow Walk, Poisonous Swamp, The Dark Art · 26: Sharp Edge...
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
