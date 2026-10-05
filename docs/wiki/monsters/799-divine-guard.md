---
title: "Divine Guard"
type: "monster"
id: 799
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 799"]
name_key: "UnitName_799"
category: 3
class_mask: 1
model: 345
model_name: "NPC_Sdrone_0_1_0_00_00"
model_path: "character/npc/neighbor/npc_minion/npc_minion_siege_02.mo"
scale: 1.6
radius: 1
sounds: [4070091, 4070091, 4070016]
---
<!-- generated:start -->
<!-- generated-keys: title=331f33 type=9bbc46 id=01c0c9 sources=c7f76b name_key=7e4e6f category=77de68 class_mask=356a19 model=35139e model_name=d31111 model_path=2f8ea0 scale=469369 radius=356a19 sounds=8c78f5 -->
|  |  |
|---|---|
| **Unit id** | `799` |
| **Category** | elite / named variant (inferred) (`category@8a` = 3) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `345` NPC_Sdrone_0_1_0_00_00 (`character/npc/neighbor/npc_minion/npc_minion_siege_02.mo`) |
| **Scale** | 1.6 (second scale / radius 1) |

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

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070091 | `Unit/UE4070091.wav` |
| 2 | 0 | 4070091 | `Unit/UE4070091.wav` |
| 6 | 0 | 4070016 | `Unit/UE4070016.wav` |

### Seen in

- [[gameplay/server-rules|Server rules checklist]] § Added from the Warmonger forum and videos (round 2) *(name match)*: [ ] Siege order: Entry Core, then ring cores, then Invasion Core; Heart of Magic down = no Divine Guard and no guardian regen; air defence (1036) down opens th…
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § 3. Entry flow (land war → siege) *(name match)*: 5. Inside: capture Entry, then the ring cores, then Invasion. Destroy the Heart of Magic: "Divine Guard will not be summoned, The guardian does not recover." D…
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § 4. Timestamped log *(name match)*: P4 2:04 · 37:53 · "The Heart of Magic has destroyed. Divine Guard will not be summoned, The guardian does not recover."

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 5 |
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
