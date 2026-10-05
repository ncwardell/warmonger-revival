---
title: "Siege Minion"
type: "monster"
id: 1104
status: "stub"
missing: ["hp", "level", "attack", "armor", "magic_resist", "move_speed", "attack_speed", "attack_range", "kill_exp", "kill_gold", "drops", "spawns"]
sources: ["client: UnitDB.cdb id 1104"]
name_key: "UnitName_1104"
category: 1
class_mask: 1
model: 337
model_name: "NPC_Minion_Siege_01"
model_path: "character/npc/neighbor/npc_minion/npc_minion_siege_01.mo"
scale: 1.5
radius: 1
sounds: [4070091, 4070091, 4070016]
---
<!-- generated:start -->
<!-- generated-keys: title=f5b5ca type=9bbc46 id=a6990e sources=448e3c name_key=3ddddf category=356a19 class_mask=356a19 model=0588f5 model_name=e64843 model_path=ed9848 scale=aa8f28 radius=356a19 sounds=8c78f5 -->
|  |  |
|---|---|
| **Unit id** | `1104` |
| **Category** | monster (`category@8a` = 1) |
| **Class mask** | 1 (monster) |
| **Model** | ObjectList `337` NPC_Minion_Siege_01 (`character/npc/neighbor/npc_minion/npc_minion_siege_01.mo`) |
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
| 1 | 0 | 4070091 | `Unit/UE4070091.wav` |
| 2 | 0 | 4070091 | `Unit/UE4070091.wav` |
| 6 | 0 | 4070016 | `Unit/UE4070016.wav` |

### Seen in

- [[gameplay/crush-mechanics|Crush Online mechanics from the forum]] § 6. War, territories, TP, safety *(name match)*: Strategy (TP) panel · goes to the first players to enter the war (up to 3 holders); can be passed on, often bugged. Siege Minion costs 500 TP in that panel · *…
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § 7. TP skill costs *(name match)*: Siege Minion · 1,000 / 100 · 1,000 / 60 (ability raised)
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] § 7. TP skill costs *(name match)*: Matches the client Skill_TP *client*. The always-available nexus skills on a war land are Shield (refills the nexus shield, not HP), Bomb (hits a standing towe…
- [[gameplay/patch-history|Patch notes and other sources]] § PvP, events, forts *(name match)*: TP skill changes (WM 1018): Siege Minion 1000 TP cd 100→60 s, Fortified cd 180→120, Fire Support 2500→2000, I'll be back! 2000→1500, Blind/Portal/Freeze 2500→1…
- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § TP skills *(name match)*: Siege Minion (4506) · Nexus · 1,000 · 100 s · 1000 / 60 · Summons a weak tanking minion; field war only
- [[gameplay/pvp-and-matches|PvP, land wars and matches]] § TP skills *(name match)*: Further client rows not in any guide: I'll be back! (4509), Recovery Shot (4510, 2,500), Fire Support (4512, 2,000), Blind (4514), Create a Portal (4516), Free…
- [[gameplay/server-rules|Server rules checklist]] § Land war *(name match)*: [ ] TP skills and costs per Skill_TP (Shield 1,500/120 s, Remote Bomb 1,500/120 s, Nexus Remote Bomb 2,000/180 s, Siege Minion 1,000, Fortified 2,000 …); Siege…
- [[gameplay/sources|Sources and gaps]] § 8. Forum threads not yet mined *(name match)*: Archived and reachable, with numbers, but not cited anywhere in the wiki yet: current-fort-placement-and-balance.260, inventory-slots-price-increase.78, siege-…
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § TP *(name match)*: Siege Minion placed · −1,000 (5,550 → 4,550, 37:43) · P1 2:08 · video, matches Skill_TP 1,000
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § TP *(name match)*: TP is one pool for the side: it drops when any ally uses a TP skill. Other TP skills used by name: Shield recovery, Siege Minion, Remote Bomb, Nexus Remote Bom…
- [[gameplay/video-fort-war|Video notes: fortress war series (ZonderCoRe)]] § 4. Timestamped log *(name match)*: P2 1:36 · 34:03 · "MISZA set a Siege Minion"
- [[gameplay/warmonger-forum|Warmonger forum (2018)]] § 9. Threads listed on index pages but never archived *(name match)*: The section indexes name threads whose pages exist in no capture on either domain. They would have filled gaps 1–4 in gameplay/sources §9: List of all Grind lo…

### Other client fields

Undecoded UnitDB columns with a value (`meaning@offset`, docs/spec/monsters.md).

| column | value |
|---|---|
| u16@88 | 4 |
| u8@91 | 15 |
| f32@c0 | 4 |
| u8@92 | 3 |
| list5@93 | 0,0,0,16,10 |
| list5@98 | 0,0,0,11,15 |
| f32@10c | 1 |
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
