# Skills — where the skill bar comes from

Short answer: **skills are the equipped weapon's.** There is no skill-list packet and no
learning step. The skill bar shows 4 skills for the main weapon (equipment slot 0) and 4 for
the sub weapon (slot 1). The client only loads them when the equipment container changes
**in game**, so after 0x2000 the server must send a **0x427 for container 3 slot 0**
(the weapon the slot record already has). Server code: `WarmongerRevamp/server/skills.py`.

## 1. Data chain (all client-side tables)

```
slot record +0x40 (char+0x243)  u16 item code, e.g. 10017 "Magical Wrath Blade"
  -> Item_Base.cdb row: 10 option pairs {type, value} (cols 20..39, record +0x3e/+0x42, stride 8)
     option type 200 = WeaponBase id                      (10017 -> 18)
  -> WeaponBase.cdb row (stWeaponBaseDef, 0x38 B): +0 id, +4..+0x10 4 ints, +0x14 int,
     +0x18 8 x Skill_Base id                               (18 -> 5022 5023 5024 5025 0 0 0 0)
  -> item record +0xab = WeaponBase def, +0xaf..+0xcf = 8 Skill_Base def pointers
```

- Item_Base loader FUN_00446fca (0x4474be: `if option type == 200 -> FUN_004412e9/FUN_004e1c8d`,
  then FUN_00497fba for each of the 8 ids). confidence high.
- WeaponBase loader FUN_004e2a41 (CWeaponBaseDB, singleton DAT_0084a738). confidence high.
- CDB text format: `count\0 header\0` then rows of NUL-separated fields, then a trailer
  (byte offset) — the header's second number is **not** the column count; use
  `(tokens - 4) / count` (Item_Base 45, WeaponBase 14, Skill_Base 74, Create_Char 19).

## 2. Client code path

| step | function | what |
|---|---|---|
| equip changes | FUN_00478d54 (0x427, container 3), FUN_004725ae (0x426, self), FUN_00472f4d (0x804, self), FUN_0048912f (alt. avatar builder) | call FUN_005848d5 on the skill controller DAT_00853cc8 |
| load skills | FUN_005848d5(ctrl, slot or -1) | for equipment slot 0/1 (FUN_004dfe59(3, slot) = char+0x243+slot*16): if the item code differs from the cached one (ctrl+0xf4+slot*0x60), copy item+0xaf[0..3] into the set |
| overrides | FUN_005849b2 | buff-granted replacements; then **UI event 0x18** (0x584b0d) |
| skill bar | DashboardHUD FUN_0051324a event 0x18 -> FUN_00512470 | reads FUN_00486387(ctrl) (+0xa4 normal, +0x168 / +0x22c transform sets) +0x10: 2 x 4 skill defs, stride 0x60; buttons "SoulWeaponSkillSlot%d" / "SubSoulWeaponSkillSlot%d" (FUN_005129d9). Kind (skill+0xc) 2 = passive, shown disabled |
| cast | FUN_005883b9 -> FUN_00586bf6 | needs button enabled, no global cooldown, own cooldown expired, kind != 2, skill reqs (+0x68/+0x70 type 1 = needs buff) met; then FUN_00587abf checks (combat.md §1.7) |

Skill set layout (base = ctrl+0xa4 + slot*0x60): +0x00 ids[4], +0x10 defs[4], +0x20 ids[4]
(display), +0x30 defs[4], +0x40 int[4] (zeroed), +0x50 cached 16-byte weapon item.

**Why the bar is empty:** the game-scene builder FUN_0048b435 (run from 0x2000) creates the
controller (FUN_00584ce6) but never calls FUN_005848d5, so the weapon in the slot record is
drawn on the avatar but its skills are never loaded. confidence high.

