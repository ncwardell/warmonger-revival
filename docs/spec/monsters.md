# Monsters: UnitDB format, tutorial monsters, spawn/combat/respawn packets

Builds on world.md (spawn packets) and combat.md (hits). Offsets are from packet start (payload at
+0x10). Server code: `WarmongerRevamp/server/world.py`. Decoded table: `data/tables/UnitDB.tsv`.

## 1. Setting/UnitDB.cdb (CUnitDB, `DAT_0084e864`)

Not encrypted once extracted: CP949 **NUL-separated text**, like Skill_Base/Quest.

- Header (`FUN_00499340`): two tokens, `512` = row count (→ `db+0x40`), `57` = a column count
  (→ `db+0x44`, unused by the loader). The loader reads **55 fields per row**. Rows land in a
  0x154-byte struct array; `FUN_00499180(id)` looks rows up by id.
- Row parser `FUN_00499b74`. Fields are `atoi`/`atof`'d (empty field = 0). Column order → record
  offset (high confidence for the offsets, which are read straight from the loader; meanings are
  marked):

| col | off | type | meaning |
|---|---|---|---|
| 1 | +0x00 | i32 | **unit id**: the value 0x803 +0x10 / 0x805 +0x1e / player class need (high) |
| 2 | +0x04 | str | **name key** `UnitName_<n>`, localised into the std::string at +0x08 (StringAll_Eng) (high) |
| 3 | +0x40 | str | second key (empty for every monster) |
| 4, 5 | +0x80, +0x84 | i32 | ? (minions: 10020) |
| 6 | +0x7c | i32 | **unit class mask**, matched by skill +0x12: 1 monster, 2 NPC, 4 player, 8 structure/bot, 0x20 = untargetable (FUN_0058786d skips it), 64 = misc (high for 0x20, medium for the rest) |
| 7 | +0x8a | u8 | **category** (unit+0x35c when 0x803 +0x13 is 0): 1 monster, 5 player, 4/50/9 NPC kinds (medium) |
| 8-10 | +0x8c, +0x8d, +0x8e | u8 | ? (+0x8c 'Z' tested with category 0x28; the loader moves a +0x8c value > 100 to +0x8f as v-100 and zeroes +0x8c) |
| 11 | +0xa2 | u16 | ? |
| 12 | +0x8b | u8 | player class number (1/4/5/7) |
| 13 | +0x88 | u16 | ? (Nexus 0x6000) |
| 14 | +0xa4 | f32 | **model scale** (Great Slime 2.0, Slime 1.0, Mini Golem 0.4) (medium-high) |
| 15 | +0xa8 | f32 | second scale / radius (0.8..1) |
| 16 | +0x91 | u8 | ? (15 nearly everywhere) |
| 17 | +0xac | i16 | **model / default part id** (all slimes 12; Bee 57, Cobra 58) (medium) |
| 18-22 | +0xae..+0xb6 | i16 | further parts (weapons for NPC/bot models) |
| 23, 24 | +0xb8, +0xbc | u32 | ? |
| 25 | +0xc0 | f32 | 1.7..7 (nameplate height or collision radius; low) |
| 26, 27 | +0x110, +0x114 | str | ? ("0" is turned into "") |
| 28 | +0x150 | i32 | ? |
| 29-33 | +0xc6, +0xc8, +0xc9, +0xca, +0xc7 | u8 | appearance bytes = parts of the words at +0xc4/+0xc8 that the 0x803 monster path copies to rec+0x23b/+0x23f (NPC faces/hair; 0 for monsters) |
| 34 | +0x92 | u8 | ? |
| 35-37 | +0x93, +0x98, +0x9d | 5 × u8 | comma lists ("0,0,0,4,91") |
| 38-51 | +0xcc + 8k, +0xd0 + 8k (k = 0..6) | 2 × i32 | 7 pairs {a, **skill id**}: the unit's skills (Skill_Base ids 40700xx for monsters, 4040001.. basic attacks for players) |
| 52 | +0x104 | i32 | ? |
| 53 | +0x90 | u8 | ? |
| 54 | +0x108 | i32 | ? |
| 55 | +0x10c | f32 | ? (1; Slime 3) |

