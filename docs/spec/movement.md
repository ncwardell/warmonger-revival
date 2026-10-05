# Local-player movement: click/hold-to-move, the 10 Hz sim, and the "stop and hop"

Client: Client.exe, VAs. This file covers the **own unit** (`DAT_0084a758`). Remote units are in
world.md §4. Where this file disagrees with group00.md or world.md, this file was checked
against the disassembly and is newer.

## TL;DR

- **No server packet is involved in local movement, and none is expected.** The local unit is
  simulated entirely on the client. An S->C 0x416 for your own uid is effectively ignored
  (§5), so echoing never helped. Nothing in 0x2000/0x41f/the slot record selects the move
  "type". **Type 0x20 is normal walking.** 0x02 means "standing on a moving model"
  (a CUnit with flag +0x1a0, or a CTrigger: ship, lift, platform), not "run". (High.)
- **The hop is a render-buffer underflow.** The render position of the local unit is
  interpolated between per-tick snapshots, with a lag of about one tick and **10 ms of slack**
  (`FUN_004feb38`). Any tick in which the sim does not move the unit pushes no snapshot. The
  render position then holds ("stops"), snaps to the newest snapshot, and resumes ("hops").
  (High for the mechanism. Simulated in §7.)
- **What causes the missing ticks for far targets is not pinned down statically.** The
  candidates are in §6, with breakpoints that settle it in one session. None of them can be
  fixed from the server. The server's only obligation is to send nothing for the own unit. Do
  not resume the echo: a self-0x416 whose position is 16–256 units off **teleports** you.

## 1. Clocks and the per-frame order

| what | where | notes |
|---|---|---|
| sim clock | `DAT_0084b080`, `FUN_0045bc55` | tick = `ftol(DAT_00846e78 / 0.1)`, i.e. **10 Hz**. Tick length +4 = 0.1. At most 10 ticks per frame (+0x10) |
| `DAT_00846e78` | written at 0x415a51 | `float32(timeGetTime()/1000)`: **seconds since OS boot in a float**. Resolution: 4 ms at 12 h uptime, 31 ms at 3–6 days, 62 ms at 6–12 days, 125 ms past 12 days |
| frame time / dt | `DAT_00846e5c` / `DAT_00846e64` (`FUN_00422bdd`, DXUT-style QPC time) | the render interpolation and every 0.5 s timer use this, not the tick clock |
| per-frame unit update | `FUN_0044e17f` | for each unit with a controller: **for every new tick:** `FUN_004611fa(1)` (drain command queue) then `FUN_005001b6(1)` (sim tick + snapshot). Then `FUN_004feb38` (render interpolation). Then for the own unit `FUN_004bba89(0)` (send 0x416) |
| player input | vtable 0x72b9b0 slot 5 `FUN_004a8fab` → slot 12 `FUN_004a9655`, then `FUN_004512cd` (camera, sends 0x417) | per frame |

## 2. Input → order → command (per frame)

The global move-order object is at **0x853cd8** (`ecx = 0x853cd8` at 0x4a9485 and 0x474cc8):
+0x54 mode (`DAT_00853d2c`), +0x58 active byte (`DAT_00853d30`), **+0x5c target** = sector +
vec3 (`0x853d34..0x853d40`), +0x6c follow-uid, +0x7c item/skill. Mode table at 0x83e668
`{f32 range, i32 kind}`: mode 1 = {1.0, kind 1 "point"}.

`FUN_004a9655` (per frame):
1. While the button is held (`this+0xd`, set in `FUN_004a9930`): `GetCursorPos` →
   **`FUN_004a9204`**:
   - picks the ground under the cursor: navmesh pick `FUN_00458461` and terrain ray
     `FUN_00459e8c(ray, maxdist 200.0)`. If neither hits, the target stays the unit's own position;
   - if `|target - unit| < 1.0` (0x720d44) → **queues a STOP command (type 0)** (0x4a942e).
     Otherwise → **`FUN_0058b288(target)`** (0x4a948a).
