# Combat — attacks, skills, damage, death, respawn, buffs, cooldowns

Conventions as in group00..03: offsets from packet start (payload at +0x10), `extra` = header u16 at +6.
`me` = local player unit (`DAT_0084a758`), `unit+0x35e` = uid, `unit+0x3a0` = char record ("char").
Char stat block (0x5c bytes at char+0x443; the block sent in 0x41f/0x453/0x804/0x803):
+0x00 HP, +0x04 MP, +0x08 max HP, +0x0c max MP, **+0x1e s16 basic-attack range (x0.01 world units)**,
+0x36 u16 move speed, **+0x40 s16 revive delay in seconds**, **+0x44 s16 MP-cost reduction %**,
**+0x46 s16 cooldown reduction %** (offsets inside the block; char offsets 0x461/0x479/0x483/0x487/0x489).
Unit alive flags: `unit+0x36c` u8 alive, `unit+0x36d` u8 (both 0 = dead; revive writes u16 0x0101).
`unit+0x5f8` = HP shown on bars (lags the real HP at char+0x443).

## 0. The one thing to know: the client is hit-authoritative

There is **no "attack request" / "cast request" packet**. The client plays the swing/cast locally,
runs its own range/cooldown/cost checks, picks the targets itself (including AoE gathering), and at
the impact frame sends the **same opcodes the server uses to report hits** — 0x411 / 0x412 with the
target list filled in and every damage slot 0. The server fills in damage, the kill mask and the
attacker's HP/MP, and broadcasts the packet back to everyone **including the sender** (the sender's
own damage numbers only appear when the echo arrives). Cast/precast announcements (0x40f, 0x410)
go the same way but need not be echoed to the sender. (confidence: high — senders below build
0x40f/0x410/0x411/0x412 inline: `0xa53c0014/38/64/88` immediates.)

Client send sites (all `myUnit+0x35e` in extra and in +0x10):

| op | size | function | when |
|---|---|---|---|
| 0x40f | 0x14 | FUN_00461f47 (ActionSkill vtable 0x728578) | precast/charge start (skill has cast time, skill+0x4f) |
| 0x410 | 0x38 | FUN_00461fc1 via FUN_00463214 | skill fires and skill+0x34 != 0 (projectile/area skill; hits come later) |
| 0x411 | 0x64 | FUN_004621bd via FUN_00463214 | skill fires, skill+0x34 == 0, skill+0x2b == 0, skill+0x26 == 0 (instant hit) |
| 0x412 | 0x88 | FUN_0046260d via FUN_00463214 | skill fires, instant, with knock-back/dash/teleport (skill+0x2b or +0x26 != 0) |
| 0x411 | 0x64 | FUN_00462af7 (ActionAttack, vtable 0x728410) | **basic attack** impact ("Assert(m_pTarget)") |
| 0x411/0x412 | 0x64/0x88 | FUN_005a233f, FUN_005a2f4d, FUN_005a3942, FUN_005a3de6 | projectile / ground-field SFX reaches targets (flag 0x200 set; one packet per tick for fields) |
| 0x42b | 0x38 | FUN_004621bd / FUN_0046260d | instead of 0x411/0x412 when the skill was triggered by an item (scroll) |
| 0x450 | 0x1c | FUN_00462f64/0046316b | channelled interaction (already in group01) |

## 1. Client -> server

### 1.1 Basic attack = C->S 0x411 (skill id 0)
FUN_00462af7. confidence high.
- +0x10 u16 attacker uid (me)
- +0x12 u16 0
- +0x14 s16 skill id = **0**
- +0x16 u16 attack motion/combo index (ActionAttack+0x64) — echo it; remote clients use it to pick the swing animation
- +0x18 u16 flags = 0
- +0x1c f32 attacker x, +0x20 f32 attacker z
- +0x24/+0x28 = 0
- +0x34 u16 target uid (only target 0 is filled), +0x36 s16 damage = 0; rest of the 12 x {u16 uid, s16 dmg} list zero

