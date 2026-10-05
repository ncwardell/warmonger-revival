---
title: "Chepa Archer Officer"
type: "monster"
id: 711
status: "partial"
missing: ["attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops"]
sources: ["client: UnitDB.cdb id 711", "client: Quest.cdb kill objectives (quests 7, 757, 762, 1023)", "design: 400 HP, level 5 and exact spawn chosen for the quest-test server; see [[testing]]", "video: [[gameplay/video-tutorial-walkthrough]] step 18, north-west Training Ground clearing; exact point checked on owned-client navmesh"]
name_key: "UnitName_711"
category: 1
class_mask: 1
kill_group: 10016
model: 31
model_name: "MOB_Chepa02_0_1_0_00_00"
model_path: "character/npc/monster/mob_chepa/mob_chepa02.mo"
scale: 2
radius: 1
projectile: 662
sounds: [4070113, 4070113, 4070014, 4070014, 4070014, 4070016]
quest_targets:
  - {"quest": 7, "need": 1}
  - {"quest": 757, "need": 1, "group": 10016}
  - {"quest": 762, "need": 1, "group": 10016}
  - {"quest": 1023, "need": 1, "group": 10016}
quest_drops:
  - {"quest": 762, "item": 2588, "rate": 50, "need": 1}
spawn_fields: [89, 93, 97, 123]
hp: 400
level: 5
spawns:
  - {"field": 89, "x": 354.0, "z": 3750.0, "count": 1}