2. `FUN_0058b288` (every held frame): `FUN_0058af2a` (clear the order) → `FUN_004fe276` (path
   from the unit's **render** position `unit+0xcc` to the target. On success the target becomes
   the path end) → `FUN_0058b0e1` (order mode 1, +0x58 = 1, click marker `FUN_0045fed0`, path
   preview `FUN_004ff084` = up to 15 samples, 10 units apart, into controller+0xbc for the
   minimap `FUN_005d29de`).
3. `FUN_0058cc24` → `FUN_0058b957(0)`: mode kind 1 **re-paths again** (`FUN_004fe276` at
   0x58bf0a) and returns:
   - **1 if `FUN_004fe276` failed** (0x58bf11 → 0x58c20d). `FUN_0058cc24` then queues a **STOP**
     and clears the order (`FUN_0058c335`, `FUN_0058af2a`);
   - while the button is held (`DAT_0084f934+0xd`), 0 otherwise. No arrival test;
   - when not held: 1 when `|render pos - path end| < speed * 0.15` (0x731098 is the double
     0.15) → STOP.
4. End of `FUN_004a9655`: if the order is active (`0x853d30`) → **queue a MOVE command
   (type 1)**. This happens every frame (0x4a9884).

Command queue `unit+0x364` (`FUN_00461178`): for the own unit (+0x10 == 0) commands are
**queued** and run on the **next tick** by `FUN_004611fa` → `FUN_004607ef` (validate) →
`FUN_00460f96` → `FUN_004ffb77`:
- type 0 STOP: `FUN_004ff011` destroys the controller path and sets action state 7 (idle);
- type 1 MOVE: `FUN_004fe759` sets action state 8 (move). `FUN_004607ef` also plays **anim 4**
  (start-walk) when a MOVE arrives in state 7. A stop then move therefore looks like
  "stop, then step forward".

## 3. The sim tick (`FUN_005001b6` → `FUN_004ff24e(dt = 0.1)`), own unit

Controller = `unit+0x368` (built in `FUN_004feef0`). +0x28 = physics body (`FUN_00505de2`, sim
position = body+0..+0xc). +0x98 = PathEngine path ("carrot": 6-dword position + [6] iPath* +
[7] id). +0xd4 = snapshot list. +0x14 = the position that gets sent.

State 8 (and `unit+0x5c4 == -1`):
1. `speed = FUN_004b8a71()`. For the own unit: `(unit+0x418)+9 * 0.2 + rec+0x645 * 0.01`. +9 =
   stat+0x36 × 5 × 0.01 (`FUN_004bc97c`), so 450 → 4.5 units/s.
2. Copies the path (`local_90`, and `local_b4` for later). `FUN_0045361e(local_90,
   speed*dt*100 cm, context 0)` = `iPath::advanceAlongPath` (vtable +0x1c). The local unit uses
   collision context 0 of the tile (`FUN_00452798(tile,0)`). Remote units use none.
3. If the carrot moved (`FUN_0044fd0c(old,new)`): heading (`FUN_004b93ae`) = direction from the
   **render** position `unit+0xcc` to the new carrot. `dir = FUN_005107e3(heading byte)`.
   **If the carrot did not move, or the path is empty or invalid, `dir` stays 0 and the unit
   does not move this tick.**
4. `FUN_0050611d(dt, dir, speed)` moves the physics body (sweep, gravity, ground snap).
5. **Lookahead (only while the order target 0x853d34 is non-zero, 0x4ff583):** `len =
   path->getLength()` (`FUN_004524c9`). Advance `local_b4` by `min(len, speed*0.5*100)`
   (0x720d38 = double 0.5) → `controller+0x14..+0x1c`. That is **the x/z sent in 0x416: about
   0.5 s ahead of the carrot, or the path end if that is closer.** It matches your logs (about
   2.25 units per 0.5 s).
   - **Side effect:** `local_b4` is a *shallow* copy, so this advances the **shared** iPath
     object. The controller's carrot is 2.7 units further along the path each tick. When the
     lookahead reaches the end, `FUN_004535ae` deletes the iPath, and the controller keeps a
     stale pointer, which it later detects via the id check `FUN_004520e3`. This only matters
     when two ticks run without an input re-path in between (fps < 10, or tick bursts). It then
     stalls the unit when the target is *near* (path < 2.7), not far, so it is not your trigger.