### 1.2 Skill hit = C->S 0x411 (skill id > 0)
FUN_004621bd. confidence high (layout), medium (flag meanings).
- +0x10 u16 caster uid
- +0x12 u16 "display" skill id (ActionSkill+0x1c: the skill as slotted; FUN_004871cf maps buff-overridden skills) — echo
- +0x14 s16 skill id (Skill_Base id)
- +0x16 u16 0
- +0x18 u16 flags: 0x0100 = basic attack replaced by a buff-granted skill (FUN_004b96e4); 0x0200 = projectile/field tick (SFX senders); 0x1000 / 0x2000 = ActionSkill+0x110 == 1 / 2 (special-trigger skills; the handler shows UI notices 0x2711 / 0x271d) — echo all of them
- +0x1c f32 caster x, +0x20 f32 caster z
- +0x24 f32 target x, +0x28 f32 target z (target unit position, or the ground point for ground skills)
- +0x34 12 x {u16 target uid, s16 0}. Target 0 = the clicked target (skill+0x17 == 1) or self (skill+0x17 == 3 / skill+0x0c == 4); AoE skills (skill+0x43 == 1) get the list from FUN_00588a96 / FUN_00588e87: units within skill+0x44 radius of the point, filtered by FUN_00488461, max skill+0x22, nearest first.

### 1.3 Knock-back / dash / teleport hit = C->S 0x412
FUN_0046260d (and SFX senders). confidence high (layout).
- +0x10 caster, +0x12 display skill id, +0x14 skill id, +0x16 0, +0x18 flags (as 0x411)
- +0x1c/+0x20 f32 caster x,z; +0x24/+0x28 f32 target x,z
- +0x34 7 x {u16 target uid, s16 0}
- +0x50 7 x f32 new x, +0x6c 7 x f32 new z — **the client computes the push/pull destination** (FUN_005852a4 / FUN_00585771); 0,0 = not moved. Echo (optionally clamp).

### 1.4 Skill cast announce = C->S 0x410
FUN_00461fc1. confidence high.
- +0x10 caster, +0x12 display skill id, +0x14 skill id, +0x16 0
- +0x20 f32 target x, +0x24 f32 target z; for unit-target skills (skill+0x17 == 1 with skill+0x19 == 1, or +0x1a == 2) +0x20 = **target uid as a float** and +0x24 = 0
- +0x28/+0x2c f32 secondary point (dash/blink destination from FUN_005852a4), 0,0 = none
- +0x30/+0x34 = 0 (server fills caster HP/MP)

### 1.5 Precast = C->S 0x40f
FUN_00461f47. +0x10 u32 skill id. Nothing else. confidence high.

