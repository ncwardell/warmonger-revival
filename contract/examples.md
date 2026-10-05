# Client-built packets: ground-truth examples

These are the places where the client builds a packet buffer itself. Each section below covers either
(A) a server->client packet the client builds and passes straight to its own S->C handler, or (B) a
debug or GM path that sends to the server. Every offset is counted from the start of the packet (the
16-byte header is +0x00..+0x0f).

Search method: every direct call to the 124 S->C handlers in `opcodes.tsv`, made from anywhere except
the dispatcher `FUN_0047a36c`; every call that follows the net-singleton getter `FUN_00411a7b`
(202 go to the send function `FUN_0046ff99`; the rest are listed here); every call to
`FUN_004a730b`; and the inline `0xa53c` headers. `FUN_0047a36c` has exactly one caller, the
receive pump `FUN_0047ada9`. No replay or injection path pushes into the receive queue
(`FUN_004a74a4` has one caller).

`FUN_004a730b(buf, opcode, size, extra, clear)` writes: `u32 +0x00 = size | 0xA53C0000` (so u16 length,
u16 magic), `u16 +0x04 = opcode`, `u16 +0x06 = extra`, and zero-fills `size` bytes first when
`clear` is set. It **never writes tick (+0x08) or key (+0x0c)**: the local examples carry tick = 0
and key = 0, and the handlers accept that.

Totals for (A): **0x803 x2, 0x806 x4, 0x44e x1, 0x416 x1** (8 local packet sites in 5 functions).

---

## A. S->C packets the client builds and passes to its own handler

### A1. Script/cutscene interpreter `FUN_005ad62b`: `exit`, `teleport`, `createmob`, `removemob`, `talkmob`

This is not a typed console. It runs one line of a timed script. The player `FUN_005ada1c`
walks a vector of 0x40-byte entries: `+0x04` u32 start time in seconds since the script began, and
`+0x08` a std::wstring command line. Each entry runs once, when the elapsed time reaches its start.
`FUN_0042d2b4` splits the line on **`,`** (L"," at 0x7265f4), so a line looks like
`createmob,1,512.0,768.0,1001,500,500`.
Token 0 is the command. Numbers go through `_wtoi` (0x6dc85a) or `_wtof` (0x6dd778).
Caller: the game-scene tick `FUN_0048d666` at 0x48e2f0, only `if (DAT_00854324 != 0)`. **Nothing
in the binary writes DAT_00854324**, so the shipped client cannot reach this code (dead debug
code). The packets are still valid templates, because they go through the real handlers.
Scripted units use uid **0x2B07 + n**, just above the normal range (C->S 0x4ca asks for ids
1..0x2B06).

| command (token count) | opcode, size, handler | header extra | fields set (all others 0) | site |
|---|---|---|---|---|
| `exit` (any) | 0x806, 0x14, `FUN_00470223` | 0x2B07+i, for i = 0..99 | +0x10 u32 = **1** (despawn with effect) | 0x5ad6d0 |
| `teleport,n,x,z` (exactly 4) | 0x44e, **0x2c**, `FUN_00473548` | local player uid (`[player+0x35e]`) | +0x14 f32 x = `_wtof(tok2)`; +0x18 f32 z = `_wtof(tok3)`. tok1 is parsed but not used. +0x10 mapid = 0, +0x12 sceneidx = 0, +0x1e mapfort = 0, +0x20.. = 0 | 0x5ad761 |
| `createmob,n,x,z,id,hp,maxhp` (exactly 7) | 0x803, **0x1c0**, `FUN_00477d13` | 0x2B07 + `_wtoi(tok1)` | +0x10 u16 unit template id = tok4; +0x14 f32 x = tok2; +0x18 f32 z = tok3; +0x20 u32 HP = tok5; +0x24 u32 max HP = tok6. +0x12 level, +0x13 category, +0x32 heading, +0x33 spawnFx, +0x34 team all 0 | 0x5ad82e |
| `removemob,n,mode,...` (needs **7** tokens: a copy-paste quirk) | 0x806, 0x14, `FUN_00470223` | 0x2B07 + tok1 | +0x10 u32 mode = `_wtoi(tok2)` (1/6 despawn with effect, 2 remove now, 5 die) | 0x5ad8d2 |
| `talkmob,n,text` | (no packet) | - | looks up unit 0x2B07+n (`FUN_0044d3b9`), adds the text to chat (`FUN_0057fd07`) and shows a speech balloon (`FUN_004be849`) | 0x5ad90d |

Takeaways:
- **0x44e with only extra, x and z set is a valid in-scene warp.** mapid 0 / sceneidx 0 is accepted.
  (Sceneidx 0 differs from a live sceneidx, so on a real server keep the current sceneidx; see loading.md.)
- **0x803 needs only template id + x + z + HP + maxHP** to create a working monster. Coordinates are
  absolute world floats.