6. `FUN_005001b6`: pushes a snapshot `{body pos, 1 tick}` **only if the body moved**
   (`FUN_004558d3`) or the list is empty. The own unit's list is not trimmed here.

## 4. Render interpolation (`FUN_004feb38`, per frame): where the hop is drawn

The list is at controller+0xd4 (count +0xd8), the clock at controller+0xe4:
- fewer than 2 nodes: clock = −0.01, hold;
- else clock += frame dt. Consume whole nodes (0.1 s each):
  - **fewer than 2 left → snap the render position to the newest node, drop the rest, clock =
    −0.01** (0x4fec63). This is the **stop then hop**. The render waits about one tick for the
    next node, then jumps;
  - nothing consumed and more than 3 nodes → drop the oldest (0x4fed3c). This is a forward hop;
  - otherwise lerp node0→node1 into `unit+0x4c..0x58` (render position, then `unit+0xcc`).

The render runs one tick behind with **10 ms of slack**. One missing snapshot (a tick where the
body did not move) is enough for a visible stop and hop. The sim position is never corrected
toward the render position. The render snaps forward "to where it should be", which is exactly
the symptom.

## 5. Server packets and the own unit

- **S->C 0x416, own uid** (`FUN_004728ff`):
  - type 1 → teleport (`FUN_004fee28`);
  - any type, if `16 < |packet pos - unit pos| <= 256` → teleport;
  - otherwise it re-paths the controller (`FUN_004fe276`, which overwrites the current path!)
    and builds a type-0 command, then hands it to `FUN_00460b41(unit+0x364)`. That function
    **returns immediately** when queue+0x10 == 0, which is the own unit's queue (the same flag
    makes `FUN_00460f96`/`FUN_004607ef` run local input). So the command is dropped. Net effect
    of an echo: nothing, a path reset that the next frame overwrites, or a teleport.
  - **Do not send it.** (High.)
- **No acknowledgement exists.** Nothing in the click/hold path waits for a reply. The tick
  clock never reads server time (the header +8 tick only feeds `FUN_0046fefd`/`DAT_0084e3e8`, a
  network-time stamp). (High.)
- **0x417** (`FUN_00450acd`/`FUN_00450caf`/`FUN_004512cd`, object `DAT_0084a7b0`) is the
  **camera** (free-look/pan toggle with the camera focus point), sent from the per-frame camera
  update. No reply is needed. (Medium-high.)
- **0x447** (`FUN_00573858`) asks for the info of a table entry (`FUN_0042855d`, 86 slots)
  and clears a 0x650 buffer at `acct+0xab3c`. A UI panel polls it (with 0x445/0x449 every 60 s
  from `FUN_005738f5`, and from `FUN_0057845e`/`FUN_0057885b`/`FUN_00578e21`). It has nothing to
  do with movement. A missing reply only leaves that panel empty. (Medium.)
- C->S 0x416 has a third sender: `0x415b56` sends **type 4**, the speed-hack check, when
  `timeGetTime` and `_time()` drift by more than 15 s. Type 1 comes from the stuck detector
  `FUN_0048d666`.

## 6. Why far targets: candidates, and how to tell them apart

A hop needs a tick where the body does not move (§3.3) or a burst of ticks. What differs
between near and far targets on the client:

