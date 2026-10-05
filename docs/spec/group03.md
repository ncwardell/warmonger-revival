# Group 03: 0x4b5..0x4ca, 0x8xx, 0x20xx, 0x42xx

Conventions: offsets are from the start of the packet (header is +0x00..+0x0F). "extra" is the header u16 at +0x06.
In-game C->S packets put the sender's own unit id (`myUnit+0x35e`) in extra. Character-select packets put the
value from 0x2001's extra (`acct+0xec`) there. FUN_004a730b(buf, op, size, extra, clear=1) zero-fills the whole
packet before the fields are written, so any field not listed below is 0.

Global names used below: `acct` = DAT_00847ac8 (account/session object); `entry[i]` = acct+0x7ea+i*0x65f
(character-slot entry, 5 slots); the 0x240-byte character record sits at entry+0x203, so record+N = entry+0x203+N.
`unit` = a world object; `unit+0x3a0` points at its entry-shaped data block.

---

## Login / character select / enter world (critical path)

### 0x4207 — token login request
- dir: C->S
- c2s: size 0x9C; +0x10..+0x13 zero; +0x14 char[128] login token (copied raw from acct+0xee, 0x80 bytes); +0x94 u32 client version = 0x41E (1054); +0x98 u8 0xFF; extra 0
- s2c: none (the reply is 0x4201)
- reply: 0x4201 with +0x10 u32 result 0 (or 1/2), +0x14 u16 server idx, +0x18/+0x1c u32 account ids, +0x20 char[32] account name
- confidence: high
- notes: Send site 0x49595b in FUN_004958d2 (login state machine). The header is built at ebp-0xac and the token at ebp-0x98.

### 0x4201 — login result
- dir: S->C
- s2c: min size 0x40; +0x10 i32 result (accepted when `r==1 || r<3`, so 0,1,2 and negatives all count as OK; anything >=3 is an error code shown by FUN_004966f8); +0x14 u16 server/world index -> acct+0xea (echoed in 0x4200 +0x44); +0x18 u32 account id A -> acct+0xe0; +0x1c u32 account id B -> acct+0xe4 (both echoed in 0x4200 +0x50/+0x54); +0x20 char[32] account name (narrow, FUN_0042d65e) -> acct+0x70 (echoed in 0x4200/0x200f +0x10)
- reply: none (the client then sends 0x4200 by itself, state 8 of FUN_004958d2)
- confidence: high
- notes: Handler FUN_00470032. It clears acct+0x628 (account UID, which 0x2001 sets again).

### 0x4200 — game-server login (request character list)
- dir: C->S
- c2s: size 0x60; +0x10 char[32] account name (acct+0x70); +0x30 char[20] password (acct+0xa8, typed into the "password" UI box; empty for token login); +0x44 u8 world/server index (token path: acct+0xea from 0x4201; id/pw path: selected world-1; in-game reconnect: a field of the channel-move object); +0x48 u32 client version 0x41E; +0x4c u8 0xFF (login paths) or channel-move byte; +0x50 u32 account id A, +0x54 u32 account id B (from 0x4201; 0 in the id/pw path); extra 0
- s2c: none
- reply: 0x2001 character list (see below). The extra of the reply becomes the session tag that later char-select packets carry.
- confidence: high
- notes: Send sites 0x4959c5 (id/pw login), 0x4960c7 (token login, after 0x4201) and 0x48dd2b (FUN_0048d666: channel move / reconnect from inside the game, with +0x44/+0x4c/+0x50/+0x54 taken from that object).

