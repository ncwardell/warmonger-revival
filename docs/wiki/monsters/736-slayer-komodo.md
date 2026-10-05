---
title: "Slayer Komodo"
type: "monster"
id: 736
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 736", "client: HeroData.cdb id 9 (hero transform of the same name)", "docs: [[gameplay/dungeon-drops]] (boss of field 123)", "docs: [[gameplay/maps-and-dungeons]] (boss of field 123)", "client: DungeonAdmission.cdb (rewards advertised by the dungeon, no rates)"]
name_key: "UnitName_736"
category: 6
class_mask: 1
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
spawn_fields: [123]
---
<!-- generated:start -->
<!-- generated-keys: title=3c5ce8 type=9bbc46 id=4b14fe sources=a56bb8 name_key=213062 category=c1dfd9 class_mask=356a19 model=35e995 model_name=18dd57 model_path=1d7960 scale=aa8f28 radius=356a19 sounds=9e090c hero=0ade7c boss_of=4feada dungeon_rewards=99d97e spawn_fields=4feada -->
|  |  |
|---|---|
|  | ![Slayer Komodo](wiki/assets/monsters/736.png) |
| **Unit id** | `736` |
| **Category** | boss (inferred: every dungeon boss and quest bosses such as Tow Chief) (`category@8a` = 6) |
| **Class mask** | 1 (monster) |
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

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]] — boss ([[gameplay/dungeon-drops]], [[gameplay/maps-and-dungeons]])

### Dungeon rewards (advertised)

What the dungeon's entry window shows (`DungeonAdmission`). It is a list of possible rewards of the whole dungeon, not this boss's drop table, and has no rates.

- [[wiki/dungeons/123-lv-4-swamps-of-snake-warrior|(Lv 4) Swamps of Snake Warrior]]: [[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]], [[wiki/items/602-blue-passion-piece-d|Blue Passion Piece (D)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/1932-essence-of-fire|Essence of Fire]], [[wiki/items/2704-horn-of-komodo|Horn of Komodo]], [[wiki/items/2754-the-slayer-komodo-s-sealed-weapon|The Slayer Komodo's Sealed Weapon]]

### Other units with this name

[[wiki/monsters/675-slayer-komodo|Slayer Komodo (675)]], [[wiki/monsters/1213-slayer-komodo|Slayer Komodo (1213)]]

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
