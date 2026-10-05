---
title: "Slime"
type: "monster"
id: 604
status: "partial"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 604", "client: Quest.cdb kill objectives (quests 2)"]
name_key: "UnitName_604"
category: 1
class_mask: 1
model: 12
model_name: "MOB_Slime_01_Green"
model_path: "character/npc/monster/mob_slime/mob_slime.mo"
scale: 1
radius: 1
sounds: [4070008, 4070008, 4070008, 4070009]
quest_targets:
  - {"quest": 2, "need": 3}
quest_drops:
  - {"quest": 2, "item": 2550, "rate": 100, "need": 3}
spawn_fields: [89, 93, 97]
---
<!-- generated:start -->
<!-- generated-keys: title=604324 type=9bbc46 id=f8d0f8 sources=e53793 name_key=5b2c27 category=356a19 class_mask=356a19 model=7b5200 model_name=b5444f model_path=0cd0f3 scale=356a19 radius=356a19 sounds=0bf31e quest_targets=c666e4 quest_drops=3a692d spawn_fields=6e2020 -->
|  |  |
|---|---|
| **Unit id** | `604` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `12` MOB_Slime_01_Green (`character/npc/monster/mob_slime/mob_slime.mo`) |
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

### Quests

- [[wiki/quests/2-the-slime-is-mine|The Slime is mine]]: collect 3 × [[wiki/items/2550-slime-mucus|Slime Mucus]] (drops at 100% while the quest is active) in [[wiki/fields/89-training-ground|Training Ground]], [[wiki/fields/93-training-ground|Training Ground]], [[wiki/fields/97-training-ground|Training Ground]]

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/fields/89-training-ground|Training Ground]] — quest map of [[wiki/quests/2-the-slime-is-mine|The Slime is mine]]
- [[wiki/fields/93-training-ground|Training Ground]] — quest map of [[wiki/quests/2-the-slime-is-mine|The Slime is mine]]
- [[wiki/fields/97-training-ground|Training Ground]] — quest map of [[wiki/quests/2-the-slime-is-mine|The Slime is mine]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 3 | 0 | 4070008 | `Unit/UE4070008.wav` |
| 4 | 0 | 4070008 | `Unit/UE4070008.wav` |
| 5 | 0 | 4070008 | `Unit/UE4070008.wav` |
| 6 | 0 | 4070009 | `Unit/UE4070009.wav` |

### Current server

What `server/` does now (our choices, not original data):

- `server/world.py` MONSTERS: 3 spawned near the tutorial centre, level 1, HP 80
- `server/loot.py` EXTRA_DROPS: [[wiki/items/839-wild-herb|Wild herb]] 10% × 1–1

### Seen in

- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § Training Ground and Camp (levels 1–11) at [6:45](https://www.youtube.com/watch?v=s04CSN16w1s&t=405s): 2. The Slime is mine (2). Shaia sends the player to collect 3 Slime mucus from Slimes (604, drop 2550 at 100%). Tracker: "Slime mucus obtained (0/3) → Bring th…
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Steps at [4:55](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=295s), [5:40](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=340s): 4. Slimes 4:55. Killing the first Slime (604) gives level 2 at once: 500 (Q1) + 200 (Q700) = 700 = Level_Table exp for level 1. Help quest 701 "Basic Combat Le…
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § Training Ground (field 93): Quest 2 "The Slime is mine" (631): kill Slime 604 for 3 Slime Mucus 2550 (100 % drop), bring them to Floyd.
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Monsters and damage: Slime · 604 · Training Ground, south · drops Slime Mucus (2550) for Q2
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § 6. Drops, shop, other numbers at [16:54](https://www.youtube.com/watch?v=s04CSN16w1s&t=1014s) *(name match)*: Wren, Training Camp (238) at 16:54: Potion of Health [D] 79, Potion of Mana [D] 79 ("regenerates mana for 16 seconds"), Scroll: Return 79, and Scroll of Transf…
- [[gameplay/video-tutorial-walkthrough|Video notes: tutorial walkthrough (Bravely Forward 2)]] § Steps at [4:00](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=240s) *(name match)*: 3. Talk to Shaia (201) 4:00. The QuestTalk 630 lines play: she asks why you are always late and sends you for slime mucus for Biologist Floyd. Q1 completes and…
- [[gameplay/consumables|Consumables and clickables]] § 1. Rules that apply to every clickable *(name match)*: 1150 · Transform · Golem, Demon, Slime, Jack
- [[gameplay/consumables|Consumables and clickables]] § 3. Potions and other clickables *(name match)*: 760 / 761 / 762 · Scroll of Transform: Golem / Demon / Slime · 1150 / 1152 / 910 · Turn into unit 613 / 741 / 627 · 5 min · 1,000 gold base (kind 19)
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 5. Other facts *(name match)*: Monsters by area: Training Ground: Slime 604, Bee 731, Cobra 732, Chepa Warrior 727, Chepa Archer 728, Chepa officers 710/711 (the officers fight inside a grou…
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation and tutorial (ZonderCoRe, June 2018)]] § 5. Other facts *(name match)*: System messages seen in chat: "Slime was destroyed.", "You acquired an &lt;item&gt; item.", "Levelup.&lt;n&gt;", "&lt;name&gt; entered the party.", "This item…
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § 5. Monsters seen *(name match)*: Kill messages ("X was destroyed") in quest order: Slime → Chepa Warrior / Chepa Archer (Training Ground circle, many killed for exp) → Bee, Cobra → Chepa Warri…

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 2.7 |
| f32@10c | 3 |
<!-- generated:end -->

## Notes

- Lives in the south of the [[wiki/fields/89-training-ground|Training Ground (89)]]; the first monster a new character fights (video, [[gameplay/video-tutorial-walkthrough]] § Monsters and damage; [[gameplay/video-early-quests]] §5).
- Drops Slime Mucus (2550) for quest 2, one per kill until 3/3 (video + client, [[gameplay/video-tutorial-walkthrough]] step 4 at [4:55](https://www.youtube.com/watch?v=CqCY2ULeVGw&t=295s); [[gameplay/video-character-creation-and-tutorial]] step 2).
- A level-2 Guardian's basic hits did 88 damage to it; no HP number is shown, only a bar (video, [[gameplay/video-tutorial-walkthrough]] § Monsters and damage).

## Behaviour

- Quest items drop at the `Quest.tsv` rate: every kill of a matching monster gave one while the quest was active (video, [[gameplay/video-early-quests]] §6).

## Sources

- [[gameplay/video-early-quests]] §4–6; [[gameplay/video-tutorial-walkthrough]] steps 4 and § Monsters and damage; [[gameplay/video-character-creation-and-tutorial]] steps 2–5

## Open questions

- Kill exp: [[gameplay/video-early-quests]] §4 says level 2 came from Slime kills before any quest was handed in, while [[gameplay/video-tutorial-walkthrough]] step 4 shows level 2 reached on the first Slime kill exactly from quest exp (500 + 200 = 700, the `Level_Table` value). Kill exp is still unknown.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