### 0x2001 — character list
- dir: S->C
- s2c: min size 0xB8C; extra u16 -> acct+0xec (session tag the client puts in the extra of 0x406/0x200f/0x499); +0x10 + i*0x240 (i=0..4): 0x240-byte character record per slot, copied verbatim to entry[i]+0x203. Record fields seen: rec+0x00 u64 char id (0 = empty slot, 0xFFFFFFFF_FFFFFFFF = locked slot that can be bought for 5000 jewels); rec+0x08 char[40] name (narrow; converted to wchar at entry+0x1b3); rec+0x34 u8; rec+0x36 u16 class/model id (MUST be non-zero and valid in the class table, or entering the world aborts in FUN_0048b435); rec+0x38/+0x3c u32; rec+0x40 0x20 bytes plus rec+0x60..+0x6f (appearance/equipment, the same fields 0x803 sends); rec+0x7c i16 guild id (char delete is only offered when <1); rec+0x8c u32 deletion time in unix seconds (an empty slot is reusable 86400 s later). Then +0xB50 u32 account UID -> acct+0x628 (used in web-log URLs); +0xB54..+0xB73 not read; +0xB74 u8 account nation/faction (0 = not chosen yet) -> acct+0x62c, also copied to each entry+0x655; +0xB78 u32 currency A -> acct+0x634; +0xB7C u32 jewels (cash) -> acct+0x638; +0xB80 u32 server time in unix seconds (time sync via FUN_0046ff6d; the client's clock = this + elapsed ms/1000); +0xB84 u8 -> acct+0xb3ac; +0xB88 u32 -> acct+0xb3b0
- reply: none. The player picks a slot and the client sends 0x406 (see the notes on 0x2000).
- confidence: high
- notes: Handler FUN_004760b2. Each slot's entry unit id (+0x1ae) is set to slot number 1..5 until 0x2000 overrides it. In the login scene it switches to char select (FUN_004958d2(8)); inside the game it returns to char select.

### 0x2000 — enter world (selected character accepted; also used for an in-game warp)
- dir: S->C
- s2c: size 0x704. The whole layout:
  - extra (+0x06) u16 = the player's own unit/object id (players are < 0x3F7). Written to entry.unit_id (+0x1ae), net+0xc and acct+0xec. Every later in-game C->S packet carries it in extra.
  - +0x10 u64 char id. **Must equal the id of one of the 0x2001 slots** (FUN_0042843a); otherwise the whole packet is silently ignored. It also becomes the selected char (acct+0x600/0x604).
  - +0x18 i16 scene index -> acct+0x656 ("sceneidx")
  - +0x1a i16 map id -> acct+0x652 ("mapid"; map 0x78/120 gets special handling in several UIs)
  - +0x1c f32 spawn X, +0x20 f32 spawn Z (Y is forced to 0 and taken from the terrain). Stored as int(x*100), 0, int(z*100) at acct+0x63c/0x640/0x644; the game scene divides by 100 to place the player.
  - +0x24 i8 team/nation index 0..3 -> own entry+0x655 (and the team table at acct+0x3628 + idx*0x1a50)
  - +0x25 i8 fort index on this map ("mapfort"; -1 = none, 0..19) -> acct+0x64c
  - +0x26..+0x27 unused
  - +0x28..+0x6D7: a 0x6B0-byte player-profile block copied verbatim to acct+0x27cc (zeros are accepted). Known sub-fields: +0x28 u8 (the same value 0x47f type 1 sets); +0x2c 0x80 bytes (same block as the 0x423 payload); +0xac 0x460 bytes (same block as the 0x424 payload); +0x50c 8x u16 and +0x51c 8x u8 (echoed back in C->S 0x494); +0x524 15 x 0x18-byte entries; +0x68c 10x u32; +0x6b4/+0x6b8/+0x6bc/+0x6c0 u32 (the same fields as 0x4a9 +0x14..+0x20; +0x6b4 non-zero adds a title string); +0x6c4 u16, +0x6c6 u16, +0x6c8 u32 (the same fields as 0x4a2/0x4a4 +0x10/+0x12/+0x18). The block continues at acct+0x2e7c, which is filled by 0x2009.
  - +0x6D8 i16 -> acct+0xb1a8 (compared against a byte in the item table to decide whether an item can be used)
  - +0x6DA u8 guild grade/rank -> own entry+0x656
  - +0x6DB u8 team that owns this map/fort -> acct+0x64d (compared with the player's team)
  - +0x6DC u32 unread mail count -> acct+0xb298 and acct+0xb29c
  - +0x6E0 u16 channel index (0-based; the UI shows it +1) -> acct+0x64a
  - +0x6E4 u32 guild id that owns this map ("mapGuild") -> acct+0x64e
  - +0x6E8 u32 currency A -> acct+0x634; +0x6EC u32 -> acct+0x630 (jewel bonus/secondary); +0x6F0 u32 jewels -> acct+0x638
  - +0x6F4 u32 -> acct+0xb1ac (a threshold compared in FUN_00567f59/005681bc)
  - +0x6F8 u32 server time in unix seconds (time resync)
  - +0x6FC u32, +0x700 u32 -> the fort record [team +0x24][fort +0x25] fields +0xa8/+0xac (only when 0 <= +0x25 < 20)
  - The client also sets acct+0x648 = 0x9F and acct+0x649 = 0 itself.
- reply: none. In the char-select scene it calls FUN_004930cb(3), which switches to scene 4 (the game). The game scene builds the player's OWN unit locally from the selected slot record (FUN_0048b435 -> FUN_0044f6a3); the server does not need to send a 0x803 for the player itself. Inside the game the same packet acts as a warp: it closes UI and teleports to (x,z) via FUN_004b9f09.
- confidence: high
- notes: Handler FUN_00472272. **The trigger is C->S 0x406**, which the opcode index does not list because its header is built inline: size 0x20, extra = acct+0xec (from 0x2001), +0x10 u64 char id of the selected slot (FUN_0049229d, 0x4922ff; rate-limited to once per 5 s). Ending with 0x44091c(7) refreshes the UI.

### 0x2004 — delete character result
- dir: S->C
- s2c: min size 0x1C; +0x10 u64 deleted char id; +0x18 u32 error sysmsg id (0 = success)
- reply: none
- confidence: medium
- notes: Handler FUN_00470140. On success in char select, FUN_00492a89 wipes the matching slot, stamps its deletion time (entry+0xa79 = now) and refreshes. An id <= 0 just closes the message box. A non-zero +0x18 shows sysmsg box type 9.

### 0x2003 — system message popup
- dir: S->C
- s2c: min size 0x1C; +0x18 u32 sysmsg id (shown in popup type 3)
- reply: none
- confidence: medium
- notes: Handler FUN_00470124; only acts while panel DAT_00850bd8 exists.

### 0x200f — jewel (cash) balance refresh
- dir: both (same opcode)
- c2s: size 0x40; extra = acct+0xec; +0x10 char[32] account name, uppercased; the rest is 0
- s2c: min size 0x40; +0x38 u32 jewel balance -> acct+0x638 (a change triggers the currency-changed notice); +0x3c u32 -> acct+0x630
- reply: 0x200f with +0x38 = jewels, +0x3c = bonus/secondary (zeros are fine)
- confidence: high
- notes: Handler FUN_004754d5. Sent from the char-select "JewelRefresh" button (0x4936a3) and from in-game code at 0x4296e0 (FUN_00429671 region); each is rate-limited to once per 10 s.

### 0x2009 — profile block, part 2
- dir: S->C
- s2c: min size 0x7C0; +0x18..+0x7BF: 0x7A8 bytes copied to acct+0x2e7c (directly after the 0x2000 profile block)
- reply: none
- confidence: medium
- notes: Handler FUN_004700e3. Refreshes UI tab 6 and fires event 0x38. FUN_00470406 (another opcode) fills the same area from +0x10 (0x5a0 bytes).

### 0x2013 — own guild-membership update
- dir: S->C
- s2c: min size 0x28; extra = the unit id it applies to (own entry); +0x18 u8 guild grade -> unit+0x656; +0x1c u16 guild id -> unit+0x27f; +0x20 u32 -> acct+0xb298 (overwrites the unread-mail counter); +0x24 u32 guild mark/emblem id -> unit+0x651 (-1 = none)
- reply: none
- confidence: medium
- notes: Handler FUN_0047018b. acct+0xb298 is written even when the unit lookup fails.

### 0x2015 — guild joined / guild data
- dir: S->C
- s2c: min size about 0x1A8 + member list; extra must equal the own unit id; +0xF4 i32 guild id -> own unit+0x27f; when it is >0: +0x10 guild info block (FUN_004b6a18(.., 4)), +0x1A8 member list (FUN_004b4e5f), then sysmsg 0x4C
- reply: none
- confidence: low
- notes: Handler FUN_00471216.

---

## World objects (spawn/despawn); needed to see anyone else

### 0x803 — spawn unit (full)
- dir: S->C. The client also builds 0x1C0-byte copies locally for debug/GM commands (0x51c620, 0x5ad82e) and passes them straight to the handler without sending them; there is no real C->S.
- s2c: extra = unit id. **Players (id < 0x3F7)**, which read up to +0x270: +0x10 char[40] name; +0x38 f32 X, +0x3c f32 Z; +0x40 u16 class/model id (must be non-zero and valid, or the packet is ignored); +0x42 u16 -> +0x659; +0x44 i16 guild id; +0x46 u8, +0x47 u8 (passed to unit creation: direction/state); +0x48 u8 guild grade; +0x49 u8 (record+0x34); +0x4a u8 team; +0x4b u8, +0x4c u8; +0x50 u32 -> +0x64d; +0x54/+0x58 u32 (record+0x38/+0x3c); +0x5c u16 (FUN_0046fe22); +0x60 0x5C-byte stats block (+0x60 u32 = current HP -> unit+0x5f8); +0xbc 0x20 bytes and +0xdc..+0xeb (appearance/equipment, record+0x40..+0x6f); +0xec u32 buff count + +0xf0 0x180-byte buff list. **Monsters/NPCs (id >= 0x3F7)**: +0x10 u16 monster template id (non-zero and valid); +0x12 u8; +0x14 f32 X, +0x18 f32 Z; +0x1c u32; +0x20 u32 HP; +0x24/+0x28/+0x2c u32 (max HP etc.); +0x30 u16; +0x34 u8 team; +0x36 u16; +0x38 u16
- reply: none
- confidence: medium (players), medium (monsters)
- notes: Handler FUN_00477d13. If the unit already exists, the packet updates it instead of creating it.

### 0x805 — spawn unit (compact)
- dir: S->C
- s2c: extra = unit id; +0x10 f32 X, +0x14 f32 Z, +0x18 u8 direction/state, +0x19 u8, +0x1a u8, +0x1b u8 team, +0x1c u16, +0x1e u16 class/template id (must be non-zero and valid). Players: +0x20/+0x24 u32, +0x28 u8 grade, +0x2a i16 guild id, +0x2c u32, +0x30/+0x34/+0x38/+0x3c u32 stats (HP first), +0x40 char[40] name -> size 0x68. Monsters: +0x22 u16, +0x24 u32, +0x28 u32 HP, +0x2c/+0x30/+0x34 u32 -> size 0x38
- reply: none
- confidence: medium
- notes: Handler FUN_0047858b.

### 0x804 — unit full refresh / respawn at position
- dir: S->C
- s2c: min size 0xBC + buffs; extra = unit id; +0x10 f32 X, +0x14 f32 Z (snaps the unit there if it is far away), +0x18 u8 direction/state, +0x19 u8 team, +0x1a u16, +0x1c u32 (FUN_00470a7b), +0x20 i16 guild id, +0x22 u8, +0x23 u8, +0x24 u8 grade, +0x25 u8, +0x28 0x5C stats block (+0x28 = HP), +0x84 0x20 + +0xa4..+0xb3 appearance, +0xb4 u16, +0xb8 u32 buff count, +0xbc buffs
- reply: none
- confidence: medium
- notes: Handler FUN_00472f4d. It updates the HUD when the unit is the player's own.

### 0x806 — remove/kill unit
- dir: S->C (the debug path also fakes it locally)
- s2c: min size 0x14; extra = unit id; +0x10 u32 mode: 1 or 6 = despawn with effect, 2 = remove immediately, 5 = dies (HP set to 0)
- reply: none
- confidence: medium
- notes: Handler FUN_00470223 -> FUN_0044e059. It never removes the player's own unit.

### 0x4ca — request unknown unit
- dir: C->S
- c2s: size 0x18; +0x10 u32 unit id the client has not seen (1..0x2B06)
- reply: send that unit's spawn (0x803 or 0x805). With no reply the client asks again at most once every 50 s per id.
- confidence: medium
- notes: Sent from inside the 0x411 handler FUN_00475654 when 0x411 names an object the client has no record of.

### 0x800 — chat message
- dir: C->S (inline-built header at 0x580e7a; FUN_004637e3 at 0x463867 sends a "/time" command the same way)
- c2s: size 0x13C; +0x10 u16 0; +0x12 u8 chat type (2 = whisper; 1 for "/time"); +0x13 u8 (DAT_00846e98); +0x14 char[40] name (whisper target, otherwise own name); +0x3c char[255] text
- s2c: no handler for 0x800
- reply: unknown here (the broadcast is a different opcode); none is required
- confidence: medium

---

## War / match data (CWarDataManager)

### 0x4b5 — war score/status update
- dir: S->C
- s2c: min size 0x54; +0x10 u16 notice kind (1 -> sysmsg 0xFF, 2 -> sysmsg 0x100, both with +0x12 as parameter; 0 = none); +0x12 u16 parameter; +0x14 u32[2] per-side value (own side's -> war+0xb0); +0x1c..+0x28 4x u32; +0x2c 6x u32; +0x44..+0x50 4x u32
- reply: none
- confidence: medium
- notes: Handler FUN_00471e7e. The notice is shown only when the extra unit exists. Fires UI events 0x1a/0x1d.

### 0x4c6 — war team stats
- dir: S->C
- s2c: min size 0x40; +0x10 4 x {u32,u32,u32}
- reply: none
- confidence: medium
- notes: Handler FUN_004711d4 -> CWarDataManager FUN_004fb254.

---

## Guild / fort / shop (fringe)

### 0x4b6 — action on a target unit (with position)
- dir: C->S
- c2s: size 0x1C; +0x10 u16 (object+0xa4); +0x12 u16 (object byte +0xa1, or a parameter); +0x14 f32 X, +0x18 f32 Z of the target unit
- reply: unknown
- confidence: low
- notes: FUN_004f98ac / FUN_004fa44d / FUN_00586bf6; fires UI event 0x45 with the target id.

### 0x4b7 — reset/refresh list
- dir: C->S
- c2s: size 0x18; empty payload
- reply: unknown
- confidence: low
- notes: FUN_005699dd clears a local 0x114-byte list before sending.

### 0x4b8 — item shop open/data
- dir: S->C
- s2c: extra must equal the own unit id; +0x10 u32 cash balance (non-zero -> acct+0xb3b4); the rest is parsed by PanelItemShop FUN_0056bf08
- reply: none
- confidence: low
- notes: Handler FUN_00471022.

### 0x4b9 — medal/fame shop purchase
- dir: C->S
- c2s: size 0x28; +0x10 u16 shop item id (item+0x5d0); +0x14 u32 count; +0x18 16 bytes item data
- reply: unknown
- confidence: low
- notes: FUN_00569e93. The client checks Money/Fame/Medal* balances first.

### 0x4ba — target/point command
- dir: C->S
- c2s: size 0x20; +0x10 u16 own unit id; +0x12 u16 mode (1 = ground point, 2 = unit); +0x14 u16 target unit id (mode 2); +0x18 f32 X, +0x1c f32 Z (mode 1)
- reply: unknown
- confidence: low
- notes: FUN_004a9930.

### 0x4bc — guild storage item move
- dir: C->S
- c2s: size 0x38; +0x10 u16 guild id; +0x12 u8 0x0B (container type); +0x13/+0x14/+0x15 u8 slot/flags; +0x18 16-byte item; +0x28 16-byte item
- reply: unknown
- confidence: low
- notes: FUN_00553cdd, FUN_00553e5e, FUN_005794d3. The client error "GUI_Guild_ErrMsg_CoreEquipPermision" suggests guild core equipment.

### 0x4bd — guild info block
- dir: S->C
- s2c: min size 0x74; +0x10 i16 guild id (must equal the current guild); +0x14 0x60 bytes -> guild+0x128
- reply: none
- confidence: low
- notes: Handler FUN_004715b6.

### 0x4be — guild action
- dir: C->S
- c2s: size 0x18; +0x10 u32 guild id; +0x14 u32 parameter
- reply: unknown
- confidence: low
- notes: FUN_00559a59 (guild panel).

### 0x4bf — guild status update
- dir: S->C
- s2c: min size 0x2C; +0x10 u32 sysmsg id (0 = none); +0x14 u32 guild id (must match); +0x18 u32 sysmsg parameter; +0x1c u32 -> guild+0xf0; +0x20 u8; +0x22 5x u16
- reply: none
- confidence: low
- notes: Handler FUN_00471611.

### 0x4c0 — guild request with value
- dir: C->S
- c2s: size 0x24; +0x10 u32 guild id; +0x14 u32 value (u16 list entry); +0x18 u8; +0x1c u32 and +0x20 u32 (sceneidx, or an argument)
- reply: unknown
- confidence: low
- notes: FUN_00559a59 and FUN_0057349b.

### 0x4c1 — numeric input submit
- dir: C->S
- c2s: size 0x18; +0x10 u32 flag 0/1; +0x14 u32 number typed in a text box
- reply: unknown
- confidence: low
- notes: FUN_005634df.

### 0x4c2 — money update
- dir: S->C
- s2c: min size 0x18; extra = own unit id; +0x10 u32 -> acct+0x341c; +0x14 u32 gold -> unit+0x283
- reply: none
- confidence: medium
- notes: Handler FUN_004702af; fires UI event 0x1b.

### 0x4c3 — fort mastery item
- dir: C->S
- c2s: size 0x1C; +0x10 u32 fort index (acct+0x64c, 0..19); +0x14 u32 item id; +0x18 u8
- reply: unknown
- confidence: low
- notes: FUN_00532f62; FortMasteryItem2.panel. Requires guild == mapGuild.

### 0x4c5 — unit guild mark update
- dir: S->C
- s2c: min size 0x18; extra = unit id (< 0x3F7); +0x10 u32 mark id -> +0x651; +0x14 u8 grade -> +0x656; +0x15 u8 -> +0x64b
- reply: none
- confidence: medium
- notes: Handler FUN_00470848.

### 0x4c7 — guild member action
- dir: C->S
- c2s: size 0x20; +0x10 u16 guild id; +0x12 u16; +0x14 u32 argument; +0x18 u64 own char id
- reply: unknown
- confidence: low
- notes: FUN_004b4d75; rate-limited to once per 5 s.

### 0x4c8 — guild/panel action result
- dir: S->C
- s2c: min size 0x14; +0x12 u16 code: 0x11C/0x11D show a sysmsg, 0x11E shows "TryAgainPlease"
- reply: none
- confidence: low
- notes: Handler FUN_00476d05; afterwards it closes a pending-panel flag.

### 0x816 — fort donation
- dir: both
- c2s: size 0x1C; +0x10 u32 fort index (acct+0x64c); +0x14 u32 amount; +0x18 u32
- s2c: min size 0x1C; +0x18 u32 new gold -> own unit+0x283
- reply: 0x816 with +0x18 = remaining gold (shows "GUI_FortDonate_Sucess")
- confidence: medium
- notes: Send site FUN_005293ab; handler FUN_00476e53.

---

## Mail

### 0x808 — mail recipient lookup
- dir: both
- c2s: size 0x48; +0x18 char[40] recipient name
- s2c: min size 0x18; +0x10 u64 char id: (0xFFFFFFFE,0xFFFFFFFF) -> result 2; all-ones or 0 -> 1 (not found); anything else -> 0 (OK)
- reply: 0x808 with the recipient's char id
- confidence: medium
- notes: Send site FUN_0053ca95; handler FUN_0047056b (event 0x2f).

### 0x809 — send mail
- dir: C->S
- c2s: size 0x328; +0x10 u64 own char id; +0x18 char[40] recipient; +0x48 u8 mail kind (1 = bill, 0x10 = with attachment/money); +0x4c u32 money; +0x50 char[40] own name; +0x80 5 x 16-byte attached items; +0xd8 5x u16 counts (0xFFFF = empty); +0xe2 wchar[256] body; +0x2e2 wchar[32] title
- reply: unknown (none is required)
- confidence: low
- notes: FUN_0053d182.

### 0x80a — take attachments from selected mails
- dir: C->S
- c2s: size 0x68; +0x10 u64 own char id; +0x18 up to 10x u64 mail ids
- reply: unknown
- confidence: low
- notes: FUN_0053e862.

### 0x80b — new mail notice
- dir: S->C
- s2c: min size 0x20; +0x18 u32 total mails -> acct+0xb29c; +0x1c u32 unread -> acct+0xb298
- reply: none
- confidence: medium
- notes: Handler FUN_00476dd6 ("msg_mailarrival").

### 0x80c — read mail
- dir: both
- c2s: size 0x20; +0x10 u64 own char id; +0x18 u64 mail id
- s2c: min size 0xA4; +0x10 u64 mail id (must be in the client's mail list); +0x18 u8; +0x19 u8 read flag; +0x1c u32; +0x50 0x54-byte body/attachment block
- reply: 0x80c with the mail contents
- confidence: medium
- notes: Send site FUN_0053dfdb; handler FUN_00474f00. That handler also handles 0x80f.

### 0x80d — take one attachment / pay bill
- dir: C->S
- c2s: size 0x18; the payload is always zero. The client writes the mail id at +0x10 and then calls FUN_004a730b(clear=1), which wipes it.
- reply: unknown
- confidence: medium (the client bug is certain)
- notes: FUN_0053e862.

### 0x80e — take money attachment
- dir: C->S
- c2s: size 0x18; the payload is always zero (same write-then-clear bug as 0x80d)
- reply: unknown
- confidence: medium

### 0x80f — mail update
- dir: S->C
- s2c: same layout as 0x80c S->C
- reply: none
- confidence: medium
- notes: Handler FUN_00474f00.

---

## Friends

### 0x811 — friend invite
- dir: C->S
- c2s: size 0x58; +0x10 u32 0; +0x18 u64 own char id; +0x28 char[40] target name
- reply: none is required. Forward it to the target as 0x813.
- confidence: medium
- notes: FUN_004b6b31 and FUN_00531320.

### 0x812 — friend invite answer
- dir: C->S
- c2s: size 0x28; +0x10 u32 1 = accept, 0 = decline; +0x18 u64 own char id; +0x20 u64 inviter char id
- reply: unknown
- confidence: medium
- notes: FUN_00530b0a.

### 0x813 — friend invite received
- dir: S->C
- s2c: min size 0x50; +0x18 u64 inviter char id (must be non-zero); +0x28 char[40] inviter name
- reply: the client answers with 0x812
- confidence: medium
- notes: Handler FUN_00476ed3 ("GUI_Friend_MB_RecvInvite_S").