- A tick of 0 is accepted everywhere.

### A2. PanelDevTest button 3 "createmob" (`FUN_0051c52e`, site 0x51c620 -> 0x51c6c4)

Panel `ui/Panel/test/PanelTestDev.panel`, class `PanelDevTest` (vtables 0x737974 / 0x737944,
panel id 0x92, built in `FUN_0045cc71`). No code that opens it was found (no `0x92` open
call). The button dispatcher is `FUN_00520368` (switch on button index). The edit boxes are
Edit0..Edit4 = this+0x28/0x2c/0x30/0x34/0x38. The panel's own help string (0x737650) reads
"0 = index, 1=HP, 2=direction, 3=nation, 4=distance".

Toggle: if unit **0x2B06** already exists, it removes it (`FUN_0044cf52(0x2B06,0,0.0)`) and builds no
packet. Otherwise, if Edit0 is non-zero and a valid UnitDB id (`FUN_00499180`):

| offset | type | value |
|---|---|---|
| +0x00 | u16/u16 | 0x01C0, 0xA53C |
| +0x04 | u16 | 0x803 |
| +0x06 | u16 extra | **0x2B06** (fixed test-mob uid) |
| +0x10 | u16 | unit template id = Edit0 |
| +0x14 | f32 | player world X − Edit4 ("distance"). World X = segX*256 + local x (`FUN_0049b7f6`) |
| +0x18 | f32 | player world Z |
| +0x20 | u32 | HP = Edit1 |
| +0x24 | u32 | max HP = Edit1 |
| +0x32 | u8 | heading/direction = Edit2 (low byte, signed) |
| +0x33 | u8 | **1** (spawn effect on) |
| +0x34 | u8 | nation/team = Edit3 |
| rest | | 0 (tick and key 0) |

This confirms the monster branch layout in group03 and monsters.md: +0x32 heading, +0x33 spawnFx,
+0x34 team/nation, HP at +0x20 and max HP at +0x24. It also confirms that **0x803 X/Z are absolute
world coordinates**.

### A3. Server list packets re-issued as single packets (shipped code)

These run in the live client, so they show the minimal packet each handler needs.

**0x43f -> 0x416 (`FUN_004751ca`, site 0x475247 -> `FUN_004728ff`).** For each of the 40 entries at
0x43f+0x14 (12 bytes: s16 id, u16 speed, f32 x, f32 z) with id > 0 and id != own uid, it zeroes a
**0x20-byte** buffer **with no length, magic or opcode** and fills it:

| offset | value |
|---|---|
| +0x06 | entity id |
| +0x08 | tick, copied from the 0x43f header +0x08 |
| +0x10 u8 | **0x7F** (heading) |
| +0x11 u8 | **0x20** (move type 0x20) |
| +0x12 u8 | 0 |
| +0x14 u16 | speed |
| +0x18 f32 | x |
| +0x1c f32 | z |

**0x43f -> 0x806 (`FUN_004751ca`, site 0x475281) and 0x49b -> 0x806 (`FUN_00470508`, site 0x47054d)**: a
0x14-byte zeroed buffer, also with no length, magic or opcode: `+0x06 = id`, `+0x10 = (i32)(s8)state`.
Source lists: 0x43f+0x1f4 (15 x {u16 id, s8, u8}) and 0x49b+0x12 (200 x {u16 id, s8, u8}).
So the 0x416 and 0x806 handlers read only extra, tick and payload; they never check length, magic or opcode.

### Not a packet, but it reuses server data the same way
`FUN_005adc10` (char-select preview) and `FUN_0048b435` (game-scene entry) build units with
`FUN_0044f6a3` from the stored 0x240-byte slot records of S->C 0x2001. That is why the server does not
send a 0x803 for the player's own unit.

---

## B. The command table and the GM and debug paths that send to the server

### B1. Command table (static, 0x833aa0, 24 entries x 0x114 bytes, built by `FUN_00463901` into `DAT_0084b0cc`)

Entry layout: +0x00 u32 index, +0x04 u32, +0x08 u32 code for C->S **0x404**, +0x0c u32 code for C->S
**0x495**, +0x10 char[256] name, +0x110 local function pointer. Two lists are built:
- list A (`*tbl`), entries with +0x0c == 0. **Chat `/name args`** looks names up here
  (`FUN_0057ed4c` -> `FUN_004634bc`). The only such entry is `time`.
- list B (`tbl+0x10`), all entries. Used by the **GMTool "EditCheat" box (`/command`, Tab key)**:
  `FUN_005216d6` -> `FUN_004635f5`.

