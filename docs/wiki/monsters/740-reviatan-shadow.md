---
title: "Reviatan Shadow"
type: "monster"
id: 740
status: "partial"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 740", "client: HeroData.cdb id 12 (hero transform of the same name)", "docs: [[gameplay/dungeon-drops]] (boss of field 126)", "docs: [[gameplay/maps-and-dungeons]] (boss of field 126)", "client: DungeonAdmission.cdb (rewards advertised by the dungeon, no rates)"]
name_key: "UnitName_740"
category: 1
class_mask: 1
model: 75
model_name: "MOB_DemonLord_Shadow_01"
model_path: "character/npc/monster/mob_demon/mob_demonlord_01.mo"
scale: 1.3
radius: 1
projectile: 853
sounds: [4070051, 4070051, 4070050, 4070050, 4070050, 4070052]
hero: 12
boss_of: [126]
dungeon_rewards:
  - {"field": 126, "items": [612, 613, 693, 694, 1935, 2707, 2757]}
spawn_fields: [126]
---
<!-- generated:start -->
<!-- generated-keys: title=245e76 type=9bbc46 id=2e0ab5 sources=63ba5a name_key=4276b2 category=356a19 class_mask=356a19 model=450dde model_name=764cd3 model_path=e1bf24 scale=2afe7d radius=356a19 projectile=43d6ee sounds=bfd9b2 hero=7b5200 boss_of=d9b420 dungeon_rewards=c61337 spawn_fields=d9b420 -->
|  |  |
|---|---|
|  | ![Reviatan Shadow](wiki/assets/monsters/740.png) |
| **Unit id** | `740` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `75` MOB_DemonLord_Shadow_01 (`character/npc/monster/mob_demon/mob_demonlord_01.mo`) |
| **Scale** | 1.3 (second scale / radius 1) |
| **Projectile?** | `u32@bc` = 853 (archers carry one; meaning *inferred*) |
| **Hero transform** | Reviatan Shadow |
| **Boss of** | [[wiki/dungeons/126-lv-7-demon-hell\|(Lv 7) Demon Hell]] |

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

- [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]] — boss ([[gameplay/dungeon-drops]], [[gameplay/maps-and-dungeons]])

### Dungeon rewards (advertised)

What the dungeon's entry window shows (`DungeonAdmission`). It is a list of possible rewards of the whole dungeon, not this boss's drop table, and has no rates.

- [[wiki/dungeons/126-lv-7-demon-hell|(Lv 7) Demon Hell]]: [[wiki/items/612-red-passion-piece-d|Red Passion Piece (D)]], [[wiki/items/613-red-passion-fragments-c|Red Passion Fragments (C)]], [[wiki/items/693-gem-stone-blue|Gem Stone : Blue]], [[wiki/items/694-gem-stone-yellow|Gem Stone : Yellow]], [[wiki/items/1935-essence-of-light|Essence of Light]], [[wiki/items/2707-horn-of-leviathan|Horn of Leviathan]], [[wiki/items/2757-the-devil-commander-leviathan-s-sealed-weapon|The Devil commander Leviathan's Sealed Weapon]]

### Other units with this name

[[wiki/monsters/678-reviatan-shadow|Reviatan Shadow (678)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070051 | `Unit/UE4070051.wav` |
| 2 | 0 | 4070051 | `Unit/UE4070051.wav` |
| 3 | 977 | 4070050 | `Unit/UE4070050.wav` |
| 4 | 977 | 4070050 | `Unit/UE4070050.wav` |
| 5 | 0 | 4070050 | `Unit/UE4070050.wav` |
| 6 | 0 | 4070052 | `Unit/UE4070052.wav` |

### Seen in

- [[gameplay/maps-and-dungeons|Maps and dungeons]] § 2. Border-area (normal/hard) dungeons: 7 · Demon Hell (*Hell of Demon*) · 126 · Reviatan Shadow (678/740; "Commander Reviatan" 739) · T2 · Diamond ×4, Spartium ×5, Borage ×3

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| f32@c0 | 7.5 |
| f32@10c | 0.5 |
<!-- generated:end -->

## Notes

- Boss of [[wiki/dungeons/126-lv-7-demon-hell|[Lv 7] Demon Hell (126)]] (guides + client ids, [[gameplay/maps-and-dungeons]] §2; [[gameplay/dungeon-drops]] §1). Crush Online name: Akasha/Reviathan (Crush Online sheet, listed for both Lv 7 and Lv 8; the forum says Akasha / Leviathan); the client's rewards for this dungeon show Leviathan's horn and sealed weapon ([[gameplay/dungeon-drops]] §1–2; [[gameplay/crush-mechanics]] §9).
- That dungeon drops T2 named-set gear, already reinforced at a random level (+0 to +11 seen) (image + guide, [[gameplay/maps-and-dungeons]] §2).
- Other units with this boss's name: [[wiki/monsters/678-reviatan-shadow|678]], [[wiki/monsters/739-commander-reviatan|739]], [[wiki/monsters/972-reviatan|972]].
- The dungeons guide shows the Demon Hell boss as **two** identical figures (a multi-boss fight); the PvE text of the Remote Bomb TP skill ("attacks all bosses after attacking the middle boss") fits (image, [[gameplay/maps-and-dungeons]] §2).

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
