---
title: "Chepa Warrior"
type: "monster"
id: 727
status: "partial"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 727", "client: Quest.cdb kill objectives (quests 100, 756, 762, 1018)"]
name_key: "UnitName_727"
category: 1
class_mask: 1
kill_group: 10015
model: 30
model_name: "MOB_Chepa01_0_1_0_00_00"
model_path: "character/npc/monster/mob_chepa/mob_chepa01.mo"
scale: 1.3
radius: 1
sounds: [4070000, 4070000, 4070013, 4070013, 4070013, 4070016]
quest_targets:
  - {"quest": 100, "need": 5}
  - {"quest": 756, "need": 1, "group": 10015}
  - {"quest": 762, "need": 1, "group": 10015}
  - {"quest": 1018, "need": 1, "group": 10015}
quest_drops:
  - {"quest": 100, "item": 2554, "rate": 100, "need": 5}
  - {"quest": 762, "item": 2587, "rate": 50, "need": 1}
spawn_fields: [89, 93, 97, 122]
---
<!-- generated:start -->
<!-- generated-keys: title=8fc8c1 type=9bbc46 id=90f98c sources=3af4f1 name_key=c500d6 category=356a19 class_mask=356a19 kill_group=848f94 model=22d200 model_name=67408a model_path=207e1f scale=2afe7d radius=356a19 sounds=14185a quest_targets=f9aa73 quest_drops=35665b spawn_fields=3b03b1 -->
|  |  |
|---|---|
| **Unit id** | `727` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10015` with [[wiki/monsters/674-tempest-fisher\|Tempest Fisher]], [[wiki/monsters/728-chepa-archer\|Chepa Archer]] |
| **Model** | ObjectList `30` MOB_Chepa01_0_1_0_00_00 (`character/npc/monster/mob_chepa/mob_chepa01.mo`) |
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

- [[wiki/quests/100-hunting-for-furs|Hunting for Furs]]: collect 5 × [[wiki/items/2554-whiter-chepa-fur|Whiter Chepa Fur]] (drops at 100% while the quest is active) in [[wiki/fields/89-training-ground|Training Ground]], [[wiki/fields/93-training-ground|Training Ground]], [[wiki/fields/97-training-ground|Training Ground]]
- [[wiki/quests/756-group-border-area-hard-mode|Group - Border Area Hard Mode]]: kill 1 in [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] — via kill group `10015` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/762-killed-boss-of-border-area-no-2|killed boss of Border area No.2]]: collect 1 × [[wiki/items/2587-the-tempest-fisher-s-pipe|The Tempest Fisher's Pipe]] (drops at 50% while the quest is active) in [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] — via kill group `10015` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/1018-tsunami-lake-boss-hunting|Tsunami Lake : Boss Hunting]]: kill 1 in [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] — via kill group `10015` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/fields/89-training-ground|Training Ground]] — quest map of [[wiki/quests/100-hunting-for-furs|Hunting for Furs]]
- [[wiki/fields/93-training-ground|Training Ground]] — quest map of [[wiki/quests/100-hunting-for-furs|Hunting for Furs]]
- [[wiki/fields/97-training-ground|Training Ground]] — quest map of [[wiki/quests/100-hunting-for-furs|Hunting for Furs]]
- [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] — quest map of [[wiki/quests/756-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/762-killed-boss-of-border-area-no-2|killed boss of Border area No.2]], [[wiki/quests/1018-tsunami-lake-boss-hunting|Tsunami Lake : Boss Hunting]]

### Other units with this name

[[wiki/monsters/544-chepa-warrior|Chepa Warrior (544)]], [[wiki/monsters/545-chepa-warrior|Chepa Warrior (545)]], [[wiki/monsters/668-chepa-warrior|Chepa Warrior (668)]], [[wiki/monsters/706-chepa-warrior|Chepa Warrior (706)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 2 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 3 | 0 | 4070013 | `Unit/UE4070013.wav` |
| 4 | 0 | 4070013 | `Unit/UE4070013.wav` |
| 5 | 0 | 4070013 | `Unit/UE4070013.wav` |
| 6 | 0 | 4070016 | `Unit/UE4070016.wav` |

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § Training Camp (field 92) and back at [8:50](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=530s): 13. 8:50 Lewellyn (Scroll Merchant, 315) offers side quest 100 "Hunting for Furs" (dialogue 644): 5 White Chepa Fur 2554 from Chepa Warrior 727 and 5 Black Che…
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § Training Ground and Camp (levels 1–11) at [17:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=1022s), [22:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=1322s): 8. Hunting for Furs (100, Lewellyn 315, Camp), accepted at 17:00: 5 Whiter Chepa Fur (Chepa Warrior 727) and 5 Black Chepa Fur (Chepa Archer 728). Turn in to L…
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Monsters and damage: Chepa Warrior / Chepa Archer · 727 / 728 · Training Ground, north clearings · furs 2554 / 2553 for Q100; they hit for 22
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 4. NPC positions (Erion copy) at [13:10](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=790s) *(name match)*: Chepa Warrior/Archer Officers 710/711 · — · 93 · north arena (not measured) · — · 13:10 · Dialogue 685 says "in the north"
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § Training Ground and Camp (levels 1–11) at [7:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=420s), [12:35](https://www.youtube.com/watch?v=s04CSN16w1s&t=757s) *(name match)*: 3. The task at hand (3, Floyd), accepted at 7:00: 5 Bee Needle from Bees (731) and 5 Cobra/Snake Leather from Cobras (732). Turn in to Floyd at 12:35. Reward:…
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

- Lives in the round clearings of the northern lobes of the [[wiki/fields/89-training-ground|Training Ground (89)]], around the Chepa officers (video, [[gameplay/video-tutorial-walkthrough]] step 13 at [16:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=960s); [[gameplay/video-early-quests]] §2 item 3).
- Drops Whiter Chepa Fur (2554) at 100% for quest 100 (video + client, [[gameplay/video-tutorial-walkthrough]] step 13; [[gameplay/video-character-creation-and-tutorial]] step 13).
- Chepas hit the player (a low-level Guardian) for 22; the player's basic hits did 98–101 damage to them (video, [[gameplay/video-tutorial-walkthrough]] § Monsters and damage).
- Players cleared the Chepa circle for exp on the way to quest 3 (video, [[gameplay/video-early-quests]] §2 item 3, §5).

## Behaviour

- Quest items drop at the `Quest.tsv` rate: every kill of a matching monster gave one while the quest was active (video, [[gameplay/video-early-quests]] §6).

## Sources

- [[gameplay/video-tutorial-walkthrough]] step 13 and § Monsters and damage; [[gameplay/video-early-quests]] §2, §5–6; [[gameplay/video-character-creation-and-tutorial]] step 13

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
