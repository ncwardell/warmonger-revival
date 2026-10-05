---
title: "Data tables"
---

# Warmonger / Crush Online game data tables (decoded)

Source: `data/setting/` (extracted from `setting.jpk`). Every file there is decoded into
`<Name>.tsv` in this folder: UTF-8, tab-separated, `#` comment lines first (format, loader,
notes), then a header row, then one row per record.

**Header convention** (same as `UnitDB.tsv`): `meaning@off` where `off` is the hex offset of
the record field the client loader writes the column to (`:f` = float). `cN@off` = column N
with no known meaning. `?` = guessed meaning. `name(Eng)` = the `*_key` column resolved
through `config/StringAll_Eng.cdb`. Tables the client never loads (server-only) have no
offsets and their names come from the data alone.

## .cdb text format (all `.cdb` except the CSV/APDC ones below)

CP949, every field NUL-terminated: `rows\0 cols\0`, then `rows x N` fields, then a trailer
`<byte length>\0 \0`. The second header number is the column count of the **original**
spreadsheet, not the number of fields stored (server-only columns were stripped on export):
**fields per row = (tokens - 2 - 2) / rows**. Loaders tokenise with `FUN_006dde60`
(strchr to NUL) + `FUN_006da829` (atoi) / `_atof`, so an empty field reads as 0. The common
open/header routine is `FUN_005cdf65` (stores rows at db+0x40, cols at db+0x44). Loaders were
found by xref'ing the `"Setting/<file>"` string address in your decompiled client (`disasm.txt`); a generic
summariser mapped each token to its `*(T*)(rec+off)` store.

## Tables

Rows = data rows (not counting comment/header lines). Key = lookup column.

### Rules-relevant (stats, exp, prices, drops, rewards)

