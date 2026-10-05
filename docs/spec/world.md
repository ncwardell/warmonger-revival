---
title: "Populating the world: spawning units, movement, the player's initial state"
---

# Populating the world: spawning units, movement, the player's initial state

Client: Client.exe (32-bit MSVC). Addresses are VAs. Offsets are from packet start (payload at
+0x10). `acct` = `*DAT_00847ac8`. `rec` = the 0x65f-byte unit record a unit keeps at `unit+0x3a0`.
The 0x240-byte character-select slot record (0x2001) is the same struct starting at `rec+0x203`,
so **slot offset = rec offset - 0x203**. This builds on group00..03.md and loading.md; where this
file disagrees with them, this file is newer and was checked against the disassembly.

## 0. Shared facts

- Dispatcher `FUN_0047a36c`: it checks only the magic and `len > 0x10`. There is **no per-opcode
  size check**. Packets are copied into 0x1010-byte ring slots, so keep every S->C packet at or under
  0x1010 bytes. Header +8 `tick` is stored on every packet (`FUN_0046ff2e`: server tick plus
  local `timeGetTime`). Send a monotonic millisecond counter there. Server packets use key 0
  (plaintext).
- Units live in a `std::map<u16 uid, unit*>` (`FUN_0044d294`/`FUN_0044d3b9`, map at `DAT_0084a754`).
  Any u16 works as a key. The handlers branch on **uid < 0x3F7 = player** and **uid >= 0x3F7 =
  monster/NPC**. Recommended ranges (high confidence):
  - players 1..0x3F6;
  - monsters/NPCs 0x3F7..0x2B05. That is the range 0x4ca can ask for (`uid-1 <= 0x2B05`). 0x806 mode 6
    renames corpses to 0x521A and ignores uid > 0x5218. The client's own debug mobs use 0x2B06+.
