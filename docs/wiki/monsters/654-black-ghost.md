---
title: "Black Ghost"
type: "monster"
id: 654
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 654", "client: Quest.cdb kill objectives (quests 33, 778, 1027)"]
name_key: "UnitName_654"
category: 1
class_mask: 1
kill_group: 10029
model: 274
model_name: "NPC_Evil001"
model_path: "character/npc/monster/NPC_Evil/NPC_Evil001.mo"
scale: 1.5
radius: 1
sounds: [4000004, 4000004, 4000004, 4000004, 4000004, 4000004]
quest_targets:
  - {"quest": 33, "need": 1, "group": 10029}
  - {"quest": 778, "need": 30, "group": 10029}
  - {"quest": 1027, "need": 30, "group": 10029}
quest_drops:
  - {"quest": 33, "item": 2582, "rate": 10, "need": 1}
spawn_fields: [124]
---
<!-- generated:start -->
<!-- generated-keys: title=d441b6 type=9bbc46 id=db00e4 sources=2f37f6 name_key=f1546a category=356a19 class_mask=356a19 kill_group=38d0a0 model=431bf3 model_name=07adc2 model_path=e26f4d scale=aa8f28 radius=356a19 sounds=2db6a5 quest_targets=e9e770 quest_drops=8250a3 spawn_fields=181a14 -->
|  |  |
|---|---|
| **Unit id** | `654` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10029` with [[wiki/monsters/655-red-ghost\|Red Ghost]] |
| **Model** | ObjectList `274` NPC_Evil001 (`character/npc/monster/NPC_Evil/NPC_Evil001.mo`) |
| **Scale** | 1.5 (second scale / radius 1) |

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

- [[wiki/quests/33-ghost-fortress|Ghost Fortress]]: collect 1 × [[wiki/items/2582-innocence-piece|Innocence Piece]] (drops at 10% while the quest is active) in [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] — via kill group `10029` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/778-ghost-soldier|Ghost soldier]]: kill 30 in [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] — via kill group `10029` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/1027-ghost-fortress-hunting|Ghost Fortress : Hunting]]: kill 30 in [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] — via kill group `10029` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] — quest map of [[wiki/quests/33-ghost-fortress|Ghost Fortress]], [[wiki/quests/778-ghost-soldier|Ghost soldier]], [[wiki/quests/1027-ghost-fortress-hunting|Ghost Fortress : Hunting]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4000004 | `voice/UV4000004.wav` |
| 2 | 0 | 4000004 | `voice/UV4000004.wav` |
| 3 | 0 | 4000004 | `voice/UV4000004.wav` |
| 4 | 0 | 4000004 | `voice/UV4000004.wav` |
| 5 | 0 | 4000004 | `voice/UV4000004.wav` |
| 6 | 0 | 4000004 | `voice/UV4000004.wav` |

### Seen in

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § 5. Monsters seen at [83:15](https://www.youtube.com/watch?v=s04CSN16w1s&t=4995s) *(name match)*: Fragile Elite Red / Black Ghost · 2000 · +40 · 83:15
- [[gameplay/precept-shop|Precept shop and precept quests]] § 3. Example rolled quest (screenshot) *(name match)*: 1 · Kill Ghost 0/10 · UnitDB kill group 10029 = Black Ghost 654, Red Ghost 655 (Ghost Fortress, field 124) *client*
- [[gameplay/video-dungeon-run|Video notes: Nas Village dungeon run (ZonderCoRe)]] § 5. Gathering in a dungeon (Crush Online, field 124) *(name match)*: Gather cast · About 3 s. The bar starts at about 87.5 s and "You acquired Moonstone" appears at 90.5 s. Being hit by a Black Ghost did not stop it · w &t=87s ·…
- [[gameplay/video-dungeon-run|Video notes: Nas Village dungeon run (ZonderCoRe)]] § 5. Gathering in a dungeon (Crush Online, field 124) *(name match)*: Monsters near the entrance · Red Ghost, Black Ghost · w &t=84s · video
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § 5. Monsters seen *(name match)*: Kill messages ("X was destroyed") in quest order: Slime → Chepa Warrior / Chepa Archer (Training Ground circle, many killed for exp) → Bee, Cobra → Chepa Warri…

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 4.3 |
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
