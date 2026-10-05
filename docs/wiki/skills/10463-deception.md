---
title: "Deception"
type: "skill"
id: 10463
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 10463"]
name_key: "Skill_10463"
desc_key: "SkillComment_10463"
kind: 1
kind_name: "active"
target: {"type": 2, "type_name": "ground", "relation": ["ally", "enemy"], "unit_classes": ["monster", "player"], "max_targets": 1}
range: 10
area: {"shape": 1, "shape_name": "circle", "radius": 1.0, "width_or_angle": 0.0}
cost: {"type": 5, "type_name": "MP", "amount": 140}
cooldown: {"ms": 25000, "group": 0}
movement: "blink / teleport"
effect_kind: 1
effects:
  - {"slot": 1, "type": 328, "value": 410, "rate": 100}
  - {"slot": 2, "type": 301, "value": 30424, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 30424, "rate": 100}]}
icon: {"file": "Skill_Miriam_01.png", "index": 30}
used_by:
  - {"weapon_base": 130, "slot": 2, "items": [16008]}
---
<!-- generated:start -->
<!-- generated-keys: title=c9399b type=86a754 id=4eeb1c sources=81d2dd name_key=d8bb8a desc_key=27ce3a kind=356a19 kind_name=9bc378 target=c9e051 range=b1d578 area=3b02d8 cost=911ade cooldown=fec9d6 movement=953fcf effect_kind=356a19 effects=a1874f damage_or_effect=25d9fb icon=b746da used_by=b87885 -->
|  |  |
|---|---|
|  | ![Deception](wiki/assets/skills/10463.png) |
| **Skill id** | `10463` |
| **Kind** | active (1) |
| **Target** | ground; ally, enemy; units: monster, player; up to 1 |
| **Range** | 10 (world units) |
| **Area** | circle, radius 1, width/angle 0 |
| **Cost** | 140 MP |
| **Cooldown** | 25 s |
| **Movement** | blink / teleport |
| **Effect kind** | damage (physical?) (1) |
| **Icon** | `ui/icons/Skill_Miriam_01.png` cell 30 |

### Tooltip

> [Active] When a character moves instantaneously to a specific position, it will summon an ally to their original position and hide them for 2 seconds.

### Effect slots

Raw `Skill_Base` effect slots; the client never applies them, the server does. Meanings are *inferred* from the data (see the module notes in `wiki/gamewiki/skills.py`).

| slot | type | meaning | value | rate |
|---|---|---|---|---|
| 1 | 328 | summon? (unknown) | 410 | 100 |
| 2 | 301 | applies buff (variant 301) | [[wiki/buffs/30424-deceive-hiding-3-secs\|Deceive : Hiding (3 secs)]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/30424-deceive-hiding-3-secs|Deceive : Hiding (3 secs)]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 130: [[wiki/items/16008-magical-hiding-dagger|Magical hiding Dagger]]

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]] § Weapons (line 97): 0420 · Magical Hiding Dagger (15008) · Q cooldown 15 → 19 s, W 20 → 25 s (client: Backstab 20 s, Deception 25 s)
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
