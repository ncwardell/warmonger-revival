---
title: "Chepa Archer"
type: "monster"
id: 669
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 669", "client: Quest.cdb kill objectives (quests 30, 736, 1001)"]
name_key: "UnitName_669"
category: 1
class_mask: 1
kill_group: 10025
model: 31
model_name: "MOB_Chepa02_0_1_0_00_00"
model_path: "character/npc/monster/mob_chepa/mob_chepa02.mo"
scale: 1.3
radius: 1
projectile: 662
sounds: [4070113, 4070113, 4070014, 4070014, 4070014, 4070016]
quest_targets:
  - {"quest": 30, "need": 10, "group": 10025}
  - {"quest": 736, "need": 5}
  - {"quest": 1001, "need": 5}
quest_drops:
  - {"quest": 736, "item": 2553, "rate": 70, "need": 5}
  - {"quest": 1001, "item": 2653, "rate": 70, "need": 5}
spawn_fields: [127]
---
<!-- generated:start -->
<!-- generated-keys: title=99fa35 type=9bbc46 id=9f3bdb sources=5ac3ab name_key=4684dc category=356a19 class_mask=356a19 kill_group=703386 model=632667 model_name=aae49c model_path=baa448 scale=2afe7d radius=356a19 projectile=091d03 sounds=8b163d quest_targets=75548d quest_drops=737a1b spawn_fields=cf6862 -->
|  |  |
|---|---|
| **Unit id** | `669` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10025` with [[wiki/monsters/668-chepa-warrior\|Chepa Warrior]] |
| **Model** | ObjectList `31` MOB_Chepa02_0_1_0_00_00 (`character/npc/monster/mob_chepa/mob_chepa02.mo`) |
| **Scale** | 1.3 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 662 (archers carry one; meaning *inferred*) |

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

- [[wiki/quests/30-chepa-village|Chepa Village]]: kill 10 in [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]] — via kill group `10025` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/736-hunting-for-furs|Hunting for Furs]]: collect 5 × [[wiki/items/2553-black-chepa-fur|Black Chepa Fur]] (drops at 70% while the quest is active) in [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]]
- [[wiki/quests/1001-chepa-village-hunting|Chepa Village : Hunting]]: collect 5 × [[wiki/items/2653-black-chepa-fur|Black Chepa Fur]] (drops at 70% while the quest is active) in [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]]

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]] — quest map of [[wiki/quests/30-chepa-village|Chepa Village]], [[wiki/quests/736-hunting-for-furs|Hunting for Furs]], [[wiki/quests/1001-chepa-village-hunting|Chepa Village : Hunting]]

### Other units with this name

[[wiki/monsters/546-chepa-archer|Chepa Archer (546)]], [[wiki/monsters/547-chepa-archer|Chepa Archer (547)]], [[wiki/monsters/707-chepa-archer|Chepa Archer (707)]], [[wiki/monsters/728-chepa-archer|Chepa Archer (728)]]

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

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § Training Camp (field 92) and back at [8:50](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=530s) *(name match)*: 13. 8:50 Lewellyn (Scroll Merchant, 315) offers side quest 100 "Hunting for Furs" (dialogue 644): 5 White Chepa Fur 2554 from Chepa Warrior 727 and 5 Black Che…
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 5. Other facts *(name match)*: Monsters by area: Training Ground: Slime 604, Bee 731, Cobra 732, Chepa Warrior 727, Chepa Archer 728, Chepa officers 710/711 (the officers fight inside a grou…
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § 5. Monsters seen *(name match)*: Kill messages ("X was destroyed") in quest order: Slime → Chepa Warrior / Chepa Archer (Training Ground circle, many killed for exp) → Bee, Cobra → Chepa Warri…

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
