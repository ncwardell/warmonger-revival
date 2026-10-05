---
title: "Skeleton Warrior Officer"
type: "monster"
id: 704
status: "partial"
missing: ["level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 704", "client: Quest.cdb kill objectives (quests 10, 107)", "video: [[gameplay/video-early-quests|Video notes: the first 20 levels]] §5, target frame at [35:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=2120s): HP 2000, regen +0/tick (2% of max) (Skeleton Warrior Officer, quest 10's target 704)"]
name_key: "UnitName_704"
category: 1
class_mask: 1
model: 42
model_name: "MOB_Skeleton_Elilte_01_02"
model_path: "character/npc/monster/mob_seleton_elite_01/mob_seleton_elite_01_02.mo"
scale: 1.5
radius: 1
sounds: [4070000, 4070000, 3060040, 3060040, 3060040, 4070003]
quest_targets:
  - {"quest": 10, "need": 1}
  - {"quest": 107, "need": 1}
quest_drops:
  - {"quest": 10, "item": 2565, "rate": 100, "need": 1}
spawn_fields: [99, 100, 101]
hp: 2000
hp_regen: 0
---
<!-- generated:start -->
<!-- generated-keys: title=d0e2f3 type=9bbc46 id=a093a3 sources=c0efa5 name_key=6fcb77 category=356a19 class_mask=356a19 model=92cfce model_name=2038a8 model_path=8e1010 scale=aa8f28 radius=356a19 sounds=6dfede quest_targets=99f878 quest_drops=e5aea6 spawn_fields=0f349c hp=a4ac91 hp_regen=b6589f -->
|  |  |
|---|---|
| **Unit id** | `704` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `42` MOB_Skeleton_Elilte_01_02 (`character/npc/monster/mob_seleton_elite_01/mob_seleton_elite_01_02.mo`) |
| **Scale** | 1.5 (second scale / radius 1) |

*No image: the client has no 2-D monster art (only the 3-D model).*

### Server stats

None of these is in the client; they were server data. Fill them in the front matter with a source (`drops: [{"item": id, "rate": %, "count": [min, max]}]`, `spawns: [{"field": id, "x": .., "z": .., "count": n, "respawn_s": s}]`).

| field | value |
|---|---|
| hp | 2,000 |
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
| hp_regen | 0 |

### Quests

- [[wiki/quests/10-find-the-secret-document|Find the Secret Document]]: collect 1 × [[wiki/items/2565-secret-document|Secret document]] (drops at 100% while the quest is active) in [[wiki/fields/99-corpse-incineration|Corpse incineration]], [[wiki/fields/100-corpse-incineration|Corpse incineration]], [[wiki/fields/101-corpse-incineration|Corpse incineration]]
- [[wiki/quests/107-hunting-skeletons|Hunting Skeletons]]: kill 1 in [[wiki/fields/99-corpse-incineration|Corpse incineration]], [[wiki/fields/100-corpse-incineration|Corpse incineration]], [[wiki/fields/101-corpse-incineration|Corpse incineration]]

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/fields/99-corpse-incineration|Corpse incineration]] — quest map of [[wiki/quests/10-find-the-secret-document|Find the Secret Document]], [[wiki/quests/107-hunting-skeletons|Hunting Skeletons]]
- [[wiki/fields/100-corpse-incineration|Corpse incineration]] — quest map of [[wiki/quests/10-find-the-secret-document|Find the Secret Document]], [[wiki/quests/107-hunting-skeletons|Hunting Skeletons]]
- [[wiki/fields/101-corpse-incineration|Corpse incineration]] — quest map of [[wiki/quests/10-find-the-secret-document|Find the Secret Document]], [[wiki/quests/107-hunting-skeletons|Hunting Skeletons]]

### Other units with this name

[[wiki/monsters/686-skeleton-warrior-officer|Skeleton Warrior Officer (686)]], [[wiki/monsters/851-skeleton-warrior-officer|Skeleton Warrior Officer (851)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 2 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 3 | 0 | 3060040 | `effect/ES3060040.wav` |
| 4 | 0 | 3060040 | `effect/ES3060040.wav` |
| 5 | 0 | 3060040 | `effect/ES3060040.wav` |
| 6 | 0 | 4070003 | `Unit/UE4070003.wav` |

### Seen in

- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § Training Camp (field 92) and back at [18:10](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1090s), [19:20](https://www.youtube.com/watch?v=-DMnhYzYiC0&t=1160s): 20. 18:10 Scout found → quest 9 complete. The Scout (dialogue 641) starts quest 10 "Find the Secret Document": kill Skeleton Warrior Officer 704 for Secret doc…
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § Training Ground and Camp (levels 1–11) at [26:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=1580s), [36:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=2184s): 11. Find the Secret Document (10, the Scout, 26:20): kill the Skeleton Warrior Officer (704) for the Secret document (2565, 100%) and give it to Frei. Done at…
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Steps at [28:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1680s), [28:40](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1720s): 24. Skeleton Warrior Officer (704) and Skeleton Archer Officer (705) in the south of field 99, guarded by elites 28:00–28:40. An officer's speech bubble shouts…
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Monsters and damage: Skeleton Warrior Officer / Archer Officer · 704 / 705 · Corpse incineration, south · Q10 / Q107
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § 5. Monsters seen at [35:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=2120s) *(name match)*: Skeleton Warrior Officer (quest boss) · 2000 · +0 · 35:20

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 5.3 |
| i32@104 | 6 |
| f32@10c | 0.5 |
<!-- generated:end -->

## Notes

- Stands in the south of [[wiki/fields/99-corpse-incineration|Corpse incineration (99)]], guarded by elite skeletons; target of quest 10 (Secret document 2565, 100%) and quest 107 (video + client, [[gameplay/video-tutorial-walkthrough]] step 24 at [28:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=1680s); [[gameplay/video-character-creation-and-tutorial]] step 20).
- An officer's speech bubble shouts "Kill them!!" (video, [[gameplay/video-tutorial-walkthrough]] step 24).
- The target frame read HP 2000 with regeneration +0 at [35:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=2120s), unlike ordinary monsters, which regenerate 2% of max (video, [[gameplay/video-early-quests]] §5); the HP is in the front matter.

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- [[gameplay/video-tutorial-walkthrough]] step 24; [[gameplay/video-early-quests]] §2, §5; [[gameplay/video-character-creation-and-tutorial]] step 20

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
