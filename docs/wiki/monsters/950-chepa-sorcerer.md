---
title: "Chepa Sorcerer"
type: "monster"
id: 950
status: "partial"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 950", "client: HeroData.cdb id 14 (hero transform of the same name)", "docs: [[gameplay/dungeon-drops]] (boss of field 127)", "docs: [[gameplay/maps-and-dungeons]] (boss of field 127)", "client: DungeonAdmission.cdb (rewards advertised by the dungeon, no rates)"]
name_key: "UnitName_950"
category: 1
class_mask: 1
model: 300
model_name: "MOB_Chepa03"
model_path: "character/npc/monster/mob_chepa/mob_chepa01.mo"
scale: 1.2
radius: 1
sounds: [4070000, 4070000, 4070012, 4070012, 4070012, 4070016]
hero: 14
boss_of: [127]
dungeon_rewards:
  - {"field": 127, "items": [611, 601, 693, 1931, 2709, 2759]}
spawn_fields: [127]
---
<!-- generated:start -->
<!-- generated-keys: title=ea3216 type=9bbc46 id=b63c6a sources=c918be name_key=9e519f category=356a19 class_mask=356a19 model=e26973 model_name=c5970a model_path=207e1f scale=8114b9 radius=356a19 sounds=c88901 hero=fa35e1 boss_of=cf6862 dungeon_rewards=3804f5 spawn_fields=cf6862 -->
|  |  |
|---|---|
|  | ![Chepa Sorcerer](wiki/assets/monsters/950.png) |
| **Unit id** | `950` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `300` MOB_Chepa03 (`character/npc/monster/mob_chepa/mob_chepa01.mo`) |
| **Scale** | 1.2 (second scale / radius 1) |
| **Hero transform** | [[wiki/heroes/14-chepa-sorcerer\|Chepa Sorcerer]] |
| **Boss of** | [[wiki/dungeons/127-lv-1-chepa-village\|(Lv 1) Chepa Village]] |

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

- [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]] — boss ([[gameplay/dungeon-drops]], [[gameplay/maps-and-dungeons]])

### Dungeon rewards (advertised)

What the dungeon's entry window shows (`DungeonAdmission`). It is a list of possible rewards of the whole dungeon, not this boss's drop table, and has no rates.

- [[wiki/dungeons/127-lv-1-chepa-village|(Lv 1) Chepa Village]]: [[wiki/items/611-red-passion-fragments-d|Red Passion Fragments (D)]], [[wiki/items/601-blue-passion-fragments-d|Blue Passion Fragments (D)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/1931-essence-of-wind|Essence of Wind]], [[wiki/items/2709-drop-of-chepa-sorcerer|Drop of Chepa Sorcerer]], [[wiki/items/2759-the-chepa-sorcerer-s-sealed-weapon|The Chepa Sorcerer's Sealed Weapon]]

### Other units with this name

[[wiki/monsters/870-chepa-sorcerer|Chepa Sorcerer (870)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 2 | 0 | 4070000 | `Unit/UE4070000.wav` |
| 3 | 0 | 4070012 | `Unit/UE4070012.wav` |
| 4 | 0 | 4070012 | `Unit/UE4070012.wav` |
| 5 | 0 | 4070012 | `Unit/UE4070012.wav` |
| 6 | 0 | 4070016 | `Unit/UE4070016.wav` |

### Seen in

- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 9. Dungeons, bosses, farming: Client check: units 672 King Deathhead, 673 Dark Knight Skull, 674 Tempest Fisher, 675 Slayer Komodo, 676 Great Summoner Spectre, 677 War Chief Garon, 849 Akas…
- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]] § 1. Per dungeon level: 1 · Chepa Village → 127 "[Lv 1] Chepa Village" · Chepa Sorcerer → 870 / 950 · Lavender 818, Peppermint 820 · Red Passion Frag [D] 611, 601, 693, Essence of Win…
- [[gameplay/maps-and-dungeons|Maps and dungeons]] § 2. Border-area (normal/hard) dungeons: 1 · Chepa Village · 127 · Chepa Sorcerer (870/950) · T1 · Lavender ×4, Peppermint ×4
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 9. Dungeons, bosses, farming *(name match)*: 1 · Chepa Village · Chepa Sorcerer · Lavender, Peppermint
- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]] § 2016-12-15: Civil War ((t816); Steam 15 Dec) *(name match)*: Boundary-area boss summon · dungeon elites drop a scroll that summons one extra boss, once per boss: DeathHead, Chepa Sorcerer, Dark Knight, Tempest Fisher, Ko…

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@8c | 113 |
| u8@91 | 15 |
| f32@c0 | 3.3 |
| f32@10c | 1 |
<!-- generated:end -->

## Notes

- Boss of [[wiki/dungeons/127-lv-1-chepa-village|[Lv 1] Chepa Village (127)]] (guides + client ids, [[gameplay/maps-and-dungeons]] §2; [[gameplay/dungeon-drops]] §1). Crush Online name: Chepa Sorcerer (Crush Online sheet, Lv 1) ([[gameplay/dungeon-drops]] §1–2; [[gameplay/crush-mechanics]] §9).
- That dungeon drops T1 named-set gear, already reinforced at a random level (+0 to +11 seen) (image + guide, [[gameplay/maps-and-dungeons]] §2).
- Other units with this boss's name: [[wiki/monsters/870-chepa-sorcerer|870]].

## Behaviour

- Drops: the dungeon entry panel advertises this dungeon's essence, horn and sealed weapon (client, front matter `dungeon_rewards`; no rates). Crush Online players said every boss (dungeon or world map) could drop every essence (player, [[gameplay/crush-mechanics]] §9). Warmonger patch 0920 raised boss-material drop rates from dungeon bosses and fort guardians (notes, [[gameplay/patch-history]] § Numbers pass (October 2026)).
- The forum says a dungeon boss only exists while the land is monster-invaded (forum, [[gameplay/warmonger-forum]] §3); in hard mode the boss waits at the end (guide, [[gameplay/maps-and-dungeons]] §2).
- Crush Online patch 2016-12-15: elites in boundary-area dungeons dropped a scroll that summoned one extra boss, once per boss; this boss's scroll is [[wiki/items/2589-the-chepa-sorcerer-s-pipe|The Chepa Sorcerer's Pipe (2589)]] in the client (staff + client, [[gameplay/crush-patch-notes]] § 2016-12-15).

## Sources

- [[gameplay/dungeon-drops]] §1–2, [[gameplay/maps-and-dungeons]] §2, [[gameplay/crush-mechanics]] §9, [[gameplay/warmonger-forum]] §3, [[gameplay/crush-patch-notes]] § 2016-12-15, [[gameplay/patch-history]]

## Open questions

- HP, level, damage, exp and drop rates: no source gives them. [[gameplay/sources]] §9 lists boss videos (Commander Reviatan solo, Komodo 5-man) that could give HP against damage numbers.
- The guides do not say which of this boss's unit ids is the normal-mode, hard-mode or field version.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
