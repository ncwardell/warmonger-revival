---
title: "Slayer Komodo"
type: "monster"
id: 675
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 675", "client: HeroData.cdb id 9 (hero transform of the same name)", "docs: [[gameplay/dungeon-drops]] (boss of field 123)", "docs: [[gameplay/maps-and-dungeons]] (boss of field 123)", "client: DungeonAdmission.cdb (rewards advertised by the dungeon, no rates)", "client: Quest.cdb kill objectives (quests 757, 762, 1023)"]
name_key: "UnitName_675"
category: 6
class_mask: 1
kill_group: 10016
model: 73
model_name: "MOB_LizardmanLord_01"
model_path: "character/npc/monster/mob_lizardman/mob_lizardmanlord_01.mo"
scale: 1.5
radius: 1
sounds: [4070044, 4070044, 4070043, 4070043, 4070043, 4070045]
hero: 9
boss_of: [123]
dungeon_rewards:
  - {"field": 123, "items": [612, 602, 693, 1932, 2704, 2754]}
quest_targets:
  - {"quest": 757, "need": 1, "group": 10016}
  - {"quest": 762, "need": 1, "group": 10016}
  - {"quest": 1023, "need": 1, "group": 10016}
quest_drops:
  - {"quest": 762, "item": 2588, "rate": 50, "need": 1}
spawn_fields: [123]
---
<!-- generated:start -->
<!-- generated-keys: title=3c5ce8 type=9bbc46 id=fcd72f sources=ff21ae name_key=3ee2ec category=c1dfd9 class_mask=356a19 kill_group=d5483a model=35e995 model_name=18dd57 model_path=1d7960 scale=aa8f28 radius=356a19 sounds=9e090c hero=0ade7c boss_of=4feada dungeon_rewards=99d97e quest_targets=d6820c quest_drops=e2f35d spawn_fields=4feada -->
|  |  |
|---|---|
|  | ![Slayer Komodo](../assets/monsters/675.png) |
| **Unit id** | `675` |
| **Category** | boss (inferred: every dungeon boss and quest bosses such as Tow Chief) (`category@8a` = 6) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10016` with [[wiki/monsters/710-chepa-warrior-officer\|Chepa Warrior Officer]], [[wiki/monsters/711-chepa-archer-officer\|Chepa Archer Officer]] |
| **Model** | ObjectList `73` MOB_LizardmanLord_01 (`character/npc/monster/mob_lizardman/mob_lizardmanlord_01.mo`) |
| **Scale** | 1.5 (second scale / radius 1) |
| **Hero transform** | Slayer Komodo |
| **Boss of** | [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior\|(Lv 4) Swamps of Snake Warrior]] |

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

- [[wiki/quests/757-group-border-area-hard-mode|Group - Border Area Hard Mode]]: kill 1 in [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] — via kill group `10016` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/762-killed-boss-of-border-area-no-2|killed boss of Border area No.2]]: collect 1 × [[wiki/items/2588-the-slayer-komodo-s-pipe|The Slayer Komodo's Pipe]] (drops at 50% while the quest is active) in [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] — via kill group `10016` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/1023-swamps-of-the-snake-warrior-boss-hunting|Swamps of the Snake Warrior : Boss Hunting]]: kill 1 in [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] — via kill group `10016` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] — boss ([[gameplay/dungeon-drops]], [[gameplay/maps-and-dungeons]]); quest map of [[wiki/quests/757-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/762-killed-boss-of-border-area-no-2|killed boss of Border area No.2]], [[wiki/quests/1023-swamps-of-the-snake-warrior-boss-hunting|Swamps of the Snake Warrior : Boss Hunting]]

### Dungeon rewards (advertised)

What the dungeon's entry window shows (`DungeonAdmission`). It is a list of possible rewards of the whole dungeon, not this boss's drop table, and has no rates.

- [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]]: [[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]], [[wiki/items/602-blue-passion-piece-d|Blue Passion Piece (D)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/1932-essence-of-fire|Essence of Fire]], [[wiki/items/2704-horn-of-komodo|Horn of Komodo]], [[wiki/items/2754-the-slayer-komodo-s-sealed-weapon|The Slayer Komodo's Sealed Weapon]]

### Other units with this name

[[wiki/monsters/736-slayer-komodo|Slayer Komodo (736)]], [[wiki/monsters/1213-slayer-komodo|Slayer Komodo (1213)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070044 | `Unit/UE4070044.wav` |
| 2 | 0 | 4070044 | `Unit/UE4070044.wav` |
| 3 | 926 | 4070043 | `Unit/UE4070043.wav` |
| 4 | 926 | 4070043 | `Unit/UE4070043.wav` |
| 5 | 0 | 4070043 | `Unit/UE4070043.wav` |
| 6 | 0 | 4070045 | `Unit/UE4070045.wav` |

### Seen in

- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 9. Dungeons, bosses, farming: Client check: units 672 King Deathhead, 673 Dark Knight Skull, 674 Tempest Fisher, 675 Slayer Komodo, 676 Great Summoner Spectre, 677 War Chief Garon, 849 Akas…
- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]] § 1. Per dungeon level: 4 · Swamps of the Snake Warrior → 123 "[Lv 4] Swamps of Snake Warrior" · Slayer Komodo → 675; 736, 1213 · Onyx 816, Borage 826, Spartium 828 · 612, 602, 693, E…
- [[gameplay/maps-and-dungeons|Maps and dungeons]] § 2. Border-area (normal/hard) dungeons: 4 · Swamps of Snake Warrior · 123 · Slayer Komodo (675/736/1213) · T1 · Onyx ×4, Borage ×5, Spartium ×3
- [[gameplay/precept-shop|Precept shop and precept quests]] § 6. Other numbers in the screenshot: The tracker shows "Defensive aggression": kill Slayer Komodo ×1, then talk to Freya. Slayer Komodo = units 675/736/1213, and 675 is in kill group 10016 *image*…
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 9. Dungeons, bosses, farming *(name match)*: 4 · Swamps of the Snake Warrior · Slayer Komodo · Onyx, Borage, Spartium
- [[gameplay/lords-of-the-land|Lords of the Land buff and quest]] § 5. Other numbers on the screenshots *(name match)*: Freya · Gives "Defensive aggression" (kill Tempest Fisher 0/1 / Slayer Komodo 0/1) · *image* [img-buff], [img-quest]
- [[gameplay/sources|Sources and gaps]] § 3. Player screenshots (image sets that still load) *(name match)*: Slayer Komodo quest: imgur YKN002t · EN · Quest "Defensive aggression" from Freya, EXP reward, boss spot in Rotten Twig Wood on the minimap · medium · catalogu…
- [[gameplay/videos|Videos]] § Dungeons and farming *(name match)*: Jonathan Silverblood: Crush Online - How to farm material in dungeons (2016-11-24, 3:47) · high · Material gathering in a dungeon, gather node positions. Embed…

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