**No HP, level, damage, exp or drop columns exist**: those were server data. The server chooses them.

Name lookup: `StringAll_Eng.cdb` is `count\0 x\0` then entries `key\0 <UTF-16LE text>\0\0 flag\0`.
The TSV's `name` column resolves `UnitName_<n>`; 392 of 512 rows have English names.

## 2. Tutorial monsters chosen

The tutorial's quests name them: Quest.cdb row 2 "The Slime is mine" (quest 631: kill/collect 3 ×
unit **604**, item 2550 Slime Mucus), quest 632 (5 × **732**, item 2551), a Bee quest (5 × **731**,
item 2552); tutorial speech: "hunting snakes, slimes and bees". Quest giver unit **201** (Shaia).

| unit id | name | class mask | category | scale | model | level (ours) | HP (ours) | count |
|---|---|---|---|---|---|---|---|---|
| 604 | Slime | 1 | 1 | 1.0 | 12 | 1 | 80 | 3 |
| 732 | Cobra | 1 | 1 | 1.3 | 58 | 2 | 120 | 2 |
| 731 | Bee | 1 | 1 | 1.3 | 57 | 3 | 150 | 2 |
| 605 | Great Slime | 1 | 1 | 2.0 | 12 | 4 | 400 | 1 |
| 201 | Shaia (NPC) | 2 | 50 | 3.0 | 275 | 10 | 1000 | 1 |

Other tutorial-flavoured rows: 606-608 Guardian/Punisher/Saint Bot-t (bots used by Npc_Carry),
220/222/223 Training Assistant, 221 Training Officer (Bell Thain).

Placement: offsets 10-22 units from the tutorial zone centre (1424, 416); `world.CENTRE` and the
`MONSTERS` table hold them. map.jpk has no spawn/regen files (only fog/minimap/navmesh/.zp terrain),
so positions are ours.

## 3. Team: monsters must be team >= 4

`FUN_004872bd(me, target)` → `FUN_00486179` decides hostility from the **target's** rec+0x655
(when either battle side +0x659 is 0):

- target team 0 → relation 2, **not hostile** (a team-0 monster can't be attacked: the
  unit-target gate `FUN_0058786d` drops it and the client never sends 0x411);
- target team 1..3 and own team 0 → not hostile; both 1..3 → hostile iff different;
- target team >= 4 (signed, < 0x80) → relation 8, **hostile to everyone**.

So `MONSTER_TEAM = 4`, NPCs team 0. world.md's "0 = neutral/attackable by all" is wrong for
attacks. Also: status flag 0x400 (+0x64d) and class mask 0x20 make a unit untargetable; the attacker
needs HP > 0. Confidence high (decompiled logic read directly).

## 4. Packets world.py sends

All extra = the unit's uid, key 0. Monsters uid 0x400.., NPC 0x3F8.

| when | op | size | fields |
|---|---|---|---|
| enter world | 0x803 | 0x1c0 | +0x10 unit id, +0x12 level, +0x13 0, +0x14/+0x18 x/z, +0x20 HP, +0x24 max HP, +0x28/+0x2c MP 0, +0x32 heading, +0x33 spawnFx 0, +0x34 team |
| enter world, after each 0x803 | 0x804 | 0xbc | +0x10/+0x14 x/z, +0x19 team, +0x23 level, +0x28 HP, +0x2c MP, +0x30 max HP, +0x34 max MP, +0x5e speed 300 (0x803 carries no speed) |
| C->S 0x411 | 0x411 | 0x64 | the client's packet with +0x36+4i damage, +0x18 \|= 0x4 on a crit, +0x1a lethal mask, +0x2c/+0x30 player HP/MP |
| C->S 0x412 | 0x412 | 0x88 | same, 7 targets; +0x50/+0x6c push positions echoed and stored |
| a hit kills | 0x420 | 0x18 | +0x10 HP 0, +0x14 MP 0 (`CONFIRM_DEATH`; the lethal bit alone already kills) |
| respawn due | 0x804 | 0xbc | as above at the home position with HP = max: revives the corpse (`FUN_004890cb`) |
| C->S 0x4ca {+0x10 u32 uid} | 0x803 + 0x804, or 0x806 mode 2 | | a dead unit is re-sent as 0x803 + 0x420 HP 0 |
| C->S 0x40f / 0x410 | nothing | | they go to other observers only |