| # | trigger | distance link | how to confirm |
|---|---|---|---|
| A | **A STOP is queued and runs on the next tick** (path cleared, state 7, then MOVE → state 8 + start anim 4). Sources: `FUN_0058b957` gets a path **failure** (0x58bf11, `FUN_004fe276` returned 0) → stop in `FUN_0058cc24`. Or `FUN_004a9204` misses the pick (0x4a942e). | Long or cross-tile queries fail more often. The goal must snap within 1 unit (`FUN_00452dda`, radius 100). Cross-tile goals go through the federation translate (`FUN_004539cb` else-branch, error 0xb). The terrain pick has a 200-unit limit. | count hits on **0x4a942e** and on the STOP path in `FUN_0058cc24` (after the call at 0x58cc84), and break on `FUN_004ff011` while walking. Breaking on `FUN_004ff011` is the most direct test: one hit per hop means A. The logs can hide these: the state-7 0x416 is only sent when you are ≥ 1.5 from the last *sent* position, which was the 0.5 s lookahead |
| B | the body stops because the carrot cannot advance: the path ended or is invalid, with no re-path between ticks (§3.5) | backwards (near) | count frames with more than one tick: watch `[DAT_0084b080+0x10] > 1` in `FUN_0044e17f` |
| C | **tick bursts from the float32 boot-time clock** (`DAT_00846e78`) | none by itself. But near targets keep stopping and starting (stop → `count<2` → clock reset), which re-syncs the buffer and hides it | check the uptime of the machine running Client.exe. Windows "fast startup" does not reset it, so weeks of uptime are common. A simulation of `FUN_004feb38` with resolution ≥ 62 ms gives repeated snaps and drops (§7). Reboot (true restart) and retest |
| D | frame hitches from per-frame pathfinding. Each held frame runs 3–4 PathEngine queries (`FUN_0058b288`, `FUN_004ff084`, `FUN_0058b957`), all under the critical section at `DAT_0084b008+0x1fc1c`, which the tile loader shares | long paths cost more | a frame-time graph. A hitch freezes the whole screen, not only the character |

My ranking: **A > C > D > B**. None of A–D is under server control. The original server could
not have prevented them either, except through the map: the navmesh and the place you walk.
If A (path failure) is confirmed, the minimal client patch is to retarget the `je 0x58c20d` at
**0x58bf11** to `0x58c263` (`xor al,al`, return 0). A failed re-path then keeps walking the
previous path instead of issuing STOP. Side effect: an unreachable click target no longer
cancels the order by itself. If the source is the pick miss (0x4a942e), it needs a different
patch. Confirm the trigger before patching.

## 7. Interpolation check (scratch simulation of `FUN_004feb38`)

With one snapshot per tick and an ideal clock: 0 snaps at 30/60/144/300 fps. With the tick clock
quantised to 62.5 ms: 1 snap in 10 s. At 125 ms (uptime over about 12 days) and 144+ fps: about
40 snaps and 10 drops in 10 s, steps up to 0.48 units (normal 0.03). So with a steady sim the
buffer is stable. Hops need missing ticks (A/B) or a coarse tick clock (C).

## 8. Answers to the four questions

1. **Path:** cursor pick (`FUN_004a9204`) → PathEngine path from the *render* position
   (`FUN_004fe276`, re-planned every held frame, twice) → order 0x853cd8 → per-frame MOVE
   command, run on the next 10 Hz tick → `FUN_004ff24e` advances the carrot at speed × 0.1 s
   and steers the physics body toward it → snapshot → `FUN_004feb38` interpolation. 0x416 is
   sent every 0.5 s while not idle, with the lookahead position. Distance-dependent pieces:
   the lookahead `min(path, 2.25)`, the path preview (10-unit samples, at most 15), the
   arrival test (speed × 0.15, only when not held), the pick limits (1.0 and 200), and
   cross-tile federation pathing. There is no "wait for server" or pending-move state, and no
   split between confirmed and predicted position.
2. **0x20 vs 0x02:** `type = (controller+0x56 == 0) ? 0x20 : 0x02` (0x4bbce0). +0x56 is physics
   +0x2e, set in `FUN_0050611d` when the ground contact is a CUnit model with byte +0x1a0 set,
   or a CTrigger. 0x20 is the normal case, and the receiver turns 0x02 into "stick to the
   platform" (`cmd+0x2d`). No enter-world field changes it. The original server would also have
   seen 0x20 on normal ground. Packet +0x12 is `unit+0x38`, not used for movement. Its 0xff/0x00
   flip is harmless.
3. **No reply is expected** for 0x416, 0x417 or 0x447 in the movement path (§5).
4. **Server fix: none.** Keep the echo off. Send S->C 0x416 for the own uid only as a type-1
   correction. Diagnose with the `FUN_004ff011` breakpoint (A) and the uptime check (C) above.
   Then patch the client as in §6 if A is confirmed.
