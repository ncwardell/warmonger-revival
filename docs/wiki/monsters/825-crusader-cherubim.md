---
title: "Crusader Cherubim"
type: "monster"
id: 825
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 825", "docs: [[gameplay/dungeon-drops]] (boss of field 824)"]
name_key: "UnitName_825"
category: 6
class_mask: 1
model: 277
model_name: "NPC_Defender_W"
model_path: "character/npc/monster/npc_defender/npc_defender_w.mo"
scale: 2.5
radius: 1
sounds: [4070080, 4070080, 4070079, 4070079, 4070079, 4070081]
boss_of: [824]
spawn_fields: [824]
---
<!-- generated:start -->
<!-- generated-keys: title=817ae8 type=9bbc46 id=5375ef sources=635925 name_key=6b1245 category=c1dfd9 class_mask=356a19 model=f33316 model_name=aad162 model_path=92cb13 scale=555a5c radius=356a19 sounds=2f2b3f boss_of=5ccc77 spawn_fields=5ccc77 -->
|  |  |
|---|---|
| **Unit id** | `825` |
| **Category** | boss (inferred: every dungeon boss and quest bosses such as Tow Chief) (`category@8a` = 6) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `277` NPC_Defender_W (`character/npc/monster/npc_defender/npc_defender_w.mo`) |
| **Scale** | 2.5 (second scale / radius 1) |
| **Boss of** | Field 824 |

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

### Where it appears

Fields the client ties it to (quest objective maps, dungeon boss tables). Positions and counts are not in the client: add them as `spawns`.

- Field 824 — boss ([[gameplay/dungeon-drops]])

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070080 | `Unit/UE4070080.wav` |
| 2 | 0 | 4070080 | `Unit/UE4070080.wav` |
| 3 | 977 | 4070079 | `Unit/UE4070079.wav` |
| 4 | 977 | 4070079 | `Unit/UE4070079.wav` |
| 5 | 0 | 4070079 | `Unit/UE4070079.wav` |
| 6 | 0 | 4070081 | `Unit/UE4070081.wav` |

### Seen in

- [[gameplay/classes-and-legions|Classes, nations and legions]] § 4. Forts (castles): Losing a fort: enemies siege it. Killing the guardian Crusader Cherubim inside (UnitDB 825) removes one fort shield and distributes part of the fort's taxes to…
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 9. Dungeons, bosses, farming: Client check: units 672 King Deathhead, 673 Dark Knight Skull, 674 Tempest Fisher, 675 Slayer Komodo, 676 Great Summoner Spectre, 677 War Chief Garon, 849 Akas…
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 5. Notable items and skills *(name match)*: Transform stones "Sacred Power" (Crusader Cherubim) / "Wrath of the Knight" (Dark Knight Skull) · 5 Essence of Light or Darkness + 5 Brilliant spell stones (10…
- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 12. Crush vs Warmonger: differences that matter for the server *(name match)*: [t254]: https://web.archive.org/web/20161022145703/http://www.crush-game.com/forum/threads/crusader-cherubim-dark-knight-skull-skill-stones.254/
- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § 2. Fort war *(name match)*: See Forts: weekly Civil War (Sunday 20:00, same-nation legions, bid on Saturday) played as a normal nexus battlefield inside the fort, and fort sieges by the o…
- [[gameplay/server-rules|Server rules checklist]] § Legions, forts, events *(name match)*: [ ] Fort siege: killing Crusader Cherubim removes a shield and pays out part of the fort's taxes; fort falls when shields reach 0; default max 3 shields; shiel…
- [[gameplay/sources|Sources and gaps]] § 6. Videos *(name match)*: ZonderCoRe Fortress War 1/4–4/4 (also 6_z6CUpZj30, 7f7QwwUyYBg, JPd7TCu-44o) · WM 06-2018 · Fort interior: gates, cores, Heart of Magic, Crusader Cherubim spot…
- [[gameplay/sources|Sources and gaps]] § 9. What is still missing *(name match)*: 8 · Fort interior: gate, core, Heart of Magic and Crusader Cherubim positions; guardian HP · Fort sieges · ZonderCoRe Fortress War 1/4–4/4, 2umwpYlKAvg, forum…
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § Video notes: fortress war series (ZonderCoRe) *(name match)*: The four parts are one continuous session. The streamer is on Erion (attacking side), legion tag &lt;Scourge&gt;. Parts 1–3 are a normal land war; the "fortres…
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § Structures *(name match)*: Room of Core cores, Heart of Magic, guardian, Crusader Cherubim · no HP readable: cores are captured by standing on the platform, and the Heart was never targe…
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § 5. Still open *(name match)*: Guardian, Crusader Cherubim, core and Heart of Magic HP. Neither this series nor the client gives them. 2umwpYlKAvg (Crush Online) is the next place to look.

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@91 | 15 |
| u32@b8 | 5 |
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