| name | 0x495 code | name | 0x495 code |
|---|---|---|---|
| move | 0x0a | fortmove | 0x6a |
| fame | 0x0e | mobkill | 0x0f |
| serveropen | 0x64 | mobhp | 0x10 |
| servershutdown | 0x65 | mobcreate | 0x11 |
| worldnotice | 0x67 | towerreset | 0x6b |
| notice | 0x68 | castle | 0x12 |
| usercount | 0x69 | newbiechannel | 0x12f |
| worldservershutdown | 0x66 | droprate | 0xc8 |
| nationblock | 0x134 | medaldouble | 0xc9 |
| returnuser | 0xca | returnuserset | 0xcb |
| pvpbotenable | 0xcc | botaiolduse | 0xcd |
| msprocessuse | 0xce | **time** | local fn 0x46382b (sends chat 0x800 type 1 "/time") |

Packet formats (C->S, extra = own uid):
- **0x495 GM command** (size 0x118): +0x10 u32 code, +0x14 u32 0, +0x18 char[256] = the arguments
  joined with single spaces (the command name is not included).
- **0x404 cheat** (size 0x114, header built inline as 0xA53C0114): +0x10 u32 code (entry +0x08),
  +0x14 char[256] arguments. No entry has a non-zero +0x08, so 0x404 is never sent in this build.
- Chat `/partyinvite`-style localized command (`FUN_0057e71d`, key "ccmd_partyinvite") sends a
  party-invite packet with a char[40] name. It is not a GM command.

### B2. GMTool panel buttons (`FUN_00521bfa`, `ui/Panel/test/GMTools.panel`, panel id 0x90)
Opened from the system menu button "GMTool" (`FUN_0057c585`). The server can also open it with S->C 0x496.
Every button sends C->S 0x495 (0x118 bytes), with +0x14 = 0 and +0x18 = text:

| button | +0x10 code | +0x18 text |
|---|---|---|
| Search | 1 | name typed in EditName |
| Teleport | 2 | "%d" selected user uid (go to the user) |
| Kick | 3 | "%d" uid |
| Summon | 4 | "%d" uid |
| Recall | 5 | "%d" uid |
| MapMove | 6 | "%d" map id of the chosen field |
| ToggleSnoop | 8 | - |
| ToggleNoDam | 9 | - |
| TKill | 0xf | "%d" target uid |
| THpEdit | 0x10 | "%d %s" target uid, HP |
| CastleMove | 0x12 | "%d" castle 1..3 |
| BtnNotice / BtnWorldNotice (`FUN_00521194`) | 0x68 / 0x67 | notice text |
| BtnCheat | from the table (B1) | arguments |
| ToggleChat / ChannelMove / BtnClear | local only (ChannelMove = `FUN_00489d6d(10,0)`) | |

### B3. Other PanelDevTest buttons (`FUN_00520368`)
| button | effect |
|---|---|
| 0 `FUN_0051ef27` | lists nearby units (local text) |
| 1 `FUN_0051f196` | shows own unit, guild, war and fort info (local) |
| 2 `FUN_0051c4a7` | **C->S 0x44e** (0x28 bytes, extra = own uid): +0x10 u16 = Edit1, +0x14 u32 = Edit0 (destination id), +0x1c u32 = 0 (cost). It is a debug warp request, which the server must answer with S->C 0x44e |
| 3 `FUN_0051c52e` | local 0x803 (A2) |
| 4 `FUN_0051c3d0` | changes a unit's appearance parts (local) |
| 5 `FUN_0051d12e` | region data tool (999 = dump to d:\file.txt) |
| 6 `FUN_0051cb3c` | texture animation test |
| 7 `FUN_0051d4e3` | achievement UI test |
| 8 `FUN_0051d667` | effect test |
| 9 `FUN_0051cc28` | item grade test |
| 10 `FUN_0051fff5` | quest bit dump ("0:info 1:UpdateReady 2:SfxRefresh") |
| 0x0b | `FUN_004be462(Edit0)`, local model swap |
| 0x62 / 0x63 | **C->S 0x401** (0x1c bytes, inline header 0xA53C001C, extra 0): +0x10 u32 = 1 / 0. This opcode is missing from opcodes.tsv. Its meaning is unknown (a dev toggle); no reply is needed |

---

## Server-side recipes taken from these examples
- Warp in place: `0x44e`, size 0x2c, extra = uid, +0x10 mapid, +0x12 **current** sceneidx, +0x14/+0x18 f32 x/z.
- Minimal monster spawn: `0x803`, size 0x1c0, extra = uid, +0x10 template, +0x14/+0x18 world x/z,
  +0x20 HP, +0x24 maxHP, +0x32 heading, +0x33 spawnFx (1 = play the appear effect), +0x34 team. Follow it with 0x804 for speed (monsters.md).
- Despawn: `0x806`, size 0x14, extra = uid, +0x10 = 1 (with effect) or 2 (immediately). Die: 5.
- Bulk move: `0x416`, size 0x20: +0x10 heading, +0x11 type (0x20 is what 0x43f expands to), +0x14 speed, +0x18/+0x1c x/z.
