# Enter-world loading: what ends it, and what causes the endless "looping" load screen

Client: Client.exe (32-bit MSVC). Addresses are VAs. `acct` = `*DAT_00847ac8`.

## TL;DR

- **CLoadingProcess finishes on its own.** No server packet is needed to end it. It is a step machine
  (`+0x214`, steps 0..0x19) that kills itself at step 0x19.
- **The loop comes from the spawn position (0,0), not from a missing packet.** Once per second,
  `FUN_004bcc6e` checks the terrain zone piece under the local player. If that piece does not exist
  (no `Map/ZPxx_yy_00.zp`) or is not loaded (state 0), it starts a brand-new CLoadingProcess.
  With x=z=0 the player sits in segment (0,0) → `Map/ZP00_00_00.zp`, which is evidently not in
  `map.jpk`. So every load "finishes", the check fails, and a new load starts. Each new load shows a
  **randomly picked** loading screen (`FUN_00497d0e` chooses a random entry), which is the
  "looping through worlds".
- The 0x416 type-1 resync the client sent is a side effect of the same thing. `FUN_0048d666` sends it
  only while no load is running (`DAT_0084f92c == 0`), in the gap between two loads, because the
  navmesh query at the player position fails (`FUN_00452d26`). Our 0x416 type-1 reply does **not**
  cause a reload by itself. It only moves the player, and back to (0,0), so the loop continues.
- **Fix:** put the player at x/z that fall inside an existing zone piece that has navmesh. sceneidx
  does not matter for loading (any value, kept the same in later 0x44e/0x44f). mapid only drives UI and
  fort tables.

Confidence: high for the mechanism (read from the disassembly at every step). Low for *which*
coordinates are valid: that depends on which `Map/ZP%02d_%02d_00.zp` files exist inside the
encrypted `Data/map.jpk`.

## 1. Scene-4 startup and CLoadingProcess

Call chain after 0x2000 (`FUN_00472272`):

1. 0x2000 stores the spawn record into `acct+0x63c` (0x1AE-byte "warp struct", below).
   - Out of game (`DAT_0084e840 != 0`): `FUN_0049330c` → `FUN_004930cb(3)` → `FUN_0049791e`
     (kills the char-select process) → `FUN_004298e4(4)`.
   - **Already in game** (`DAT_0084e840 == 0 && DAT_0084e3ec != 0`): kills the running loading
     process if `DAT_0084f92c` is set, then `FUN_004883b5(acct+0x63c)` starts a **new** load. So
     re-sending 0x2000 while in game restarts loading.
2. `FUN_004298e4(4)` → `FUN_00428ac6(scene, acct+0x63c)` creates the loading process. Then
   `FUN_0042932e` builds the game scene (`FUN_0048b435`: avatar, UI). That function calls
   `FUN_004a7e6a` (sets `load+0x21c = 1`, which enables the resource-preload steps) while a load is
   active.
3. `FUN_00428ac6`: `new(0x22c)` → `FUN_004a7eb2` (ctor; Process base `FUN_00497a94`, TerrainListener
   at +0x60) → vtbl[5] `FUN_00497b78` (attach to the parent process; calls vtbl[7] `FUN_004a7dad`,
   which sets **`DAT_0084f92c = this`**, the global "loading in progress" flag) → `FUN_004a7fd7(struct)`
   (copies the struct to `+0x64`, builds the loading UI with a random background, "ProgBar") → vtbl[6]
   `FUN_00497910` (Process state +0x48: 0 → 1 = running).

CLoadingProcess vtable `0x72b900`: [0] 0x4920a1 dtor, [2] **`FUN_004a8446` = per-frame tick**,
[3] `FUN_004a7f57` OnKill (unregister terrain listener, close the loading UI group, fade),
[5] 0x497b78 init, [6] 0x497910 start, [7] `FUN_004a7dad` (`DAT_0084f92c = this`),
[8] `FUN_004a7db6` (`DAT_0084f92c = 0`), [9] `FUN_004a7da7` (name). TerrainListener vtable
`0x72b8d8`, slot 5 = `FUN_004a83a1` (progress-bar update).

Process kill is `FUN_0049791e`: state becomes 2, then vtbl[3] (OnKill), then state 3, then vtbl[8]
(clears `DAT_0084f92c`).

### Loading object layout (copied warp struct at +0x64)

| obj off | struct off | acct off | meaning |
|---|---|---|---|
| +0x64 | +0x00 | 0x63c | i32 x * 100 (0x2000: `ftol(f32 x * 100)`) |
| +0x68 | +0x04 | 0x640 | i32 y * 100 (0) |
| +0x6c | +0x08 | 0x644 | i32 z * 100 |
| +0x70 | +0x0c | 0x648 | u16 heading/flags (0x9f) |
| +0x74 | +0x10 | 0x64c | i8 mapfort |
| +0x75 | +0x11 | 0x64d | u8 (0x2000 +0x6db) |
| +0x76 | +0x12 | 0x64e | u32 mapGuild (0x2000 +0x6e4) |
| +0x7a | +0x16 | 0x652 | i32 mapid |
| +0x7e | +0x1a | 0x656 | i32 sceneidx (not read by the loader) |
| +0x82 | +0x1e | 0x65a | 100 × {u16 fortId, i8 value, pad} fort/scene-object table |