0x805 (0x38 bytes) is built by `spawn_compact()` but not used.

Damage: basic attack 30, skill 45, × 0.75..1.25, 10 % crit × 2 (flag 0x4); NPCs, unknown and dead
units get 0. A Slime takes about 3 basic hits.

Respawn without a timer: a death stores `dead_until = now + 10 s`. Every reply world.py makes, plus
whatever handlers.py appends through `due_respawns()` (0x416 movement arrives every 0.5 s while the
player moves), carries the 0x804 of each monster whose time has passed. The corpse lies until then.

Death ordering: 0x420 HP 0 is applied at once, while the lethal 0x411 hit plays at the swing's impact
frame. So with `CONFIRM_DEATH` the death animation may start a moment before the damage number.
`FUN_00488565` checks the alive flags, so the death never plays twice.

## 5. Uncertain

- No server-side monster stats survive. Levels, HP and damage are invented.
- Speed 300 for monsters is a guess; nothing moves them yet (no AI, no 0x43f push).
- The heading convention isn't checked; all units face heading 0.
- Whether the Slime/Bee/Cobra models have an "appear" action (spawnFx is left at 0).
- Whether the client wants the 0x420 death confirmation or just the lethal bit.
- Positions are offsets from the zone centre and not checked against the navmesh. A unit placed
  off the terrain is still created, but its Y comes from the terrain lookup.

## 6. Basic attack (auto-attack): why it did nothing, and the fix

**What the live log really showed** (play machine, 04 Oct 23:22-23:39): 39 C->S 0x411 and 10 0x412,
every one a **weapon skill** — 0x139e 5022 Blade storm (AoE around self: target list empty or
{0x403..}), **0x139f 5023 Wings of fair wind** (Skill_Base col 8 relation = 1 self, col 9 target
type = 3 self, so target[0] = the caster, uid 1 — correct, it is a self buff), 0x13a0 5024 (0x412
dash), 0x13a1 5025. **Not one skill-0 0x411 was sent.** The "auto-attack packet that lists only
uid 1" was 5023. The basic attack never reached its impact frame, so the client never reported it.

**Cause: basic-attack range 0.** `FUN_00587abf` (the gate for every command) takes the range for a
command of type 1 (basic attack) from `FUN_0058641a`: online, with no hero transform
(me+0x418 == 0), range = **(s16) char+0x461 × 0.01** = stat block **+0x1e** (0x41f +0x2e, 0x804
+0x46). Offline it is 2.0 (`_DAT_00722c18`), or Item_Base option type 4 × 0.01; status flag 0x2000
forces 1.5. Then `FUN_004bb979(target, range)`: in range iff distance < target radius + range.
handlers.stat_block() fills only HP/MP/maxes/speed, so the range was 0: the avatar walks up to the
monster but is never close enough, never swings, never sends 0x411. Skills carry their own range
(Skill_Base +0x41), which is why they work. The target/hostility gate (`FUN_0058786d`, team 4) was
already satisfied — 5024 hits the same monsters by unit target. Confidence high (code read
directly; matches the log).

Fix (world.py, no handlers.py change needed): `spawn_all()` now starts with its own
**0x41f** (`player_stats()`): HP/MP/maxes and speed as handlers sends them, plus
- block +0x1c (0x41f +0x2c) s16 attack speed = 500 (×0.002 = 1.0; `FUN_004b8b5f` clamps players to
  200..1000, used for the swing timing),
- block +0x1e (0x41f +0x2e) s16 **basic-attack range = 200** (2.0 units); 700 for guns, bows,
  wands and the cannon (a guess),
