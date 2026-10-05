# Warmonger / Crush Online: client <-> server contract

This folder defines what a replacement server must send and accept so that the shipped
32-bit client (`Client.exe`, Joyimpact engine) works. Everything here was reverse engineered
from the **client**: your decompiled client (`decompiled.c`), your decompiled client (`disasm.txt`) and the extracted data. Where a
packet is marked live-tested, the working server in `../server/*.py` sends exactly that packet.

Status on 2026-10-05 (completeness review):

- **All 206 opcodes in the inventory are documented. None are missing.**
- Five opcodes are documented in two files. Their byte layouts agree; one of them (0x498) is given two different meanings.
- 181 of 211 opcode entries carry `verified: true`.
- The login -> play -> PvP match -> logout path is covered end to end. Four steps have known gaps, listed under [Flow coverage](#flow-coverage).

## How the contract is organised

One YAML file per subsystem. Each file has three top-level lists, plus extras in two files:

| key | contents |
|---|---|
| `opcodes[]` | One entry per opcode the subsystem owns: `opcode` (YAML int; write it as hex), `name`, `direction` (`c2s` / `s2c` / `both`), `c2s` {`size`, `extra`, `fields[]` {`offset`, `type`, `name`, `values`, `notes`}, `variants`}, `s2c` {`min_size`, `extra`, `accepted_if`, `fields[]`}, `server_reply`, `client_effect`, `handler` (S->C handler function), `send_sites` (C->S builder functions), `confidence` (high / medium / low), `verified`, `verifier_note`, `evidence`, `claimed` (set when the opcode was moved from the inventory's subsystem). |
| `flows[]` | `name` + ordered `steps`: packet sequences for one feature, both directions. |
| `server_rules[]` | Decisions the client cannot make for the server. Each has what the client expects, the data table that informs it, and a suggested default. **The key names differ between files:** `client_expects`/`expects`, `data_table`/`informed_by`/`data`, `suggested_default`/`default`. A loader has to accept all of them. |
| `web_endpoints[]` | (session, social) The HTTP POST `.asp` pages and their XML row shapes. |
| `notes_on_assignment[]` | (session) Opcodes the inventory put in the wrong subsystem. |

Conventions shared by every file are in the header comment of `session.yaml`:

- **Header:** 16 bytes, `u16 len | u16 0xA53C | u16 opcode | u16 extra | u32 tick | u32 key`. All offsets are counted from the start of the packet.
- **Size:** S->C packets of 16 bytes or less are dropped.
- **Obfuscation:** C->S payload words are sent as `~(w - key)`. `key` is set from the 0x2000 `extra`, and the client never resets it on the same socket.
- **Tick:** every S->C packet re-bases the client's tick.

| file | subsystem |
|---|---|
| `session.yaml` | Login server and game-server login, character list / create / delete / buy slot, leave game, channel move, heartbeat, web `.asp` endpoints |
| `world.yaml` | Enter world, unit spawn and despawn, movement, AOI, warps and teleports, portals, world map, scene objects (gadgets) |
| `combat.yaml` | Hits, skills, damage and heals, buffs, death and revive, exp and levels, capture channelling, TP skills, summons |
| `items.yaml` | Containers, equipment, shops and buyback, consumables, warehouse, crafting, reinforcement, runes, gacha, cash mall, auction |
| `pvp.yaml` | Match offer and queue, team queue, arena match, custom rooms, nation war and forts, nation vote, dungeon entry |
| `quests.yaml` | Quest log, accept / progress / turn-in, quest board, achievements, Lords of the Land rewards |
| `social.yaml` | Chat, party, friends, mail, legion (guild) and its warehouse / stock / donation, inspect, web lists |
| `system.yaml` | System messages and confirm prompts, revive request, GM tool, create-scene errors |

Companion inputs (read-only):

- `contract/inventory.tsv`: the opcode inventory with its send sites.
- `contract/examples.md`: packets the client builds for itself, which serve as ground truth.
- `docs/spec/data-tables.md`: the decoded data tables the server rules refer to.

## Coverage per subsystem

Columns:

- **inv**: opcodes the inventory assigns to the subsystem.
- **doc**: opcodes the file documents. This includes opcodes the file claimed from another subsystem.
- **verifier errors**: errors from the verifier pass, all fixed in the file.

| subsystem | inv | doc | high | med | low | verified | flows | rules | verifier errors |
|---|---|---|---|---|---|---|---|---|---|
| session | 15 | 15 | 12 | 3 | 0 | 15 | 14 | 17 | **7** (all applied, `verifier_note` on each) |
| world | 24 | 26 | 16 | 9 | 1 | 21 | 12 | 13 | **at least 8** (applied; the verdict passed to this review was cut off after 8) |
| combat | 17 | 17 | 10 | 6 | 1 | 15 | 15 | 17 | no verdict supplied, plus 1 error found by this review (revive) |
| items | 38 | 41 | 20 | 18 | 3 | 37 | 24 | 15 | no verdict supplied |
| pvp | 37 | 37 | 12 | 23 | 2 | 31 | 9 | 13 | no verdict supplied |
| quests | 16 | 16 | 14 | 2 | 0 | 16 | 12 | 12 | no verdict supplied |
| social | 49 | 49 | 26 | 21 | 2 | 36 | 14 | 13 | no verdict supplied, plus 2 errors found by this review (0x498, 0x469) |
| system | 10 | 10 | 6 | 4 | 0 | 10 | 9 | 11 | no verdict supplied |
| **total** | **206** | **211 entries / 206 distinct** | 116 | 86 | 9 | 181 | 109 | 111 | |

Opcodes still marked `low`:

- **items:** 0x433, 0x434, 0x498 (auction)
- **pvp:** 0x44a, 0x476
- **social:** 0x4bc, 0x4be
- **combat:** 0x4b6
- **world:** 0x48c

### Is the inventory itself complete?

For this review the inventory was checked against three independent sources:

- **`out/opcodes.tsv`:** every opcode in it is in the inventory.
- **The dispatcher `FUN_0047a36c`:** every `case` label is in the inventory.
- **Every C->S header in `disasm.txt`:** this covers both forms, the builder (`push <op>` before `call 0x4a730b`) and the inline `,0xa53c` header with its opcode store. All are in the inventory.

The only inline `0xa53c` sites with no opcode are framework code: the magic check in the dispatcher (0x47a386), the builder (0x4a7330) and the send path (0x4a7604, 0x4a7c48).

## Uncovered opcodes

**None.** Every one of the 206 inventory opcodes has an entry in at least one contract file, and no file documents an opcode that the inventory lacks.

### Opcodes documented in two files

| opcode | files | layouts | verdict |
|---|---|---|---|
| 0x415 | world (`scene_object_state_change`), quests (same) | Identical offsets: C->S +0x10 map id, +0x14..+0x17 table entry; S->C +0x14 id, +0x16 state | No conflict. **world.yaml is the owner.** It has the verifier-added second sender `FUN_0056e3d8` (any state, no 0x451). quests.yaml has the same fact in its flow. |
| 0x47b | pvp (`set_my_mapfort`), world (`set_mapfort`) | Identical: +0x10 i8 mapfort, +0x18 u32 sceneidx | No conflict. world claims it. Keep sceneidx at 0x7FFF or below (rule `sceneidx_allocation`). |
| 0x4b7 | items, system | Identical: C->S 0x18, 8 zero bytes | No conflict. items owns it (`misassigned_opcodes`). system.yaml keeps the 0x4b8 detail. |
| 0x4c1 | items, system | Same offsets. **Types differ:** amount is `u32` in items, `i32` in system. The value notes also differ: the client clamps to the balance and to 2,000,000,000; 0 is never sent. | Minor. Treat it as u32 and reject 0 or a value above the balance. items owns it. |
| **0x498** | items (`auction_cancel`), social (`auction_buy`) | Same offsets (+0x18 u64 listing, +0x20 u64 char id, +0x28 u16, +0x2a u16, +0x2c u32) | **Conflict of meaning, resolved: it is CANCEL.** `FUN_0053a7c2` sends it on msgbox 0x45 OK. Msgbox 0x45 is opened at 0x53a29f with string 0x73ddc0 `GUI_Auction_Msg_CancelItem`, after the `CancelItem` button (string 0x73dbb0). **social.yaml is wrong**, and so is the inventory name ("mail/item list action"). |

Two other inconsistencies:

- **0x469** (social): `direction: c2s`, but the entry has an `s2c` block, the inventory says `both`, and the handler is `FUN_00471530`. The direction should be `both`.
- **Death and revive** (combat vs system): see the first gap under [Flow coverage](#flow-coverage).

## Flow coverage

The steps a playable server needs, in play order. Values in **Covered**:

- **yes**: there is a flow with exact packets.
- **partial**: packets are known, but a server decision or some data is missing.
- **live**: the step already works in `../server`.

| # | step | packets | covered | where | gap |
|---|---|---|---|---|---|
| 1 | Pre-login world and channel status (web) | `WorldChannel.asp`, `ChannelList.asp` | partial (live) | session `login_production_path`, `web_endpoints` | An empty 200 body works. A full WorldChannel row stopped the TCP login in the stub; the row shape is unverified. |
| 2 | Login server: token login | 0x4207 -> 0x4201 | yes (live) | session | none |
| 3 | Duplicate session / errors | 0x4201 results 3..10, 0x4202 | yes | session `login_error_and_duplicate_session` | The 0x4202 reply is inferred. |
| 4 | Game server login -> character list | 0x4200 -> 0x2001 | yes (live) | session | none |
| 5 | Create, delete, buy slot | 0x407/0x2003, 0x408/0x2004, 0x499 | yes | session, system `character-create error` | A refused delete cannot be redrawn by 0x2001 (session `delete_rules`); the alternative is untested. |
| 6 | Select -> enter world burst | 0x406 -> 0x2000, 0x41f, 0x427, 0x2009, 0x452, 0x490 ... | yes (live) | world `enter_world`, combat/items/quests enter-world flows | none |
| 7 | See NPCs, monsters, other players (AOI) | 0x803/0x805/0x804, 0x806/0x43e/0x43f, 0x4ca | partial (live for monsters) | world `movement_relay`, `unknown_attacker`, rules `area_of_interest`, `npc_placement` | **No NPC position data exists in the client tables.** `npc_placement` cites "Npc*/Unit* tables" that are not in `data/tables`. NPC spawn lists must be written by hand. |
| 8 | Movement and resync | 0x416 (types 0/1/2/0x20), 0x417 | yes (live) | world | Never send 0x416 for a corpse (it revives the unit) or blank types for the own uid. |
| 9 | Chat | 0x800 | yes | social `chat` | No echo to the sender. |
| 10 | NPC services: shop, buyback, warehouse | 0x44b, 0x430/0x431, 0x4b7-0x4b9, 0x42a, 0x4c1/0x4c2, 0x452 | yes | items | The 0x452 rate value (100/100) is assumed. |
| 11 | Teleporter NPC, portals, world-map warp | 0x44e/0x44c/0x44f, 0x445/0x446, 0x48c, 0x47a | partial | world `npc_teleport`, `map_portal`, `worldmap_warp` | Portal link ids -> destinations need map trigger data that has not been recovered (rule `portal_links`). The 0x446 reply is required, or auto-travel stalls. |
| 12 | PvE combat, skills, buffs | 0x40f-0x413, 0x41e/0x41f/0x420 | yes (live) | combat | Damage numbers are server-invented (`damage_formula`). |
| 13 | Monster death, loot, exp, level-up | 0x411 lethal bit, 0x420, 0x427/0x428, 0x422, 0x804 | yes (live) | combat, items `loot_pickup`, world `monster_death_and_respawn` | none |
| 14 | Player death -> revive (open world) | 0x420/0x421 HP 0 -> **C->S 0x41a** -> 0x421 + 0x416 type 1 / 0x804 | yes, **conflict** | system `death -> revive`, combat `player_death_and_revive` | **combat.yaml says the client "sends NOTHING" after death; that is wrong.** `FUN_0048d666` opens msgbox 5 `WaitingRevive` (string 0x72a124, push 5 at 0x48e2d7) when the countdown ends. `FUN_0048cd72` sends 0x41a (+0x10 = 1) for msgbox 5 on button 1, button 3 or timeout 32000. The revive delay is 0x41f +0x50 (char +0x483), which is the stat block's +0x40. So both files agree on the value and differ only in how they count. Use system's flow and keep the timer revive as a fallback. |
| 15 | Items: equip, use, split, destroy | 0x42a, 0x42d, 0x432, 0x42c, 0x427 | yes (equip live) | items | none |
| 16 | Quests | 0x48e/0x48f/0x491/0x492 | yes | quests | Quest 1 is offered only on maps 89/93/97; the live spawn map 117 shows no quests (`tutorial_map_mismatch`). |
| 17 | Party (for team play) | 0x4ac/0x4ad | yes | social | none |
| 18 | PvP: match offer and queue | 0x470 (state 0 -> action 1 -> state 1), team 0x471/0x472 | yes | pvp | The Match button stays hidden until 0x470 state 0 is pushed. |
| 19 | PvP: warp to arena + roster | 0x44f (map 140/141, new sceneidx), 0x803 (+0x42 team), 0x43c, 0x43b state 3 | partial | pvp `queued match`, `custom game room` | **Arena coordinates are unknown** (`arena_location`; map.jpk encrypted). Plan: reuse a known-good area under its own sceneidx. Custom rooms must re-send 0x43c after the warp. |
| 20 | PvP: in-match combat | 0x411/0x412 player -> player, ally/enemy from char +0x659 battle side | partial | combat `friend_or_foe`, pvp loop (0x4b5/0x443/0x439/0x4c6/0x43a) | **No flow for player-hits-player, and no rule for death and respawn inside a match.** combat `death_and_respawn` defers to "match rules per match subsystem", and pvp.yaml has none. A respawn delay and point per side must be decided. |
| 21 | PvP: score, result, return | 0x43a, 0x440, C->S 0x442, 0x44f back, 0x470 state 0 | yes | pvp | Scoring and rewards are invented (`match_duration_and_win`, `match_rewards`). The 0x43a state values are only partly known. |
| 22 | Channel move | 0x40a -> reconnect 0x4200 -> 0x2000 | yes | session `channel_move` | The server-initiated newbie move (0x41d 0xe3) may never reconnect (verifier RISK); test it live. |
| 23 | Back to character select | 0x409 mode 0 -> 0x2001 on the same socket | yes | session | The key is not reset: keep de-obfuscating with header +0x0c. 4.95 s countdown before the send. |
| 24 | Exit game | 0x409 mode 1, then the client quits | yes | session `exit_game` | The server saves on 0x409 or on socket close. |
| 25 | Keepalive and disconnect | 0x401 every 240 s | yes (live) | session | The server sets the drop timeout (600 s suggested). |
| 26 | Social web lists (friends, mail, guild) | `FriendList.asp` ... (12 pages) | yes | social `web_endpoints` | Optional: empty `<ROOT/>` is accepted. |
| — | Persistence of characters, items, quests | none (server-only) | n/a | | Not part of the wire contract. Every flow assumes the server keeps state per character. |

Optional systems with flows but not needed for the core loop:

- crafting, reinforcement, runes, gacha and cash mall
- guild warehouse, stock and donation
- mail
- forts and nation war
- nation vote
- dungeons
- achievements
- the GM tool

Auction has **no S->C path** that fills its lists (items `auction (incomplete)`), so it cannot work with this client as understood today.

## Server-only decisions, prioritised

All 111 `server_rules` from the eight files.

| priority | count | meaning |
|---|---|---|
| **P0** | 34 | The client crashes, soft-locks or never gets past the step without it. |
| **P1** | 40 | The core login -> PvE -> PvP -> logout loop is wrong or unfair without it. |
| **P2** | 34 | Secondary systems. |
| **P3** | 3 | Bookkeeping. |

Defaults are the files' suggestions, shortened. "Invented" defaults mean nothing in the client or data supports a value.

### P0: must hold for the client to work

| subsystem | rule | suggested default | informed by |
|---|---|---|---|
| session | authentication | Accept 0x4207 (token or anonymous dev login). Issue a random ticket A/B bound to the account. Authenticate 0x4200 by (account, ticket A, ticket B). Reject with 0x4201 result 3. | accounts server-side |
| session | version_check | Accept only 0x41e (1054); otherwise 0x4201 result 8. | |
| session | channel_assignment | 0x4201 +0x14 = index 0 into the client's serverlist.sof channels; one listener per gsN entry. | serverlist.sof |
| session | login_socket_close | The login server must not close the socket after 0x4201; the client closes it. Drop idle login sockets after 60 s. | live stub |
| session | session_tag | 0x2001 `extra` = the future player uid. Check it on 0x406/0x407/0x408/0x499/0x200f. | |
| session | player_uid_and_key | uid 1..0x3F6, unique per scene. De-obfuscate C->S with key = header +0x0c, even after going back to character select. | |
| session | character_ids | u64 global autoincrement. Never 0 or all-ones (those mean empty and locked). | |
| session | slots | Exactly 5 records in 0x2001. Locked = id -1, empty = id 0 plus delete time (reusable after 86400 s). | |
| session | character_creation_rules | Re-validate the name (1..16 alnum, unique), class, starting weapon (Create_Char) and nation. Fill level 1 with stats from UnitDB / Level_Table. | Create_Char, UnitDB, Level_Table |
| session | leave_to_character_select | Answer 0x409 mode 0 with 0x2001 within 3 s on the same socket. Despawn (0x806) and save first. | |
| session | clocks | Unix seconds in 0x2001 +0xb80 and 0x2000 +0x6f8. Header tick = server monotonic ms. | |
| session | heartbeat_timeout | The client pings only every 240 s. Drop after 600 s of silence. | |
| world | spawn_point_and_terrain | Every 0x2000/0x44e/0x44f x/z must lie on an existing terrain piece with navmesh, never (0,0). Otherwise the client loops reloading at 1 Hz. | map.jpk, tools/navmesh.py |
| world | sceneidx_allocation | One sceneidx per (map, channel, instance), range 0..0x7FFF. The same sceneidx means an in-place warp, a different one a full reload. | |
| world | uid_allocation | Players 1..0x3F6, monsters and NPCs 0x3F7..0x2B05, per scene. Reuse a uid only after 0x806 mode 2/6. | |
| world | area_of_interest | Spawn (0x803/0x805) before any 0x416 for a unit. View radius about 200 units with hysteresis, plus the 0x417 camera point. | |
| world | npc_placement | The client never places NPCs; spawn every NPC with 0x803/0x805. **Positions must be written by hand** (no table found). | UnitDB |
| world | move_validation | Accept positions within speed x elapsed x 1.5 + 3. Otherwise send a 0x416 type 1 correction to the sender only. | navmesh |
| world | monster_move_speed | Speed travels only in 0x41f/0x804/0x416/0x43f (0x803 has none): monsters 300, players 450. | |
| combat | hit_authority_and_validation | The client reports hits with damage 0; the server decides. Check: attacker == sender and alive, skill in the equipped weapons, target alive and hostile, range plus 3 units, max targets. | Skill_Base, WeaponBase |
| combat | lethal_bit_and_hp_tracking | Track HP/MP for every unit. Set the lethal bit only when HP reaches 0. Always fill the attacker's real HP/MP (0 kills the attacker on screen). | |
| combat | stat_derivation | Every stat comes from the server's 0x41f: base(class, level) + items + sets + buffs. Resend after equip, level-up or buff. | Level_Table, Item_Base, ItemOption |
| combat | death_and_respawn | Revive delay 5 s; revive with 0x421 + 0x416 type 1 at the town spawn. Monsters respawn after 30 s via 0x804. **The match variant is missing.** | |
| system | revive policy | On C->S 0x41a from a dead player, revive at the map's respawn point. Keep the timer revive as a fallback and never revive twice. | ZoneDB |
| combat | friend_or_foe | The same non-zero battle side (char +0x659) means ally, else the same nation means ally. Monsters of nation 0 are hostile. Status bit 0x400 = untargetable. | |
| pvp | match_offer_schedule | Push 0x470 state 0, kind 1, lifetime 86400 after login, after every match and after every cancel. Without it the Match button is hidden. | |
| pvp | matchmaking | No accept round trip. Start at 2 queued players (1 for testing). Type 2 for nation teams, 7 for mixed teams with ids 1/2. | Level_Table |
| pvp | arena_location | Map 140/141 with a fresh sceneidx and x/z on loaded terrain. Until arena coordinates are recovered, reuse a known-good area. | SceneList, ZoneDB |
| pvp | match_duration_and_win | 600 s; TP per kill 100, per tower 1000; first to 10000 or most TP wins (invented). The winner is shown only in 0x440. | Skill_TP |
| items | item_record_and_ids | Store the 16-byte item16 record verbatim. Code 0 = empty. Stack cap 99. Never send count 0 for a stackable item. | Item_Base, ItemKind |
| items | authoritative_echo_vs_local_changes | Sort, 0x42d decrement, reinforce materials and 0x4b1 are applied by the client before any reply. After a refusal, resend 0x427/0x428 to undo them. | |
| system | which system message to send | 0x41b for plain errors, 0x41c with %d/%s, 0x41d only for display-3 prompts. An unknown id shows nothing. | system_msg.tsv |
| system | confirm-prompt state | Keep a pending {id: cookie, expiry 60 s} per player. Accept a 0x41d answer only when it matches. | |
| system | GM authority | Check gm_level server-side on every 0x495. Never send char +0x656 >= 200 to normal players. | |

### P1: needed for a correct core loop

| subsystem | rule | suggested default |
|---|---|---|
| session | duplicate_login | Answer 7 when the account is already online. On 0x4202, kick the old session (sysmsg 118) and answer 0. |
| session | delete_rules | Refuse if the character is in or owns a guild. On success, stamp the delete time. To undo a client-side wipe, try a 0x407 echo (untested). |
| session | channel_move_tickets | Key byte (not 0xff) + ticket, single use, valid 30 s. Refuse during combat or a match with a sysmsg id in +0x24. |
| session | web_endpoints | HTTP POST to `/JoyImpact/<Page>.asp`, 200, XML. Serve empty bodies unless a feature needs rows. |
| session | world_and_channel_state | Use the empty WorldChannel reply (known to work) until a full row is verified live. |
| world | teleport_destinations_and_costs | Destinations per NPC from Teleport_List. Cost 0 until there is an economy. Destination id = map id. |
| world | portal_links | Table of link id -> (mapid, x, z). **Data not recovered yet** (map.jpk trigger params). |
| world | world_map_state | Answer every 0x445/0x449 poll (0x446/0x44a) with neutral bases, or the panel and auto-travel wait. |
| world | scene_objects | Gadget states 0..2 all zero until capture points exist. |
| world | channel_list | A single channel 0. |
| combat | damage_formula | `max(1, atk x coeff x 100 / (100 + max(0, armor - pen))) x rand(0.9..1.1)`, with crit and evade rolls (invented). |
| combat | skill_costs_and_cooldowns | Deduct the cost once per cast. Enforce cooldown x 0.9. Drop early casts silently. Report MP in +0x30 and 0x420. |
| combat | heal_and_mana_effects | Heals only through 0x411 (0x412 applies none). Heal = effect value x (1 + magic / 1000). |
| combat | buffs_and_status | Full 0x41e table on every change and on expiry. CC effects map to status bits (stun bit 5, silence bit 13, disarm bit 10). Resend 0x41f when a buff changes stats. |
| combat | absorb_shields | Shields go in buff slot 0 only. Mirror the client's absorb arithmetic. |
| combat | knockback_clamping | Destinations within range + 2 of the start, snapped to navmesh, never coordinates <= 0. |
| combat | exp_rewards_and_levels | Kill exp = 10 + 5 x monster level, scaled by the level gap (invented). On level-up send 0x422 {lvl, 1, exp} + 0x41f + 0x421. Cap at level 30. |
| combat | item_skill_map | Item -> skill from Item_Base option 301/340. Reject otherwise. |
| combat | tp_economy | TP from kills and captures. 0x4b4 buys, 0x4b6 uses with the Skill_TP cooldown. |
| combat | capture_channel | 5 ticks of 0x450 action 10. Damage or movement cancels (action 11). Completion is action 1 broadcast. |
| items | move_validation | Only kind-compatible moves (container 3 = kind 31, 4 = 32, 5 = 18, 2 = 50..57). Merge equal stacks. Set the bind flag. |
| items | capacity | Bag and warehouse start at 2 rows each. Expansion only to current + 1, maximum 14 / 18 rows. |
| items | price_formula | Send 0x452 {100, 100, 0} after entering the world and charge with the client's formula (rates are percent). |
| items | shop_stock | Validate 0x430 against Npc_Carry[UnitDB +0xa2]. |
| items | gold_and_currency_limits | Cap at 2,000,000,000. Always send totals (0x428/0x4c2), never deltas. |
| items | item_effects_and_cooldowns | Potions, scrolls, exp and random boxes. Enforce the option 0x105/0x106 cooldown on the server. |
| system | when to offer a move-map prompt (0x41d id 0x1a) | On entering a map-exit region: cookie = destination map id. On OK, warp with 0x44e/0x44f. |
| system | create-scene errors | 0x2003 {18} for a duplicate name, {19} when slots are full. |
| quests | quest ids, bits and availability | Persist 15 slots, 320 flag bits, daily points and the periodic mask. Re-check prerequisite and exclusion bits on accept. |
| quests | objective stages | Mirror the flag1..5 active window when accepting 0x492 and when counting kills. |
| quests | objective types the server must detect | Implement 1 (kill/collect), 4/5 (via 0x492) and 7 (level). Auto-complete unknown types so quest chains do not stall. |
| quests | client-detected objectives | Trust 10001..10012 reports after validating the slot, quest and objective index. |
| quests | quest rewards | Type 2 exp, 4 gold, 1/8 items into free slots. Ignore unknown types. |
| quests | tutorial map mismatch | Spawn new characters on map 89/93/97 by nation, or accept that quests are invisible on 117. |
| pvp | match_rewards | Win: gold medal, fame 100, money 1000. Lose: bronze medal, fame 20, money 200 (invented). |
| pvp | kill_points | Killer 10, assist 5 (0x443). |
| pvp | custom_room_rules | Room id is a counter, max 30 players, cost 0. If the host leaves, the next member becomes host. |
| social | social lists live behind the web endpoint | Serve the 12 `.asp` pages from the same store as the TCP server. Empty `<ROOT/>` when there is nothing. |
| social | chat routing and range | Never echo to the sender. Type 1 = scene or about 40 m, 3 = match, 6 = channel. 1 line per 0.5 s, 254 bytes. |
| social | party rules | Up to 5 members. Party id = the leader's uid. Disband at 1 member. |

### P2: secondary systems

| subsystem | rule | suggested default (short) |
|---|---|---|
| combat | mastery | Not on the wire; fold any bonuses into 0x41f. |
| combat | summon_control | Summons have category 0x0b and owner = the player's uid. 0x4ba move or attack. |
| items | buyback | Last 16 sold items per character, at the buy price. |
| items | jewels | Yellow (code 8) and Purple (code 7). Code 0xd spends Yellow first (assumed). |
| items | craft_reinforce_rune_odds | Table success % (100 if absent). A failed reinforce keeps the item. |
| items | gacha_odds | Grade weights 70/25/5, free draw every 12 h (invented). |
| items | decomposition | Return 1-3 materials of the item's tier and charge the client's point cost. |
| items | auction | Ignore 0x433/0x434/0x498: no list channel exists. |
| system | notice broadcast | GM notice as 0x800 chat type 7 (low confidence). |
| system | GM command semantics | Implement search / goto / summon / recall / kick / mapmove / kill / setHP / notice. Log the rest. |
| system | GM toggle state display | Buffs 912/913 on the GM for Snoop / NoDamage. |
| system | /time chat command | Answer `/time` (0x800 type 1) with a 0x800 system line, or ignore it. |
| world | change_nation_policy | Free change while the account nation is 0; otherwise a fee or cooldown. |
| quests | quest board / notice quests | Daily, weekly and monthly resets; point rewards from NoticeQuestReward. |
| quests | achievement counters | Start with gold, monsters, bosses and deathblows. 0x489 on each grade crossing. |
| quests | titles | Achievement Time = unix time of the last grade. |
| quests | fame and fame rank | Send fame through 0x4a2 +0x1c; rank bands from Level_Table. |
| quests | Lords of the Land rewards | 1 pending reward per winning-nation player after a war. |
| quests | currencies | Two balances per account: Yellow (0x488/0x4a4) and cash (0x200f). |
| pvp | field_and_fort_ownership | Each nation owns its home fields; forts start unowned. |
| pvp | war_schedule_and_state_values | All 0 (peace) until the enumerations are recovered. |
| pvp | fort_economy | Tax 5% of shop sales; donations 1:1 (invented). |
| pvp | nation_vote | Weekly vote between the top 3 guild masters by fame; one vote per account. |
| pvp | dungeon_entry | Deduct tickets again on the server. Party of at most 4. Warp to the default spawn. |
| social | block list is client-side only | Also refuse whispers and invites from blocked players on the server. |
| social | guild grades and permissions | Grades 0..4: master 0xFFFF, sub-master all except 0x80, at most 3 sub-masters. |
| social | guild level, member cap and level-up cost | Level_Table_Guild as-is. |
| social | guild creation cost and name rules | 100,000 gold, 2..16 characters, unique (invented). |
| social | guild mastery | Unimplemented: **no buy packet found**. Check whether 0x4a6 (fort mastery) covers it. |
| social | ether price and dividend | Ether 1,000 gold; weekly dividend over 2,000,000 (invented). |
| social | donation | 200,000 gold or 100 jewels per day; weekly reset. |
| social | mail rules | 5% tax + 100 per item; expiry 30 days, then return to sender. |
| social | open-mail state for 0x80d/0x80e | Both arrive empty; act on the last 0x80c mail id per session. |
| social | guild member session ids | 0x45d on every member login and logout (it is the kick and summon target). |

### P3: bookkeeping

| subsystem | rule | note |
|---|---|---|
| items | misassigned_opcodes | 0x4b7, 0x4c1 and 0x498 belong to items. Several inventory names are wrong (0x434 is buy, 0x4b9 is buyback, 0x493 is decompose, ...). |
| pvp | misassignment_notes | 0x47e is the vote cast, not dungeon entry. 0x47c is the vote block, 0x4c6 the minimap markers, 0x48d the field-war scoreboard. |
| system | unused or never-sent opcodes | 0x404 is never sent by this build; the BattleArenaInvite prompt has no opener. |

## Open items, in order

1. **combat.yaml:** fix `player_death_and_revive` and `death_and_respawn`. The client does send C->S 0x41a (see flow step 14).
2. **social.yaml:** rename 0x498 to `auction_cancel` (or drop it, since items owns it). Set 0x469 `direction: both`.
3. **pvp.yaml:**
   - Add a match death/respawn rule (delay, point per side, TP effects).
   - Add an explicit player-vs-player hit flow.
4. **Data recovery:**
   - NPC spawn positions per map (none in client data).
   - Portal link table and arena coordinates (map.jpk trigger and terrain data).
5. **Live tests still owed:**
   - the 0x41d 0xe3 newbie channel move
   - the 0x407 echo to restore a refused delete
   - the 0x2001 character-select key carry-over after 0x409
   - a full WorldChannel.asp row
   - the 0x4202 and 0x409 mode 0 replies
6. **Schema:** harmonise the `server_rules` key names across files (`client_expects`/`expects`, `data_table`/`informed_by`/`data`, `suggested_default`/`default`).
