# Match / battlefield lifecycle (queue → match → result → back to world)

Client: Client.exe (32-bit MSVC). Addresses are VAs. `acct` = `*DAT_00847ac8`. `self` = own unit
`DAT_0084a758` (uid at `+0x35e`, char record at `+0x3a0`). `mgr` = the match manager
**CWarDataManager**, singleton `DAT_0084a75c` (0x2b0 bytes), created by `FUN_0044ad5f`, ctor
`FUN_004fbedc`, reset `FUN_004fbd4c`. The opcodes below extend group00..03. Where those specs
disagree with this file, this file is newer and was read from the code more closely.

Confidence: **H** = read from code at every step. **M** = layout certain, meaning inferred.
**L** = guess.

---

## 0. The pieces

| Piece | Where | What |
|---|---|---|
| Queue state | `acct+0xb1b0..+0xb293` (0xe4 bytes) | `+0xb1b0` u8 "offer present" (gates the Match button), `+0xb1bc` u8 queue state, `+0xb1bd` offer kind, `+0xb1be`, `+0xb1b4` offer-expiry tick, `+0xb1c0` 5×u16 team uids, `+0xb1ca` 5×char[40] names |
| Match manager | `mgr` | `+0xad` u8 **match type**, `+0xac` u8 **match state**, `+0xae` u8 progress %, `+0xa4` u32 remaining s, `+0xa8` clock at receipt, `+0xb0` u32 **own team TP (score)**, `+0xb4` i8 **own team index** (0/1, -1 = none), `+0xb6` u16[2] team "side" values, `+0x0c` u32[30] room roster uids, `+0x84` i8[30] room roster team (-1 = undecided), `+0x04` "I am host", `+0x08` host uid, `+0xcc` [2][15]{u32 uid, u16 kills, u16 assists} team table, `+0x204/+0x214` std::vector of 0x68-byte scoreboard rows per team, `+0x224..+0x24c` result block, `+0x250/+0x260` frozen final scoreboard, `+0x1d4` 4 minimap pings |
| Match-type table | `DAT_0083a888`, 8-byte rows, looked up by `FUN_004fb1ee(type)` (unknown type → row 0 = all zero) | see §2 |
| HUD | `Teamscore.panel` (FUN_0054e505 init, FUN_0054ea05 draw, FUN_0054eee9 events) | Time, Kill/Assist, Defence/Attack badge, Tower0-2/DTower0-2, FortWarGauge, TP gauge "TP: %d / 10000" |
| Tab scoreboard | PanelGameInfo (FUN_00543f95) | rows from `mgr+0x204/+0x214`, or from the frozen `+0x250/+0x260` once a result arrived |
| Result | PanelGameResultSimple, GUI id 0x43 (`GameResultSimple*.panel`, FUN_005432b8 / FUN_00543318 / render FUN_005434b5) | Win/Lose, medals, money, fame, legion fame/contribution |
| Lobby | `CustomGameList/Create/Match/Invite/Rejoin.panel` | custom rooms (§6) |

"Match active" predicate `FUN_004fb2c2`: `type != 0 && state ∉ {0, 7, 9}`. The HUD and several
gameplay checks key off this (H).

---

## 1. Ordered sequence: offer → solo queue → match → result → back to world

All packets use the 16-byte header (u16 len, u16 0xA53C, u16 opcode, u16 extra, u32 tick, u32 key).
For S→C, `extra` = the subject unit uid where noted. Otherwise use the player's uid (harmless).

### Step 1. Offer the match (S→C 0x470, state 0). H
Size 0xec. `+0x10` u8 0 · `+0x11` u8 **offer kind**: 0 = "War of Warmonger is being held",
1 = "Battle Arena is held" (`GUI_MatchPopup_Message_%d` / `GUI_Minimap_Match_Join_%d`) · `+0x12` u8
(echoed back; use 0) · `+0x14` i16 sysmsg id (0 = none) · `+0x16` u16[5] 0 · `+0x20` char[5][40] 0 ·
`+0xe8` u32 offer lifetime in seconds.
Handler `FUN_004705ac`: `acct+0xb1b0 = 1`, expiry = now + `+0xe8`*1000. The minimap tick
`FUN_00572593` memsets the whole 0xe4-byte queue block when the expiry passes while the state is still 0.
**Safe default: `+0xe8` = 86400.** Re-push after login, after every match, and after a cancel.