| table | rows | key | purpose | loader | references |
|---|---|---|---|---|---|
| Level_Table | 31 | level | **Player exp curve** (exp@04: 700 → 42,350,740 at 30), fame-rank thresholds (fame_threshold@0c, 10 used), linear per-level values hp?/mp?/atk?/def? (130+30/lv, 70+20/lv, ...) | FUN_005ce0df (CItemLevelDB, DAT_00853c90) | 0x422 exp/level; HUD exp bar (0x534659); ranking FAME→FAMERANK (FUN_005cde32); FameRank |
| Level_Table_Guild | 10 | level | Legion level exp curve + per-level values | FUN_005ce2db (CLevelGuildDB) | guild opcodes 0x457.. |
| Item_Base | 1192 | id | **Items**: kind (ItemKind.tsv), buy/sell currency + price (currency 2 = gold, = 0x428 field), fame price, bind, required class, 10 stat options {type,value} (ItemOption.tsv; type 200 → WeaponBase), period | FUN_00446fca | 0x424/0x427 item records (+0 u16 code), shops, Npc_Carry, RandomBox, Quest rewards, Item_Make, WeaponBase |
| ItemOption | 47 | code | Stat/option code names (Attack, Ability Power, Armor, Health, crit, life steal, %-variants 101+, 212 CDR, 273 drop chance) — derived from StringAll | – | Item_Base opt*, Skill_Buff eff*, SetBounsItem, Item_Jewel |
| ItemKind | 46 | kind | Item kind names (31 weapon, 32 costume, 35 rune, 50-57 armour slots, 59 gold...) — from StringAll | – | Item_Base kind@1c |
| Npc_Carry | 171 | shop_id | **NPC shop inventories**, 30 items each; NPC → shop via UnitDB u16@a2 (units 203/204/330 → 281). Price = Item_Base buy_price | FUN_00446c3d (DAT_00853cbc); panel FUN_0056bd8b | UnitDB u16@a2; Item_Base; 0x44b NPC service, 0x452 price rate |
| PrimiumShop | 57 | id | Cash shop catalogue: item, price, currency?, discount, sale window (unix) | FUN_0059ce63 | 0x42f / 0x4b8 item shop, 0x484 jewel shop, 0x200f jewel balance |
| Gacha_00..06 | 83/84/59/24/188/91/2 | id | Hero gacha pools (item, grade). **No odds column** — server side | FUN_0059cd0e ×7 | 0x4aa hero gacha |
| RandomBox | 40 | id | Random box contents: 10 × {item, count, p} + gold? (no probability column) | FUN_00446a5a | Item_Base kind 28/29/30/43, 0x42d use item |
| Quest | 291 | id | **Quests**: prerequisites, 5 objectives (type 1 = kill unit, need, drop rate %, item = quest drops), **5 rewards {type, values}** (type 2 = exp, type 1 = item, 4 gold?, 5 fame?) | FUN_0043e5a5 | 0x48e–0x492 quests; UnitDB; Item_Base; QuestTalk |
| QuestTalk | 245 | quest_id | Quest NPC dialogue (10 lines) | FUN_0043e12d | Quest |
| NoticeQuest / NoticeQuestReward | 51 / 6 | id | Quest-board daily quests / completion rewards | FUN_0043ed10 / FUN_0043eeb7 | Quest |
| Item_Make | 465 | id | Crafting: 3 materials, gold cost, success %, result item | FUN_005ceaa5 | 0x4a8 craft |
| ItemSancMet | 81 | id | Reinforcement: gold + 6 steps × 5 {material, count} | FUN_004e28a2 | 0x436 reinforce |
| JewelSocket / JewelSocketMake | 21 / 210 | id | Socket profiles; jewel crafting/upgrade recipes | FUN_004e3d60 / FUN_004e3ea1 | 0x4a7, 0x4a8 |
| Item_Jewel | 211 | id | **Server-only.** Jewel/rune stats: level, option type/value | none | Item_Base 7002+ |
| SetBounsItem | 9 | id | Set bonuses: 8 pieces, 8 tiers {pieces, option, value} | FUN_004e2ea6 | Item_Base |
| WeaponBase | 100 | id | Weapon base values + 8 skill ids (4 normal, 4 hero) | FUN_004e2a41 | Item_Base opt type 200; Skill_Base; skills.md |
| Skill_Base | 675 | id | Skills: targeting, cost, range, AoE, cast/channel/cooldown ms, 4 effect slots {type, value/buff id, rate}. **No damage numbers** (server formula) | FUN_004c518d (CSkillDB) | 0x40f/0x410/0x411/0x412, WeaponBase, UnitDB skills, skillVisual, Skill_Buff |
| Skill_Buff | 844 | id | Buffs: duration ms, 3 {stat code, value} effects | FUN_004c45a4 (CBuffDB) | buff entries in 0x426/0x804/0x2000; Skill_Base eff values; WinAffect |
| Skill_TP | 21 | id | War "TP" skills: skill id, TP cost, cooldown | FUN_004c4994 | 0x4b4 |
| HeroData | 22 | id | Hero transforms: 10 skills, weapon/base, 4 stats | FUN_004e2c4e | 0x4aa, Gacha |
| Mastery / GuildMastery / FortMastery | 78 / 14 / 28 | id | Passive trees: tiers, max level, values, costs | FUN_005b96a4 / FUN_005b998e / FUN_005b9cf4 | 0x4c3 fort mastery, guild opcodes |
| ExpandSlot | 18 | step | Bag/storage expansion costs | FUN_004e26d4 | 0x47f expand bag, 0x499, 0x4a3 |
| Achievement_Base | 32 | id | Achievements: 10 goals + 10 rewards | FUN_00596986 | 0x485–0x489 |
| WinAffect | 7 | id | War-winner reward: duration, buff, item | FUN_005bf050 | 0x48a/0x48b |
| DungeonAdmission / Dungeon / Event_Dungeon | 15 / 3 / 5 | field | Dungeon entry tickets (item 688 ×N), displayed rewards; dungeon groups; event schedule | FUN_005c18d6 / FUN_004c2273 / FUN_005c1d9a | 0x47e/0x481 dungeon |
| GuildMissionReward | 3 | id | Legion mission rewards | FUN_005c1ba6 | guild |
| ConnectReward | 6 | step | **Server-only.** Play-time rewards (30..300 min) | none | – |
| Policy / PolicyActive / LabData | 14 / 18 / 8 | id | **Server-only.** Nation policies (3 levels of value/cost), active policies, legion lab | none | – |
| UnitDB *(kept)* | 512 | id | Units/monsters/NPCs (see docs/spec/monsters.md). Add: **u16@a2 = NPC shop id → Npc_Carry** | FUN_00499b74 | 0x803/0x805, Npc_Carry, Trigger |
| Create_Char | 4 | class | Creation classes: starting weapon choices, customisation lists | FUN_004c6298 | char create (skills.md §4) |

