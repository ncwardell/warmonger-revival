---
title: "Test Buff 2"
type: "buff"
id: 902
status: "stub"
missing: ["effects"]
sources: ["client: Skill_Buff.cdb id 902", "gameplay: [[gameplay/consumables]] (Skill_Buff duration = 200 ms ticks)"]
name_key: "SkillBuff_901"
duration: {"ticks": 15, "seconds": 3.0, "permanent": false}
is_buff: 0
stack_type: 1
group: 2
effects: []
icon: {"file": "Policy.png", "index": 0}
applied_by:
  - {"item": 903}
---
<!-- generated:start -->
<!-- generated-keys: title=0e036f type=6143a1 id=0e2a8d sources=df3dff name_key=55d920 duration=0aac5a is_buff=b6589f stack_type=356a19 group=da4b92 effects=97d170 icon=f877b6 applied_by=1a734c -->
|  |  |
|---|---|
|  | ![Test Buff 2](../assets/buffs/902.png) |
| **Buff id** | `902` |
| **Duration** | 3 s (15 ticks of 200 ms; unit from [[gameplay/consumables]]) |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 2 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Policy.png` cell 0 |

### Tooltip

> Test Buff 2

### Effects

No effect codes in the client: what this buff does (a stun, a mark, a status) is server-side. Add `effects:` by hand when known.

### Applied by

- Using [[wiki/items/903-deadly-fire|Deadly Fire]] (Item_Base option 301)
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