### Step 2. Player clicks Match → Single (C→S 0x470). H
Size 0xec: `+0x10` u8 1 (solo) / 2 (team, from MatchTeam.panel) / 4 (cancel) · `+0x11` = offer kind ·
`+0x12` = echo. Sender `FUN_005360a0` (Single sets `+0xb1bc = 1` locally before sending).

### Step 3. Acknowledge the queue (S→C 0x470, state 1). H
Same size and layout with `+0x10 = 1` (2 for a team). The minimap shows "Queue" (`GUI_Minimap_Match_Waiting`).
For team queues, `+0x16`/`+0x20` hold the members and state 3 means "team formed" (group01).

### Step 4. Match found → scene change into the match map (S→C 0x44f, or 0x44e). H
- 0x44f size 0x1bc: `extra` = player uid · `+0x10` u16 mapid (140 "Battle Arena", 141 "Temple", or the
  arena's field id) · `+0x12` u16 sceneidx **≠ the current sceneidx** (that difference is what makes it
  a full reload) · `+0x14` f32 x · `+0x18` f32 z · `+0x1e` i8 -1 · `+0x1f` u8 0 · `+0x20` u32 0 · `+0x24/+0x28` 0 ·
  `+0x2c` 400-byte scene-object table (zero if the map has no gadgets).
- Side effects of a scene change (handler `FUN_00473ab5` / `FUN_00473548`, H):
  **`FUN_004fbd4c(1)` wipes the match manager.** The result panel, if open, has its button turned into a
  plain "Close" (`FUN_00543270`). All non-own entities are dropped (`FUN_00486ff1`). A new
  CLoadingProcess starts. **So every match packet (0x43b/0x43c/0x43a) must come after this warp, never before.**
- The x/z must fall on an existing terrain zone piece (`Map/ZPxx_yy_00.zp`, 256-unit grid). mapid does
  not pick terrain (loading.md). The arena is just another area of the single world grid. **Its
  coordinates are the main unknown** (§8).
- No "match found / accept" round trip is needed by the client. (`msgbox_battlearenainvite.panel`,
  GUI 0x81, "StrDef_AreYouJoinMatch", exists, but no packet path to it was found. L.)

### Step 5. Match info / start (S→C 0x43b). H (layout), M (meanings)
Handler `FUN_00471125` → `FUN_004fc4e7`. **Size 0x16e.**

| off | type | meaning |
|---|---|---|
| +0x10 | u8 | match type (§2), → `mgr+0xad` |
| +0x11 | u8 | state, → `mgr+0xac`. **3 = start** (the client rewrites it to 4 = "in progress" and fires UI 0x32 twice). 1 = recruiting/lobby, 2 = (L) preparing |
| +0x12 | u8 | progress 0..100 (gauge for type 8 only), → `+0xae` |
| +0x13 | u8[2] | → `mgr+0xbc/+0xc0` (unknown, 0) |
| +0x16 | u16[2] | team side values, → `mgr+0xb6`. Type with flag2=1: the custom team ids written to every roster member's `char+0x659` when state==3 (use **1 and 2**; 0 means "no match team"). Type with flag2=0: the nation id per side (`char+0x655`); 4 = "any other nation" |
| +0x1c | u32 | remaining time in seconds (the HUD counts down locally; display is capped at 5940 s) |
| +0x20 | [2][15] × {u32 uid, u16 kills, u16 assists} | team table, → `mgr+0xcc`. **Team 0 = Defence, team 1 = Attack.** Own team index `mgr+0xb4` = the team whose table holds self's uid |
| +0x110 | u32[2] | TP per team. Own team's value → `mgr+0xb0` (TP gauge, cap 10000) |
| +0x118 | 2×{u32,u32} | → `mgr+0x288..` (L, war panel) |
| +0x128 | 3×{u32,u32} | → `mgr+0x298..` (L) |
| +0x140 | 2×{u32,u32} | → `mgr+0x278..` (L) |
| +0x150 | u32[4] + u16 (+0x160) | → `mgr+0x1bc..+0x1cc` (same as 0x43d; no reader found) |
| +0x162 | u16[6] | queue/dungeon panel counters (only used if that panel is open) |

