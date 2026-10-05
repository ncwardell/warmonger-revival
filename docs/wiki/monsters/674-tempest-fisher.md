---
title: "Tempest Fisher"
type: "monster"
id: 674
status: "partial"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 674", "client: HeroData.cdb id 8 (hero transform of the same name)", "docs: [[gameplay/dungeon-drops]] (boss of field 122)", "docs: [[gameplay/maps-and-dungeons]] (boss of field 122)", "client: DungeonAdmission.cdb (rewards advertised by the dungeon, no rates)", "client: Quest.cdb kill objectives (quests 756, 762, 1018)"]
name_key: "UnitName_674"
category: 6
class_mask: 1
kill_group: 10015
model: 70
model_name: "MOB_fisher Boss_01"
model_path: "character/npc/monster/mob_fisher/mob_fisher boss_01.mo"
scale: 1
radius: 1
projectile: 774
sounds: [4070036, 4070036, 4070035, 4070035, 4070035, 4070037]
hero: 8
boss_of: [122]
dungeon_rewards:
  - {"field": 122, "items": [612, 602, 693, 1933, 2703, 2753]}
quest_targets:
  - {"quest": 756, "need": 1, "group": 10015}
  - {"quest": 762, "need": 1, "group": 10015}
  - {"quest": 1018, "need": 1, "group": 10015}
quest_drops:
  - {"quest": 762, "item": 2587, "rate": 50, "need": 1}
spawn_fields: [122]
---
<!-- generated:start -->
<!-- generated-keys: title=c1779d type=9bbc46 id=ee4988 sources=6b42c2 name_key=e5b49b category=c1dfd9 class_mask=356a19 kill_group=848f94 model=b7103c model_name=df608e model_path=213684 scale=356a19 radius=356a19 projectile=66c4d1 sounds=12ed91 hero=fe5dbb boss_of=d4ee27 dungeon_rewards=4fc487 quest_targets=aaab23 quest_drops=9cd855 spawn_fields=d4ee27 -->
|  |  |
|---|---|
|  | ![Tempest Fisher](wiki/assets/monsters/674.png) |
| **Unit id** | `674` |
| **Category** | boss (inferred: every dungeon boss and quest bosses such as Tow Chief) (`category@8a` = 6) |
| **Class mask** | 1 (monster) |
| **Kill group** | `10015` with [[wiki/monsters/727-chepa-warrior\|Chepa Warrior]], [[wiki/monsters/728-chepa-archer\|Chepa Archer]] |
| **Model** | ObjectList `70` MOB_fisher Boss_01 (`character/npc/monster/mob_fisher/mob_fisher boss_01.mo`) |
| **Scale** | 1 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 774 (archers carry one; meaning *inferred*) |
| **Hero transform** | [[wiki/heroes/8-tempest-fisher\|Tempest Fisher]] |
| **Boss of** | [[wiki/dungeons/122-lv-3-tsunami-lake\|(Lv 3) Tsunami Lake]] |

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

- [[wiki/quests/756-group-border-area-hard-mode|Group - Border Area Hard Mode]]: kill 1 in [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] — via kill group `10015` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/762-killed-boss-of-border-area-no-2|killed boss of Border area No.2]]: collect 1 × [[wiki/items/2587-the-tempest-fisher-s-pipe|The Tempest Fisher's Pipe]] (drops at 50% while the quest is active) in [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] — via kill group `10015` (*inferred* from UnitDB `i32@80`)
- [[wiki/quests/1018-tsunami-lake-boss-hunting|Tsunami Lake : Boss Hunting]]: kill 1 in [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] — via kill group `10015` (*inferred* from UnitDB `i32@80`)

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]] — boss ([[gameplay/dungeon-drops]], [[gameplay/maps-and-dungeons]]); quest map of [[wiki/quests/756-group-border-area-hard-mode|Group - Border Area Hard Mode]], [[wiki/quests/762-killed-boss-of-border-area-no-2|killed boss of Border area No.2]], [[wiki/quests/1018-tsunami-lake-boss-hunting|Tsunami Lake : Boss Hunting]]

### Dungeon rewards (advertised)

What the dungeon's entry window shows (`DungeonAdmission`). It is a list of possible rewards of the whole dungeon, not this boss's drop table, and has no rates.