Not involved: player level (no gate found), Mastery.cdb (passive tree), Skill_TP.cdb (match
"TP" skills, C->S 0x4b4), HeroData.cdb (hero transforms; their skills go to the transform sets).
The quick bar (0x2000 +0x50c u16[8] codes, +0x51c u8[8] types; acct+0x2cb0/+0x2cc0) is for
items: drag-drop (FUN_005127ab) only accepts items and FUN_00512081 only draws type 0. Type 1
(skill) is only used to show cooldowns (FUN_00511f2f).

## 3. What the server sends

1. Slot record (0x2001) +0x40: the main weapon (16-byte item, u16 code first). The client's
   create-character request already fills it with the weapon picked at creation. +0x50: sub
   weapon (optional).
2. 0x2000 as before. Optional: the class's other starting weapons in the bag (+0xac, 70 x 16 B).
3. After 0x2000 + 0x41f: **0x427** (0x28 bytes, extra = player uid): +0x10 u16 reason 0,
   +0x12 u16 container 3, +0x14 u16 slot 0, +0x18 16-byte item (code = the record's weapon).
   One more for slot 1 if there is a sub weapon. 0x426 also works but carries the stat block
   and buffs; 0x804 also repositions.
4. Weapon swap: C->S 0x42a (move item) — echo it (extra = uid) to perform the swap
   (FUN_004e1357); that path does **not** reload skills, so follow it with a 0x427 for any
   container 3 slot involved.
5. Re-send step 3 after every 0x2000 (a full reload builds a fresh controller).

Casting itself needs no server reply (combat.md): the client animates and sends 0x40f/0x410/
0x411/0x412; the server applies damage and MP cost.

## 4. Starting weapons and their skills (Create_Char + Item_Base + WeaponBase + StringAll_Eng)

| class | weapon item | WeaponBase | skills |
|---|---|---|---|
| 1 Saint | 10017 Magical Wrath Blade | 18 | 5022 Blade storm, 5023 Wings of fair wind, 5024 Blink like wind, 5025 Wrath of the West |
| 1 Saint | 10011 Magical adapted Dual Gun | 12 | 5102 Ankle Aim, 5103 Rapid Reload, 5104 Entangling Bullet, 5105 Suppressing Fire |
| 1 Saint | 10001 Magical Thunder Wand | 2 | 5004 Thunderbolt, 5005 Lightning Strike, 5006 Ball of Lighting, 5007 Might of Thunder God |
| 1 Saint | 10002 Magical Life Wand | 64 | 5277 Mother Nature's Blessing, 5279 Blessing of Light, 5280 Essential Blessing, 5281 Savior's Gift |
| 4 Punisher | 15007 Magical judge Dagger | 29 | 5026 Shadow Hurl, 5027 Shadow Walk, 5028 Poisonous Swamp, 5029 The Dark Art |
| 4 Punisher | 15004 Magical Frost Bow | 26 | 5112 Sharp Edges, 5113 Potential Power, 5114 Hail of Arrows, 5115 Spinning Whirlwind |
| 5 Gardian | 20001 Magical Demolition Hammer | 43 | 5036 Soul Infestation, 5038 Aura of Demise, 5040 Severe Blow, 5041 Dark Transformation |
| 5 Gardian | 20021 Magical Protect Cannon | 63 | 5107 Nimble Pursuit, 5109 Firm Hand, 5110 Buckshot, 5111 Explosive Mortar |
| 5 Gardian | 20003 Magical Crush Hammer | 45 | 5067 Crushing Blow, 5068 Head Butt, 5069 Howl of Victory, 5070 Unyielding Will |
| 7 Valkyrie | none listed | | |

All 36 are active (Skill_Base kind 1), cost MP, no requirements, no weapon-type column set.
Create_Char row: class id, ?, ?, comment key, chart, 4 x {weapon item, name key}, 3 appearance
lists, 3 portrait lists.

## Unknowns
- Whether the sub weapon slot (container 3 slot 1) has restrictions (level, unlock); untested.
- Item 16-byte layout beyond +0 code / +4 count.
- Whether 0x42a needs any check besides the echo (the client validates class before sending).
- Not yet confirmed in the live client; derived from the decompile and data.