Notes:
- If the client is still queued (`acct+0xb1bc` ∈ {1,2}) when 0x43b/0x43c/0x43a arrives, it calls
  `FUN_00428e81`, which **sends C→S 0x470 action 4** and clears the queue UI. The server must ignore a
  0x470 cancel from a player who is already in a match (H). An alternative is to clear the queue silently
  before the warp with S→C **0x41b id 3** (memsets the queue block). That also shows sysmsg 3.
- Scoreboard rows are built only for units that are spawned (`FUN_0044d3b9` lookup), so spawn the
  participants (0x803, `+0x42` u16 = match team → `char+0x659`) before or right after 0x43b. A later
  spawn of a player unit auto-slots it into a team (`FUN_00487a34` → `FUN_004fc393`, by `char+0x659` or
  nation, depending on flag2).
- Enmity during a match (`FUN_00486179`, H): if **both** units have a non-zero `char+0x659`, they are
  enemies iff the values differ. Otherwise nations decide (`+0x655`: 0 = neutral, equal = ally, ≥ 4 = hostile).

### Step 6. While the match runs (all optional for the client). M
- **0x4b5** (size 0x54, group03) is the cheap score tick: `+0x14` u32[2] TP per team → `mgr+0xb0`
  (own), UI 0x1a/0x1d refresh the TP gauge. `+0x10` notice kind 1/2 → sysmsg 0xFF/0x100 with
  `+0x12` as parameter. `+0x1c..+0x50` → `mgr+0x278..+0x2ac` (L).
- **0x43a** (size 0x15a, `FUN_004fc840`) is the full status refresh: `+0x10` state · `+0x11` progress ·
  `+0x14` u32 remaining s · `+0x18` u32[2] TP per team (applied only when the state changed) · `+0x20`
  team table (same as 0x43b +0x20; the rows are rebuilt if any uid changed) · `+0x110/+0x120/+0x138`
  blocks as in 0x43b · `+0x148` u32[4] + u16. Use it to change state, e.g. to 7/9 at the end (L: 7/9
  are the two "finished" states; both hide the HUD).
- **0x443** (size 0x68, `FUN_004fcc10`) is a kill: `+0x10` u16 killer uid · `+0x12` u16 victim uid ·
  `+0x14` u16 points to self if self is the killer · `+0x16` u16 points to self if self assisted
  (both added to `char+0x233`, capped 31,250,000) · `+0x18` u16[15] and `+0x36` u16[15] assister uids ·
  `+0x54` u32[2] TP per team (→ own TP) · `+0x5c/+0x60/+0x64` u32 → killer `char+0x613/617/61b`.
  The client increments the killer's kills and each assister's assists on its own copy of the rows.
- **0x439** minimap ping (`+0x10` u8 flag, `+0x14` f32 x, `+0x18` f32 z) and **0x4c6** 4 timed minimap
  markers (`+0x10` 4 × {u16 seconds-to-show (<121), u16 uid (0 = static), f32 x, f32 z}; the timer is
  decremented once a second by `FUN_00572593`). Correction to group03: 0x4c6 is not "team stats".
- **0x450** capture/channel (group01): on completion `+0x18` becomes the target's `char+0x659`
  (flag2=1) or `+0x655`. This is how capture objectives change side.
- **Objective display**: towers are units with kind `+0x35c == 0x1f`. The HUD counts the visible ones and
  shows Tower/DTower icons per side. Units of kind 0x22/0x23 are attackable only in state 4. The
  displayed goal is the TP gauge **"TP: x / 10000"** plus the countdown. The client never decides the
  winner; the server does, in 0x440.

### Step 7. Result (S→C 0x440). H (layout), M (labels)
Handler `FUN_004711ea` → `FUN_004fc9c5`. Requires self spawned. **Size 0x220.**