The 0x44f payload (+0x10..+0x1bc) maps onto this through the handler's local copy. That is why
0x44f is about the same size as the struct.

### Tick `FUN_004a8446`, step counter `+0x214`

- 0: build/position the loading UI, then step 1.
- 1..0x13 run only if `+0x21c` (set by `FUN_004a7e6a`) and `DAT_00846e90`. Otherwise it jumps
  straight to 0x14.
  - 1: optional wait `FUN_0043c9de(DAT_00849894)` (`+0x34 == 0`).
  - 2..0xb: preload resources listed at `DAT_0084694c+0x1304..0x1308` (0x38-byte entries, .MO/.DDS/
    .PNG/.TGA), 25 per tick.
  - 0xc: `FUN_0045ca42` (waits for queued type-4 jobs). 0xd: misc UI object (0x68). 0xe:
    `FUN_004a7dee`. 0x11: `FUN_00470981`. 0x12: UI refresh events 0x2e/0x10/0xe/0xf/0x13/0x1b/0x1d/0x26.
- 0x14: `FUN_004c7a04`, `FUN_0046013b`.
- **0x15: place the world.** pos = struct.xyz / 100 → `FUN_0042c290` re-centres the 5×5 terrain window
  (origin seg = player seg − 2, clamped ≥ 0; `DAT_0084ccb0/2` = camOriginSeg) →
  `FUN_0045a7cd` → `FUN_0045a154` **synchronously loads the player's piece** `Map/ZP%02d_%02d_00.zp`
  (`FUN_004a57e2`; piece state `+0x41290 = 3`). If the file does not exist (`FUN_0049a60c` false),
  the piece is left at state 0 and nothing is logged. Then the own unit is placed (`FUN_004fee28`),
  its height comes from the terrain, and the camera is set.
- **0x16: terrain streaming wait.** It holds while `FUN_0045b787` returns true, i.e. while any of the
  5×5 pieces is in load state 1/2 (re-checked every 0.5 s). With no terrain manager (`DAT_0084b014 == 0`)
  it does not wait.
- 0x17: apply the fort table: for every fort whose map == `+0x7a` (mapid), take the value from the
  `+0x82` table (`FUN_0044fab0`).
- 0x18: `FUN_0044be50`, `FUN_0044a396`, `FUN_004505fd`.
- **0x19: done** → `FUN_0047cb65`, **`FUN_0049791e(this)`** (kill → `DAT_0084f92c = 0`, loading UI
  closed), `FUN_00487c28`.

**End condition:** reaching step 0x19. Nothing in it depends on a server packet. The only real
waits are step 1 (a local subsystem), step 0xc (local job queue) and step 0x16 (terrain I/O).

## 2. Is any server packet required?

No. 0x41f/0x421, 0x803, time sync and 0x44e/0x44f are not checked by the loader. 0x44e/0x44f matter
only during a load: on a same-sceneidx 0x44e/0x44f, `FUN_004a7dbe` patches the running loader's struct
(new position, and the fort table if 0x44e), and also updates `acct+0x63c`.

## 3. The loop: `FUN_004bcc6e` (per unit, once per second)

Called from the unit update `FUN_004bee8a` when `DAT_00846e88` is set. That global is a 1 Hz tick
set in the frame-time code `FUN_00422bdd`: `DAT_00846e88 = 1.0 < accum`.

```
if (unit+0x10 == 2) { ...
  if (unit == DAT_0084a758 /*own*/ && DAT_0084f92c == 0 /*not loading*/) {
     piece = FUN_00455403(DAT_0084b014, &unit->localPos /* +0xd0/+0xd8 */);   // 0x4bcd6f
     if (piece == 0 || piece->state(+0x41290) == 0)
         FUN_004883b5(DAT_0084e3ec, acct+0x63c);   // 0x4bcd91 -> new CLoadingProcess
  }
}
```

`FUN_00455403` maps the window-relative position to a cell with `floor(pos/256)` over 0..4.
`DAT_008338c0 = 256.0`.

So whenever the player stands on a piece whose `.zp` file is missing, the client reloads every
second, forever. That is exactly the reported symptom. Each reload picks a random loading image,
and the reload uses `acct+0x63c`, which is still (0,0).

Other ways to restart a load (do not trigger them):
- re-sending 0x2000 while in game;
- 0x44e/0x44f with a **different** sceneidx from `acct+0x656`: full scene change → `FUN_004883b5`.
  With the same sceneidx it is an in-place teleport.

