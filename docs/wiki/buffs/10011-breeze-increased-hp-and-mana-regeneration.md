---
title: "Breeze: Increased HP and Mana Regeneration"
type: "buff"
id: 10011
status: "stub"
missing: ["effects"]
sources: ["client: Skill_Buff.cdb id 10011", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_10011"
duration: {"ticks": 10, "seconds": 2.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 6
effects: []
icon: {"file": "Skill_Einsel_01.png", "index": 1}
applied_by:
  - {"skill": 5008, "slot": 3, "type": 314, "rate": 100}
---
<!-- generated:start -->
<!-- generated-keys: title=4180d8 type=6143a1 id=31559f sources=e4e214 name_key=1027af duration=2a0b1e is_buff=b6589f stack_type=356a19 group=c1dfd9 effects=97d170 icon=86c28e applied_by=03308f -->
|  |  |
|---|---|
|  | ![Breeze: Increased HP and Mana Regeneration](../assets/buffs/10011.png) |
| **Buff id** | `10011` |
| **Duration** | 2 s (10 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 6 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Skill_Einsel_01.png` cell 1 |

### Tooltip

> Breeze: Increased HP and Mana Regeneration

### Effects

No effect codes in the client: what this buff does (a stun, a mark, a status) is server-side. Add `effects:` by hand when known.

### Applied by

- Skill [[wiki/skills/5008-squall|Squall]], effect slot 3 (type 314, rate 100%)
- Nation policy 12 `PolicyName_12` (Policy.cdb, server-only; buff_or_skill)
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