| off | type | effect |
|---|---|---|
| +0x10 | u8 | **result: 0 = win (WinImg), 1 = lose (LoseImg)**, other = neither. Also feeds a win/lose counter (`FUN_0059c2ab(1/2)`) |
| +0x11 | u8 | → `char+0x296` (echo the current value; 0 is fine) |
| +0x12 | u8 | → `char+0x656` (**echo the current value**; it is the value shown in the scoreboard's Race column) |
| +0x14 | u8 | match type for the result panel (13 = no medal section; 8/9 = fort-war value + Attack/Defence text) |
| +0x18 | u32 | → `mgr+0x228` |
| +0x1c/+0x20/+0x24 | u32 | Gold / Silver / Bronze medal counts |
| +0x28 | u32 | Legion contribution (section hidden if 0) |
| +0x2c | u32 | Legion fame (hidden if 0) |
| +0x30 | u32 | Fame (hidden if 0); **added** to `char+0x287` and `+0x651` |
| +0x34 | u32 | icon flags: 0x08/0x10/0x20 medal-icon variants, 0x40, 0x80, 0x200/0x400/0x800/0x1000 highlight the four medal rows |
| +0x38 | u32 | fort-war value (types 8/9) |
| +0x3c | u32 | Money; **added** to gold `char+0x283` (hidden if 0) |
| +0x40 | u16 | → `char+0x297` via `FUN_004bf8c1` (title/emblem; **echo current**) |
| +0x44 | 0x5c bytes | stat block → `char+0x443` (`FUN_004bc97c`). **Must be the real stats: HP < 1 = dead** |
| +0xa0 | 0x180 bytes | 32 × 12-byte slot table → `char+0x49f` (`FUN_004bf542`, equipment/visual). **Echo the current table or the gear disappears** |

Then the client freezes the scoreboard (`+0x224 = 1`, rows copied to `+0x250/+0x260`), fires UI
**0x33**, which opens/refreshes GameResultSimple, applies the rewards, and **resets the manager to state 0**
(`FUN_004fbd4c(1)`). The HUD disappears.

### Step 8. Back to the world. H
- The result panel button is "Close" (normal types) or "Exit" (types with flag2=1). For types with
  flag2=1, pressing it sends **C→S 0x442, size 0x18, `+0x10` u32 = 1** ("leave match", site 0x543237).
  The Tab scoreboard's ExitAtt/ExitDef send the same thing for types with flag5 (site 0x543f4c).
- The server then (or after a timeout of a few seconds for normal types) sends **0x44f/0x44e back to the
  world**: original mapid, a **different sceneidx** from the arena's, and a valid world x/z. This reloads,
  wipes the manager again, and turns the result panel button into "Close".
- Re-spawn nearby entities, then **re-push 0x470 state 0** so the Match button comes back
  (`FUN_00428e81` cleared `acct+0xb1b0`).

**0x48d is not part of this flow.** It is the field-war score sheet for the World Map
`GameInfoWM.panel` (FUN_00578e21 → FUN_00576302, refreshed on UI 0x23 only while that panel is open). M.

---

## 2. Match types (`DAT_0083a888`, dumped from .data). H (values), M (flag meanings)

Row = `type, f1..f7`:

| type | f1 | f2 | f3 | f4 | f5 | f6 | f7 | notes |
|---|---|---|---|---|---|---|---|---|
| 2 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | normal queued match, teams by nation |
| 3 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | same |
| 4 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | same |
| 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | no scoreboard |
| 6 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | **custom room** (lobby, team ids) |
| 7 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | team ids, no lobby |
| 8 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | fort war (FortWarGauge, `+0xae` %) |
| 9 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | fort war |
| 0xa | 1 | 1 | 1 | 1 | 1 | 0 | 1 | custom room |
| 0xc | 1 | 0 | 0 | 0 | 0 | 0 | 1 | |
| 0xd | 1 | 1 | 0 | 0 | 0 | 0 | 1 | no medals in the result |

- f1 = keep per-team scoreboard rows (`FUN_004fc016`).
- f2 = teams by `char+0x659` match-team id (1) vs by nation `+0x655` (0).
- f3 = scoreboard panel usable in state 1.
- f4 = custom room (0x441/0x442 room packets accepted, lobby auto-opens).
- f5 = Exit buttons send 0x442(1).
- f6 = gates something in `FUN_0055815c` (L).
- f7 = towers (kind 0x1f/0x22) drawn hostile (`FUN_0058c9e8`, L).

Types 2/3/4/8/9/13 also block some world action in `FUN_00489d6d` (L).

---

## 3. Teams, score and win condition (summary)

- Two sides, index **0 = Defence ("GUI_GameInfo_Defence"), 1 = Attack ("Intruder")**. The Custom lobby
  buttons "Def" → 0, "Att" → 1, and the result text uses FortWarStrD for team 0. H for the mapping in code;
  the labels come from panel element names.
- Membership: the `[2][15]` uid table in 0x43b/0x43a (authoritative for "my team"), plus `char+0x659`
  from 0x803 `+0x42` or 0x43b state 3, which drives friend/foe.
- Score: TP per team (0x43b +0x110, 0x43a +0x18, 0x443 +0x54, 0x4b5 +0x14), shown as a gauge out of
  **10000**. Personal kills/assists live in the team table / 0x443.
- Win: decided by the server, shown by 0x440 `+0x10` (0 win / 1 lose). A plausible rule is first to 10000 TP,
  or higher TP when the timer ends (L).

---

## 4. Minimal 1-player test match

1. (after enter-world) **0x470** state 0, `+0x11` 1, `+0xe8` 86400.
2. Client → 0x470 action 1. Reply **0x470** state 1.
3. **0x44f** (or 0x44e size 0x2c): extra = uid, `+0x10` = 140, `+0x12` = a new sceneidx (e.g. world+1000),
   `+0x14/+0x18` = **a known-good x/z** (for a first test the current world position works fine; only the
   sceneidx must change), `+0x1e` = -1.
4. Immediately after: **0x43b** size 0x16e: `+0x10` = 2 (or 7 to get team-id enmity), `+0x11` = 3,
   `+0x16` = {1, 2} (type 7) or {own nation, 4} (type 2), `+0x1c` = 600, `+0x20` = {self uid, 0}
   (team 0, slot 0), everything else 0. The HUD appears with a 10:00 countdown, Kill/Assist 0/0 and TP 0/10000.
   Ignore the 0x470 action 4 the client sends here.
5. Optional: **0x4b5** with `+0x14[0]` = 5000 to watch the gauge move. **0x443** with killer = self to bump Kill.
6. **0x440** size 0x220: `+0x10` = 0, `+0x14` = 2, `+0x1c` = 1 (one gold medal), `+0x3c` = 100,
   `+0x11/+0x12/+0x40/+0x44/+0xa0` = the player's **current** values (stat block with HP > 0,
   equipment table). The result panel opens with "Win".
