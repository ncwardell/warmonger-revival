---
title: "Deception"
type: "skill"
id: 5463
status: "complete"
missing: []
sources: ["client: Skill_Base.cdb id 5463", "notes: [[gameplay/classes-and-legions]] §5 Weapons, WM 0420 (W cooldown 20 → 25 s; matches client)"]
name_key: "Skill_5463"
desc_key: "SkillComment_5463"
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
  - {"slot": 2, "type": 301, "value": 10424, "rate": 100}
damage_or_effect: {"kind": "damage (physical?)", "buffs": [{"buff": 10424, "rate": 100}]}
icon: {"file": "Skill_Miriam_01.png", "index": 30}
used_by:
  - {"weapon_base": 30, "slot": 2, "items": [15008]}
---
<!-- generated:start -->
<!-- generated-keys: title=c9399b type=86a754 id=ce665c sources=e5d24e name_key=dc782f desc_key=9cf1db kind=356a19 kind_name=9bc378 target=c9e051 range=b1d578 area=3b02d8 cost=911ade cooldown=fec9d6 movement=953fcf effect_kind=356a19 effects=75fe86 damage_or_effect=009308 icon=b746da used_by=eae9cf -->
|  |  |
|---|---|
|  | ![Deception](wiki/assets/skills/5463.png) |
| **Skill id** | `5463` |
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
| 2 | 301 | applies buff (variant 301) | [[wiki/buffs/10424-deceive-hiding-3-secs\|Deceive : Hiding (3 secs)]] | 100 |

**Reading:** damage (physical?); applies [[wiki/buffs/10424-deceive-hiding-3-secs|Deceive : Hiding (3 secs)]] (100%).

### Used by

- Weapon skill **W** of WeaponBase 30: [[wiki/items/15008-magical-hiding-dagger|Magical hiding Dagger]]

### Mentioned in

- [[gameplay/classes-and-legions|Classes, nations and legions]] § Weapons (line 97): 0420 · Magical Hiding Dagger (15008) · Q cooldown 15 → 19 s, W 20 → 25 s (client: Backstab 20 s, Deception 25 s)
<!-- generated:end -->

## Notes

- Patch history: [WM 0420](https://steamcommunity.com/games/718790/announcements/detail/2758894130315567397) raised Magical Hiding Dagger's W cooldown 20 → 25 s; the client has Deception at 25 s. ([[gameplay/classes-and-legions]] §5 Weapons). *notes*

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- Gameplay pages this page draws on: [[gameplay/classes-and-legions]] §5 Weapons.

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