0x416 type 1 (`FUN_004728ff`): for the own unit with `+0x11 == 1` it only calls `FUN_004fee28`
(set position). No reload. If that position is on a missing piece, the 1 Hz check above reloads
again. The sender `FUN_0048d666` runs only when `DAT_0084f92c == 0`. It is a stuck detector: when
the navmesh/collision lookup `FUN_00452d26` fails at the player position it waits about 5 s, sends
0x416 type 1 (`FUN_004a730b` + `FUN_0046ff99`), and then waits 30 s before repeating.

The "File open error(10035) : MODEL/FX/UI/WORLDMAP/FIELD87.MO" line is harmless. It comes from
`FUN_004defc5`, and the number is just the stale `GetLastError` (a WSAEWOULDBLOCK left over from the
socket). It is the world-map UI panel loading `ui/WorldMap/field%d.mo` for fields 1..90 (`0x5a`). The
error only means that art file is absent. It has nothing to do with the loop.

## 4. sceneidx vs mapid

- No mapid → sceneidx lookup exists in code. sceneidx (`acct+0x656`) is read only to:
  - compare with incoming 0x44e/0x44f (same = in-scene teleport, different = full reload);
  - match `FUN_0047069f` (mapfort update);
  - print the debug line "MyUnit uid %lld sceneidx: %d / mapid :%d / mapfort :%d / mapGuild:%d".

  It behaves like a server-side instance id. Any value works, as long as it stays consistent.
- mapid (`acct+0x652`) drives UI and tables only: fort matching at loader step 0x17, `FUN_004e1c8d(mapid)`
  field info, the world-map panel, and a special UI case `mapid == 0x78` (120, fortress ranks 0x14..0x1c).
  **Terrain is not chosen by mapid.** The world is a single continuous grid of 256-unit segments,
  with files `Map/ZP{segX:02d}_{segZ:02d}_00.zp` plus navmesh `map/navi/ZP%02d_%02d_00.*`. The
  player's world x/z alone pick which pieces load (segX = floor(x/256), segZ = floor(z/256)).
- Debug console commands (`FUN_005ad62b`):
  - `teleport <n> <x> <z>` builds a zeroed 0x2c-byte 0x44e with **mapid 0, sceneidx 0**, x/z f32 at
    +0x14/+0x18, and feeds it straight to `FUN_00473548`.
  - `createmob ...` builds a local 0x803.

  No hard-coded coordinate pairs were found. The `teleport` command itself confirms that
  mapid 0 / sceneidx 0 is acceptable to the handler.

## 5. Recommendation

0x2000 (unchanged except position):
- extra = 1, +0x10 u64 char id, +0x18 i16 sceneidx = **87** (any value; the stub already uses 87, so
  keep the same value in every later 0x44e), +0x1a i16 mapid = 87, +0x24 team, +0x25 mapfort = -1,
  +0x6f8 time.
- **+0x1c f32 x / +0x20 f32 z = a point inside an existing zone piece with navmesh.** Use a segment
  centre, `x = segX*256 + 128`, `z = segZ*256 + 128`. **Never (0,0).**
- Send 0x41f/0x421 as now. Do **not** re-send 0x2000.
- Answer 0x416 type 1 with a valid position, not (0,0).

Finding valid coordinates (the main open question):
1. Deterministic: decrypt the `map.jpk` index and list `Map/ZP??_??_00.zp`. Any listed segment works.
   Pick one whose navmesh `map/navi/ZPxx_yy_00.*` also exists. Village 87's real spawn is in the
   (encrypted) server or `WorldmapData/Teleport_List` tables.
2. Empirical probe, which works even while the client is looping. Every ~4 s send S→C **0x44e**
   (size 0x2c, extra = 1, +0x10 u16 mapid 87, +0x12 u16 sceneidx 87 (= the value sent in 0x2000, so it
   is an in-place teleport), +0x14 f32 x, +0x18 f32 z, +0x1e i8 -1, rest 0).
   - That path writes `acct+0x63c`, so the next 1 Hz reload uses the new position.
   - Step through segment centres, for example a spiral outward from seg (16,16), then (8..40)².
     Log each candidate.
   - Once the world renders and stays, the last-logged position is valid. Hard-code it as the spawn
     point.
   - Signs of success: no new loading screens. 0x416 type-1 resyncs stop, or still come every 30 s if
     the point is on terrain but off navmesh; move a few metres in that case.
3. If the client debug console can be opened, typing `teleport 0 <x> <z>` does the same locally.
   Caveat: it uses sceneidx 0, so with sceneidx 87 it performs a full scene change to map 0. That is
   harmless for probing.

Confidence:
- loop mechanism, end condition, and the claim that sceneidx is irrelevant: high;
- the claim that ZP00_00 is missing: high, inferred from the symptom plus the code path;
- actual valid coordinates for map 87: unknown statically.