7. After about 5 s (or on C→S 0x442 `+0x10`=1): **0x44f** back to the original mapid/sceneidx/x/z,
   re-send the stat/visual packets you send on enter-world if anything looks off, then **0x470** state 0.

---

## 5. C→S packets in this area that were not indexed (built inline)

| op | size | fields | site |
|---|---|---|---|
| 0x442 | 0x18 | `+0x10` u32: **0 = host "Start" (custom lobby)**, **1 = leave match/room** | 0x540b35 (Start), 0x540bcf (lobby Exit), 0x543237 (result Exit), 0x543f4c (ExitAtt/ExitDef) |
| 0x441 | 0x18 | `+0x10` u32: 1 = Att, 0 = Def, 0xffffffff = Wait (undecided) | 0x540db8 (Att/Def), 0x540c89 (Wait) |
| 0x46c | 0x18 | none: request room list | 0x542ad1 / 0x542bac (list open/Refresh) |
| 0x46e | 0x18 | `+0x10` u16 mode (0 join from list), `+0x12` u16 room id | 0x542c57 (list "Join") |
| 0x46f | 0x3c | `+0x10` char[40] character name: invite to my room | 0x541cce (CustomGameInvite) |

Lobby Start is sent only if every visible player in the roster has a team ≠ -1; otherwise the client
shows "SomeUserNotSelectTeam". Room buttons work only when the type has f4 and state == 1.

---

## 6. Custom game rooms (separate path, same manager). M

1. NPC (Training Officer BellThain, "Create room for mock battle") opens CustomGameList (GUI 0x62). The
   client sends **0x46c**. The server replies **0x46d** (size 0x72c): `+0x10` 10 × 0xb6-byte rooms:
   `+0x00` i16 room id (≠ 0) · `+0x02` i16 field/map id (must be a valid field; 0 ends the list) · `+0x04` i16
   > 0 = valid entry · `+0x06` char[40] host name · `+0x2e` char[128] room name · `+0xae` i8 current
   players (shown as "n / field.maxPlayers") · `+0xb4` i16 cost-item count ("Mat"). Ignored unless the
   list panel is open.