### World / UI / presentation

| table | rows | key | purpose | loader |
|---|---|---|---|---|
| SceneList *(kept)* | 133 | id | Scenes/fields and links | FUN_004c1c28 |
| Teleport_List *(kept)* | 340 | gate | Gates / teleport destinations (0x44c–0x44e) | FUN_004fddf8 |
| ZoneDB *(kept)* | 152 | id | Zone rectangles (CSV) | FUN_0046028a |
| ZoneTable | 5729 non-zero cells | z,x | BINARY 256×256 u32 zone grid (see file header) | FUN_004600b3, lookup FUN_004601fc |
| FieldNames *(kept)* | 136 | id | FieldName_<n> strings | – |
| WorldmapData | 89 | field | World-map rectangles | FUN_004c20c6 |
| Trigger | 123 | id | Field trigger/device objects (position, model, unit name) | FUN_005ba251 |
| deviceTrigger | 394 | id | BINARY 'APDC' 24-byte records (meanings unknown) | ref. FUN_004a8446 |
| sign | 20 | id | BINARY 'APDC' sign-post texts (Korean, UTF-16 pool); not loaded by client | none |
| weather | 120 files | scene | BINARY per-scene lighting (106 floats) | FUN_0047d69c |
| system_msg | 241 | id | System message id → string key (0x41b etc.) | FUN_00498386 |
| FameRank | 20 | rank | Fame rank names (thresholds in Level_Table) | FUN_0046fab5 |
| combatmessage | 20 | id | Floating combat-text styles | FUN_0048ec18 |
| LoadingTip, Speech, emotion, CommonIcon, AddonData | 10/15/54/78/4 | id | UI tips, NPC speech bubbles, emotes, icons, map layers | FUN_00497ddd / FUN_005a8fe5 / FUN_0059076b / FUN_005c1757 / FUN_005c21b6 |
| ColorDB, CustmizeBase, CostumeDB | 93/80/75 | id | Dye palette, face/hair parts, costume visuals | FUN_0046f3ce / FUN_0046f62b / FUN_004996e6 |
| skillVisual, sfx | 332 / 756 | id | CSV skill visual sets / SFX definitions (Skill_Base visual@bd) | FUN_005c02c9 / FUN_0058a629 |
| ObjectList, Acting, sound, FxTextures | 2366/12/523/2 | id | CSV model list, banners, sound ids, shader textures | FUN_00413a98 / FUN_0059b54b / FUN_0058f897 / – |
| constants, guisound, soundconfig | 39/5/4 | section,key | INI (constants.ini is UTF-16): fonts, navmesh build, HP-bar and chat colours, GUI sounds, volumes | FUN_0043178a / FUN_004bfdf9 / FUN_004c8d47 |
| Sl | 274 | idx | Chat profanity filter word list (UTF-16) | FUN_004cd139 |

Not converted: `DefaultDataList.txt` (1981 lines: plain list of asset paths preloaded at
start, loader FUN_00415fe1), `particle/*.txt` (UTF-16 INI particle emitters `[particleN]`
flags/pos/texName..., loader FUN_00414f24), `font/*` (TTF/OTF fonts).

## What is NOT in the client data (must be server-defined)

Monster HP/level/damage/exp/gold drops, skill damage formulas, gacha and random-box odds,
reinforce success rates (ItemSancMet has costs only), NPC shop restock, quest exp is present
(Quest rew type 2) but kill exp is not. Item_Jewel / Policy / PolicyActive / LabData /
ConnectReward exist only as server tables (shipped by accident) and are decoded here.

## Uncertain points

- Quest reward types other than 1 (item) and 2 (exp) are inferred from value ranges.
- Level_Table hp?/mp?/atk?/def? are not read by any client code found; the server used them.
- Many `cN` columns are unknown; offsets are exact (straight from the loaders).
- Gacha `grade` and PrimiumShop `currency?`/`discount%?` are guesses.