- block +0x40 (0x41f +0x50) s16 revive delay = 5 s (the client's death countdown).
Monster 0x804 also carries attack speed 500 / range 200 at +0x44/+0x46. Basic hits arrive as
0x411 skill 0 and `world.hit()` already handles them (BASIC_DAMAGE 30). Not handled: a weapon
swap (0x42a) does not resend the range.

**C->S 0x417 is the camera, not combat.** Sender object `DAT_0084a7b0` (camera; +0x30 the D3D
camera, +0x114..+0x120 map bounds clamp, `D3DXVec3Normalize`). 0x1c bytes, extra = player uid:
+0x10 f32 x, +0x14 f32 z, +0x18 u8 1 = camera detached (free camera) — all zero when it reattaches.
`FUN_00450acd` sets/clears bits of camera+0xcc (keys '+' / ',' via `FUN_0048d03c` toggle bit 4;
other callers use 8/0x10/0x40); `FUN_00450caf`/`FUN_004512cd` send the pan position while the arrow
keys (VK 0x25/0x27) or the screen edge move it (rate-limited by `_DAT_0084a7ec` + 0.5 s). No S->C
handler exists; the server needs no reply (presumably used for area of interest). world.py answers
it with nothing (`camera()`). Hypothesis refuted. Confidence high.

## 7. Monster AI packets (server/ai.py)

`ai.tick(now, player)` runs every ~200 ms; state per monster in world.Unit (`state` idle / chase /
attack / leash, `dest`, `move_speed`, `next_attack`, …); the player's HP/alive in world.PLAYER.
The server walks each monster along its last 0x416 at the same speed so its position matches.

| when | op | size | fields |
|---|---|---|---|
| aggro (player ≤ 8 u, or monster damaged and player ≤ 25 u from its home); chase every 0.5 s while the player moved > 1 u | 0x416 | 0x20 | extra = monster; +0x10 heading, +0x11 type **2**, +0x14 speed 300, +0x18/+0x1c a point 1.6 u short of the player |
| in range (≤ 2.5 u) | 0x416 | 0x20 | type **0** at its own position, heading toward the player (stop and face) |
| every 1.5 s in range (first after 0.5 s) | 0x411 | 0x64 | extra = monster; +0x10 monster uid, +0x14 skill 0, +0x16 motion 0, +0x18 0x4 on crit, +0x1a bit 0 if lethal, +0x1c/+0x20 monster x/z, +0x24/+0x28 player x/z, +0x2c monster HP (> 0!), +0x30 MP, +0x34 {player uid, damage} |
| player HP reaches 0 | 0x420 | 0x18 | extra = player; HP 0 (the lethal bit already kills) |
| 5 s later | 0x421 + 0x416 | 0x20 + 0x20 | 0x421 {HP, MP, max HP, max MP} revives in place (`FUN_004890cb`); 0x416 type **1** snaps the avatar to world.PLAYER["spawn"] |
| player > 25 u from home, monster > 25 u from home, or player dead | 0x416 | 0x20 | type 0 to home at speed 600; on arrival 0x420 with full HP |
| respawn due | 0x804 | 0xbc | world.due_respawns(), now on the timer |

Damage = (40 + 15 × (level − 1)) × 0.8..1.2, 5 % double (crit flag). A 0x804 for the player was not
used for the revive: for uids < 0x3f7 it also overwrites equipment (+0x84, 2 × 16 B), team +0x19,
battle side, guild, and reloads the skill bar, so it would need the full player state.

Heading = atan2(dx, dz) / 2π × 256 (from `FUN_005106ab` = atan2(x, z) behind `FUN_004708dd`);
medium confidence. Unit skills (UnitDB cols 38-51, Skill_Base 40700xx) are not used; a monster
skill would be the same 0x411 with +0x12/+0x14 = the skill id.

Uncertain: whether motion 0 is a valid swing for every monster model; whether the client wants
0x416 type 2 or 0x20 for monsters (0x43f converts to 0x20); chase speed 300 vs the player's 450
means a running player always escapes.

## Loot

**There is no ground-item system in the client.** No S->C opcode spawns an item object in the
world, no C->S opcode picks one up, and the binary has no drop/field-item class or string
(searched: `drop`, `loot`, `pickup`, `FieldItem`, `ItemBox`; opcodes.tsv has nothing unclaimed
that fits; 0x803's category byte only selects unit kinds; 0x451 kind 1 "gadgets" are static
scene objects from the map). What exists is the *acquisition* feedback, so the original server
almost certainly put kill drops straight into the bag. The passive item 1619 "Increase the item
drop rate by 20%" confirms drops were real but server-side. Confidence: high (absence of a
ground path), high (0x427 reason 0x46 behaviour, read from FUN_00478d54).

