---
title: "Group 00 — opcodes 0x405 .. 0x445"
---

# Group 00 — opcodes 0x405 .. 0x445

Conventions: offsets from packet start (payload at +0x10). "entity id" = the u16 at header +6
(`extra`), which the client looks up with FUN_0044d3b9/FUN_0044d294 (entity table). For C->S
packets the client always puts its own entity id (`DAT_0084a758+0x35e`) in header +6 unless noted.
Char record = the 0x65f-byte per-character struct (`entity+0x3a0`); notable fields used below:
+0x203/+0x207 u64 char id, +0x233 u32 exp, +0x237 u8 level, +0x243..+0x262 equipment (16-byte items),
+0x283 u32 gold, +0x443 0x5c-byte stat block (+0x443 HP, +0x447 MP, +0x44b max HP, +0x44f max MP),
+0x479 u16 move speed, +0x49f 32x12-byte buff table, +0x64d u32 status flags, +0x655 u8 nation.

### 0x405 — login-screen kick/error notice
- dir: S->C
- s2c: min size 0x1c; +0x18 u32 reason (only 0x14 acted on)
- reply: none
- confidence: low
- notes: FUN_0047000f. Only while the login UI (DAT_0084e84c) exists: reason 0x14 -> FUN_004966f8(3,0x14) (login error dialog, "GUI_Login_Msg_Err_*"). Safe to never send.

### 0x407 — create character (request / result)
- dir: both
- c2s: size 0x260; header +6 = DAT_00847ac8+0xec (account/session word, NOT the entity id); +0x10 u32 slot (0-4); +0x18 u8 class/body type; +0x20 0x240-byte char record of which the client fills: +0x28 char[40] name (narrow), +0x56 u16, +0x58 u32, +0x5c u32, +0x60 u16 (appearance: face/hair/colour etc.)
- s2c: min size 0x260; +0x10 u32 slot; +0x18 u8 (if non-zero stored to DAT_00847ac8+0x62c, likely "selected slot/char count"); +0x20 0x240-byte char record (+0x20 u64 char id, +0x28 name char[]) — accepted only if the i64 at +0x20 is > 0
- reply: 0x407 echo: same slot, record copied back with a non-zero u64 char id at +0x20 (and the name at +0x28)
- confidence: high
- notes: handler FUN_00477a62 copies the record into the slot table DAT_00847ac8 + slot*0x65f + 0x7ea and refreshes the char-select UI; id <= 0 = failure (silently ignored). Sender FUN_00504dcc (send at 0x50528e).

### 0x409 — leave game (back to character select / quit)
- dir: C->S
- c2s: size 0x14; header +6 = own entity id; +0x10 u32 mode: 1 = exit client, otherwise (uninitialised stack) = return to character select
- reply: none — client disconnects itself after a timer (3000 ms for char-select, 1000 ms for exit)
- confidence: medium
- notes: sent from the per-frame state machine FUN_0048d666 (0x48df5f: char-select path set up by FUN_0059c700; 0x48e0d1: quit path from FUN_0041f68b). After char-select it calls FUN_004298e4(2) and must log in to the game server again (0x4200).

