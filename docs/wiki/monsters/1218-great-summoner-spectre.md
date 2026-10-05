---
title: "Great Summoner Spectre"
type: "monster"
id: 1218
status: "partial"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 1218", "client: HeroData.cdb id 10 (hero transform of the same name)", "docs: [[gameplay/dungeon-drops]] (boss of field 124)", "docs: [[gameplay/maps-and-dungeons]] (boss of field 124)", "client: DungeonAdmission.cdb (rewards advertised by the dungeon, no rates)"]
name_key: "UnitName_1218"
category: 6
class_mask: 1
model: 78
model_name: "MOB_GhostKing_01_0_0_0_00_00"
model_path: "character/npc/monster/npc_evil/mob_ghostking_01.mo"
scale: 1.7
radius: 1
projectile: 865
sounds: [4070059, 4070059, 4070058, 4070058, 4070058, 4070060]
hero: 10
boss_of: [124]
dungeon_rewards:
  - {"field": 124, "items": [612, 693, 694, 1934, 2705, 2755]}
spawn_fields: [124]
---
<!-- generated:start -->
<!-- generated-keys: title=d638eb type=9bbc46 id=7f1426 sources=6d0fc2 name_key=731781 category=c1dfd9 class_mask=356a19 model=eb4ac3 model_name=25777e model_path=8c1900 scale=58e6d3 radius=356a19 projectile=81d51c sounds=823e44 hero=b1d578 boss_of=181a14 dungeon_rewards=3e13ad spawn_fields=181a14 -->
|  |  |
|---|---|
|  | ![Great Summoner Spectre](wiki/assets/monsters/1218.png) |
| **Unit id** | `1218` |
| **Category** | boss (inferred: every dungeon boss and quest bosses such as Tow Chief) (`category@8a` = 6) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `78` MOB_GhostKing_01_0_0_0_00_00 (`character/npc/monster/npc_evil/mob_ghostking_01.mo`) |
| **Scale** | 1.7 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 865 (archers carry one; meaning *inferred*) |
| **Hero transform** | [[wiki/heroes/10-great-summoner-spectre\|Great Summoner Spectre]] |
| **Boss of** | [[wiki/dungeons/124-lv-6-ghost-fortress\|(Lv 6) Ghost Fortress]] |

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

- [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]] — boss ([[gameplay/dungeon-drops]], [[gameplay/maps-and-dungeons]])

### Dungeon rewards (advertised)

What the dungeon's entry window shows (`DungeonAdmission`). It is a list of possible rewards of the whole dungeon, not this boss's drop table, and has no rates.

- [[wiki/dungeons/124-lv-6-ghost-fortress|(Lv 6) Ghost Fortress]]: [[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/694-gem-stone-yellow|Gem Stone : Yellow]], [[wiki/items/1934-essence-of-earth|Essence of Earth]], [[wiki/items/2705-bone-of-spector|Bone of Spector]], [[wiki/items/2755-the-wizard-spector-s-sealed-weapon|The Wizard Spector's Sealed Weapon]]

### Other units with this name

[[wiki/monsters/676-great-summoner-spectre|Great Summoner Spectre (676)]], [[wiki/monsters/743-great-summoner-spectre|Great Summoner Spectre (743)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070059 | `Unit/UE4070059.wav` |
| 2 | 0 | 4070059 | `Unit/UE4070059.wav` |
| 3 | 925 | 4070058 | `Unit/UE4070058.wav` |
| 4 | 925 | 4070058 | `Unit/UE4070058.wav` |
| 5 | 0 | 4070058 | `Unit/UE4070058.wav` |
| 6 | 0 | 4070060 | `Unit/UE4070060.wav` |

### Seen in

- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]] § 1. Per dungeon level: 5 *(client: 6)* · Fortress of Ghost → 124 "[Lv 6] Ghost Fortress" · Great Summoner Spectre → 676; 743, 1218 · Moonstone 808, Lavender 818, Peppermint 820 · 612…
- [[gameplay/maps-and-dungeons|Maps and dungeons]] § 2. Border-area (normal/hard) dungeons: 6 · Ghost Fortress (*Fortress of Ghost*) · 124 · Great Summoner Spectre (676/743/1218) · T2 · Moonstone ×4, Lavender ×3, Peppermint ×5
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 9. Dungeons, bosses, farming *(name match)*: 5 · Fortress of Ghost · Great Summoner Spectre · Moonstone, Lavender, Peppermint
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 12. Crush vs Warmonger: differences that matter for the server *(name match)*: [t402]: https://web.archive.org/web/20161026230614/http://www.crush-game.com/forum/threads/war-chief-garon-great-summoner-spectre-quests.402/

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 7.5 |
| f32@10c | 1 |
<!-- generated:end -->

## Notes

- Boss of [[wiki/dungeons/124-lv-6-ghost-fortress|[Lv 6] Ghost Fortress (124)]] (guides + client ids, [[gameplay/maps-and-dungeons]] §2; [[gameplay/dungeon-drops]] §1). Crush Online name: Great Summoner Spectre (Crush Online sheet, *Fortress of Ghost*, Lv 5 there) ([[gameplay/dungeon-drops]] §1–2; [[gameplay/crush-mechanics]] §9).
- That dungeon drops T2 named-set gear, already reinforced at a random level (+0 to +11 seen) (image + guide, [[gameplay/maps-and-dungeons]] §2).
- Other units with this boss's name: [[wiki/monsters/676-great-summoner-spectre|676]], [[wiki/monsters/743-great-summoner-spectre|743]].
- Warmonger patch 0809 added a **Spector** boss set (3 bonus steps); the essences for these sets drop from fort guardians (notes, [[gameplay/patch-history]] § Items).

## Behaviour

- Drops: the dungeon entry panel advertises this dungeon's essence, horn and sealed weapon (client, front matter `dungeon_rewards`; no rates). Crush Online players said every boss (dungeon or world map) could drop every essence (player, [[gameplay/crush-mechanics]] §9). Warmonger patch 0920 raised boss-material drop rates from dungeon bosses and fort guardians (notes, [[gameplay/patch-history]] § Numbers pass (October 2026)).
- The forum says a dungeon boss only exists while the land is monster-invaded (forum, [[gameplay/warmonger-forum]] §3); in hard mode the boss waits at the end (guide, [[gameplay/maps-and-dungeons]] §2).
- Crush Online patch 2016-12-15 let dungeon elites drop a scroll that summoned one extra boss, once per boss (this boss is on the list); the client's summon items 2585–2589 do not include one for it (staff + client, [[gameplay/crush-patch-notes]] § 2016-12-15).

## Sources

- [[gameplay/dungeon-drops]] §1–2, [[gameplay/maps-and-dungeons]] §2, [[gameplay/crush-mechanics]] §9, [[gameplay/warmonger-forum]] §3, [[gameplay/crush-patch-notes]] § 2016-12-15, [[gameplay/patch-history]]

## Open questions

- HP, level, damage, exp and drop rates: no source gives them. [[gameplay/sources]] §9 lists boss videos (Commander Reviatan solo, Komodo 5-man) that could give HP against damage numbers.
- The guides do not say which of this boss's unit ids is the normal-mode, hard-mode or field version.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
