---
title: "Tow Chief"
type: "monster"
id: 826
status: "stub"
missing: ["level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 826", "client: Quest.cdb kill objectives (quests 80, 81, 82)", "video: [[gameplay/video-early-quests|Video notes: the first 20 levels]] §5, target frame at [70:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=4200s): HP 5000, regen +100/tick (2% of max) (Tow Chief 826)"]
name_key: "UnitName_826"
category: 6
class_mask: 1
model: 241
model_name: "MOB_Orc_Lord_01_02"
model_path: "character/npc/monster/mob_orc/mob_orc_lord_01.mo"
scale: 1.3
radius: 1
sounds: [4070074, 4070074, 4070004, 4070004, 4070005, 4070069]
quest_targets:
  - {"quest": 80, "need": 1}
  - {"quest": 81, "need": 1}
  - {"quest": 82, "need": 1}
spawn_fields: [108, 109, 111]
hp: 5000
hp_regen: 100
---
<!-- generated:start -->
<!-- generated-keys: title=56325f type=9bbc46 id=cdd308 sources=f4c30a name_key=df306f category=c1dfd9 class_mask=356a19 model=9ffd1a model_name=de9127 model_path=d78802 scale=2afe7d radius=356a19 sounds=720726 quest_targets=0c9e78 spawn_fields=20d88d hp=f8237d hp_regen=310b86 -->
|  |  |
|---|---|
| **Unit id** | `826` |
| **Category** | boss (inferred: every dungeon boss and quest bosses such as Tow Chief) (`category@8a` = 6) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `241` MOB_Orc_Lord_01_02 (`character/npc/monster/mob_orc/mob_orc_lord_01.mo`) |
| **Scale** | 1.3 (second scale / radius 1) |

*No image: the client has no 2-D monster art (only the 3-D model).*

### Server stats

None of these is in the client; they were server data. Fill them in the front matter with a source (`drops: [{"item": id, "rate": %, "count": [min, max]}]`, `spawns: [{"field": id, "x": .., "z": .., "count": n, "respawn_s": s}]`).

| field | value |
|---|---|
| hp | 5,000 |
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
| hp_regen | 100 |

### Quests

- [[wiki/quests/80-support-the-abyss-expedition|Support the Abyss expedition]]: kill 1 in [[wiki/fields/108-the-land-of-greed|The land of Greed]], [[wiki/fields/109-the-land-of-greed|The land of Greed]], [[wiki/fields/111-the-land-of-greed|The land of Greed]]
- [[wiki/quests/81-support-the-abyss-expedition|Support the Abyss expedition]]: kill 1 in [[wiki/fields/108-the-land-of-greed|The land of Greed]], [[wiki/fields/109-the-land-of-greed|The land of Greed]], [[wiki/fields/111-the-land-of-greed|The land of Greed]]
- [[wiki/quests/82-support-the-abyss-expedition|Support the Abyss expedition]]: kill 1 in [[wiki/fields/108-the-land-of-greed|The land of Greed]], [[wiki/fields/109-the-land-of-greed|The land of Greed]], [[wiki/fields/111-the-land-of-greed|The land of Greed]]

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/fields/108-the-land-of-greed|The land of Greed]] — quest map of [[wiki/quests/80-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/81-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/82-support-the-abyss-expedition|Support the Abyss expedition]]
- [[wiki/fields/109-the-land-of-greed|The land of Greed]] — quest map of [[wiki/quests/80-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/81-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/82-support-the-abyss-expedition|Support the Abyss expedition]]
- [[wiki/fields/111-the-land-of-greed|The land of Greed]] — quest map of [[wiki/quests/80-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/81-support-the-abyss-expedition|Support the Abyss expedition]], [[wiki/quests/82-support-the-abyss-expedition|Support the Abyss expedition]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070074 | `Unit/UE4070074.wav` |
| 2 | 0 | 4070074 | `Unit/UE4070074.wav` |
| 3 | 926 | 4070004 | `Unit/UE4070004.wav` |
| 4 | 926 | 4070004 | `Unit/UE4070004.wav` |
| 5 | 0 | 4070005 | `Unit/UE4070005.wav` |
| 6 | 0 | 4070069 | `Unit/UE4070069.wav` |

### Seen in

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § 5. Monsters seen at [70:00](https://www.youtube.com/watch?v=s04CSN16w1s&t=4200s), [88:20](https://www.youtube.com/watch?v=s04CSN16w1s&t=5300s): Tow Chief (826) · 5000 · +100 · 70:00, 88:20
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 9. Dungeons, bosses, farming: Client check: units 672 King Deathhead, 673 Dark Knight Skull, 674 Tempest Fisher, 675 Slayer Komodo, 676 Great Summoner Spectre, 677 War Chief Garon, 849 Akas…
- [[gameplay/server-rules|Server rules checklist]] § Added from the Warmonger forum and videos (round 2): [ ] Quests 80–82 "Support the Abyss expedition": kill 10/10/1 (Tow Chief 826) in field 108 for 220,000 EXP and a class weapon. — client Quest.tsv — H
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § After the tutorial (Fortress, from 22:00): Next come side quests 749 "Kill monster of The land of Greed" (50 Tow, 50 Elite Tow, return to Athan), 752 "Join & Create Legion" (Kesley), 104 "Delivering Pun…
- [[gameplay/warmonger-forum|Warmonger forum (2018)]] § 3. Bosses, essences and the Tow quest: Same quest in WM · quest ids 80–82 "Support the Abyss expedition": kill 10 × unit 10001, 10 × unit 10002 and 1 × unit 826 Tow Chief in field 108 (The land of G…
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § Fortress (levels 12–20) at [41:25](https://www.youtube.com/watch?v=s04CSN16w1s&t=2490s), [52:15](https://www.youtube.com/watch?v=s04CSN16w1s&t=3137s) *(name match)*: 16. Support the Abyss expedition (17, Freya, 41:25): the Tow Chief is stirring up an uprising; meet the Scout Leader in the Abyss. Done in The land of Greed at…
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 9. Dungeons, bosses, farming *(name match)*: Tow Chief (Abyss) · drops reinforcement stones, spell-stone patterns and (rarely) Essence of Darkness; must be killed by a level 15–20/25 character · *player*…
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § 5. Monsters seen *(name match)*: Kill messages ("X was destroyed") in quest order: Slime → Chepa Warrior / Chepa Archer (Training Ground circle, many killed for exp) → Bee, Cobra → Chepa Warri…
- [[gameplay/warmonger-forum|Warmonger forum (2018)]] § 3. Bosses, essences and the Tow quest *(name match)*: Tow Chief (Abyss) loot · only three drops: reinforcement stones, spell-stone patterns, Essence of Darkness (very rare); must be killed by a level 15–20 (or 25)…

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 6.5 |
| f32@10c | 0.5 |
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
