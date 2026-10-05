---
title: "Superior Nas Warrior"
type: "monster"
id: 1219
status: "partial"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 1219"]
name_key: "UnitName_1219"
category: 1
class_mask: 1
model: 383
model_name: "MOB_Chepa01_0_1_0_02_02"
model_path: "character/npc/monster/mob_chepa/mob_chepa01.mo"
scale: 2
radius: 1
sounds: [4070000, 4070000, 5000006, 5000006, 5000006, 4070003]
---
<!-- generated:start -->
<!-- generated-keys: title=225b94 type=9bbc46 id=15d1ee sources=3b556c name_key=0f44a6 category=356a19 class_mask=356a19 model=8c4a0a model_name=76fb72 model_path=207e1f scale=da4b92 radius=356a19 sounds=dddd70 -->
|  |  |
|---|---|
| **Unit id** | `1219` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `383` MOB_Chepa01_0_1_0_02_02 (`character/npc/monster/mob_chepa/mob_chepa01.mo`) |
| **Scale** | 2 (second scale / radius 1) |

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
| 1 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 2 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 3 | 0 | 5000006 | `effect/EW5000006.wav` |
| 4 | 0 | 5000006 | `effect/EW5000006.wav` |
| 5 | 0 | 5000006 | `effect/EW5000006.wav` |
| 6 | 0 | 4070003 | `Unit/UE4070003.wav` |

### Seen in

- [[gameplay/video-dungeon-run|Video notes: Nas Village dungeon run (ZonderCoRe)]] § 2. Pack positions (field 133): Monster types: humanoid warriors with shields and bow archers (v &t=51s). The client has exactly these for Nas: 688 Nas Warrior, 689 Nas Archer, 690 Elite Nas…

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 2.7 |
| f32@10c | 0.5 |
<!-- generated:end -->

## Notes

- One of the client's six Nas units for the Nas Village Entrance event dungeon ([[wiki/dungeons/133-sinking-nest-crystal|Sinking Nest (Crystal), 133]]) (client, [[gameplay/video-dungeon-run]] §2).
- A June 2018 hard-mode run shows packs of about 5–7 warriors with shields and bow archers at six stops along the dungeon; positions are on the dungeon page (video, [[gameplay/video-dungeon-run]] §2).
- Party members hit them for about 2,180–2,400 and most died after a few hits; the HP cannot be read at 360p (video, [[gameplay/video-dungeon-run]] §2).

## Behaviour

- With 3 players a cleared pack was back after about 90–100 s (video, [[gameplay/video-dungeon-run]] §3).
- Loot per kill: one or two stacks of Faded Passion fragments/Piece/Pattern (1900–1902) and crystals (700–703) (video, [[gameplay/video-dungeon-run]] §4).

## Sources

- [[gameplay/video-dungeon-run]] §2–4

## Open questions

- Which of the six Nas ids spawn in the run is a *guess*, so no `spawns` are set.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
