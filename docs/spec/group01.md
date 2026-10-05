# Group 01: opcodes 0x446 to 0x47c

Conventions: offsets are from the start of the packet (payload starts at +0x10). "uid" is the u16 in-world unit/object id. The local player's uid is the header `extra` (+6) of 0x2000 (enter world), stored at `DAT_00847ac8+0xec` and in unit+0x35e. Every C->S packet in this group carries the sender's uid in header +6. Several S->C handlers look up the target unit with `FUN_0044d3b9(header+6)` and drop the packet if that unit does not exist.
Global "char/world state" `DAT_00847ac8`: +0x652 mapid, +0x656 sceneidx, +0x64c mapfort (i8, -1..19), +0x64d u8, +0x64e mapGuild, +0x64a channel idx (labels come from the client's own debug string "sceneidx / mapid / mapfort / mapGuild").
Unit nation is the i8 at unit->info(+0x3a0)+0x655. Character id is the u64 at info+0x203/+0x207. Guild id is the u16 at info+0x27f, or the guild object's +0xe4.

### 0x446 — war/world-map full state (nations, forts)
- dir: S->C
- c2s: never sent
- s2c: min size 0x7dc; +0x10 u32 -> wardata[0]; +0x14 u32 -> wardata[+0x18]; +0x18 u32 event arg (passed to UI notify 0x20); +0x1c 87 x 20-byte fort/base records (to +0x6e8); +0x6e8 0xe4-byte block (0x39 dwords); +0x7cc,+0x7d0,+0x7d4,+0x7d8 u32 x4 (-> state+0xab2c..0xab38)
- reply: none
- confidence: medium (layout high, meaning medium)
- notes: handler FUN_00474eb1 -> FUN_0042a814 (war-data object FUN_004285cf). It also clears a pending "waiting" handle (FUN_00470940()+0x5c), so this is probably the answer to the world-map refresh 0x449 (or 0x445).

### 0x448 — war/base state change (single event)
- dir: S->C
- c2s: never sent
- s2c: min size ~0xd0; +0x10 u16 event id; +0x12 u8 kind (4 = only the three u16s are used); +0x13 u8; +0x14 u32; +0x18 u16[3]; +0x1e i8 nation; +0x20 0xb0-byte fort record (first byte = fort idx 0..19); +0x24 u8 "record present" flag
- reply: none
- confidence: low
- notes: handler FUN_00471751 -> FUN_00429516 (stores into wardata+0x7514). Ignored unless the game-state object DAT_00847ac8 exists.

### 0x449 — world-map info refresh request
- dir: C->S
- c2s: size 0x18; empty payload (8 zero bytes)
- s2c: none (no handler)
- reply: probably the war/map state (0x446, and/or 0x44a/0x475/0x476); not required to keep playing
- confidence: medium
- notes: sent from the WorldMap panel (FUN_005738f5 every few seconds while it is open, FUN_0057867a on open), always right after 0x445. On open it is followed by 0x473.

### 0x44a — base/fort owner table
- dir: S->C
- c2s: never sent
- s2c: min size 0xc4; +0x10 u32 -> wardata[0]; +0x14 u16[87] per-base value (owner nation/guild) -> wardata+0x695c stride 0x20
- reply: none
- confidence: medium
- notes: handler FUN_00471771 -> FUN_0042861a; raises UI notify 0x22.

### 0x44b — NPC service request (NPC menu entries 4 / 0x27 / 0x28)
- dir: C->S
- c2s: size 0x18; +0x10 i32 my nation (info+0x655); +0x14 u32 NPC uid
- s2c: none
- reply: unknown (depends on the NPC service); none needed to stay connected
- confidence: medium
- notes: FUN_0056dd87 (NPC dialog menu dispatcher). Built twice: once by hand (header 0xa53c0018, opcode 1099) and once through FUN_004a730b. Before sending, the client checks that the NPC is not an enemy (FUN_004872bd).

### 0x44c — teleporter NPC offer (destinations + costs)
- dir: S->C
- c2s: never sent
- s2c: min size 0x3c; +0x10 u16 NPC uid (echoed back in 0x44e); +0x14 u16[2] destination map ids (map-table type 5 = one class, others = another); +0x1c i32 cost (0 = free, otherwise checked against money info+0x283, "MoneyIsLow"); +0x20 i32[4] per-destination cost; +0x30 i16[4] destination map ids; +0x38 u8[4] destination enabled
- reply: none directly. The user confirms "DoYouTeleport_S"/"DoYouTeleportTax_SS" -> C->S 0x44e
- confidence: medium
- notes: handler FUN_00479d4c. If the game mode (DAT_00853ce4) != 0xb, it instead opens PanelTeleport (FUN_00540042) with this packet.

### 0x44d — open teleport panel (list with counters)
- dir: S->C
- c2s: never sent
- s2c: min size 0x24; +0x10 i16 NPC uid (must exist); +0x12 u16[3] destination map ids (0 = empty); +0x18 u16[3] per-destination value; +0x1e i8[3] counter shown as "%s (%d/20)"
- reply: none. The panel later sends 0x44e (+0x10 NPC uid, +0x14 chosen destination)
- confidence: medium
- notes: handler FUN_00470f83 -> PanelTeleport FUN_0054066b (panel mode 3).

### 0x44e — warp / teleport (request and result share the opcode)
- dir: both
- c2s: size 0x28; +0x10 u16 NPC/portal uid (0 when walking into a map portal); +0x14 u32 destination id (map id or portal link id); +0x18 u32 (usually 0; world-map variant passes a value); +0x1c u32 cost/tax (0 if free); +0x20 u16 flag (1 = world-map warp FUN_0057349b, else 0)
- s2c: min size 0x2c; header +6 = uid of the unit being moved (must exist; the local-player branch runs only when it equals the local player's uid); +0x10 u16 mapid; +0x12 u16 sceneidx; +0x14 f32 x; +0x18 f32 z (y comes from the terrain); +0x1e i8 mapfort (-1 = none); +0x1f u8; +0x20 u32 mapGuild; +0x24 u32,+0x28 u32 fort extra (stored only if 0 <= mapfort < 20)
- reply: S->C 0x44e with header+6 = player uid, the destination mapid/sceneidx and spawn x/z. If sceneidx == the current sceneidx the client just repositions (in-scene teleport). If it differs, the client does a full scene change (unloads, loads mapid, shows PanelGameResultSimple if open)
- confidence: high (layout), medium (C->S field meanings)
- notes: handler FUN_00473548. Send sites FUN_00479d4c, FUN_00487809, FUN_0048796a (portal trigger, throttled to 3 s), FUN_0048cd72, FUN_0053f3fa, FUN_0056dd87, FUN_0057349b and others. A debug console command at 0x5ad761 builds a 0x2c-byte 0x44e and feeds it straight to the handler with floats at +0x14/+0x18, which confirms they are f32. For a non-local uid the client only moves that unit (FUN_004fee28).

### 0x44f — warp / scene change with scene data block
- dir: S->C
- c2s: never sent
- s2c: min size 0x1bc; same fields as 0x44e (+0x10 mapid, +0x12 sceneidx, +0x14 f32 x, +0x18 f32 z, +0x1e i8 mapfort, +0x1f u8, +0x20 u32 mapGuild, +0x24/+0x28 fort extra) plus +0x2c 400-byte block (100 u32) -> state+0x65a (scene object table; u16 entries are matched against gadget ids by 0x415 senders)
- reply: none
- confidence: high (layout), medium (block meaning)
- notes: handler FUN_00473ab5. This is the variant to use when entering an instanced scene or match map that has interactive objects. FUN_004a7dbe is called with 0 here and 1 in 0x44e.

### 0x450 — channelled interaction on another unit (capture/rescue-type cast)
- dir: both
- c2s: size 0x1c; +0x10 u16 target uid; +0x16 u16 action (10 = channel tick sent about once a second while holding; 11 = cancel/stop)
- s2c: min size 0x1a; header +6 = actor uid; +0x10 u16 target uid (must exist and have info); +0x12 u16 effect id A; +0x14 u16 effect id B; +0x16 i16 action: 0 = abort (+0x18 i16 count >0 plays an effect), 1 = completed (+0x18 -> target's nation/side byte or u16; plays effect A or B depending on enemy/ally), 10 = progress (+0x18 i16 progress value), 11/12/13/14 = ended/cancelled
- reply: S->C 0x450 with action 10 to acknowledge progress, and action 1 to complete. Silence only leaves the client channelling
- confidence: medium
- notes: handler FUN_0047963d. Senders FUN_00462f64 (tick) and FUN_0046316b (stop), an interaction state machine at mode +0x108. Target uid 0x5219 is special-cased.

### 0x451 — interact with object/unit start/stop
- dir: both
- c2s: size 0x18; +0x10 u16 target id (gadget id or unit uid); +0x12 u16 kind (1 = gadget/object, 2 = unit); +0x14 u16 state (1 = start, 0 = stop); +0x16 u16 object type (gadget record[6]; 5 = scene-object type)
- s2c: min size 0x18; header +6 = actor uid (must exist); +0x10 u16 target; +0x12 u16 kind (1: requires +0x16 == 5 and the gadget to exist; 2: target unit must exist); +0x14 u16 state; +0x16 u16 type
- reply: optional broadcast of the same packet to the others (drives the animation through FUN_0048d424); no ack is needed
- confidence: medium
- notes: handler FUN_004750f0. Senders FUN_00462d41/00462db9/00462eea/0046307a and FUN_00487809 (message-box ids 0x49/0x4a -> kind 1/2 with state 0). FUN_00462db9 also sends 0x415 for matching scene objects.

### 0x452 — shop price-rate update
- dir: S->C
- c2s: never sent
- s2c: min size 0x1c; +0x10 u32 buy-price multiplier (state+0xb3b4, default 1); +0x14 u32 sell-price multiplier (state+0xb3b8, default 1); +0x18 i32 system-message id to display (0 = none)
- reply: none
- confidence: medium
- notes: handler FUN_00470d80. Multipliers are used by the item price helpers near 0x4e0603. Send 1/1 (or never send it).

### 0x453 — unit stat/appearance refresh
- dir: S->C
- c2s: never sent
- s2c: min size 0x78 (+12 bytes per set bit); header +6 = unit uid; +0x10 u32 status flags (unit info+0x64d; bit 0x200 toggles an effect); +0x14 0x5c-byte stat block (23 u32 -> unit info+0x443); +0x74 u32 bitmask of 32 slots; +0x78 packed 12-byte entries, one per set bit in ascending order (-> unit slot table +0x49f, e.g. equipment/visual)
- reply: none
- confidence: medium
- notes: handler FUN_004732fd (FUN_00472103, FUN_0046fd59, FUN_00470a7b). If the uid is not spawned yet, the data goes to the pending-spawn record (FUN_00428494) with matching +0x1ae.

### 0x454 — inventory "ItemSort"
- dir: C->S
- c2s: size 0x58; +0x10 u8[70] new order: for each of the 70 slots of bag type 1, the old slot index after sorting
- s2c: none
- reply: none needed (the client rearranges locally via FUN_004e1301)
- confidence: high
- notes: built in the undecompiled function at 0x4e16a7, called from the inventory panel button "ItemSort" (0x57bd96). The listed send-site function FUN_004e1653 is a vector helper, not the real site.

### 0x455 — guild create
- dir: C->S
- c2s: size 0x1e8; +0x11 char[32] guild name; +0x1b0 char[40] creator character name (info+0x20b)
- s2c: none
- reply: unknown; guild info is probably pushed with 0x457/0x458
- confidence: medium
- notes: real site 0x5537ff (Guild_Create panel). Fringe.

### 0x456 — guild disband
- dir: both
- c2s: size 0x18; +0x10 u32 guild id; +0x14 u32 0
- s2c: min size 0x18; +0x14 i32 result: 0 = disbanded (clears my guild id, notify 0x28); -1 GuildDeleteFail_RemainMember; -2 GuildDeleteFail_StockHave; -3 GuildDeleteFail_EtherHave
- reply: 0x456 with +0x14 = 0
- confidence: high
- notes: handler FUN_004799cf; sender FUN_00557cdc (cmd 0x10).

### 0x457 — guild info (with my member index)
- dir: S->C
- c2s: never sent
- s2c: min size 0x1ac; +0x10 0x198-byte guild record (+0xf4 u16 guild id -> my info+0x27f); +0x1a8 i32 member index/extra (>= 0)
- reply: none
- confidence: medium
- notes: handler FUN_004712a6 -> FUN_004b6a18. Fringe.

### 0x458 — guild info (no member index)
- dir: S->C
- c2s: never sent
- s2c: min size 0x1a8; +0x10 0x198-byte guild record (+0xf4 u16 guild id)
- reply: none
- confidence: medium
- notes: handler FUN_004712f3 (same as 0x457 with index -1).

### 0x45b — guild invite / member added
- dir: both
- c2s: size 0x58; +0x10 u16 guild id; +0x20 char[40] invitee name
- s2c: min size 0x58; +0x10 u16 guild id; +0x18 u64 char id + member record (FUN_004b4e5f). If the char id is mine, sets my guild id
- reply: 0x45b member record (fringe)
- confidence: medium
- notes: handler FUN_0047133c; sender FUN_00557cdc (cmd 0xd).

### 0x45c — guild kick/leave
- dir: both
- c2s: size 0x58; +0x10 u16 guild id; +0x18 u64 target char id; +0x50 u32 target uid
- s2c: min size 0x20; +0x18 u64 char id removed (FUN_004b4b8f)
- reply: 0x45c echo
- confidence: medium
- notes: handler FUN_004713d9; sender FUN_00557cdc (cmd 0xe).

### 0x45d — guild member field update
- dir: S->C
- c2s: never sent
- s2c: min size 0x24; +0x10 u32 guild id (must equal mine); +0x18 u64 member char id; +0x20 u32 value (member+0x50, e.g. online/status)
- reply: none
- confidence: medium
- notes: handler FUN_0047140c.

### 0x45e — guild cargo (warehouse) open/close
- dir: both
- c2s: size 0x2c4; +0x10 u16 guild id; +0x298 u16 1 = open, 0 = close
- s2c: min size ~0x2c4; +0x14 guild cargo block (FUN_004b3fb6); +0x29a i16 other users (>= 1 -> "StrDef_GUILD_Cargo_using" with +0x29c char[] name; < 1 -> opens the cargo)
- reply: 0x45e with +0x29a = 0
- confidence: medium
- notes: handler FUN_004778da (PanelGuildCargo). Fringe.

### 0x45f — guild cargo item move
- dir: both
- c2s: size 0x2ec; +0x10 u16 slot/item index; +0x14 u32; +0x18 u16 guild id; +0x1a..+0x1d u8 x4 (src/dst slot, count); +0x20 16-byte item; +0x30 16-byte item
- s2c: min size ~0x2ec; +0x68 guild cargo block (FUN_004b3fb6)
- reply: 0x45f with the updated cargo
- confidence: low
- notes: handler FUN_00471451; senders FUN_005525c2/005527ec/005794d3.

### 0x460 — guild upgrade/donate (funds operation)
- dir: both
- c2s: size 0x28; +0x10 u16 guild id; +0x12 u16 item/option; +0x14 u32 amount
- s2c: min size 0x28; +0x12 i16 value (applied when ok); +0x18 i16 error message id (0 = ok); +0x20 u32,+0x24 u32 guild funds
- reply: 0x460 with +0x18 = 0
- confidence: low
- notes: handler FUN_0047146b; sender FUN_0055231e.

### 0x461 — guild member rank change
- dir: both
- c2s: size 0x70; +0x10 u64 my char id; +0x18 u16 guild id; +0x1c u16 new rank (4 = special/transfer); +0x20 0x40-byte member record
- s2c: min size 0x70; same record (FUN_004b5130)
- reply: 0x461 echo
- confidence: medium
- notes: handler FUN_004714d2; sender FUN_00557cdc (cmd 0xf, needs rank permission bit 0x80).

### 0x462 — guild settings
- dir: both
- c2s: size 0x1c; +0x10 u16 guild id; +0x12 10-byte settings blob
- s2c: min size 0x1c; +0x12 u32, +0x16 u32, +0x1a u16 (same blob -> guild+0x108..0x110)
- reply: 0x462 echo
- confidence: low
- notes: handler FUN_00471501 -> FUN_004b405f; sender FUN_00559a59 area (0x55aade).

### 0x463 — guild command (purpose unclear)
- dir: C->S
- c2s: size 0x14; +0x10 u16 guild id; +0x12 u16 argument
- s2c: none
- reply: unknown
- confidence: low
- notes: FUN_00557cdc cmd 0x11.

### 0x464 — guild notice edit
- dir: C->S
- c2s: size 0xd4; +0x10 u16 guild id; +0x12 char[0xbe] notice text
- s2c: none
- reply: none known
- confidence: medium
- notes: senders 0x557982 and 0x55a9c5 ("noticeedit"/"noticeok").

### 0x465 — guild ether trade (buy/sell)
- dir: both
- c2s: size 0x30; +0x11 u8 3 = sell ether, 4 = buy ether; +0x12 u8 guild flag; +0x14 u16 guild id; +0x18 u32 amount; +0x20..+0x2c current funds snapshot (u32 x4)
- s2c: min size 0x30; +0x11 u8 3/4; for 3: +0x20 ether, +0x28/+0x2c funds; for 4: +0x20/+0x24 funds, +0x28 ether
- reply: 0x465 with new totals
- confidence: medium
- notes: handler FUN_00476a53. Fringe.

### 0x466 — guild war invite
- dir: both
- c2s: size 0x44; +0x12 u16 my guild id; +0x14 u16 channel; +0x16 u16 map id; +0x18 char[40] target guild name; +0x40 u16
- s2c: min size 0x44; +0x12 i16 guild id (must equal mine); +0x14 i16; +0x16 i16; +0x18 char[40] inviting guild name; whole packet stored at guild+0x928 -> "GUI_Guild_WarInvite_PopupMsg"
- reply: forward to the target guild; its answer comes as 0x467
- confidence: medium
- notes: handler FUN_00479ad8; sender 0x55b1d2.

### 0x467 — guild war invite answer
- dir: C->S
- c2s: size 0x44; +0x12 u16 my guild id; +0x14 u16 arg; +0x16 u16 arg (accept/decline); +0x18 char[40] stored inviter name; +0x40 u16 stored value
- s2c: none
- reply: unknown
- confidence: low
- notes: FUN_0051238b.

### 0x468 — guild stock/share trade (variant A)
- dir: both
- c2s: size 0x48; +0x18 u64 my char id; +0x20 u32 item/amount; +0x24 u32; +0x28 u32; +0x2c u32; +0x30 u8
- s2c: min size 0x28; +0x10 i32 result (0 = ok, else message id shown); +0x14 u32 guild id; +0x18/+0x1c u32 funds; +0x20 u16; +0x24 u16
- reply: 0x468 with +0x10 = 0
- confidence: low
- notes: handler FUN_00471530; senders FUN_0054f172, FUN_00550824.

### 0x469 — guild stock/share trade (variant B)
- dir: C->S
- c2s: size 0x48; +0x10 u32; +0x14 u32; +0x18 u64 my char id; +0x20 u32; +0x24 u32 count; +0x28 u32; +0x2c u32; +0x30 u8 my nation
- s2c: none
- reply: probably 0x468
- confidence: low
- notes: same panels as 0x468.

### 0x46a — guild dividend
- dir: both
- c2s: size 0x48; +0x18 u64 my char id; +0x20 i32 guild id; +0x24..+0x2c 0; +0x30 u8 nation
- s2c: min size 0x38; +0x10 i32 result (0 = ok, else message id); +0x14 u32 guild id; +0x18/+0x1c funds; +0x20 u16; +0x24 u16; +0x28/+0x2c amounts for "GUI_GuildManage_DividendMsg_D"; +0x34 u32
- reply: 0x46a with +0x10 = 0
- confidence: medium
- notes: handler FUN_00476c02.

### 0x46b — custom game: create room
- dir: C->S
- c2s: size 0xc8; +0x12 u16 field/map id (0x77 for the special "Join" mode); +0x16 char[40] host name (info+0x20b); +0x3e char[128] room name (only from the Create dialog); +0xc2 u8 flag (1 from the special Join path, else 0); +0xc4 u16 max player count (MatCnt)
- s2c: none
- reply: unknown (a room/lobby opcode outside this group)
- confidence: medium
- notes: real sites 0x5425c9 (CustomGame create dialog; room name must be < 120 chars) and FUN_00542b01. List refresh there is 0x46c.

### 0x46d — custom game room list
- dir: S->C
- c2s: never sent
- s2c: min size 0x72c; +0x10 10 x 0xb6-byte room entries (entry +4 i16 > 0 = valid)
- reply: none
- confidence: medium
- notes: handler FUN_00471696 -> FUN_0054310d (CustomGameList panel 0x62; ignored when the panel is closed). Reply to 0x46c.

### 0x46e — custom game join / rejoin
- dir: both
- c2s: size 0x18; +0x10 u16 mode (0 = join from list, 1 = "Rejoin", 2 = decline/close); +0x12 u16 room id (join from list)
- s2c: min size 0x11; +0x10 u8 3 = offer rejoin (opens CustomGameRejoin panel 0x66, or sets state+0xb294)
- reply: unknown for joins
- confidence: medium
- notes: handler FUN_004716c5; senders FUN_00540814 (Rejoin panel) and FUN_00542b01 (list "Join").

### 0x470 — match queue (state push and register/cancel request)
- dir: both
- c2s: size 0xec; +0x10 u8 action (1 = register solo, 2 = register team, 4 = cancel/leave queue); +0x11 u8 match type (echo of the last S->C +0x11); +0x12 u8 (echo of the last S->C +0x12)
- s2c: min size 0xec; +0x10 u8 state (0 = match offered, so the minimap "Match" button and Match.panel are available; 1 = queued solo; 2 = queued team; 3 = team formed); +0x11 u8 match type (stored only when state 0); +0x12 u8; +0x14 i16 message id (state 0, shown if non-zero); +0x16 u16[5] team member uids (first = leader); +0x20 char[5][40] member names; +0xe8 u32 offer timeout in seconds (state 0; when it expires with state 0 the offer is cleared)
- reply: to action 1/2 send 0x470 with +0x10 = 1/2 (queued). To 4 send state 0 or nothing (the client already resets locally). The match itself starts with a scene change (0x44f/0x44e or 0x2000)
- confidence: medium-high
- notes: handler FUN_004705ac sets state+0xb1b0 = 1, which gates the whole match UI; the server must push state 0 first. Senders FUN_005360a0 (Match.panel "Single"; "Team" sets state 3 locally and opens MatchTeam.panel), FUN_005362e8 (team register), FUN_00571c20/FUN_00571e3a (minimap button, "MatchOnDoYouCancle"), FUN_00428e81 (cancel).

### 0x471 — match team: invite by name
- dir: C->S
- c2s: size 0x3c; +0x10 char[40] character name
- s2c: none
- reply: 0x472 to the invitee, then 0x470 state 3 with the member list
- confidence: medium
- notes: FUN_0053623e (msgbox 0x2e "InputInviteCharName" from MatchTeam.panel).

### 0x472 — match team invite / team-state push (opens MatchTeam panel)
- dir: S->C
- c2s: never sent
- s2c: min size 0xec; same layout as S->C 0x470 (+0x10 u8 state, +0x12 u8, +0x16 u16[5] uids, +0x20 char[5][40] names); also opens GuiTogglePanel 0x74 (MatchTeam.panel)
- reply: none
- confidence: medium
- notes: handler FUN_004717d1.

### 0x473 — nation info request (world map / debug panel)
- dir: C->S
- c2s: size 0x18; +0x10 i32 nation id (info+0x655); +0x14 u32 0
- s2c: none
- reply: probably 0x475 (per-nation war data, keyed by the nation index at +0x14) and/or 0x476
- confidence: medium
- notes: senders FUN_0057867a (WorldMap open) and FUN_0051f196 (debug info panel).

### 0x474 — nation info panel request
- dir: C->S
- c2s: size 0x18; +0x10 i32 my nation; +0x14 u32 0
- s2c: none
- reply: probably 0x476/0x475
- confidence: medium
- notes: FUN_00534aaa (PanelNationInfo, panel 0x2b).

### 0x475 — per-nation war data
- dir: S->C
- c2s: never sent
- s2c: min size 0x4b8; +0x14 i8 nation index (0..3, else ignored); +0x15 u8; +0x18..+0x24 u32 x4; +0x28 4 x 40-byte records; +0xc8 4 x 0xb0-byte fort records (byte 0 = fort idx, byte 4 = present); +0x388 0x130-byte block
- reply: none
- confidence: medium
- notes: handler FUN_00471791 -> FUN_0042865a (stride 0x1a50 per nation).

### 0x476 — war statistics block
- dir: S->C
- c2s: never sent
- s2c: min size 0x6f8; +0x18 0x6e0-byte block (-> wardata+0x1240)
- reply: none
- confidence: medium
- notes: handler FUN_004717b1 -> FUN_0042873d; UI notify 0x1e.

### 0x479 — fort record update
- dir: S->C
- c2s: never sent
- s2c: min size 0xf0; +0x11 i8 nation; +0x12 i8 fort idx (0..19); +0x14 u32[10] fort counters; +0x40 0xb0-byte fort record; +0x48 i16 owning guild (also copied to mapGuild if this is my current fort)
- reply: none
- confidence: medium
- notes: handler FUN_00471883.

### 0x47a — warp to fort/field via world map (with channel)
- dir: C->S
- c2s: size 0x24; +0x10 u32 mapfort/target type; +0x14 u32 map id; +0x18 u8 option; +0x1c u32 fort byte/target; +0x20 u32 channel index (WorldMap channel list at state+0x618, 0x74-byte entries; rejected if the channel is in maintenance or is the current one)
- s2c: none
- reply: presumably a scene change, S->C 0x44f/0x44e with the new mapid/sceneidx (inferred)
- confidence: low
- notes: senders FUN_005275df (channel select, "ThisChannelMaintenace"), FUN_00532f62 (NationInfo fort list), FUN_0057349b (WorldMap).

### 0x47b — set my mapfort
- dir: S->C
- c2s: never sent
- s2c: min size 0x1c; +0x10 i8 new mapfort; +0x18 u32 sceneidx (applied only if it equals the current sceneidx)
- reply: none
- confidence: high
- notes: handler FUN_0047069f.

### 0x47c — war result / season block
- dir: S->C
- c2s: never sent
- s2c: min size 0x140; +0x10 0x130-byte block (-> wardata+0x1920); +0x10 u8 != 0 opens panel 0x2e (or sets state+0xb295)
- reply: none
- confidence: low
- notes: handler FUN_00471948.