- **Unit DB:** `CUnitDB` at `DAT_0084e864` is loaded from `Setting/UnitDB.cdb` (inside the encrypted
  `setting.jpk`) by `FUN_00499b74`. Rows are 0x154 bytes, looked up by `FUN_00499180(id)`, and the
  lookup returns 0 for an unknown id. **Player classes and monster/NPC templates are ids in the
  same table.** Known row fields:
  - +0x00 id; +0x08 name (std::string; it becomes a monster's display name);
  - +0x8a u8 unit category (copied to `unit+0x35c` when the packet leaves it 0; values seen:
    0x26 '&', 0x27 ''' = minimap marker 2, 0x28 '(' with +0x8c=='Z' = marker 3; players use 5);
  - +0xa4/+0xa8 f32; +0xac/+0xae/+0xb0 i16 (+0xac = default weapon/model part);
  - +0xc4/+0xc8 u32 (copied to `rec+0x23b/+0x23f`, the appearance words, for monsters).

  Class id 1 exists (the user's character). Static analysis cannot recover monster ids until
  UnitDB.cdb is decrypted; see §6 for an in-client way to probe ids.
- **Creation (both kinds):** the handler builds a full `rec` on the stack (`FUN_0042882a` = zeroed
  ctor) and calls the creator:
  - player: `FUN_0044f6a3(dbRow, &pos, heading, rec, isOwn=0, spawnFx)`;
  - monster/NPC: `FUN_0044f890(dbRow, &pos, heading, rec, spawnFx)`.

  Both go through `FUN_0044f40e(kind 2=player / 1=monster, uid, category, ...)` and
  `FUN_004be09d`, which builds the model and the movement controller (`unit+0x368`) **synchronously**,
  so a unit can receive 0x416 straight after its spawn packet. Then `FUN_0046fdb0` (buffs),
  `FUN_0046fe22` and `FUN_0044091c(8, unit, uid)` (UI "unit added") run.
- **`rec+0x443` HP == 0 creates the unit dead** (`unit+0x36c = 0`, `FUN_004bcdc1(2,0)` = death state).
  Always send HP > 0 for a live unit. Position is world x/z, the same space as 0x2000. Y always comes
  from the terrain (`FUN_004589aa`).
- If the uid already exists, 0x803/0x805 **update** that unit in place (no re-create, no position
  change). Removing a unit therefore needs 0x806 (or 0x43f/0x43e).

### Unit record fields (`rec`) that spawn packets fill

| rec | slot rec | type | meaning (confidence) |
|---|---|---|---|
| +0x1ae | — | u32 | uid |
| +0x1b2 | — | u8 | unit category override (players: always 5; monsters: packet byte, 0 = use UnitDB +0x8a) (high) |
| +0x1b3 | — | wchar[40] | display name (player: from the packet; monster: from UnitDB) |
| +0x20b | +0x08 | char[40] | name (narrow) |
| +0x233 | +0x30 | u32 | exp (0x422 writes it) (high) |
| +0x237 | +0x34 | u8 | **level** (0x422 writes it; many `< 0x1e` checks) (high) |
| +0x239 | +0x36 | u16 | class / UnitDB id (high) |
| +0x23b | +0x38 | u32 | appearance word A (face/hair/colour; read by the model builder) (medium) |
| +0x23f | +0x3c | u32 | appearance word B (medium) |
| +0x243 | +0x40 | 2 × 16 B | equipment slots 0-1 (container 3; items, u16 item code first) (medium) |
| +0x263 | +0x60 | 16 B | special/costume slot (container 4) (medium) |
| +0x27f | +0x7c | i16 | guild id (high) |
| +0x443 | — | 0x5c B | stats block (below) |
| +0x49f | — | 32 × 12 B | buff slots (u16 buff id first, 0 = empty) (medium) |
| +0x64b | — | u8 | flag byte (bit 0x80 and 0x02 tested by the nameplate/minimap code) (low) |
| +0x64c | — | u8 | per-unit fort/role byte (value 4 tested) (low) |
| +0x64d | — | u32 | status flags (0x200 = visual state; 0x80/0x2000/0x4000 = mount-type states); `FUN_00470a7b` diffs them (medium) |
| +0x655 | — | i8 | nation/team 0..3 (0 = neutral) (high) |
| +0x656 | — | u8 | guild grade (high) |
| +0x659 | — | u16 | battle side / party id. When both units have it non-zero it overrides team for friend/foe (`FUN_00486179`) (medium) |
| +0x65d | — | u8 | set to 1 by every spawn path ("record valid") |

Stats block (0x5c bytes, `rec+0x443`; also the 0x41f payload, the 0x804 +0x28 block and 0x803 +0x60),
applied by `FUN_004bc97c`:

| off | type | meaning |
|---|---|---|
| +0x00 | u32 | HP (also `unit+0x5f8`) |
| +0x04 | u32 | MP |
| +0x08 | u32 | max HP |
| +0x0c | u32 | max MP |
| +0x10..+0x35 | i16/u32 | combat stats shown in the character panel (`FUN_0056xxxx` @ decomp line ~323330). +0x1c i16 and +0x1e i16 feed the movement/animation controller (+0x1e*2*0.01 = rate) |
| **+0x36** | **i16** | **move speed.** World units/s = value × 0.01, for the own unit (`FUN_004bc97c`: ×5×0.01, then ×0.2 in `FUN_004b8a71`) and for remote units. **The client's default is 4.5, so send 450.** 0 = cannot move (high for the formula, medium for 450 as the right value) |
| +0x38..+0x5b | | more panel stats (`%d%%` values at +0x48/+0x4a/+0x50/+0x52/+0x54) |

## 1. Spawn and update packets

### 0x803: spawn unit (full). Handler `FUN_00477d13`

The branch is chosen by `extra` (uid). Only the player branch reads a name from the packet.

**Player branch (uid < 0x3F7). Send 0x270 bytes.**

| off | type | → | notes |
|---|---|---|---|
| +0x06 | u16 | uid | must not equal the own uid; the same uid updates the own unit |
| +0x10 | char[40] | rec+0x20b, rec+0x1b3 (widened) | name, ASCII, NUL-padded (**required**, or the nameplate is empty) |
| +0x38 | f32 | X | **required**, world coords |
| +0x3c | f32 | Z | **required** |
| +0x40 | u16 | rec+0x239 class | **required**: non-zero and present in UnitDB, else the packet is silently ignored |
| +0x42 | u16 | rec+0x659 | battle side / party (0) |
| +0x44 | i16 | rec+0x27f | guild id (0 = none) |
| +0x46 | u8 | `unit+0x374` heading | 0..255 = full turn (`FUN_004b93ae`: angle = h·2π/256) |
| +0x47 | u8 | spawnFx | 1/2/3 = play the "appear" action 0x3d when the unit is in view (`FUN_004bbd42`); 0 = none |
| +0x48 | u8 | rec+0x656 | guild grade |
| +0x49 | u8 | rec+0x237 | **level** (use >= 1) |
| +0x4a | i8 | rec+0x655 | team/nation 0..3 |
| +0x4b | u8 | rec+0x64c | 0 |
| +0x4c | u8 | rec+0x64b | 0 |
| +0x4d..+0x4f | | — | unused |
| +0x50 | u32 | rec+0x64d | status flags (0) |
| +0x54 | u32 | rec+0x23b | appearance A (copy slot rec+0x38) |
| +0x58 | u32 | rec+0x23f | appearance B (copy slot rec+0x3c) |
| +0x5c | u16 | `FUN_0046fe22` → rec+0x297 | territory/fame buff (0) |
| +0x60 | 0x5c B | rec+0x443 | stats; **HP (+0x60) must be > 0**; speed at **+0x96** (= +0x60+0x36) |
| +0xbc | 0x20 B | rec+0x243 | equipment items 0-1 (copy slot rec+0x40) |
| +0xdc | 0x10 B | rec+0x263 | costume/special item (copy slot rec+0x60) |
| +0xec | u32 | buff **bitmask** | bit i set means slot i present (it is a mask, not a count) |
| +0xf0 | n × 12 B | buffs, packed | one 12-byte entry per set bit, in bit order (`FUN_0046fdb0`); 0x180 bytes reserved |

So a remote player's 0x803 is the slot record (name, level, class, appearance, equipment, guild)
plus position, team and stats. **Confidence: high** (every load/store traced in the disassembly at
0x477d56..0x477f89; update path 0x477f8e..0x4781ee).

On update (uid exists) every field above is rewritten, then `FUN_004bd738`/`FUN_004bc19e` refresh the
model. For the own uid it also runs the HP/revive sync `FUN_004890cb` and refreshes the HUD.

**Monster/NPC branch (uid >= 0x3F7). Send 0x1c0 bytes** (the client's own builders use 0x1c0).

| off | type | → | notes |
|---|---|---|---|
| +0x10 | u16 | rec+0x239 | **UnitDB template id: required**, non-zero and present, else ignored |
| +0x12 | u8 | rec+0x237 | level |
| +0x13 | u8 | rec+0x1b2 → unit+0x35c | category override; **send 0** to use UnitDB +0x8a |
| +0x14 | f32 | X | **required** |
| +0x18 | f32 | Z | **required** |
| +0x1c | u32 | rec+0x64d | status flags (0) |
| +0x20 | u32 | rec+0x443 | **HP, must be > 0** (0 spawns a corpse) |
| +0x24 | u32 | rec+0x44b | max HP |
| +0x28 | u32 | rec+0x447 | MP |
| +0x2c | u32 | rec+0x44f | max MP |
| +0x30 | u16 | rec+0x45f | stats +0x1c (0) |
| +0x32 | u8 | heading | |
| +0x33 | u8 | spawnFx | as players +0x47 |
| +0x34 | i8 | rec+0x655 | team (0 = neutral/attackable by all; 1..3 = nation) |
| +0x36 | u16 | rec+0x659 | battle side (0) |
| +0x38 | i16 | rec+0x27f | guild id (fort guards) (0) |
| +0x3a | u16 | `FUN_0046fe22` | 0 |
| +0x3c | u32 | buff bitmask | |
| +0x40 | n × 12 B | buffs | packed |

The name and appearance come from UnitDB (`row+8`, `row+0xc4/+0xc8`). Move speed is not in this
packet: stats +0x36 stays 0 until a 0x41f/0x804 for that uid, and `FUN_004b8a71` then treats it as 0.
**So for a monster that moves, follow the 0x803 with a 0x41f (or use 0x804) carrying a speed.**
Confidence: high for the layout (the client's own GM "create mob" panel `FUN_0051c52e` and the console
`createmob` in `FUN_005ad62b` fill exactly +0x10, +0x14, +0x18, +0x20, +0x24, +0x32, +0x33, +0x34 in a
zeroed 0x1c0 buffer and call the handler; that is the minimal valid monster spawn). Medium for the
speed caveat.

### 0x805: spawn unit (compact). Handler `FUN_0047858b`

No appearance, no buffs, no stats block. Use it for crowds and monsters. Requirements are as for 0x803.
This table supersedes group03's layout (players +0x20/+0x24 are appearance, and the HP order is
HP, maxHP, MP, maxMP).

| off | player (uid < 0x3F7), **size 0x68** | monster/NPC, **size 0x38** |
|---|---|---|
| +0x10 f32 | X | X |
| +0x14 f32 | Z | Z |
| +0x18 u8 | heading | heading |
| +0x19 u8 | — | category override (0) |
| +0x1a u8 | level | level |
| +0x1b i8 | team | team |
| +0x1c u16 | battle side → rec+0x659 | battle side |
| +0x1e u16 | **class (required)** | **template id (required)** |
| +0x20 u32 | appearance A → rec+0x23b | — |
| +0x22 i16 | — | guild id → rec+0x27f |
| +0x24 u32 | appearance B → rec+0x23f | status flags → rec+0x64d |
| +0x28 | u8 guild grade | u32 **HP** |
| +0x2a i16 | guild id | — |
| +0x2c u32 | status flags | max HP |
| +0x30 u32 | **HP** | MP |
| +0x34 u32 | max HP | max MP |
| +0x38 u32 | MP | — |
| +0x3c u32 | max MP | — |
| +0x40 char[40] | name | — |

There is no spawnFx (always 0). The player branch gets **no equipment** (it renders the base model) and
**speed 0** (stats +0x36 not sent). Follow it with 0x41f/0x804, or use 0x803 for players.
Confidence: high.

### 0x804: unit full refresh / reposition. Handler `FUN_00472f4d`

Ignored if the uid is unknown (it never creates a unit).

| off | | notes |
|---|---|---|
| +0x10 f32 X, +0x14 f32 Z | target position | snaps (`FUN_004fee28`) if more than 5 units from the current position, or if the unit is below y = -100 |
| +0x18 u8 | heading | |
| +0x19 i8 | team | all units |
| +0x1a u16 | battle side → rec+0x659 | all units |
| +0x1c u32 | status flags (`FUN_00470a7b`) | |
| +0x20 i16 | guild id | players only (+0x20, +0x22, +0x24, +0x25, +0x84..+0xb3) |
| +0x22 u8 → rec+0x64c, +0x24 u8 guild grade, +0x25 u8 → rec+0x64b | | players only |
| +0x23 u8 | **level** | all units |
| +0x28 0x5c B | stats block (HP first, speed at +0x5e) | all units |
| +0x84 0x20 B, +0xa4 0x10 B | equipment, costume | players |
| +0xb4 u16 | → `FUN_0046fe22` | |
| +0xb8 u32 | buff bitmask; +0xbc packed buffs | |

Size 0xbc + 12 × popcount(mask). It also runs `FUN_004890cb`, which **revives a dead unit when
HP > 0** (and kills it when HP < 1). This is the generic "respawn at position" packet and the best
way to give a monster its speed. Confidence: high.

### 0x806: remove / kill unit. Handler `FUN_00470223` → `FUN_0044e059(uid, mode)`

Size 0x14: extra = uid, +0x10 u32 mode. It never touches the own unit.

| mode | effect |
|---|---|
| 1 | death pose (if not already dead) then remove with a 4 s fade (`FUN_00487e17`, `FUN_0044cf52(uid,1,4.0)`) |
| 2 | **remove immediately** (use for "left view" / logout) |
| 5 | dies in place (HP = 0, death animation); the corpse stays until mode 1/2 |
| 6 | if alive: hide and rename the uid to 0x521A (deferred removal after +1.5 s), else like mode 1 |
| other | ignored |

Confidence: high.

### Bulk forms

- **0x43f** (`FUN_004751ca`, size 0x230): +0x14 40 × {i16 uid, u16 speed, f32 x, f32 z}. Each entry
  with uid > 0 that is not the own uid becomes a synthetic 0x416 {heading 0x7f, type 0x20, speed, x, z}
  with the packet's header tick. +0x1f4 15 × {i16 uid, i8 mode, u8}: each uid > 0 becomes a synthetic
  0x806 with that mode. High.
- **0x43e** (`FUN_00471087`): +0x12 up to 30 × {i16 uid, u8 action, u8}, ending at uid 0.
  **Correction to group00:** action 1 is *not* revive. It is death-fade-remove (same as 0x806 mode 1);
  2 = remove immediately. Skips the own unit. High.

### 0x411 / 0x412 / 0x4ca

0x411/0x412 are combat results (group00), not unit updates. They update HP via `FUN_00485e4b`, and
0x412 also pushes targets to new x/z. The only spawn link: in `FUN_00475654` (0x4756c2..0x47579a), if
the **attacker** uid (0x411 +0x10) is in 1..0x2B06, unknown, and the own unit exists, the client sends
**C->S 0x4ca**: size 0x18, extra = own uid, +0x10 u32 = the unknown uid. It is rate-limited by a
100-entry cache with a 50 s (0xC350 ms) expiry. The client does not request unknown targets.
**Reply:** that unit's 0x803 (or 0x805), or 0x806 mode 2 if it no longer exists. High.

### Correction: 0x414 is not a quest list

`FUN_00474fda` diffs its 100 × {u16 id, i8 value, u8} against `acct+0x65a`, which is the warp
struct's **fort/scene-object table** (loading.md), not quest state. Treat 0x414 as a fort-state
refresh. Medium.

## 2. Monster/NPC vs player

| | player | monster / NPC |
|---|---|---|
| uid | 1..0x3F6 | 0x3F7..0x2B05 |
| table id field | 0x803 +0x40 / 0x805 +0x1e = class | 0x803 +0x10 / 0x805 +0x1e = template |
| table | UnitDB (`FUN_00499180`); 0 or unknown = packet dropped | same UnitDB |
| creator | `FUN_0044f6a3`, kind 2, category 5 | `FUN_0044f890`, kind 1, category = packet byte or UnitDB +0x8a |
| name | from the packet | from UnitDB row +8 |
| appearance | packet (A/B words + 3 items) | UnitDB +0xc4/+0xc8; no items |
| HP layout in packet | stats block (HP, MP, maxHP, maxMP) | HP, maxHP, MP, maxMP |
| 0x416 filter | always processed | dropped while `FUN_004b8824` says the unit is in a locked state (stun/etc. flag) |

NPCs (shops, quest givers, teleporters) are **not** placed by the client from map data: the only
unit creators are the spawn handlers, the own-avatar builders (`FUN_0048b435`, `FUN_0048912f`) and
the debug console. So **the server must spawn every NPC** with 0x803/0x805 using its UnitDB id. The
interaction menus key off the category byte (UnitDB +0x8a). Confidence: medium (inferred from the
call-graph of `FUN_0044f6a3`/`FUN_0044f890`).

## 3. Initial state after 0x2000

What 0x2000 already does (FUN_00472272, synchronous):
- It switches to the game scene, **builds the own avatar from the selected slot record** (a copy of the
  0x65f-byte char-select entry; `FUN_0048b435`), and starts loading.
- It **creates the quest manager and loads quests** (`FUN_00470940` + `FUN_00599b7f`), exactly as
  0x490 does.
- Its 0x6B0-byte profile block (+0x28..+0x6d7 → `acct+0x27cc`) already carries:
  - +0x2c, container 2 (8 × 16 B, the same bytes as 0x423);
  - +0xac, the inventory (70 × 16 B, the same as 0x424);
  - +0x50c u16[8] quick-slot codes and +0x51c u8[8] quick-slot types (0 item, 1 skill; mirrored in
    C->S 0x494);
  - +0x524, 15 × 0x18 quest slots and +0x68c 0x28 B quest flags (the same as 0x490 +0x40/+0x18);
  - +0x6c4/+0x6c6/+0x6c8 quest counters.
- Level and exp come from the slot record (+0x34, +0x30). **Store level >= 1** (the current test
  character has level 0).
- There is **no skill-list packet**. Skills come from `Skill_Base.cdb`/`WeaponBase.cdb`/
  `Skill_TP.cdb` keyed on class and equipped weapon. The quick bar stores only codes. (low/medium:
  no handler in the opcode table writes a skill list.)

**The catch:** the avatar is built inside the 0x2000 handler from the entry's `+0x443` stats, which
nothing has filled yet. So HP = 0 and the **avatar is created dead with speed 0**. The 0x41f that
follows applies the stats (`FUN_004bc97c`) and, because HP > 0, `FUN_004890cb` → `FUN_00487e82`
**revives** it (action 0x17). Sending stats earlier does not work: before 0x2000, `FUN_00428494` has no
selected char (`acct+0x600` is set by 0x2000). So the 0x41f right after 0x2000 is mandatory.

Minimal ordered burst, all with extra = player uid, key 0, tick = server ms:

| # | op | size | content | status |
|---|---|---|---|---|
| 1 | 0x2000 | 0x704 | as now (valid x/z, see loading.md) plus optional profile fields above | required |
| 2 | **0x41f** | 0x6c | +0x10 HP 1000, +0x14 MP 500, +0x18 maxHP 1000, +0x1c maxMP 500, **+0x46 i16 speed 450**, rest 0 | **required** (revive and movement) |
| 3 | 0x421 | 0x20 | HP, MP, maxHP, maxMP | optional (redundant with #2) |
| 4 | 0x422 | 0x18 | +0x10 u8 level 1, +0x11 u8 0 (no level-up FX), +0x14 u32 exp 0 | optional (the slot record already gives level/exp) |
| 5 | 0x41e | 0x1c | +0x10 u32 flags 0, +0x14 u16 0, +0x18 u32 mask 0 | optional (empty buff bar is the default) |
| 6 | 0x424 | 0x470 | 70 × 16 B items (zero = empty; u16 item code first) | optional (only to refresh; 0x2000 has it) |
| 7 | 0x423 | 0x90 | 8 × 16 B | optional |
| 8 | 0x2009 | 0x7c0 | storage etc. (+0x18 → acct+0x2e7c); 0x425 (0x5b0) is the same 90-item area | optional |
| 9 | 0x490 | 0x1a8 | quest block (zeros) | optional (0x2000 did it) |
| 10 | 0x486 | 0x210 | achievement table (zeros) | optional; the panel asks with 0x485 when opened |
| 11 | 0x803/0x805 × n | | every unit within view (players, NPCs, monsters), then 0x41f/0x804 for moving monsters | required to see anyone |

Notes:
- The HUD reads HP/MP from the unit record. With #2 sent, nothing in the HUD path dereferences a
  missing manager (quest manager made by 0x2000; the inventory is `acct` arrays).
- 0x41f also works for any other uid. Use it (or 0x804) to set a remote unit's speed/stats after a
  0x805.
- Keep 0x2000's +0x18 sceneidx constant across later 0x44e (loading.md).

Confidence: high for the creation and revive mechanics, the profile offsets and the speed formula.
Medium for "nothing else is needed" (no client error paths were found for the omitted ones).

## 4. Movement relay

Client sender `FUN_004bba89` (own unit only, needs the movement controller):
- **While moving:** every **0.5 s** (`DAT_00720d38`), 0x416 with +0x10 heading, +0x11 type = **0x02**
  (controller+0x56 set, run) or **0x20** (walk/other), +0x12 stance (`unit+0x38`), +0x14 speed
  (stats +0x36), +0x18/+0x1c = a **predicted point ahead** (`FUN_004fe8ff`), not the current position.
- **Heading change > 0x23/256:** forces a send within 300 ms.
- **Stopped (state 7):** one 0x416 type **0x00** with the current position once it has moved ≥ 1.5 units
  since the last send.
- **Type 1:** stuck resync (`FUN_0048d666`). **Type 4:** clock drift (`FUN_004156b0`).

Receiver `FUN_004728ff` (S->C 0x416):
- Needs a game scene and the unit spawned. Updates `unit+0x60c/0x610` (last server x/z) and terrain
  height.
- Own unit with type 1: snap (`FUN_004fee28`).
- Any unit while no load is running and `unit+0xc == 0` (not currently visible): if the distance to
  the new point is in (16, 256], snap there.
- Otherwise it accepts types 0, 2, 0x10, 0x20 (others dropped). It drops monsters in a locked state and
  remote units with `unit+0x5c0` set (knock-back/cast lock).
- It path-finds (`FUN_004fe276`) and **walks the unit to (x,z)** at speed +0x14 (stored to stats
  +0x36, animation rate = speed × 0.05). Type 0 means arrive and stop (facing from the heading when the
  distance is 0). Type 2 also sets the heading from +0x10 at the end.

Server relay rules (high confidence):
1. For every C->S 0x416 of type 0x00/0x02/0x20 from player P, update P's server position to (x,z).
   Forward the **same 32 bytes** to every other client that has P spawned: extra = P's uid, key 0,
   own tick. The client's packet already has the right fields. Do not echo it to P.
2. Type 1 (resync): reply to P only, with a 0x416 of type 1 and its authoritative position. Type 4:
   log/ignore.
3. A new player entering someone's view: 0x803 first, then their movement. 0x416 for an unknown uid is
   silently dropped (no 0x4ca for movement).
4. **0x43f cadence:** the client has no timer for it; it is purely server-pushed. Use it for
   server-driven units (monster AI, NPC patrols) and periodic drift correction: **one 0x43f per
   client every 1 s** with up to 40 moving units in view (each entry = destination plus speed). Use
   its second list to drop units that left view (mode 2). Players moving are already covered by
   rule 1, about 2 packets/s each. Medium (cadence is a design choice; 1 s matches the client's 0.5 s
   prediction horizon with headroom).
5. A monster's speed in 0x43f/0x416 is written to its stats each time, so speed is always explicit there.

## 5. Spawn/despawn lifecycle (server side)

- Player A enters (after its 0x2000 burst): send A one 0x803 for every player in view, plus
  0x803/0x805 for NPCs and monsters. Send every player in view of A one 0x803 for A.
- A leaves view or logs out: 0x806 mode 2 to each viewer.
- A monster dies: 0x806 mode 5 (corpse), then after a delay mode 1 (fade out). Respawn: 0x803 with a
  new or the same uid (if the uid still exists, use 0x804 with HP > 0, which revives and repositions).
- Equipment change: 0x426. Stats: 0x41f/0x804. Level: 0x422 (own only) or 0x804 +0x23.

## 6. Self-test: spawn a second copy of your own character next to you

A 0x803 for uid 2 (not the own uid 1), class 1, the same appearance words as the stored slot record
(`characters.json` slot 0: rec+0x38 = `03 03 09 0b`, rec+0x3c = `06 00 21 27`), level 1, HP 1000,
speed 450. Put it 3 units east of the spawn. The example uses spawn (4224.0, 4224.0) → X = 4227.0;
**replace +0x38/+0x3c with SPAWN_X+3, SPAWN_Z** (a position on loaded terrain).

```
len 0x270, magic a53c, op 0803, extra 0002, tick 0, key 0
0000: 70 02 3c a5 03 08 02 00 00 00 00 00 00 00 00 00
0010: 74 65 73 74 63 6c 6f 6e 65 00 00 00 00 00 00 00   name "testclone" (char[40] to +0x37)
0020: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0030: 00 00 00 00 00 00 00 00 00 18 84 45 00 00 84 45   +0x38 X=4227.0  +0x3c Z=4224.0
0040: 01 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00   class 1, side 0, guild 0, heading 0, fx 0, grade 0, level 1, team 0
0050: 00 00 00 00 03 03 09 0b 06 00 21 27 00 00 00 00   flags 0, appearance A, B, +0x5c 0
0060: e8 03 00 00 f4 01 00 00 e8 03 00 00 f4 01 00 00   HP 1000, MP 500, maxHP 1000, maxMP 500
0070..0090: zero, except
0090: 00 00 00 00 00 00 c2 01 00 00 00 00 00 00 00 00   +0x96 speed 450
00a0..026f: zero (equipment, costume, buff mask 0)
```

Python:

```python
p = bytearray(0x260)                                    # payload (packet - 16)
p[0x00:0x09] = b"testclone"
struct.pack_into("<ff", p, 0x28, SPAWN_X + 3, SPAWN_Z)   # packet +0x38
struct.pack_into("<HHh", p, 0x30, 1, 0, 0)               # +0x40 class 1
p[0x39] = 1                                              # +0x49 level
p[0x3a] = TEAM                                           # +0x4a team
p[0x44:0x4c] = slot_record[0x38:0x40]                    # +0x54 appearance A/B
p[0xac:0xcc] = slot_record[0x40:0x60]; p[0xcc:0xdc] = slot_record[0x60:0x70]   # +0xbc/+0xdc items
struct.pack_into("<IIII", p, 0x50, HP, MP, MAX_HP, MAX_MP)                      # +0x60 stats
struct.pack_into("<H", p, 0x86, 450)                     # +0x96 speed
pkt = build(0x803, bytes(p), extra=2)
```

Expected result: a second "testclone" model standing beside you with a nameplate. Then verify movement
by sending `build(0x416, struct.pack("<BBBBHHff", 0, 2, 0, 0, 450, 0, SPAWN_X+10, SPAWN_Z), extra=2)`:
the clone should run 10 units east. Remove it with `build(0x806, struct.pack("<I", 2), extra=2)`.
If nothing appears, the usual cause is the class id (a slot record with class 0) or X/Z off the loaded
5×5 terrain window.

Monster probe without knowing UnitDB ids: the client's debug console command
`createmob <n> <x> <z> <unitDefId> <hp> <maxhp>` (`FUN_005ad62b`) and the GM tool "create mob"
(`FUN_0051c52e`, panel opened by S->C 0x496) spawn a local monster (uid n+0x2B07 / 0x2B06) with
nothing sent to the server. They can be used to find which UnitDB ids exist (an unknown id simply
spawns nothing) until `setting.jpk` is decrypted.

## 7. Python multiplayer prototype and verification

The current Python server puts connected players in one shared tutorial scene (map 117,
scene 87). Each game connection has a distinct player UID, character selection, inventory,
gold and combat state. Entering sends mutual player 0x803 packets using the layout above;
movement 0x416 and combat results are relayed to other players in that scene. Leaving
sends 0x806. One server timer advances monsters, so adding a player does not reset their
health or increase their attack rate. These are prototype server rules, not recovered
official rules; see `server/sessions.py`, `handlers.py`, `world.py` and `ai.py`.

Use distinct `-ologin=<name>` development identities for simultaneous clients. Character
creation is saved per identity; inventory and earned gold survive character selection on
the same connection but reset on disconnect. Loot currently belongs to the killing
player. Authentication, durable progress, party sharing, PvP, quests and NPC dialogue
remain open work. The prototype currently enters the tutorial only.

### Windows client evidence (2026-10-05)

- **World status:** empty responses and the previously assumed XML left the world at
  "Checking" in token-login mode. `FUN_0042a92f` calls `FUN_006d7b70`
  (`Json::Reader::parse`); `FUN_006d4400` performs object-key lookup. JSON arrays
  containing a world row made the world selectable, with a green "Medium" status.
  See `contract/session.yaml` for the fields returned by `WorldChannel.asp` and
  `ChannelList.asp`.
- **Launch argument:** `FUN_00407510` compares the `-ologin=` prefix and reads the
  token from offset 8 (`0x40752d`-`0x40755a`). Use one argument, `-ologin=alice`;
  a separate `-ologin alice` did not activate token login and opened the obsolete
  OAuth flow. `scripts/play-windows.ps1` uses the single-argument form.
- **One real client:** local server logs recorded login, character creation, entering
  map 117 at (1427, 429), movement 0x416, basic attacks 0x411, skill casts 0x410 and
  hits 0x412, monster kills, loot/gold, monster respawns, and player death/revival.
  These observations establish the single-client flow; they do not verify remote
  player rendering or synchronization between two real clients.
- **Automated tests:** `server/test_multiplayer.py` exercises two independent TCP
  clients through login, spawn, obfuscated movement, character selection/re-entry
  and disconnect. Unit checks cover shared monster state, private loot, AI timing,
  handler reloads and malformed packets. The suite runs without client assets.

### Remaining two-client check

Run the server bound to the host's LAN address. On each computer, point its own client
copy at that address with `scripts/play-windows.ps1 -ServerAddress <server-LAN-IP>`
and distinct `-Account` values. Verify both character models and equipment, movement
in both directions, shared monster damage/death/respawn, private loot, and removal
when one player returns to selection or disconnects. This real two-client check is
still pending; synthetic packet tests cannot establish the visual result.

## Function index

| Function | Role |
|---|---|
| `FUN_0047a36c` | S->C dispatcher (magic + len > 0x10 only) |
| `FUN_00477d13` | 0x803 |
| `FUN_0047858b` | 0x805 |
| `FUN_00472f4d` | 0x804 |
| `FUN_00470223` / `FUN_0044e059` | 0x806 / remove-kill by mode |
| `FUN_004751ca` | 0x43f |
| `FUN_00471087` | 0x43e |
| `FUN_004728ff` | 0x416 receive |
| `FUN_004bba89` | 0x416 send |
| `FUN_00475654` | 0x411 (sends 0x4ca at 0x47577e) |
| `FUN_0044f6a3` / `FUN_0044f890` / `FUN_0044f40e` / `FUN_004be09d` | create player / create monster / allocate unit / build model and controller |
| `FUN_00499180` (`DAT_0084e864`, CUnitDB, `FUN_00499b74` loads `Setting/UnitDB.cdb`) | unit DB lookup |
| `FUN_004733a4` → `FUN_00472103` → `FUN_004bc97c` | 0x41f → stats apply (speed, revive) |
| `FUN_004890cb` / `FUN_00487e82` | HP sync / revive |
| `FUN_00470eeb`, `FUN_0046fdb0`, `FUN_0046fd59`, `FUN_00470a7b`, `FUN_0046fe22` | buffs (mask + packed 12 B), status flags, +0x297 |
| `FUN_0048b435` | game scene and own avatar from the slot record |
| `FUN_00472079` | 0x420/0x421 HP/MP apply (also revives) |
| `FUN_0047684e` | 0x422 (level → rec+0x237, exp → rec+0x233) |