- [[wiki/dungeons/122-lv-3-tsunami-lake|(Lv 3) Tsunami Lake]]: [[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]], [[wiki/items/602-blue-passion-piece-d|Blue Passion Piece (D)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/1933-essence-of-water|Essence of Water]], [[wiki/items/2703-fin-of-fisher|Fin of Fisher]], [[wiki/items/2753-the-tempest-fisher-s-sealed-weapon|The Tempest Fisher's Sealed Weapon]]

### Other units with this name

[[wiki/monsters/733-tempest-fisher|Tempest Fisher (733)]], [[wiki/monsters/1209-tempest-fisher|Tempest Fisher (1209)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070036 | `Unit/UE4070036.wav` |
| 2 | 0 | 4070036 | `Unit/UE4070036.wav` |
| 3 | 770 | 4070035 | `Unit/UE4070035.wav` |
| 4 | 770 | 4070035 | `Unit/UE4070035.wav` |
| 5 | 0 | 4070035 | `Unit/UE4070035.wav` |
| 6 | 0 | 4070037 | `Unit/UE4070037.wav` |

### Seen in

- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 9. Dungeons, bosses, farming: Client check: units 672 King Deathhead, 673 Dark Knight Skull, 674 Tempest Fisher, 675 Slayer Komodo, 676 Great Summoner Spectre, 677 War Chief Garon, 849 Akas…
- [[gameplay/dungeon-drops|Dungeon drops (ores and herbs)]] § 1. Per dungeon level: 3 · Lake of the tsunami → 122 "[Lv 3] Tsunami Lake" · Tempest Fisher → 674; 733, 1209 · Topaz 814, Blue Bloodstone 804, Rosemary 822, Jasmine 824 · Red Passion…
- [[gameplay/maps-and-dungeons|Maps and dungeons]] § 2. Border-area (normal/hard) dungeons: 3 · Tsunami Lake (*Lake of the tsunami*) · 122 · Tempest Fisher (674/733/1209) · T1 · Topaz, Blue Bloodstone, Rosemary, Jasmine ×2 each
- [[gameplay/classes-and-legions|Classes, nations and legions]] § Heroes *(name match)*: 0420 · Tempest Fisher · MR penetration 20 → 10
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 9. Dungeons, bosses, farming *(name match)*: 3 · Lake of the Tsunami · Tempest Fisher · Topaz, Blue Bloodstone, Rosemary, Jasmine
- [[gameplay/crush-patch-notes|Crush Online patch notes 2016–17]] § 2016-12-15: Civil War ((t816); Steam 15 Dec) *(name match)*: Boundary-area boss summon · dungeon elites drop a scroll that summons one extra boss, once per boss: DeathHead, Chepa Sorcerer, Dark Knight, Tempest Fisher, Ko…
- [[gameplay/lords-of-the-land|Lords of the Land buff and quest]] § 5. Other numbers on the screenshots *(name match)*: Freya · Gives "Defensive aggression" (kill Tempest Fisher 0/1 / Slayer Komodo 0/1) · *image* [img-buff], [img-quest]
- [[gameplay/sources|Sources and gaps]] § 3. Player screenshots (image sets that still load) *(name match)*: Steam discussion album → MKB7Toy · EN · Ashcolor Hill boss Tempest Fisher, a quest list, SP per kill and per assist · medium · catalogued
- [[gameplay/warmonger-forum|Warmonger forum (2018)]] § 4. Levelling and medals *(name match)*: Silver from precepts · B scroll "kill Tempest Fisher" → 4 silver; B scroll "kill 10/10 Tow" → 2 silver; C scroll "occupy territory 10/10" or "kill players" (Ab…

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 6.5 |
| f32@10c | 0.5 |
<!-- generated:end -->

## Notes

- Boss of [[wiki/dungeons/122-lv-3-tsunami-lake|[Lv 3] Tsunami Lake (122)]] (guides + client ids, [[gameplay/maps-and-dungeons]] §2; [[gameplay/dungeon-drops]] §1). Crush Online name: Tempest Fisher (Crush Online sheet, *Lake of the tsunami*, Lv 3) ([[gameplay/dungeon-drops]] §1–2; [[gameplay/crush-mechanics]] §9).
- That dungeon drops T1 named-set gear, already reinforced at a random level (+0 to +11 seen) (image + guide, [[gameplay/maps-and-dungeons]] §2).
- Other units with this boss's name: [[wiki/monsters/733-tempest-fisher|733]], [[wiki/monsters/1209-tempest-fisher|1209]].
- Also a world-map boss: a player screenshot shows Tempest Fisher as the boss of Ashcolor Hill (image, [[gameplay/sources]] §3), and Freya's quest "Defensive aggression" asks for 1 Tempest Fisher / 1 Slayer Komodo kill (image, [[gameplay/lords-of-the-land]] §5). A B-grade precept "kill Tempest Fisher" paid 4 silver medals (forum, [[gameplay/warmonger-forum]] §4).
- Warmonger patch 0809 added a **Fisher** boss set (3 bonus steps); the essences for these sets drop from fort guardians (notes, [[gameplay/patch-history]] § Items).

## Behaviour

- Drops: the dungeon entry panel advertises this dungeon's essence, horn and sealed weapon (client, front matter `dungeon_rewards`; no rates). Crush Online players said every boss (dungeon or world map) could drop every essence (player, [[gameplay/crush-mechanics]] §9). Warmonger patch 0920 raised boss-material drop rates from dungeon bosses and fort guardians (notes, [[gameplay/patch-history]] § Numbers pass (October 2026)).
- The forum says a dungeon boss only exists while the land is monster-invaded (forum, [[gameplay/warmonger-forum]] §3); in hard mode the boss waits at the end (guide, [[gameplay/maps-and-dungeons]] §2).
- Crush Online patch 2016-12-15: elites in boundary-area dungeons dropped a scroll that summoned one extra boss, once per boss; this boss's scroll is [[wiki/items/2587-the-tempest-fisher-s-pipe|The Tempest Fisher's Pipe (2587)]] in the client (staff + client, [[gameplay/crush-patch-notes]] § 2016-12-15).

## Sources

- [[gameplay/dungeon-drops]] §1–2, [[gameplay/maps-and-dungeons]] §2, [[gameplay/crush-mechanics]] §9, [[gameplay/warmonger-forum]] §3, [[gameplay/crush-patch-notes]] § 2016-12-15, [[gameplay/patch-history]]

## Open questions

- HP, level, damage, exp and drop rates: no source gives them. [[gameplay/sources]] §9 lists boss videos (Commander Reviatan solo, Komodo 5-man) that could give HP against damage numbers.
- The guides do not say which of this boss's unit ids is the normal-mode, hard-mode or field version.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