### 1.6 Item-triggered skill = C->S 0x42b (no S->C handler)
Size 0x38. +0x10 u8 container, +0x11 u8 slot, +0x12 u16 item code, +0x14 u16 1, +0x16 12 x u16 target uids (0x411 variant; the 0x412 variant leaves it zero), +0x30 f32 x, +0x34 f32 z. Reply: treat like 0x411 (broadcast 0x411 with the item's skill) + 0x427 for the consumed item. confidence medium.

### 1.7 Local gating (what the client refuses before sending)
FUN_00587abf (called from FUN_00588302 / skill bar FUN_005883b9). Returns an AR code (section 3); 0 = go.
- target: FUN_0058786d. skill+0x17 target type: 1 = unit, 2 = ground point, 3 = self. skill+0x16 relation bits: 1 self, 2 ally, 4 enemy (FUN_004872bd), 8 party member. skill+0x12 u32 class mask & target template(+0x3a4)+0x7c. Dead target -> 7 (WRONGTARGET); none -> 6.
- range: FUN_004bb979(target, range): dist < target radius + range. Range = skill+0x41 (u16, world units) or, for basic attacks, stat block +0x1e * 0.01 (default 2.0; status flag 0x2000 -> 1.5). Fail -> 2.
- cooldowns (all client-side, see section 6): per-skill (FUN_005851a9) -> 8; current action still running (FUN_004a15fc) -> 11; global (controller[0x1a]) -> 10; melee (controller[0x1b]) -> 9. If the blocking timer is < 1500 ms the command is queued instead of refused.
- cost: skill+0x39 type / +0x3d value: 4 = HP % (need HP >= HP*v/100) -> 28; 5 = MP (reduced by stat +0x44 %) -> 14; 0xe = TP (match obj +0xb0) -> 27; 6 = EXP (char+0x233) -> 30.
- pose/state table at 0x835eb4 (12-byte entries per command type) -> 4 (MUSTSTOP); casting while moving with skill+0x4f > 0 -> 4.

## 2. Server -> client

### 2.1 0x411 — hit result (basic attacks and instant/projectile skills)
Handler FUN_00475654. Size 0x64. confidence high unless noted.
- extra: attacker uid (see "numbers" below)
- +0x10 s16 attacker uid. Unknown uid in 1..0x2B05 -> client sends C->S 0x4ca (once per 50 s).
- +0x14 s16 skill id (0 = basic attack). Unknown non-zero id -> packet ignored.
- +0x16 u16 basic: attack motion index (event+9); skill: projectile FX param
- +0x18 u16 flags: **0x0004 critical** (crit hit SFX + crit number style 0x10), **0x0008 evade/miss** (shows "Evade", no blood), 0x0100/0x0200/0x1000/0x2000 echo. Basic attack flags 0 are treated as 1.
- **+0x1a u16 lethal mask**, bit i for target i: FUN_00485e4b(target, dmg, bit) does `if (HP < dmg) HP = bit ? 0 : 1; else HP -= dmg`. Without the bit an overkill leaves the target at 1 HP. (The group00 note calling this "critical" is wrong.)
- +0x24/+0x28 f32 ground point (used for ground skills' cast FX)
- **+0x2c u32 attacker HP, +0x30 u32 attacker MP** — applied with FUN_00472079 to the attacker for every receiver. **Must be the attacker's real values: 0 kills the attacker** (FUN_004890cb: alive and HP < 1 -> death).
- +0x34 12 x {u16 target uid, s16 amount}; uid 0 / unknown / template class 0x10 are skipped.

What each part drives:
- Animation: remote attacker -> FUN_0048d424 -> FUN_004bd8d5: skill 0 = event 6 (eADPTYPE attack: swing on the attacker, motion = +0x16, hit queued to the impact frame); skill > 0 with skill+0x34 == 0 = event 2 (unit) / 5 (ground) cast animation, then per target event 7 (hit). Local attacker: FUN_005865f3 attaches the hits to the running action so they play on its impact frame.
- HP: applied immediately on receipt (FUN_00485e4b); for skill+0x67 in {0x1f, 0x21, 0x2d} the amount is a heal HP / restore MP / drain MP instead (FUN_00485f58, clamped to max).
- Absorb: buff slot 0 (char+0x49f) — if its buff record's first effect code is 0x1b8 the damage hits MP first; else the u16 at entry+6 (char+0x4a5) absorbs and is decremented; when used up slot 0 is cleared.
- Numbers (FUN_0048aa79 -> FUN_00487ff8): shown only if the receiver is the attacker, the target, or **extra == the receiver's uid**; amount 0 shows nothing unless flag 0x8 ("Evade"). Styles: 0x40 normal, 0x10 crit, 4 evade, 0x20000000 heal HP, 0x4000000 MP.
- Death: after the hit plays, target char HP < 1 -> alive flag cleared, FUN_00488565 death animation.

### 2.2 0x412 — hit with displacement
Handler FUN_0047445f. Size 0x88. Same semantics as 0x411: +0x10 caster, +0x14 skill, +0x18 flags, +0x1a lethal mask (7 bits), +0x1c/+0x20 caster x,z (FX), +0x24/+0x28 target point, +0x2c/+0x30 caster HP/MP (same "0 kills" rule), +0x34 7 x {u16 uid, s16 amount}, +0x50 7 x f32 x, +0x6c 7 x f32 z (target moved there when non-zero). confidence high.

### 2.3 0x410 — cast announcement (no damage)
Handler FUN_00474062. Size 0x38. +0x10 caster, +0x14 skill id, +0x20/+0x24 target point (or target uid as float), +0x28/+0x2c dash/blink destination (skill+0x26 == 2 -> event 10 dash, == 1 -> event 11 teleport; 0,0 = skip), +0x30 u32 caster HP, +0x34 u32 caster MP (same "0 kills" rule). Plays the cast animation on remote casters (event 5 ground / 2 unit). Send to everyone except the caster (the caster already animates; echoing to it only re-applies HP/MP and pokes its action state machine — avoid). confidence medium-high.

### 2.4 0x40f — precast/charge animation
Handler FUN_004734b3. Size 0x14. extra = caster, +0x10 u32 skill id. Event 4 (ground) / 1 (unit) with the cast time from skill+0x4f. Broadcast to others. confidence high.

### 2.5 HP/MP and death/revive
- 0x420 (extra = unit, +0x10 HP, +0x14 MP) and 0x421 (+max) -> FUN_00472079 -> FUN_004890cb(unit, hp, mp):
  - unit alive and HP < 1 -> **death** (alive = 0, FUN_00488565, death animation, revive countdown for me)
  - unit dead and HP > 0 -> **revive in place** (FUN_00487e82: HP/MP set, alive flags 0x0101, idle animation)
  - This works for **every unit including the local player** -> the preferred authoritative death/revive signal. confidence high.
- 0x413 DoT/environment tick (FUN_00478c1a): extra ignored; +0x12 s16 source uid; +0x2a u16 lethal flag (non-zero lets HP reach 0); +0x2c u16 target uid; +0x2e s16 damage. Always shows the number on the target, dies if HP < 1. Size 0x30. confidence high.
- 0x806 mode 5 (FUN_0044e059): set HP 0 + death animation — **ignored for the local player**. Mode 2 removes. confidence high.
- 0x43e action 1: revive/clear dead for listed units — skips the local player. confidence medium.
- 0x804 (FUN_00472f4d): full refresh at a position, stats block at +0x28 (+0x28 HP, +0x2c MP); snaps the unit to +0x10/+0x14 if far, then FUN_004890cb -> revives if dead and HP > 0. Works for the local player. **This is the respawn packet.** confidence high.

### 2.6 Buffs
- Full list per unit: 0x41e (FUN_00470eeb): extra = unit; +0x10 u32 status flags (char+0x64d); +0x14 u16 (char+0x297); +0x18 u32 slot mask; +0x1c packed 12-byte entries in ascending slot order. Add/remove = resend the whole list (no delta opcode found). Also carried by 0x426/0x453 (+0x74 mask), 0x804 (+0xb8 count/mask, +0xbc), 0x803.
- 12-byte entry (FUN_004bf542 -> FUN_00485d07 -> FUN_004bd1d9): +0 s16 buff id (Skill_Buff.cdb, CBuffDB at DAT_0085005c; 0 = empty); +2 u16 param (source/transform uid for effect 0x167); +4 u16 stacks/level; +6 u16 absorb amount (shield); +8 u32 **remaining seconds** (x1000 ms; buff record+0x4c == 2100000000 = permanent and the value is used raw). confidence medium.
- Buff record: +0x44 u32 category; 3 x {s16 effect code at +0x64+8i, s32 value at +0x68+8i}. Codes seen: 0x1b8 mana shield, 0x167 transform, 0xe7/0xe8 levels -> char+0x657/0x658, 0x192/0x193/0x194/0x19b basic-attack override, 0x3e9. confidence medium.

### 2.7 Cooldowns
Client-only. On send the client starts skill+0x5b ms (minus stat +0x46 %) keyed by (skill id, skill+0x0d) via FUN_00584ed6; FUN_00584fab sets an explicit value. **No S->C cooldown set/reset opcode exists** (no handler touches FUN_0045c0ca/FUN_0041162f except 0x42a item path). The server cannot reset a cooldown; enforce server-side cooldowns by silently dropping early hits. confidence high.

## 3. Result code -> AR_* string
FUN_0048960f(code) shows `StringAll[key]` with key = table **0x835be0[code]** (= 0x7ed618[code] static copy), i.e. **code N -> entry N-1**. Codes 9 and 10 are never shown; the same code within 4000 ms is suppressed; 4 is suppressed on repeat.
Codes come from the client's own gates (FUN_00587abf / FUN_0058786d) — there is **no server packet carrying an AR code**, except 0x450 action 13 which shows code 0x20. confidence high.

| code | key | code | key |
|---|---|---|---|
| 1 | AR_ACTION_TARGET_INVISIBLE | 17 | (none) |
| 2 | AR_ATTACK_TOOFAR | 18 | AR_USEITEM_COOLTIME |
| 3 | AR_ATTACK_INVALIDSKILL | 19 | AR_WRONG_POSE |
| 4 | AR_ACTION_MUSTSTOP | 20 | AR_ITEM_LOCKED |
| 5 | AR_ATTACK_CANNOT_YET | 21 | AR_BUSY |
| 6 | AR_NEEDTARGETING | 22 | AR_WRONG_SLOT |
| 7 | AR_WRONGTARGET | 23 | (none) |
| 8 | AR_NEEDCOOLDOWN_SKILL | 24 | AR_CANT_IN_BATTLE |
| 9 | AR_NEEDCOOLDOWN_MELEE (silent) | 25 | AR_CANT_USE_NOTNOW |
| 10 | AR_NEEDCOOLDOWN_GLOBAL (silent) | 26 | AR_CANT_REPLACE_WEAPON_IN_WAR |
| 11 | AR_WAITACTIONFINISH | 27 | AR_SKILL_COND_ERROR_TP |
| 12 | AR_CANRESERVE | 28 | AR_SKILL_COND_ERROR_HP |
| 13 | AR_SKILL_COND_ERROR_STACK | 29 | AR_MOVE_ERROR_AutoMove |
| 14 | AR_SKILL_COND_ERROR_MP | 30 | AR_SKILL_COND_ERROR_EXP |
| 15 | StrDef_InventoryIsFull | 31 | AR_CANT_ON_HEROTRANSFORM |
| 16 | AR_CANT_IN_BATTLE | 32 | AR_CANT_IMPRINT_OTHERNOW |

To show an error from the server, use 0x41b (system message id) instead.

## 4. Minimal server algorithm

Keep per unit: hp, mp, maxes, alive, position, per-skill cooldown expiry.

**On C->S 0x411** (sender S, extra == S):
1. Drop if S is dead, attacker uid != S, the skill is unknown/not owned, or its cooldown has not expired (silently; the client already animated).
2. For each non-zero target uid in +0x34 (max 12): drop if dead/unknown/out of range (range + margin, positions lag) or not a valid target. dmg = formula (crit -> set flag 0x4; miss -> flag 0x8, dmg 0). Heals use a positive amount.
3. Apply: hp -= dmg; if hp <= 0 then hp = 0 and set bit i in +0x1a.
4. Deduct the skill's MP cost from S.
5. Build S->C 0x411 = the client's packet with: extra = S, +0x18 |= crit/miss bits, +0x1a = lethal mask, +0x2c = S.hp, +0x30 = S.mp, +0x36+4i = dmg_i. Send to every client that sees S or a target, **including S**.
6. Optional resync: 0x420 {hp, mp} for each target (and S) to its own client and observers.
7. For each target that died: it already plays the death on every receiver of step 5. To make it authoritative everywhere also send 0x420 hp=0 (works for players and monsters). For a match kill feed send 0x443. Schedule respawn.

**On C->S 0x412**: same, list of 7, echo +0x50/+0x6c (clamped), update server positions of moved targets.
**On C->S 0x410**: deduct cost, set cooldown, send 0x410 with +0x30/+0x34 = caster hp/mp to all observers except the caster; send the caster 0x420. Hits arrive later as 0x411/0x412 with flag 0x200.
**On C->S 0x40f**: forward to observers unchanged (extra = caster).
**Monster attacks**: send the same 0x411 with +0x10 = monster uid, skill 0, +0x16 motion index, +0x2c/+0x30 monster hp/mp, target list.
**DoT**: 0x413 {+0x12 source, +0x2a 1 if lethal, +0x2c target, +0x2e dmg}.

**Respawn**: the dead client counts down stat +0x40 seconds ("RemainReviveSec_D"/"WaitingRevive") and sends **nothing**. After that delay the server sends 0x804 (extra = uid, +0x10/+0x14 spawn x/z, +0x28 stats block with HP = max HP, buffs) to the player and observers; or, when changing scene, 0x44e/0x44f/0x2000 then 0x420/0x421 with HP > 0 (HP > 0 on a dead unit revives it). Same-place revive: just 0x420 with HP > 0.

## 5. Skill definitions — Setting/Skill_Base.cdb (CSkillDB)
Loader FUN_004c518d (filename string at 0x72e8e8); CSkillDB at DAT_00850058; lookup FUN_00497fba / FUN_004c2f58 ("Not In Skill DB (Id: %d)"). Rows are **NUL-separated text fields** (same tokenizer as StringAll: strchr(p,'\0'), atoi/atof), record struct 0xdd bytes. Column order -> record offset -> meaning (meaning confidence medium unless noted):

| col | off | type | meaning |
|---|---|---|---|
| 1 | +0x00 | int | skill id (high) |
| 2 | +0x04 | str | name key (-> +0x08 localized) |
| 3 | +0x0c | u8 | kind (4 = ground point + self in target list) |
| 4 | +0xb0 | u8 | ? |
| 5 | +0x0d | int | cooldown group key (with id) |
| 6 | +0x11 | u8 | use flags (bit1/2 targeting cursor behaviour) |
| 7 | +0x12 | int | target unit-class mask (high) |
| 8 | +0x16 | u8 | relation bits 1 self/2 ally/4 enemy/8 party (high) |
| 9 | +0x17 | u8 | target type 1 unit / 2 ground / 3 self (high) |
| 10 | +0x18 | u8 | ? |
| 11 | +0x19 | u8 | send target uid instead of point (with +0x17 == 1) |
| 12 | +0x1a | int | (== 2: unit target in 0x410) |
| 13 | +0x1e | int | ? |
| 14 | +0x22 | int | max AoE targets |
| 15 | +0x34 | u8 | delivery: 0 instant, non-0 projectile/SFX (5 = ground field, ticks) (high) |
| 16 | +0x35 | f32 | field tick/duration |
| 17,18 | +0xb1,+0xb3 | u16 | ? |
| 19 | +0x26 | u8 | movement: 1 teleport/blink, 2 dash (high) |
| 20-23 | +0x27..+0x2a | u8 | ? |
| 24 | +0x2b | u8 | projectile hit packet: 0-2 -> 0x411, 3-4 -> 0x412 (high) |
| 25-32 | +0x2c..+0x33 | u8 | (+0x30: turn caster toward target) |
| 33 | +0x39 | int | cost type 4 HP% / 5 MP / 6 EXP / 0xe TP (high) |
| 34 | +0x3d | int | cost value (high) |
| 35 | +0x41 | u16 | cast range, world units (high) |
| 36 | +0x43 | u8 | AoE flag (gather targets) |
| 37 | +0x44 | f32 | AoE radius |
| 38 | +0x48 | f32 | ? |
| 39 | +0x4c | u8 | chain/bounce flag (FUN_00584b1c) |
| 40,41 | +0x4d,+0x4e | u8 | ? |
| 42,43 | +0x5f,+0x63 | f32 | ? |
| 44 | +0x4f | int | precast / cast time ms (0 = instant) |
| 45 | +0x53 | int | channel duration ms |
| 46 | +0x57 | int | channel tick interval ms |
| 47 | +0x5b | int | **cooldown ms** (high) |
| 48 | +0xb5 | int | ? |
| 49 | +0x67 | u8 | effect type: 0x1f heal HP, 0x21 restore MP, 0x2d drain MP, else damage (high) |
| 50 | +0xb9 | int | ? |
| 51-56 | 2 x {+0x68,+0x70,+0x78} | int | requirements; +0x70 == 1 -> needs FUN_004b981e/004b98ee (item/buff) |
| 57-68 | 4 x {+0x80,+0x90,+0xa0} | int | effect slots (likely buff id / value / chance — damage is not read by the client) |
| 69 | +0xbd | int | ? |
| 70 | +0xc1 | int | required weapon type |
| 71,72 | +0xc5,+0xc9 | str | ? |
| 73 | +0xcd | int | ? |
| 74 | +0xd1 | str | description key (-> +0xd5) |

The client never reads damage numbers from this table: damage formulas are entirely server-side.
Related tables: Setting/Skill_Buff.cdb (CBuffDB, buff ids in 12-byte entries), Setting/Skill_TP.cdb (CTPSkillDB, 0x4b4), Setting/WeaponBase.cdb.

## Unknowns
- The damage formula and the meaning of the effect columns (+0x80..+0xac) — need the real Skill_Base.cdb rows (setting.jpk).
- +0x1000/+0x2000 flag semantics (ActionSkill+0x110); 0x42b reply; whether echoing 0x410 to the caster is harmless.
- Exact skill range units (u16 used without the 0.01 scale that basic-attack range gets).
