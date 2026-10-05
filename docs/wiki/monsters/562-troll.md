---
title: "Troll"
type: "monster"
id: 562
status: "partial"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 562"]
name_key: "UnitName_831"
category: 8
class_mask: 1
model: 284
model_name: "MOB_Troll_Rava_01"
model_path: "character/npc/monster/mob_troll_01/mob_troll_01.mo"
scale: 2
radius: 1
sounds: [4070112, 4070112, 4070010, 4070010, 4070010, 4070011]
---
<!-- generated:start -->
<!-- generated-keys: title=c17a97 type=9bbc46 id=904f2c sources=b52621 name_key=daaacf category=fe5dbb class_mask=356a19 model=7f3541 model_name=ef5f88 model_path=cc4083 scale=da4b92 radius=356a19 sounds=e898d3 -->
|  |  |
|---|---|
| **Unit id** | `562` |
| **Category** | field monster (inferred: ogres, trolls, bears, phytons) (`category@8a` = 8) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `284` MOB_Troll_Rava_01 (`character/npc/monster/mob_troll_01/mob_troll_01.mo`) |
| **Scale** | 2 (second scale / radius 1) |

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

### Other units with this name

[[wiki/monsters/563-troll|Troll (563)]], [[wiki/monsters/583-troll|Troll (583)]], [[wiki/monsters/584-troll|Troll (584)]], [[wiki/monsters/831-troll|Troll (831)]], [[wiki/monsters/832-troll|Troll (832)]], [[wiki/monsters/833-troll|Troll (833)]], [[wiki/monsters/834-troll|Troll (834)]], [[wiki/monsters/835-troll|Troll (835)]], [[wiki/monsters/836-troll|Troll (836)]], [[wiki/monsters/837-troll|Troll (837)]], [[wiki/monsters/838-troll|Troll (838)]]

### Sounds

UnitDB's seven `{a, id}` pairs (+0xcc..+0x100). docs/spec/monsters.md reads the ids as skills, but they are `sound.csv` ids (*client*); `a` is unknown.

| slot | a | sound id | file |
|---|---|---|---|
| 1 | 0 | 4070112 | `Unit/UE4070112.wav` |
| 2 | 0 | 4070112 | `Unit/UE4070112.wav` |
| 3 | 0 | 4070010 | `Unit/UE4070010.wav` |
| 4 | 0 | 4070010 | `Unit/UE4070010.wav` |
| 5 | 0 | 4070010 | `Unit/UE4070010.wav` |
| 6 | 0 | 4070011 | `Unit/UE4070011.wav` |

### Seen in

- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § 1. Land war (field war): Jungle bosses (Troll, Ogre, Bear): when killed they join the killer's team and push the nearest enemy towers, then the nexus once the towers are gone. Spawn ti…
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § 8. Jungle and land-war timers *(name match)*: Each battle lasts 40 min. Troll and Ogre first appear at 36:00 and respawn 4 min after dying; the Bear appears at 35:00 and respawns 5 min after dying (blog pv…
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § 8. Jungle and land-war timers *(name match)*: TP per kill per the blog: normal 30, elite 100, Ogre/Bear/Troll 1,500 each; tower 500 TP. The definitive and strategy guides give Ogre 2,500 and Bear 3,000, so…
- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § 1. Land war (field war) *(name match)*: TP from kills: normal monster 30, elite 100, Troll 1,500, Ogre 2,500, Bear 3,000 (the definitive guide rounds all three to "1,500+"). *guides* strategy guide,…
- [[gameplay/server-rules|Server rules checklist]] § Land war *(name match)*: [ ] TP is a shared team pool. Kill TP: normal 30, elite 100, Troll 1,500, Ogre 2,500, Bear 3,000. — strategy, definitive — M
- [[gameplay/server-rules|Server rules checklist]] § Land war *(name match)*: [ ] Jungle: Troll & Ogre spawn at 36:00 then 4 min after death; Bear at 35:00 then 5 min after death; killed jungle bosses fight for the killer's team (towers,…
- [[gameplay/server-rules|Server rules checklist]] § PvP, events, forts *(name match)*: [ ] Jungle: medium jungle mob spawns at PvP start; Troll/Ogre at 36:00, respawn 4 min; Bear at 35:00, respawn 5 min — WM 0830, blog — M
- [[gameplay/video-early-quests|Video notes: first session, levels 1+ (charmanmugen)]] § 5. Monsters seen *(name match)*: Kill messages ("X was destroyed") in quest order: Slime → Chepa Warrior / Chepa Archer (Training Ground circle, many killed for exp) → Bee, Cobra → Chepa Warri…

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u8@8c | 111 |
| u8@91 | 15 |
| f32@c0 | 2.7 |
| f32@10c | 1 |
<!-- generated:end -->

## Notes

- [[gameplay/pvp-and-matches]] §1 lists this unit among the land-war **jungle bosses** (Troll) (client ids; the guides do not say which id spawns on which land).

## Behaviour

- Spawns first at 36:00 on the 40:00 war clock, then 4 minutes after each death (guides, [[gameplay/pvp-and-matches]] §1; blog, [[gameplay/events-and-schedules]] §8).
- When killed it joins the killer's team and pushes the nearest enemy towers, then the nexus (guides, [[gameplay/pvp-and-matches]] §1).
- TP for the kill: 1,500 (guides, [[gameplay/pvp-and-matches]] §1; [[gameplay/events-and-schedules]] §8).

## Sources

- [[gameplay/pvp-and-matches]] §1; [[gameplay/events-and-schedules]] §8; [[gameplay/video-fort-war]]

## Open questions

- Which jungle id spawns where is unknown, so no `spawns` are set.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
