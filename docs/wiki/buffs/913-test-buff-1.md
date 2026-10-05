---
title: "Test Buff 1"
type: "buff"
id: 913
status: "stub"
missing: ["effects"]
sources: ["client: Skill_Buff.cdb id 913"]
name_key: "SkillBuff_900"
duration: {"ticks": 2100000000, "permanent": true}
is_buff: 0
stack_type: 1
group: 11
effects: []
icon: {"file": "Policy.png", "index": 0}
applied_by: []
---
<!-- generated:start -->
<!-- generated-keys: title=b06753 type=6143a1 id=fa5b7e sources=25950a name_key=ca0081 duration=6c141f is_buff=b6589f stack_type=356a19 group=17ba07 effects=97d170 icon=f877b6 applied_by=97d170 -->
|  |  |
|---|---|
|  | ![Test Buff 1](wiki/assets/buffs/913.png) |
| **Buff id** | `913` |
| **Duration** | permanent |
| **Buff / debuff** | flag 0 (is_buff?, guessed column) |
| **Stack type** | 1 (guessed column) |
| **Group** | 11 (+0x44 category; buffs of one group replace each other?) |
| **Icon** | `ui/icons/Policy.png` cell 0 |

### Tooltip

> Test Buff 1

### Effects

No effect codes in the client: what this buff does (a stun, a mark, a status) is server-side. Add `effects:` by hand when known.

### Current server

- `contract/system.yaml` line 208: `client_effect: "Fills the GM tool's user info (name (uid), channel, level, nation, class, field, guild). Also refreshes the Chat/Snoop/Unbea`
- `contract/system.yaml` line 343: `data_table: "Skill_Buff.cdb 912/913"`
- `contract/system.yaml` line 344: `suggested_default: "On ToggleSnoop/ToggleNoDam, add or remove buff 912/913 on the GM with the normal buff-list update (0x41e); apply no-dama`
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
