---
title: "Group 02 — opcodes 0x47e..0x4b4"
---

# Group 02 — opcodes 0x47e..0x4b4

Conventions: offsets are from packet start (payload at +0x10). In every C->S packet in this group the
header `extra` (+6) is the local player's entity id (`DAT_0084a758+0x35e`), except 0x499 (char select),
which uses `DAT_00847ac8+0xec` (the client's own id/session word). All C->S buffers are zero-filled
before the fields are written (FUN_004a730b clear=1), so unwritten bytes are 0.
Global shorthands: `G` = DAT_00847ac8 (client game-state block), `PC` = local player's char record
(`DAT_0084a758+0x3a0`; PC+0x203 = the 0x240-byte character record from 0x2001, so PC+0x203 = u64 char id).
Inventory (bag 1) = `G+0x2850`, 70 slots x 16-byte item records (u16 item code first).
`G+0x634` = account Jewel (cash) balance (u32; +0x638 high word).

### 0x47e — dungeon / instance entry request
- dir: C->S
- c2s: size 0x18; +0x10 u32 nation/side byte (PC+0x655, sign-extended); +0x14 u32 entry choice index (0..2 from the "ok" path, 0..3 from the other path)
- s2c: none (no handler for 0x47e)
- reply: not in this group; the entry itself presumably comes back as a zone-change opcode. A minimal server can ignore it.
- confidence: medium
- notes: send sites FUN_00529cf6 (panel "ok" button) and 0x5735d5 (UI msg 0x26). Pairs with 0x481 (PanelDungeonEntry3).

### 0x47f — expand bag capacity
- dir: both
- c2s: size 0x18; +0x10 u32 bag type (1 = inventory, 6 = second bag/warehouse); +0x14 u32 expansion amount (edi at send time)
- s2c: min size 0x18; +0x10 u32 bag type (only 1 or 6 handled); +0x14 u8 new capacity/expansion value (type 1 -> G+0x27cc, type 6 -> G+0x3420)
- reply: 0x47f with the same type and the new value
- confidence: medium
- notes: handler FUN_00470240; send sites FUN_005629d5 (checks money PC+0x283 / jewels, "MoneyIsLow"/"NotEnoughJewel"), 0x579907 (type 1).

### 0x481 — dungeon entry panel data
- dir: S->C
- s2c: min size 0x134; +0x10 u8 nation filter (0 = all, else must equal PC+0x655 or packet is ignored); +0x12 u16 zone/dungeon id; +0x1a s16[10] selectable dungeon/mode ids (0 = end). The whole 0x134 bytes are copied into the panel.
- reply: none
- confidence: low
- notes: handler FUN_004719d5 -> FUN_00535827 (PanelDungeonEntry3). In mode 0x78 entries are hidden by level (PC+0x237) thresholds 0x14..0x1c.

### 0x482 — inspect player (target info) request
- dir: C->S
- c2s: size 0x18; +0x10 u32 target entity id (must be a player, entity type 2, id < 0x2eef)
- reply: 0x483
- confidence: high
- notes: FUN_005714b0 (PanelTargetInfo). The panel remembers the target id itself; reply does not need to echo it.

### 0x483 — inspect player result
- dir: S->C
- s2c: min size 0xfc; +0x44 u32 nation fame (-> char+0x651); +0x4c 16 bytes (-> char+0x263, costume/appearance words); +0x5c 32 bytes (-> char+0x243, equipment item codes); +0x7c 0x80 bytes (detail block copied to the panel, likely equipment records)
- reply: none
- confidence: medium
- notes: handler FUN_00471a4e -> FUN_005715a1; ignored unless the TargetInfo panel is open; target taken from the panel's stored id.

### 0x484 — shop buy (jewel shop)
- dir: C->S
- c2s: size 0x1c; +0x10 u64 product id; +0x18 u32 price after discount (in jewels)
- reply: unknown (likely an inventory/jewel update opcode outside this group, e.g. 0x4a4-style balance update)
- confidence: low
- notes: send at 0x5650fe inside the shop panel ("Buy", "ChargeJewel", "StrDef_NotEnoughJewel"); the s2c file lists the wrong enclosing function.

### 0x485 — request achievement list
- dir: C->S
- c2s: size 0x18; no payload fields (all zero)
- reply: 0x486 with the achievement table
- confidence: medium
- notes: FUN_0052f2a5 (PanelCharacterAchieve), sent when the window opens.

### 0x486 — achievement table
- dir: S->C
- s2c: min size 0x210; +0x10 0x200-byte table -> G+0x3424 (40 entries x 12 bytes used; byte +1 of each entry = grade/level)
- reply: none
- confidence: medium
- notes: handler FUN_00470731; fires UI msg 0x38. All-zero table is acceptable.

### 0x487 — claim achievement reward
- dir: C->S
- c2s: size 0x18; +0x10 u32 achievement index; +0x14 u32 its current grade (s8 from G+0x3425+idx*0xc)
- reply: 0x488 (table + jewels) and/or 0x48b (reward item)
- confidence: medium
- notes: FUN_0052f30b, "Reward" button.

### 0x488 — achievement table + jewel balance
- dir: S->C
- s2c: min size 0x214; +0x10 0x200-byte achievement table -> G+0x3424; +0x210 u32 jewel balance -> G+0x634
- reply: none
- confidence: medium
- notes: handler FUN_00470763; UI msgs 0x38 and 0x1b.

### 0x489 — achievement(s) completed notice
- dir: S->C
- s2c: min size 0x238; +0x10 u8[40] per-achievement "newly completed" flags; +0x38 0x200-byte table -> G+0x3424
- reply: none
- confidence: medium
- notes: handler FUN_00479c30; shows a toast "Achievements.%02d" per flagged entry.

### 0x48a — claim win/affect reward
- dir: C->S
- c2s: size 0x18; +0x10 u32 reward index (1..6)
- reply: 0x48b
- confidence: medium
- notes: FUN_0052cf63 (PanelWinAffect).

### 0x48b — affect reward result
- dir: S->C
- s2c: min size 0x28; +0x10 u8 reward-state byte (-> PC+0x296); +0x12 u16 inventory slot; +0x14 u32 -1 = no item, else item granted; +0x18 16-byte item record (u16 item code first) written to bag 1 slot
- reply: none
- confidence: medium
- notes: handler FUN_00476fa7; message "GUI_WinAffect_RewardItemMsg_D".

### 0x48c — world-map location action (warp/move to location)
- dir: C->S
- c2s: size 0x18; +0x10 u32 location id (1..0x56)
- reply: unknown (probably a teleport/zone change outside this group)
- confidence: low
- notes: FUN_00578c17, world map panel, a specific button when the location is enabled.

### 0x48d — match scoreboard / battle result
- dir: S->C
- s2c: min size 0x652; +0x10 u32[2] team values (score); +0x18 u32[3]; +0x24 [2 teams][15] x 8-byte stats (+4 u16 kills, +6 u16 assists); +0x114 [2][15] x 0x2c-byte players (+0 char[0x2a] name, empty = no player; +0x2a u16 race/class); +0x640 [2 teams][9] u8 award slots (3 award types x 3 player indices)
- reply: none
- confidence: medium
- notes: handler FUN_00471a6d -> G+0xab4c, UI msg 0x23; rendered by FUN_00576302 (Name/Race/Kill/Assist/Icon0-3, AttTitle/DefTitle). Relevant to match flow (end of match).

### 0x48e — quest accept / complete
- dir: C->S
- c2s: size 0x18; +0x10 u16 related id (NPC/quest giver or 0); +0x12 u16 action (1 = accept, 2 = complete); +0x14 u16 quest step/sub id; +0x16 u16 quest id
- reply: 0x491 (single quest slot update)
- confidence: medium
- notes: send sites FUN_0055c84c ("QestAccept"), FUN_00597990, FUN_0059a36b (only when a free slot exists in G+0x2cc8).

### 0x48f — quest objective/choice action
- dir: C->S
- c2s: size 0x18; +0x10 u16 quest id; +0x12 u16 quest step (list entry +0xc); +0x14 s16 choice (-1 sent as 0)
- reply: probably 0x491
- confidence: low
- notes: FUN_00597a70.

### 0x490 — quest list (full)
- dir: S->C
- s2c: min size 0x1a8; +0x10 u16 quest counter A (-> G+0x2e68); +0x14 u32 (-> G+0x2e6c); +0x18 0x28 bytes quest flags (-> G+0x2e30); +0x40 15 x 0x18-byte quest slots (-> G+0x2cc8; slot +0 u16 quest id, 0 = empty)
- reply: none
- confidence: medium
- notes: handler FUN_0047529d -> FUN_00470940 (creates quest manager) + FUN_00599b7f; UI msg 0x26. Likely sent at world entry; an all-zero payload is safe.

### 0x491 — quest slot update
- dir: S->C
- s2c: min size 0x5c; +0x10 s8 slot (0..14); +0x11 u8 notify flag; +0x12 u16 counter A (-> G+0x2e68); +0x14 0x28 bytes quest flags; +0x40 u32 (-> G+0x2e6c); +0x44 0x18-byte quest slot record
- reply: none
- confidence: medium
- notes: handler FUN_004752b3 -> FUN_00599ab2.

### 0x492 — quest reward/item choice
- dir: C->S
- c2s: size 0x1c; +0x10 u16 quest step; +0x12 u16 quest id; +0x14 u16 extra arg; +0x16 s16 choice index; +0x18 u32 arg
- reply: probably 0x491
- confidence: low
- notes: FUN_00597b0e / FUN_00597c31.

### 0x493 — exchange decomposition points for item
- dir: both
- c2s: size 0x484; +0x10 u8 count/flag; +0x12 u16 item code (rest zero)
- s2c: min size 0x484; +0x14 0x460-byte full inventory (70 x 16 -> G+0x2850); +0x474 u16[3] gained item codes; +0x47a u16[3] gained counts; +0x480 u16 decomposition points (-> PC+0x293)
- reply: 0x493 with refreshed inventory and points
- confidence: medium
- notes: handler FUN_00471b4e; send at 0x579bb7 ("StrDef_NotEnoughDecompositionPoint", "InventoryIsFull").

### 0x494 — save quick-slot bar
- dir: C->S
- c2s: size 0x28; +0x10 u8[8] slot type (0 = item, 1 = skill); +0x18 u16[8] item code / skill id (0 = empty)
- reply: none
- confidence: high
- notes: FUN_005125e8; mirrors G+0x2cc0/G+0x2cb0.

### 0x495 — GM command
- dir: C->S
- c2s: size 0x118; +0x10 u32 command code (e.g. 0x67/0x68); +0x14 u32 arg; +0x18 char[256] text
- reply: none needed
- confidence: medium
- notes: 14 send sites in the GM tool panel (FUN_00521194 etc.).

### 0x496 — open GM tool
- dir: S->C
- s2c: min size 0x11 (no fields read)
- reply: none
- confidence: medium
- notes: handler FUN_00471f92 opens PanelGMTool. Do not send to normal players.

### 0x498 — item/mail list action (context 0x45 dialog)
- dir: C->S
- c2s: size 0x30; +0x18 u64 entry id; +0x20 u64 own character id (PC+0x203); +0x28 u16; +0x2a u16; +0x2c u32 (fields of the selected list entry)
- reply: unknown
- confidence: low
- notes: FUN_0053a7c2; 2-second client cooldown afterwards.

### 0x499 — buy character slot (character select)
- dir: both
- c2s: size 0x20; no payload fields (all zero); header extra = G+0xec
- s2c: min size 0x20; +0x10 u32 result (0 = ok, else "CharSel_Msg_BuySlotFail"); +0x14 u32 slot index (0..4); +0x18 u32 / +0x1c u32 new jewel balance (lo/hi -> G+0x634/0x638)
- reply: 0x499 result=0, slot = first locked slot, balance
- confidence: high
- notes: handler FUN_0047630a sets the slot's char id to 0. In the 0x2001 character list a slot whose u64 char id is 0xFFFFFFFFFFFFFFFF is LOCKED (purchasable); 0 = empty and usable. Send site FUN_004935a7.

### 0x49b — batch entity state events
- dir: S->C
- s2c: min size 0x332; 200 entries of 4 bytes starting at +0x12: u16 entity id (<=0 skips), s8 state, u8 pad
- reply: none
- confidence: medium
- notes: handler FUN_00470508; each entry goes through the same path as single opcode 0x806 (FUN_0044e059: 2 = remove entity, 5 = reset/clear, 1/6 = other state changes).

### 0x49c — guild war: request eligibility
- dir: both
- c2s: size 0x18; +0x10 u32 nation (PC+0x655); +0x14 u32 fort id (G+0x64c)
- s2c: min size 0x18; +0x10 u32 result: 1 = allowed (opens Guild_GuildWarRequest panel), 2/3/4 = open other guild-war panels, 5 = "already requested"
- reply: 0x49c with +0x10 = 1
- confidence: medium
- notes: handler FUN_004707c5 -> FUN_004887ff; ignored unless the client set its "waiting" flag (sent from FUN_0056dd87).

### 0x49d — guild war: submit request
- dir: C->S
- c2s: size 0x24; +0x10 u32 nation; +0x14 u32 fort id; +0x18 u32 guild rank/level (PC+0x27f); +0x1c u32 bid amount (guild money)
- reply: unknown
- confidence: low
- notes: send at 0x528b07 ("GuildMoneyIsLow").

### 0x49e — fort: collect tax
- dir: C->S
- c2s: size 0x1c; +0x10 u32 fort id (0..0x13)
- reply: unknown
- confidence: medium
- notes: send at 0x533b87 ("TaxRecv"); only when the player's guild owns the fort (G+0x64e).

### 0x4a0 — sort bag 6
- dir: C->S
- c2s: size 0x6c; +0x10 u8[90] new order (source slot for each position)
- reply: none needed (client re-sorts locally)
- confidence: medium
- notes: FUN_004e17f2.

### 0x4a1 — use item after cast bar
- dir: C->S
- c2s: size 0x18; +0x10 u8 1; +0x11 u8 inventory slot; +0x14 u32 item code
- reply: unknown (inventory update)
- confidence: low
- notes: FUN_00546fb0; sent when a timed channel finishes and the slot still holds the same item.

### 0x4a2 — entity stats / equipment refresh
- dir: S->C
- s2c: min size 0x20c; header +6 u16 = entity id; +0x10 u16 / +0x12 u16 quest counters (own char -> G+0x2e68/0x2e6a); +0x14 u32 effect id (0 = none; shows an effect on the local player); +0x18 u32 (-> G+0x2e6c); +0x1c u32 nation fame (-> char+0x651); +0x20 16 bytes (-> char+0x263); +0x30 0x180-byte equipment/appearance block (FUN_0046fd59); +0x1b0 0x5c-byte stats block (FUN_00472103)
- reply: none
- confidence: medium
- notes: handler FUN_004752cb. The same sub-blocks are parsed by other entity handlers, so their layout is shared.

### 0x4a3 — buy quest slot page
- dir: C->S
- c2s: size 0x18; +0x10 u32 page number (1-based, one packet per page)
- reply: 0x4a4
- confidence: medium
- notes: sent from FUN_0055c84c (quest window Tab_2) for each locked page up to the clicked one.

### 0x4a4 — quest page purchase result
- dir: S->C
- s2c: min size 0x18; +0x10 u16 counter A (-> G+0x2e68); +0x12 u16 unlocked quest pages (-> G+0x2e6a); +0x14 u32 new jewel balance (-> G+0x634)
- reply: none
- confidence: medium
- notes: handler FUN_00475412.

### 0x4a5 — fort level up
- dir: C->S
- c2s: size 0x20; +0x10 u32 fort id; +0x14 u32 nation; +0x18 u32 guild id; +0x1c u32 new level (current + 1)
- reply: unknown
- confidence: medium
- notes: send at 0x533c35 ("FortLevelUp").

### 0x4a6 — fort facility purchase
- dir: C->S
- c2s: size 0xd0; +0x10 u32 fort id; +0x14 u32 nation; +0x18 u32 guild id; +0x1c u32 facility/item id (rest zero)
- reply: unknown
- confidence: low
- notes: send at 0x532ce2; checks the cost against fort funds.

### 0x4a7 — socket jewel equip / unequip
- dir: C->S
- c2s: size 0x1c; +0x10 u8 item slot; +0x11 u8 jewel slot; +0x12 u8 socket index; +0x14 u16 recipe/jewel id; +0x16 u16 1 = equip, 0 = unequip; +0x18 u16; +0x1a u16 jewel item code (equip only)
- reply: unknown (inventory update)
- confidence: low
- notes: send sites 0x545b89 / 0x546a6f (PanelJewelSocket).

### 0x4a8 — jewel upgrade / item craft
- dir: C->S
- c2s: size 0x58; +0x10 u16 recipe id; +0x12 u16 target code; +0x14 u8 slot; +0x18.. material inventory slots (u32 each)
- reply: unknown
- confidence: low
- notes: send at 0x545431 (PanelJewelUpgrade / PanelMakeItem).

### 0x4a9 — special slot item update
- dir: S->C
- s2c: min size 0x24; +0x14 16-byte item record (u16 item code first) -> G+0x2e58 (bag type 5, single slot)
- reply: none
- confidence: medium
- notes: handler FUN_004704c8; UI msg 0x3a. Same store as 0x427 sub-type 5.

### 0x4aa — hero gacha draw
- dir: both
- c2s: size 0xcc; +0x10 u8 gacha type (rest zero)
- s2c: min size 0xcc; +0x10 s8 gacha type (1..6 picks a result effect); +0x12 u16[10] inventory slots; +0x28 10 x 16-byte item records (u16 code 0 = unused); +0xc8 u32 next free-draw time (0 = keep)
- reply: 0x4aa with the drawn items
- confidence: medium
- notes: handler FUN_00472798 (PanelHeroGacha/Result); send sites FUN_00514328, 0x564e2c, 0x5653ee.

### 0x4ac — party command
- dir: C->S
- c2s: size 0x40; +0x10 u32 sub-command (0 = invite, 1 = accept invite, 3 = leave, 4 = kick, 5 = give leader/"Move"); +0x14 u32 target entity id (own id for leave, 0 for invite by name); +0x18 char[40] name (invite/accept)
- reply: 0x4ad (party member list)
- confidence: medium
- notes: send sites FUN_0052646e (Ban/Exit/Move), FUN_005274c0 (accept "ok"), 0x57e870 / 0x58218c / 0x5cf872 ("AddParty").

### 0x4ad — party member list
- dir: S->C
- s2c: min size 0x108; +0x10 u32 party id (0 = no party); +0x14 u32 leader/extra; +0x18 5 x 0x30-byte members (+0 u16 entity id, +8 char[] name)
- reply: none
- confidence: medium
- notes: handler FUN_004770a1 -> G+0xb2b4; prints "msg_partyadd_s"/"msg_partydel_s" by diffing; UI msg 0x3b.

### 0x4b1 — set decomposition mode
- dir: C->S
- c2s: size 0x18; +0x10 u32 mode (0..4)
- reply: none (client sets PC+0x295 itself); server may answer 0x4b3
- confidence: medium
- notes: FUN_00579420 ("DecomCombo").

### 0x4b2 — decomposition result
- dir: S->C
- s2c: min size 0x48; +0x10 u16 decomposition points (-> PC+0x293); +0x12 u16[3] inventory slots (<70); +0x18 3 x 16-byte item records
- reply: none
- confidence: medium
- notes: handler FUN_00471c88; UI msg 0x3c.

### 0x4b3 — decomposition points / mode
- dir: S->C
- s2c: min size 0x14; +0x10 u16 points (-> PC+0x293); +0x12 u8 mode (-> PC+0x295)
- reply: none
- confidence: high
- notes: handler FUN_004707e8.

### 0x4b4 — TP skill selection
- dir: C->S
- c2s: size 0x14; +0x10 u16 slot/group id; +0x12 u16 chosen skill id
- reply: unknown
- confidence: low
- notes: FUN_0052d716 (PanelTPSkillQuick/Hud).