2. Create: C→S **0x46b** (size 0xc8; group01). Join: C→S **0x46e** `{0, room id}`.
3. Server → each member **0x43c** (size 0xa8): `+0x10` type 6 (or 0xa), `+0x11` state 1, `+0x12` i8[30]
   team per member (0xff = undecided), `+0x30` u32[30] member uids, **first = host**. If the manager was
   idle and the type has f4, the client opens **PanelCustomGameMatch** (lobby, GUI 0x65). `mgr+4` = "I am host".
4. Team pick: C→S 0x441 `{team}`. Server broadcasts S→C **0x441** (size 0x18): extra = member uid,
   `+0x10` u8 team (0/1/0xff), `+0x14` u32 0. A non-zero `+0x14` instead means "new host = this uid".
   Leave: C→S 0x442(1). Broadcast S→C **0x442** (size 0x14+, extra = leaver uid).
5. Invite: C→S 0x46f name. The invitee presumably gets a 0x41c-style prompt (unknown, L).
6. Host Start: C→S 0x442(0). Then the server runs §1 steps 4–8 for all members (warp, 0x43b state 3 with
   `+0x16` = {1,2} so `char+0x659` is set from the roster teams, …).
7. Reconnect: S→C **0x46e** `+0x10` = 3 offers "Rejoin" (CustomGameRejoin, GUI 0x66). C→S 0x46e mode 1 =
   rejoin, 2 = decline.

---

## 7. Function index

| addr | role |
|---|---|
| FUN_004705ac | S 0x470 queue state |
| FUN_004717d1 | S 0x472 team state + open MatchTeam |
| FUN_00428e81 | auto-cancel: C 0x470 action 4 when the match manager receives data while queued |
| FUN_005360a0 | Match.panel Single/Team |
| FUN_00572593 | minimap match button / offer expiry / 0x4c6 markers |
| FUN_0044ad5f / FUN_004fbedc / FUN_004fbd4c | manager get / ctor / reset |
| FUN_004fb1ee | match-type row lookup |
| FUN_004fb2c2 | match active predicate |
| FUN_004fc4e7 | 0x43b |
| FUN_004fc70a | 0x43c |
| FUN_004fc840 | 0x43a |
| FUN_004fb223 | 0x43d |
| FUN_004fc9c5 | 0x440 |
| FUN_004fcc10 | 0x443 |
| FUN_004fd4ff / FUN_004fd5a9 | 0x441 / 0x442 |
| FUN_004fb254 | 0x4c6 |
| FUN_004fb3c7 | 0x439 |
| FUN_00471e7e | 0x4b5 |
| FUN_004fc016 | build scoreboard rows |
| FUN_004fc393 / FUN_004fc487 | auto add/remove on spawn/despawn |
| FUN_00486179 | friend/foe by `+0x659` / nation |
| FUN_0054ea05 / FUN_0054eee9 | Teamscore HUD draw / events (0x32 state, 0x1d TP, 0x34 kills) |
| FUN_005434b5 / FUN_00543dc1 | result panel render / open on UI 0x33 |
| FUN_00543e9a, FUN_0054099e | result-panel / lobby buttons |
| FUN_00542de8 | room list render |
| FUN_00473ab5 / FUN_00473548 | 0x44f / 0x44e (scene change wipes the manager) |

## 8. Open questions

1. **Arena coordinates.** Which 256-unit segments hold the Battle Arena/Temple terrain is in the encrypted
   `map.jpk`. Until it is known, a test match can reuse a valid world position (only sceneidx must change).
2. Which type id the live server used for "Battle Arena" (offer kind 1) vs "War of Warmonger" (offer kind 0).
   2/3/4 are the plain queued types. Exact pairing L.
3. Meaning of states 2/5/6/7/8/9 beyond "0, 7, 9 = inactive" and "3 → 4 = live".
4. Contents of the per-team blocks (`+0x110..+0x160` region) beyond TP. Readers sit in war/world-map panels.