server_policy_source: "design: prototype HP, level and exact spawn; north-west Training Ground is supported by video-tutorial-walkthrough step 18; point checked on the owned-client navmesh"
---
<!-- generated:start -->
<!-- generated-keys: title=8184f6 type=9bbc46 id=7919ae sources=fe12e5 name_key=2e4981 category=356a19 class_mask=356a19 kill_group=d5483a model=632667 model_name=aae49c model_path=baa448 scale=da4b92 radius=356a19 projectile=091d03 sounds=8b163d quest_targets=ea3b97 quest_drops=e2f35d spawn_fields=31c28e -->
|  |  |
|---|---|
| **Unit id** | `711` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10016` with [[wiki/monsters/675-slayer-komodo\|Slayer Komodo]], [[wiki/monsters/710-chepa-warrior-officer\|Chepa Warrior Officer]] |
| **Model** | ObjectList `31` MOB_Chepa02_0_1_0_00_00 (`character/npc/monster/mob_chepa/mob_chepa02.mo`) |
| **Scale** | 2 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 662 (archers carry one; meaning *inferred*) |

*No image: the client has no 2-D monster art (only the 3-D model).*

### Server stats

None of these is in the client; they were server data. Fill them in the front matter with a source (`drops: [{"item": id, "rate": %, "count": [min, max]}]`, `spawns: [{"field": id, "x": .., "z": .., "count": n, "respawn_s": s}]`).

| field | value |
|---|---|
| hp | 400 |
| level | 5 |
| attack | **missing** |
| armor | **missing** |
| magic_resist | **missing** |
| move_speed | **missing** |
| attack_speed | **missing** |
| attack_range | **missing** |
| kill_exp | **missing** |
| kill_gold | **missing** |
| drops | **missing** |
| spawns | 1 entries (below) |

### Spawns

| field | x | z | count | respawn s |
|---|---|---|---|---|
| [[wiki/fields/89-training-ground\|Training Ground]] | 354.0 | 3750.0 | 1 |  |

### Quests

- [[wiki/quests/7-the-1st-challenge-chepas-ahead|The 1st Challenge: Chepas ahead]]: kill 1 in [[wiki/fields/89-training-ground|Training Ground]], [[wiki/fields/93-training-ground|Training Ground]], [[wiki/fields/97-training-ground|Training Ground]]
- [[wiki/quests/757-group-border-area-hard-mode|Group - Border Area Hard Mode]]: kill 1 in [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] — via kill group `10016` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/762-killed-boss-of-border-area-no-2|killed boss of Border area No.2]]: collect 1 × [[wiki/items/2588-the-slayer-komodo-s-pipe|The Slayer Komodo's Pipe]] (drops at 50% while the quest is active) in [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] — via kill group `10016` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/1023-swamps-of-the-snake-warrior-boss-hunting|Swamps of the Snake Warrior : Boss Hunting]]: kill 1 in [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] — via kill group `10016` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/fields/89-training-ground|Training Ground]] — quest map of [[wiki/quests/7-the-1st-challenge-chepas-ahead|The 1st Challenge: Chepas ahead]]
- [[wiki/fields/93-training-ground|Training Ground]] — quest map of [[wiki/quests/7-the-1st-challenge-chepas-ahead|The 1st Challenge: Chepas ahead]]
- [[wiki/fields/97-training-ground|Training Ground]] — quest map of [[wiki/quests/7-the-1st-challenge-chepas-ahead|The 1st Challenge: Chepas ahead]]
- [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] — quest map of [[wiki/quests/757-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/762-killed-boss-of-border-area-no-2|killed boss of Border area No.2]], [[wiki/quests/1023-swamps-of-the-snake-warrior-boss-hunting|Swamps of the Snake Warrior : Boss Hunting]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070113 | `Unit/UE4070113.wav` |
| 2 | 0 | 4070113 | `Unit/UE4070113.wav` |
| 3 | 0 | 4070014 | `Unit/UE4070014.wav` |
| 4 | 0 | 4070014 | `Unit/UE4070014.wav` |
| 5 | 0 | 4070014 | `Unit/UE4070014.wav` |
| 6 | 0 | 4070016 | `Unit/UE4070016.wav` |

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § Training Camp (field 92) and back at [12:35](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=755s), [13:10](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=790s), [13:45](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=825s), [14:55](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=895s): 15. 12:35 Back at Shaia (Training Ground): quest 6 completes. Quest 7 (same title, offer dialogue 685: the Chepa leaders are in the north) asks the player to k…
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Steps at [21:50](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1310s), [22:15](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1335s): 18. Chepa Warrior Officer (710) and Chepa Archer Officer (711) in the north-west clearing of the Training Ground, among normal Chepas 21:50–22:15. Each is a si…

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 4.5 |
| f32@10c | 0.5 |
<!-- generated:end -->

## Notes

The Python quest-test server loads `hp`, `level`, and `spawns` from this page:
400 HP, level 5, one officer at (354, 3750) in Training Ground (89).
These are test values, not recovered original server values. The coordinate is
walkable with 8.49 units of mesh-edge clearance. Combat and respawn timing still
use the shared prototype rules; see [[testing]].
The generated client-data section above has not been rebuilt with these manual
runtime fields; the front matter and this note contain the current test values.

## Behaviour

- Stands among normal Chepa Warriors and Archers in the north-west clearing of the Training Ground; each is a single kill for quest 7 (video, [[gameplay/video-tutorial-walkthrough]] step 18 at [21:50](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1310s)). Shaia's dialogue says the Chepa leaders are "in the north"; in the Erion copy both died in the round stone arena in the north of the Training Ground (video, [[gameplay/video-character-creation-and-tutorial]] §3 step 15 at [13:10](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=790s)). The charmanmugen video calls the place the Training Ground's spiral circle (video, [[gameplay/video-early-quests]] §2 item 7).

## Sources

- [[gameplay/video-tutorial-walkthrough]] step 18 and § Monsters and damage; [[gameplay/video-character-creation-and-tutorial]] §3; [[gameplay/video-early-quests]] §2

## Open questions

- No source shows this officer's HP, level or damage: the videos show only bars ([[gameplay/video-tutorial-walkthrough]] § Monsters and damage). The 400 HP / level 5 in the front matter remain test values.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