### Packets (all S->C, extra = own player uid)

| opcode | size | fields | client effect |
|---|---|---|---|
| 0x427 | 0x28 | +0x10 u16 reason **0x46** · +0x12 u16 container 1 (bag) · +0x14 u16 slot (<70) · +0x18 16-byte item (+0 u16 code, +4 u8 count) | stores bag slot (`G+0x2850+slot*16`), highlights it (FUN_005793b2), opens ItemPickupMessage panel 0x3e: "You acquired *name*" (`Item_pickup`) or "*name* x N" (`Item_pickup2`), N = new count − old count when the slot already held that code; then, since reason != 0, system message 70 `StrDef_GetItem` "You acquired an <item>." |
| 0x428 | 0x1c | +0x10 u16 reason 0 · +0x12 u16 field **2** · +0x14 u32 new gold total · +0x18 u32 0 | char+0x283 = value, UI event 0x1b (money display). Reason 6 adds "%s Gold has been paid in the country". |
| 0x428 | 0x1c | field 0xd, reason 4/5 · +0x14 currency A (acct+0x634) · +0x18 jewels (acct+0x638) | pickup popup for item 1006 "Yellow Jewel" × delta — not gold |
| 0x41b | 0x18 | +0x10 u32 36 (`StrDef_InventoryIsFull`) | bag-full notice |

Correction to group00.md 0x427: reason 0x46 is not "reinforce" — it is system message 70
`StrDef_GetItem`, the item-acquired path. Any non-zero reason also prints that system message
(FUN_00498605/FUN_00498a40 at the end of the handler).

Item record (16 bytes): +0 u16 Item_Base code, +4 count (read as a signed char by FUN_004dfa01;
0 means 1; only used when the item def's type +0x1c is stackable per FUN_00440e65), rest 0.
Gold = slot record +0x80 (char+0x283). Item_Base 1003/1004/1005 are the "Gold"/"Fame"/"Exp"
pseudo-items used for reward display.

### Drop table

Quest drops are client data: Quest.cdb kill-and-collect objectives are 10 fields before each
`Quest_QuickText_*` key: `type, unit, count, rate %, item, 0, map, map, map, 0`; type 1 with an
item = "kill *unit*, it drops *item* at *rate*%, collect *count*".

| unit | quest | item | rate | need |
|---|---|---|---|---|
| 604 Slime | 631 "The Slime is mine" | 2550 Slime Mucus | 100 % | 3 |
| 731 Bee | 632 | 2552 Bee Needle | 100 % | 5 |
| 732 Cobra | 632 | 2551 Snake Leather | 100 % | 5 |

(30 units in all have such objectives; 26xx items repeat 25xx objectives for a parallel quest line.)
Gold and other materials are server data the client never had; the server's choice
(server/loot.py `EXTRA_DROPS`):

| unit | gold | extras |
|---|---|---|
| 604 Slime | 2-5 | 839 Wild herb 10 % |
| 732 Cobra | 3-8 | 611 Red Passion Fragments [D] 5 %, 839 10 % |
| 731 Bee | 4-10 | 601 Blue Passion Fragments [D] 5 %, 839 10 % |
| 605 Great Slime | 20-40 | 2550 ×2-3 100 %, 692 Gem Stone: Blue 25 %, 601 15 %, 611 15 % |

Quest items stop dropping once the bag holds the objective count (no server quest state yet).

### Server model (server/loot.py)

`world.deaths()` → `loot.on_kill(unit)`: rolls the table, lays drops (server-side only) within
0.8 units of the corpse and collects at once whatever is within 12 units of the player (auto-loot;
ranged weapons reach 7). Leftovers (bag full, far kill) last 60 s; `loot.tick()` picks them up
when the player walks within 3 units, and a C->S 0x451 (kind 2, state 1) on the corpse uid picks
up that corpse's drops within 15 units (whether the client sends 0x451 for a corpse is untested).
Bag stacks are tracked in `skills.STATE["count"]` (parallel to `"bag"`), stack cap 99.
Untested in the live client: the popup and the 0x428 gold display.
