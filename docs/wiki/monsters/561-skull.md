---
title: "Skull"
type: "monster"
id: 561
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 561"]
name_key: "UnitName_561"
category: 8
class_mask: 1
model: 35
model_name: "MOB_Seleton King_01"
model_path: "character/npc/monster/mob_seleton king/mob_seleton king_01.mo"
scale: 1.5
radius: 1
sounds: [4070017, 4070017, 4070018]
---
<!-- generated:start -->
<!-- generated-keys: title=2dbae4 type=9bbc46 id=77c818 sources=387790 name_key=c8f731 category=fe5dbb class_mask=356a19 model=972a67 model_name=0cf010 model_path=6a4c49 scale=aa8f28 radius=356a19 sounds=10cd19 -->
|  |  |
|---|---|
| **Unit id** | `561` |
| **Category** | field monster (inferred: ogres, trolls, bears, phytons) (`category@8a` = 8) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `35` MOB_Seleton King_01 (`character/npc/monster/mob_seleton king/mob_seleton king_01.mo`) |
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

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070017 | `Unit/UE4070017.wav` |
| 2 | 0 | 4070017 | `Unit/UE4070017.wav` |
| 6 | 0 | 4070018 | `Unit/UE4070018.wav` |

### Seen in

- [[gameplay/README|Gameplay]] § Pages *(name match)*: Abyss map and portals, Lords of the Land, Skull artifact set, Potion regeneration, Arena ranking rewards, Precept shop — from player screenshots
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 3. Artifacts: additional effects, crafting, reinforcing *(name match)*: Crafting can fail for top items (Thorns Armor, Invincible Armor, transform stones, Skull weapons via alchemy); the materials are lost. No protection item exist…
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 5. Notable items and skills *(name match)*: Skull artifact set · 3-piece bonus bugged (about 1,000 attack instead of ~20), Feb 2017; see gameplay/skull-artifact-set · *player* [t928]
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 9. Dungeons, bosses, farming *(name match)*: 1 · Temple of the Skull · Deathhead · Garnet, Red Bloodstone
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 9. Dungeons, bosses, farming *(name match)*: 2 · Cemetery of the Skull · Death Knight (Dark Knight Skull) · Topaz, Blue Bloodstone, Rosemary, Jasmine
- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]] § 2017-02-02: Season 2 ((t898); German copy t897; Steam 2 Feb) *(name match)*: Weapon alchemy · combine a level 30 weapon with materials; a higher-grade input weapon raises the success chance; on failure all materials are lost; Skull weap…
- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]] § 1. Per dungeon level *(name match)*: 1 · Temple of the Skull → 121 "[Lv 1] Skull Temple" · Deathhead → King Deathhead 672; Tough King Deathhead 804; 1501 · Garnet 802, Red Bloodstone 812 · Blue Pa…
- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]] § 1. Per dungeon level *(name match)*: 2 · Cemetery of the Skull → 128 "[Lv 2] Skull Cemetery" · Death Knight → Dark Knight Skull 673; 809, 1205, 1504 · Topaz 814, Blue Bloodstone 804, Rosemary 822,…
- [[gameplay/maps-and-dungeons|Maps and dungeons]] § 2. Border-area (normal/hard) dungeons *(name match)*: 1 · Skull Temple (*Temple of the Skull*) · 121 · King Deathhead (672; "Tough" 804) · T1 · Garnet ×4, Red Bloodstone ×4
- [[gameplay/maps-and-dungeons|Maps and dungeons]] § 2. Border-area (normal/hard) dungeons *(name match)*: 2 · Skull Cemetery (*Cemetery of the Skull*) · 128 · Dark Knight Skull (673/809/1205) · T1 · Blue Bloodstone, Topaz, Rosemary, Jasmine ×2 each
- [[gameplay/patch-history|Patch notes and other sources]] § Items *(name match)*: Boss sets (Death Head, Skull, Fisher, Komodo, Spector, Garon, Fame Knight, Fame Warrior) with 3 bonus steps (WM 0809); essences for them drop from fort guardia…
- [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]] § 6. Boss and fame set bonuses *(name match)*: Skull (2, 3011–) · Armor 30 · Magic Resist 30 · Armor 50, MR 50
- … and 21 more lines

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 4 |
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
