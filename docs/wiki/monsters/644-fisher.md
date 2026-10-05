---
title: "Fisher"
type: "monster"
id: 644
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 644", "client: Quest.cdb kill objectives (quests 732, 782, 1016)"]
name_key: "UnitName_644"
category: 1
class_mask: 1
model: 55
model_name: "MOB_Fisher_01"
model_path: "character/npc/monster/mob_fisher/mob_fisher.mo"
scale: 1.3
radius: 1
sounds: [4070032, 4070032, 4070031, 4070031, 4070031, 4070016]
quest_targets:
  - {"quest": 732, "need": 20}
  - {"quest": 782, "need": 20}
  - {"quest": 1016, "need": 20}
quest_drops:
  - {"quest": 732, "item": 2577, "rate": 100, "need": 20}
  - {"quest": 1016, "item": 2677, "rate": 100, "need": 20}
spawn_fields: [122]
---
<!-- generated:start -->
<!-- generated-keys: title=3c5b25 type=9bbc46 id=4c8596 sources=93d532 name_key=8acc22 category=356a19 class_mask=356a19 model=8effee model_name=c911e6 model_path=0cce97 scale=2afe7d radius=356a19 sounds=e76ac0 quest_targets=668dba quest_drops=6c3dae spawn_fields=d4ee27 -->
|  |  |
|---|---|
| **Unit id** | `644` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `55` MOB_Fisher_01 (`character/npc/monster/mob_fisher/mob_fisher.mo`) |
| **Scale** | 1.3 (second scale / radius 1) |

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

### Quests

- [[wiki/quests/732-fisher-s-scales|Fisher's scales]]: collect 20 × [[wiki/items/2577-fisher-s-scales|Fisher's Scales]] (drops at 100% while the quest is active) in [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]]
- [[wiki/quests/782-tsunami-lake|Tsunami Lake]]: kill 20 in [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]]
- [[wiki/quests/1016-tsunami-lake-hunting|Tsunami Lake : Hunting]]: collect 20 × [[wiki/items/2677-fisher-s-scales|Fisher's Scales]] (drops at 100% while the quest is active) in [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]]

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] — quest map of [[wiki/quests/732-fisher-s-scales|Fisher's scales]], [[wiki/quests/782-tsunami-lake|Tsunami Lake]], [[wiki/quests/1016-tsunami-lake-hunting|Tsunami Lake : Hunting]]

### Other units with this name

[[wiki/monsters/556-fisher|Fisher (556)]], [[wiki/monsters/557-fisher|Fisher (557)]], [[wiki/monsters/560-fisher|Fisher (560)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070032 | `Unit/UE4070032.wav` |
| 2 | 0 | 4070032 | `Unit/UE4070032.wav` |
| 3 | 0 | 4070031 | `Unit/UE4070031.wav` |
| 4 | 0 | 4070031 | `Unit/UE4070031.wav` |
| 5 | 0 | 4070031 | `Unit/UE4070031.wav` |
| 6 | 0 | 4070016 | `Unit/UE4070016.wav` |

### Seen in

- [[gameplay/patch-history|Patch notes and other sources]] § Items *(name match)*: Boss sets (Death Head, Skull, Fisher, Komodo, Spector, Garon, Fame Knight, Fame Warrior) with 3 bonus steps (WM 0809); essences for them drop from fort guardia…
- [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]] § 6. Boss and fame set bonuses *(name match)*: Fisher (3, 3021–) · AP 30 · AP 40, MR Pen 20 · AP 60, MR Pen 30

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 2.7 |
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