### 0x40a — channel move (request / result)
- dir: both
- c2s: size 0x28; +0x20 u32 target channel index (index into the client's channel list DAT_00847ac8+0x618, 0x74-byte entries)
- s2c: min size 0x28; +0x10 u8 key byte; +0x18 u32 key A; +0x1c u32 key B; +0x20 u32 channel index; +0x24 u32 error (0 = ok; non-zero = system message id shown via FUN_00498a40)
- reply: 0x40a with +0x24 = 0, +0x20 = requested index (must differ from the current channel DAT_00847ac8+0x624 and be within the list), +0x10/+0x18/+0x1c = session keys the client will echo in its re-login
- confidence: high
- notes: PanelChannelMove (FUN_005315a7) starts a 4.95 s countdown in FUN_0048d666, which sends this (0x48db16). On success (FUN_00472165) the client disconnects, connects to the channel's ip/port (from the client-side list, NOT the packet) and sends **0x4200 size 0x60: +0x10 char[32] account, +0x30 char[20] password/token, +0x44 u8 channel idx, +0x48 u32 0x41e (version const), +0x4c u8 = key byte, +0x50 u32 = key A, +0x54 u32 = key B**. Also sent from FUN_00487809 (GUI msg 0x42) with +0x20 = param.

### 0x40c — change nation request
- dir: C->S
- c2s: size 0x28; +0x10 u64 char id (char+0x203/+0x207); +0x18 u32 new nation (1-3)
- reply: 0x429 with +0x10 = 1, +0x14 = nation (header +6 = player entity), plus 0x428 (gold) if a fee is charged
- confidence: medium
- notes: PanelChangeNation (FUN_00532186, dialog id 0x31 OK). Fringe.

### 0x40f — skill cast/charge visual on entity
- dir: S->C
- s2c: min size 0x14; header +6 caster entity; +0x10 u32 skill id
- reply: none
- confidence: low
- notes: FUN_004734b3 looks up skill (FUN_004c2f58) and posts entity event 4 (ground-target skill) or 1 (other) via FUN_0048d424 — looks like "start casting" animation.

### 0x410 — skill used (broadcast, no damage)
- dir: S->C
- s2c: min size 0x38; +0x10 s16 caster entity; +0x14 s16 skill id; +0x20 f32 target x (or target entity id as float for entity-target skills); +0x24 f32 target z; +0x28/+0x2c f32 secondary position (0,0 = none); +0x30 u32 caster HP; +0x34 u32 caster MP
- reply: none
- confidence: medium
- notes: FUN_00474062. Turns caster toward target, plays cast FX, then FUN_00472079(caster,+0x30,+0x34) updates HP/MP. Client skill-use request is in another group.

### 0x411 — attack / skill hit result (up to 12 targets)
- dir: S->C
- s2c: min size 0x64; +0x10 s16 attacker entity; +0x14 s16 skill id (0 = basic attack); +0x16 u16 hit FX param; +0x18 u16 flags (0x1000 crit-style msg, 0x2000 alt msg); +0x1a u16 per-target bitmask (critical); +0x24 f32 x, +0x28 f32 z (ground target); +0x2c u32 attacker HP, +0x30 u32 attacker MP; +0x34 12 x {u16 target entity, s16 damage}
- reply: none
- confidence: medium
- notes: FUN_00475654; damage applied with FUN_00485e4b. If the attacker entity is unknown the client sends 0x4ca (0x18) to request it (rate-limited, 100-entry cache). Needed for combat, not for movement.

### 0x412 — skill hit with knock-back (up to 7 targets)
- dir: S->C
- s2c: min size 0x88; +0x10 s16 caster; +0x14 s16 skill id; +0x18 u16 flags; +0x1a u16 crit bitmask; +0x1c u32, +0x20 u32 (FX params); +0x24 f32 x, +0x28 f32 z; +0x2c u32 caster HP, +0x30 u32 caster MP; +0x34 7 x {u16 target, s16 damage}; +0x50 7 x f32 new x; +0x6c 7 x f32 new z
- reply: none
- confidence: medium
- notes: FUN_0047445f; targets with non-zero new x/z are pushed/pulled there.

### 0x413 — damage tick on entity (DoT / environment)
- dir: S->C
- s2c: min size 0x30; +0x12 s16 source entity; +0x2a u16 flag; +0x2c u16 target entity; +0x2e s16 damage
- reply: none
- confidence: medium
- notes: FUN_00478c1a; if target HP (char+0x443) < 1 the target is marked dead (entity+0x36c = 0).

### 0x414 — quest state list (full)
- dir: S->C
- s2c: size 0x1a2; +0x12 100 x {u16 quest id, s8 state, u8 pad}
- reply: none
- confidence: low
- notes: FUN_00474fda diffs against DAT_00847ac8+0x65a and updates NPC quest markers (FUN_00483b5c). Probably sent on enter world; zeros = no quests.

### 0x415 — quest state change (request / update)
- dir: both
- c2s: size 0x18; +0x10 u16 DAT_00847ac8+0x652 (current NPC/char index); +0x12 u16 0; +0x14 {u16 quest id, u8 state, u8}
- s2c: min size 0x18; +0x14 u16 quest id; +0x16 s8 new state
- reply: 0x415 with +0x14 quest id, +0x16 new state
- confidence: low
- notes: handler FUN_004706c2; senders FUN_00462db9 (also emits 0x451) and FUN_0056e3d8 (quest panel). Fringe.

### 0x416 — movement (client move / server move broadcast)
- dir: both
- c2s: size 0x20; header +6 own entity; +0x10 u8 heading (0-255, entity+0x374); +0x11 u8 move type: 0x02 normal move, 0x20 alt move (mount/other state), 0x00 stop/state-7 move, 0x01 position-resync request (sent when the client thinks it is stuck/off-mesh), 0x04 clock-drift/speed-hack report; +0x12 u8 entity+0x38 (stance/anim); +0x14 u16 move speed (char+0x479); +0x18 f32 dest x; +0x1c f32 dest z
- s2c: min size 0x20; header +6 entity id; +0x10 u8 heading/action; +0x11 u8 type (0 normal, 1 = force-teleport when it is the local player, 2 = run/jump, 0x10, 0x20 accepted; anything else ignored); +0x14 u16 speed; +0x18 f32 x; +0x1c f32 z (y is from terrain)
- reply: normally none to the sender (client predicts locally); broadcast 0x416 with the mover's entity id in header +6 to others. To answer a type-1 resync or to correct a position, send 0x416 to that client with +0x11 = 1 and the position.
- confidence: high
- notes: handler FUN_004728ff requires the entity to exist with char record (+0x3a0) and model (+0x368) loaded, i.e. spawned first. Ignores remote entity if id > 0x3f6 and FUN_004b8824 says so. Senders: FUN_004bba89 (normal, throttled; heading-change > 0x23 forces send), FUN_0048d666 (0x48d7dc, type 1), FUN_004156b0 (0x415b56, type 4 after two >15 s wall-clock vs tick drifts, then the client goes into a disconnect path).

### 0x41b — system message by id
- dir: S->C
- s2c: min size 0x18; +0x10 u32 message id; +0x14 u32 parameter
- reply: none
- confidence: medium
- notes: FUN_00477307 -> FUN_00498a40(id,...,param). Special ids: 3 clears DAT_00847ac8+0xb1b0 (match/queue info), 0x61/0x48 close crafting panels, 0x86 NPC-related. Generic error channel — useful for replying "failed".

### 0x41c — system message with args (+ war join prompt)
- dir: S->C
- s2c: min size 0x20+; +0x10 u32 message id; +0x14 u32; +0x18 u32 (field/war id); +0x1c u32; +0x20 string args
- reply: none (ids 0x73/0x74 open PanelMsgboxWarAlram "DoYouJoinWarSomeFiled_S" whose answer is sent with another opcode)
- confidence: medium
- notes: FUN_00477525.

### 0x41d — confirm prompt (move-map etc.) / answer
- dir: both
- c2s: size 0x40; +0x10 u32 prompt code (echoed); +0x14 u32 prompt param (echoed)
- s2c: min size 0x18+; +0x10 u32 code (0x1a = "move map?" PanelMsgboxMoveMap, 0xe3 = notice popup, other = plain system message); +0x14 u32 param; +0x18 string
- reply: when the client answers OK (0x41d with code/param), perform the action (e.g. warp: 0x40a/0x2000-style map change)
- confidence: medium
- notes: handler FUN_00477741; senders FUN_005272dd / FUN_0052754d (PanelMsgboxMoveMap OK buttons).

### 0x41e — buff/status list for entity
- dir: S->C
- s2c: min size 0x1c + 12*n; header +6 entity; +0x10 u32 status flags (char+0x64d; bit 0x200 has a visual); +0x14 u16 (char+0x297); +0x18 u32 bitmask of present entries; +0x1c packed 12-byte buff entries (one per set bit, slots 0-31)
- reply: none
- confidence: medium
- notes: FUN_00470eeb -> FUN_0046fd59 / FUN_0046fe22 / FUN_00470a7b. Empty (mask 0) is valid.

### 0x41f — full stat block for entity
- dir: S->C
- s2c: size 0x6c; header +6 entity; +0x10 0x5c bytes copied to char+0x443 (+0x10 HP, +0x14 MP, +0x18 max HP, +0x1c max MP, rest = stats)
- reply: none
- confidence: medium
- notes: FUN_004733a4 -> FUN_00472103 (also works before the entity spawns, on the char-select record whose +0x1ae matches). Send on enter world so HP is non-zero (HP < 1 = treated as dead by several paths).

### 0x420 — HP/MP update
- dir: S->C
- s2c: min size 0x18; header +6 entity; +0x10 u32 HP; +0x14 u32 MP
- reply: none
- confidence: high
- notes: FUN_00473401 -> FUN_00472079.

### 0x421 — HP/MP + max update
- dir: S->C
- s2c: min size 0x20; header +6 entity; +0x10 u32 HP; +0x14 u32 MP; +0x18 u32 max HP; +0x1c u32 max MP
- reply: none
- confidence: high
- notes: FUN_0047341e.

### 0x422 — exp / level update
- dir: S->C
- s2c: min size 0x18; header +6 entity; +0x10 u8 level; +0x11 u8 level-up flag (1 = play level-up, "msg_levelup_d"); +0x14 u32 exp
- reply: none
- confidence: high
- notes: FUN_0047684e.

### 0x423 — container 2 contents (8 items)
- dir: S->C
- s2c: size 0x90; header +6 own entity; +0x10 8 x 16-byte item (copied to DAT_00847ac8+0x27d0)
- reply: none
- confidence: medium
- notes: FUN_0047043d; refreshes container type 2.

### 0x424 — inventory contents (70 items)
- dir: S->C
- s2c: size 0x470; +0x10 70 x 16-byte item (u16 item id first) -> DAT_00847ac8+0x2850
- reply: none
- confidence: medium
- notes: FUN_004703cf; container type 1 (same array 0x427 type 1 indexes). Likely part of enter-world burst; all-zero = empty bag.

### 0x425 — warehouse/storage contents (90 items)
- dir: S->C
- s2c: size 0x5b0; +0x10 90 x 16-byte item -> DAT_00847ac8+0x2e7c
- reply: none
- confidence: medium
- notes: FUN_00470406; container type 6.

### 0x426 — equipment / appearance change for entity
- dir: S->C
- s2c: min size 0x98 + 12*n; header +6 entity; +0x10 2 x 16-byte items (self: equip slots 0-1 of container 3; others: +0x10..+0x2f copied to char+0x243..+0x262); +0x30 u32 status flags; +0x34 0x5c-byte stat block; +0x94 u32 buff bitmask; +0x98 packed 12-byte buff entries
- reply: none
- confidence: medium
- notes: FUN_004725ae (reuses FUN_00472103, FUN_0046fd59, FUN_00470a7b).

### 0x427 — single item slot update
- dir: S->C
- s2c: size 0x28; header +6 entity; +0x10 u16 reason code (0x46 reinforce, 0x48/0x4a/0x5f/0x60 crafting, 0xf8-0xfb jewel, 0 plain); +0x12 u16 container (1 inventory, 2, 3 equipment -> char+0x243+slot*16, 4 special -> char+0x263, 5, 6 storage, 0xa); +0x14 u16 slot; +0x18 16-byte item (u16 item id, ...; zero = empty)
- reply: none
- confidence: medium
- notes: FUN_00478d54. The generic way to tell the client an item moved/appeared.

### 0x428 — character value update (gold etc.)
- dir: S->C
- s2c: min size 0x1c; header +6 entity; +0x10 u16 reason (6 = nation pay msg); +0x12 u16 field: 2 gold (char+0x283), 3 DAT+0x341c, 5 MP (char+0x447), 7 DAT+0x638, 9 char+0x287 & +0x656(+0x18 u8) & +0x651(+0x1c), 0xd cash pair (+0x14 -> DAT+0x634, +0x18 -> DAT+0x638), 0xe match obj+0xb0; +0x14 u32 value; +0x18 u32 value2
- reply: none
- confidence: medium
- notes: FUN_00476461.

### 0x429 — character attribute update
- dir: S->C
- s2c: min size 0x18; header +6 entity; +0x10 u32 type: 1 nation (char+0x655, u8), 3 title/rank (char+0x27f, s16), 5 char+0x656 (u8); +0x14 value
- reply: none
- confidence: medium
- notes: FUN_00470dd1; also applies to the char-select record if the entity is not spawned. Reply to 0x40c.

### 0x42a — move/swap item between slots
- dir: both
- c2s: size 0x18; +0x10 u8 dst container; +0x11 u8 dst slot; +0x12 u8 src container; +0x13 u8 src slot (sites write +0x10=1, +0x11=chosen slot, +0x12/+0x13 = source)
- s2c: size 0x18; same four bytes
- reply: echo the same 0x42a (header +6 = player entity) to perform the swap; refuse by not answering or 0x41b
- confidence: medium
- notes: handler FUN_00470376 -> FUN_004e1357(src_cont,src_slot,dst_cont,dst_slot). Senders FUN_0048bd47, FUN_0048c6b6, FUN_0048c92a, FUN_00562cc2, FUN_005794d3.

### 0x42c — inventory item action (confirm-box 0x17; likely destroy/discard)
- dir: C->S
- c2s: size 0x18; +0x10 u8 1 (inventory); +0x11 u8 slot; +0x12 u16 item id
- reply: 0x427 (slot cleared) — guess
- confidence: low
- notes: FUN_005794d3 (send 0x5797f3). Fringe.

### 0x42d — use item
- dir: both
- c2s: size 0x18; +0x10 u8 0; +0x11 u8 inventory slot; +0x14 u16 slot-sub/index; +0x16 u16 param (confirm-box 0x36)
- s2c: min size 0x14; header +6 entity; +0x12 u16 item id (starts cooldown + use FX for local player)
- reply: 0x42d with +0x12 = item id, plus 0x427 for the consumed slot and 0x420 for HP/MP if relevant
- confidence: low
- notes: handler FUN_00470316; sender FUN_0057349b.

### 0x42f — item-shop (cash) info
- dir: S->C
- s2c: min size 0x1c; header +6 own entity; +0x14 u32, +0x18 u32 (stored DAT+0xb3b4/0xb3b8, default 1); rest passed to PanelItemShop FUN_0056be7c
- reply: none
- confidence: low
- notes: FUN_00470fb2. Fringe.

### 0x432 — inventory item action with quantity (split/drop stack)
- dir: C->S
- c2s: size 0x18; +0x10 u8 container; +0x11 u8 slot; +0x12 u16 quantity; +0x14 u16 item id
- reply: 0x427 updates — guess
- confidence: low
- notes: FUN_005794d3 confirm-box 0x19 (send 0x5799d1). Fringe.

### 0x433 — auction register/bid
- dir: C->S
- c2s: size 0x60; +0x10 40-byte item/search block; +0x38..+0x4c u32 fields (price etc.)
- reply: unknown (auction result opcode in another group)
- confidence: low
- notes: PanelAuction (send 0x53a6f2). Fringe.

### 0x434 — auction search
- dir: C->S
- c2s: size 0x58; +0x10 40-byte name filter; +0x38 u8, +0x39 u8 flag, +0x3a u16, +0x3c u16 (grade/level range/page), +0x48..+0x54 u32
- reply: unknown
- confidence: low
- notes: PanelAuction (send 0x53a48c). Fringe.

### 0x436 — item reinforce request
- dir: C->S
- c2s: size 0x28; +0x10 u8 container; +0x11 u8 slot; +0x14 u16 item id; +0x17 u8; +0x18 u32 cost; then up to 5 material {u8 slot, u16 id}
- reply: 0x427 (reason 0x46) with the new item, 0x428 gold
- confidence: low
- notes: ItemReinforce panel FUN_0054837c; client deducts gold locally before sending. Fringe.

### 0x439 — match: map ping / objective position
- dir: S->C
- s2c: min size 0x1c; header +6 entity; +0x10 u8 flag (1 + self = show message 0x1462); +0x14 f32 x; +0x18 f32 z
- reply: none
- confidence: low
- notes: FUN_00474e60 -> match manager (FUN_0044ad5f) FUN_004fb3c7 (minimap marker/FX).

### 0x43a — match: periodic status / scoreboard
- dir: S->C
- s2c: min size 0x15a; +0x10 u8 match state (0 none, 1 recruiting, 2, 3 playing->shown as 4 ended); +0x11 u8; +0x14 u32 remaining time; +0x20 2 teams x 15 x {u32,u32} score rows; +0x110 per-team blocks; +0x148 4 x u32 + u16 team scores
- reply: none
- confidence: low
- notes: FUN_004711a8 -> FUN_004fc840 (match manager object, 0x2b0 bytes).

### 0x43b — match: info / start (team assignment)
- dir: S->C
- s2c: min size 0x16e; +0x10 u8 match type (index for FUN_004fb1ee); +0x11 u8 state; +0x12 u8; +0x13 2 x u8; +0x16 2 x u16 team values (written to members' char+0x659); +0x1c u32 time; +0x162 6 x u16 (queue panel counts)
- reply: none
- confidence: low
- notes: FUN_00471125 -> FUN_004fc4e7; refreshes queue panel (FUN_004e1425(0xb)).

### 0x43c — match: roster
- dir: S->C
- s2c: min size 0xa8; +0x10 u8 match type; +0x11 u8 state (3 is converted to 4); +0x12 30 x u8 team per member; +0x30 30 x u32 member entity ids (first = host)
- reply: none
- confidence: low
- notes: FUN_00471192 -> FUN_004fc70a; for custom games in state 1 opens PanelCustomGameMatch.

### 0x43d — match: team scores
- dir: S->C
- s2c: min size 0x22; +0x10 4 x u32 scores; +0x20 u16
- reply: none
- confidence: low
- notes: FUN_004711be -> FUN_004fb223.

### 0x43e — bulk entity revive/despawn
- dir: S->C
- s2c: min size 0x14 + 4*n; +0x12 up to 30 x {s16 entity id, u8 action (1 revive/clear dead, 2 despawn), u8}; list ends at id 0
- reply: none
- confidence: medium
- notes: FUN_00471087; skips the local player.

### 0x43f — bulk position snapshot
- dir: S->C
- s2c: size 0x230; header +8 tick; +0x14 40 x {s16 entity id, u16 speed, f32 x, f32 z}; +0x1f4 15 x {u16 entity id, s8 value, u8}
- reply: none
- confidence: medium
- notes: FUN_004751ca turns each first-list entry into a synthetic 0x416 (+0x10=0x7f, +0x11=0x20) for remote entities (id > 0, not self); second list = synthetic 0x806 (FUN_0044e059). Efficient alternative to per-entity 0x416.

### 0x440 — match: result
- dir: S->C
- s2c: min size 0x40+; +0x10 u8; +0x14 u8; +0x18..+0x3c u32 result fields (rewards/exp/points); followed by per-team member rows (0x68 bytes each)
- reply: none
- confidence: low
- notes: FUN_004711ea -> FUN_004fc9c5.

### 0x441 — match room: join / team change (request / update)
- dir: both
- c2s: size 0x18; +0x10 u32 team (0/1, depends on which button)
- s2c: min size 0x18; header +6 member entity; +0x10 u8 team; +0x14 u32 new host entity (0 = plain join/team change)
- reply: 0x441 echo with header +6 = requester, +0x10 = team, +0x14 = 0 (broadcast to room)
- confidence: low
- notes: handler FUN_00471715 -> FUN_004fd4ff (only for match types with the "custom" flag); sender FUN_0054099e (custom game room panel).

### 0x442 — match room: member left
- dir: S->C
- s2c: min size 0x14 (payload ignored); header +6 entity that left
- reply: none
- confidence: medium
- notes: FUN_00471736 -> FUN_004fd5a9.

### 0x443 — match: kill event / score credit
- dir: S->C
- s2c: min size 0x68; +0x10 u16 killer entity; +0x12 u16 victim entity (< 0x3f7 = player); +0x14 u16 score add; +0x16 u16 score add 2; +0x36 assist list; +0x5c/+0x60/+0x64 u32 written to char+0x613..
- reply: none
- confidence: low
- notes: FUN_00471200 -> FUN_004fcc10.

### 0x445 — world map / field status request
- dir: C->S
- c2s: size 0x18; no payload
- reply: 0x446 (world map / fortress state; handler FUN_00474eb1, other group). Client usually sends 0x449 right after (-> 0x44a).
- confidence: medium
- notes: senders FUN_005738f5 / FUN_0057867a (world map panel, rate-limited), FUN_00598a5f.
