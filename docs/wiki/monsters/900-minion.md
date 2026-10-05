---
title: "Minion"
type: "monster"
id: 900
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 900"]
name_key: "UnitName_900"
category: 1
class_mask: 1
kill_group: 10020
model: 339
model_name: "NPC_Minion_01_0_1_0_01_01"
model_path: "character/npc/neighbor/npc_minion/npc_minion_01.mo"
scale: 1
radius: 1
sounds: [4070091, 4070091, 4070091, 4070016]
---
<!-- generated:start -->
<!-- generated-keys: title=72ff9f type=9bbc46 id=28cc22 sources=17a786 name_key=fd064c category=356a19 class_mask=356a19 kill_group=122673 model=6c4110 model_name=91158c model_path=16beb0 scale=356a19 radius=356a19 sounds=d14674 -->
|  |  |
|---|---|
| **Unit id** | `900` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10020` with [[wiki/monsters/901-minion\|Minion]], [[wiki/monsters/902-minion\|Minion]], [[wiki/monsters/903-minion\|Minion]] |
| **Model** | ObjectList `339` NPC_Minion_01_0_1_0_01_01 (`character/npc/neighbor/npc_minion/npc_minion_01.mo`) |
| **Scale** | 1 (second scale / radius 1) |

*No image: the client has no 2-D monster art (only the 3-D model).*

### Server stats

None of these is in the client; they were server data. Fill them in the front matter with a source (`drops: [{"item": id, "rate": %, "count": [min, max]}]`, `spawns: [{"field": id, "x": .., "z": .., "count": n, "respawn_s": s}]`).

| field | value |
|---|---|
| hp | **missing** |
| level | **missing** |
| attack | **missing** |
| armor | **missing** |
| magic_resist | **missing** |
| move_speed | **missing** |
| attack_speed | **missing** |
| attack_range | **missing** |
| kill_exp | **missing** |
| kill_gold | **missing** |
| drops | **missing** |
| spawns | **missing** |

### Other units with this name

[[wiki/monsters/901-minion|Minion (901)]], [[wiki/monsters/902-minion|Minion (902)]], [[wiki/monsters/903-minion|Minion (903)]], [[wiki/monsters/904-minion|Minion (904)]], [[wiki/monsters/905-minion|Minion (905)]], [[wiki/monsters/906-minion|Minion (906)]], [[wiki/monsters/907-minion|Minion (907)]], [[wiki/monsters/908-minion|Minion (908)]], [[wiki/monsters/909-minion|Minion (909)]], [[wiki/monsters/910-minion|Minion (910)]], [[wiki/monsters/911-minion|Minion (911)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 3 | 1069 | 4070091 | `Unit/UE4070091.wav` |
| 4 | 1069 | 4070091 | `Unit/UE4070091.wav` |
| 5 | 0 | 4070091 | `Unit/UE4070091.wav` |
| 6 | 0 | 4070016 | `Unit/UE4070016.wav` |

### Seen in

- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § TP skills *(name match)*: Siege Minion (4506) · Nexus · 1,000 · 100 s · 1000 / 60 · Summons a weak tanking minion; field war only

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 1.7 |
| u8@92 | 3 |
| list5@93 | 0,0,0,16,10 |
| list5@98 | 0,0,0,11,15 |
| f32@10c | 1 |
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
