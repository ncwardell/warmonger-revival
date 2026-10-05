---
title: "Server rules checklist"
---

# Server rules checklist

Concrete rules and values the server has to implement, recovered from player sources. Each line: the rule, where it comes from, and a confidence:

- **H** — in the client data, or several independent sources agree.
- **M** — one clear source (a guide or a screenshot).
- **L** — vague, contradictory, old (Crush Online era) or a guess.

Where the client data and a 2018 guide disagree, **the client is the final build: use the client value** and keep the guide value as history. Details and full citations are in the topic pages: [[gameplay/maps-and-dungeons|Maps and dungeons]], [[gameplay/classes-and-legions|Classes, nations and legions]], [[gameplay/items-and-crafting|Items and crafting]], [[gameplay/pvp-and-matches|PvP]], [[gameplay/progression-and-economy|Progression and economy]].

## Characters and accounts

- [ ] Nation is per account; all characters share it; changeable at the castle (moves the whole account). — [noob][g-noob], [strategy][g-strat] — **H**
- [ ] Armia (green, third nation) not selectable; only Arslan and Erion. — [definitive][g-def], [PT-BR][g-ptbr] — **H**
- [ ] Classes Punisher / Saint / Guardian, two weapons each, weapon decides the 4 skills; X = hero transform. — guides + `WeaponBase` — **H**
- [ ] Max level 30; exp curve from `Level_Table`. — client + guides — **H**
- [ ] Hero transformation only at level 30. — [Turkish][g-tr] — **M**

## Dungeons

- [ ] Entry costs Dimensional Energy (item 688) per `DungeonAdmission` (normal/hard counts). — client; guide tables differ by patch — **H**
- [ ] Dimensional Energy sold by Wren for 5,000 base (5,500 shown with tax). — client + [definitive][g-def] — **H**
- [ ] Hard mode: more/stronger monsters, boss at the end, better loot. — [noob][g-noob] — **H**
- [ ] One instance per portal, max 5 players; "Can not enter" option locks the instance to the party. — [noob][g-noob] — **M**
- [ ] Solo: no respawn. Party of ≥2 in hard mode: respawn after the room is cleared, first after ~3–5 min (or when the dungeon timer reaches 10:00 / after 9 min), then every ~1 min; faster with more players. — [ES def][g-def-es], [Turkish][g-tr], [strategy][g-strat] — **M** (numbers vary)
- [ ] Loot: every party member who damaged the monster and is alive gets a drop; party size raises drop rate. (March 2018: last hit only.) — [Turkish][g-tr], [noob][g-noob] — **M**
- [ ] Dungeon tier on a land = distance (cells) from the nearest fort of the owning nation; Lv 1 (Chepa) next to forts, Lv 8 far away; each nation sees dungeons on its own lands only. — [Turkish][g-tr], [strategy][g-strat], map images — **M**
- [ ] Lv 1–4 dungeons drop T1 gear, Lv 5–8 drop T2; dropped gear comes pre-reinforced at a random level (+0…+11 seen). — [dungeons][g-dng] images — **H** (tiers), **M** (random +level)
- [ ] Boss per dungeon and multi-boss fights (Demon Hell ×2, Thorn's Hell ×3). — [dungeons][g-dng], UnitDB — **M**
- [ ] Event dungeons (Avenue of Spirit, Place for Scattered Troops, Gollam Hill, Siren Lake, Nas Village) open on random lands on a schedule (`Event_Dungeon`: 180 / 80-minute windows). — guides + client — **M**

## World, lands, grey zones

- [ ] Lands owned by nation/legion; ownership changes by war. — all guides — **H**
- [ ] Safety Factor per land; abandoning a war on an enemy land lowers it by ~5; at 0 the land becomes a monster-invasion (grey) land. — [ES upgrade][g-es-upg], [Turkish][g-tr] — **M**
- [ ] Grey zone resets every 40 min unless its boss is killed; killing the boss gives the land to the killer's nation. — [ES upgrade][g-es-upg] — **M**
- [ ] Grey land monster level drives farm: Lv 7 → Red Passion T2/T3, Lv 8 → Blue Passion T2/T3. — [definitive][g-def] — **M**
- [ ] Monster invasion (purple skull) clears give legion fame + bronze medals. — [Turkish][g-tr] — **M**
- [ ] Teleporter: Castle 10,000, Fortress 6,000, Gaia/Abyss free. — [noob][g-noob] image — **M**
- [ ] Abyss monsters give no loot to level-30 characters. — [ES upgrade][g-es-upg] — **L**

## Land war

- [ ] War lasts 40:00; defenders start with all towers; defence wins on time-out. — [definitive][g-def], [strategy][g-strat] — **H**
- [ ] Attack wins on enemy nexus destroyed (and/or team TP reaching 10,000; Crush era). — [Crush basics][g-crush-basics], client gauge — **M**
- [ ] Nexus takes damage only when ≤1 of its towers stands. — [definitive][g-def] — **M**
- [ ] TP is a shared team pool. Kill TP: normal 30, elite 100, Troll 1,500, Ogre 2,500, Bear 3,000. — [strategy][g-strat], [definitive][g-def] — **M**
- [ ] Rebuild a destroyed tower for 500 TP, available ~20 s after it falls. — [definitive][g-def] — **M**
- [ ] Jungle: Troll & Ogre spawn at 36:00 then 4 min after death; Bear at 35:00 then 5 min after death; killed jungle bosses fight for the killer's team (towers, then nexus). — [definitive][g-def], [strategy][g-strat] — **M**
- [ ] Golems on some lands give TP (1,500/2,500) and a buff, no tower attack. — [strategy][g-strat] — **L**
- [ ] TP skills and costs per `Skill_TP` (Shield 1,500/120 s, Remote Bomb 1,500/120 s, Nexus Remote Bomb 2,000/180 s, Siege Minion 1,000, Fortified 2,000 …); Siege Minion only in field war; extra skills unlock with legion Cores. — client + [strategy][g-strat] images — **H**
- [ ] "Lords of the Land" stacking buff for wins vs NPC and successful defences (not for successful attacks); stacks exchanged for a chest. — [Crush basics][g-crush-basics] — **L**
- [ ] Medals awarded by PvP performance. — [Turkish][g-tr] — **M**

## Legions, forts, events

- [ ] War Nexus on a land costs 500 legion fame (permission-gated). — [Turkish][g-tr] — **M**
- [ ] Owned lands produce ether; 1 ether sells for 700 legion gold. — [Turkish][g-tr] — **M**
- [ ] Legion wages paid Saturday 04:00 from legion gold. — [Turkish][g-tr] — **M**
- [ ] Legion level-up manual, costs legion EXP + legion gold (`Level_Table_Guild`). — [Turkish][g-tr] + client — **M**
- [ ] Civil War: Saturday 00:00–23:59 legion-gold bids per fort; highest bid = challenger; battle Sunday 20:00 inside the fort; members summoned once at 20:00. — [Turkish][g-tr] — **M**
- [ ] Fort EXP from donations (Hadrian, any player) and taxes; level-up also costs treasury gold (10 M / 20 M); each level = 1 mastery point; mastery costs from `FortMastery` (10 M / 20 M / 50 M), paid from treasury only. — [Turkish][g-tr] + client — **H**
- [ ] Fort masteries gate crafting tiers in that fort (weapon/gear/rune tier, passion conversion, A/S alchemy, cores, shields, teleporter), usable by the whole nation. — [strategy][g-strat], client — **H**
- [ ] Fort taxes: a cut of every NPC sale/service in the fort; collectable Sunday 21:00–23:59 into legion gold. — [Turkish][g-tr] — **M**
- [ ] Fort siege: killing Crusader Cherubim removes a shield and pays out part of the fort's taxes; fort falls when shields reach 0; default max 3 shields; shields regenerate over time. Floor 1: 6 cores + Heart of Magic (stops boss regen, respawns); floor 2: strong boss. — [Turkish][g-tr], [strategy][g-strat] — **M**
- [ ] Holy Gift: Mon–Sat 07:00 and 19:00, random land, 90 min, owner legion gets Grabie (new fort) / Frey (+5% MP nation-wide) / Ru (+5% HP) / Innus (move fort ≤2 cells, −10 durability, loses shields) fragment. — [Turkish][g-tr] — **M**
- [ ] Possibly max 2 forts per nation. — [Turkish][g-tr] — **L**

## Items

- [ ] Tier T1–T3, +0…+15 per tier; reinforcing never fails; costs gold + Red (weapon) / Blue (gear) Passion of the item's tier (`ItemSancMet`). — guides + client — **H**
- [ ] Tier-up needs the item at +15 + an identical +15 copy (consumed) + Blue/Red/Orange Passion + gold; normal gear never fails; superior/fame gear tier-up to T3 can fail and destroys materials. — [definitive][g-def], [ES upgrade][g-es-upg], [strategy][g-strat] image — **H** / **M**
- [ ] Sockets (1–3) rolled at item creation (craft or drop), never added later, kept through tier-ups. — [noob][g-noob], [ES gear][g-es-gear] — **H**
- [ ] Runes: socket restrictions per rune type; set costs 5,000 gold; removable; bound, unsellable; max +9; upgrade can fail (drops a level, or destroys the rune unless a sub-material is used — sources disagree). — [definitive][g-def], [noob][g-noob] images — **M**
- [ ] Crafting per `Item_Make` (materials, gold, success %); superior items can fail; passion conversion e.g. 200 D Frag → 100 D Piece, 60 D Piece → 100 D Frag. — client + guides — **H**
- [ ] Craft gold cost appeared × 1.5 in-game (fort multiplier?). — [ES upgrade][g-es-upg] images vs client — **L**
- [ ] Decomposition (hammer) turns gear into Orange Passion (chance rises with tier) and gemstones into crystals; auto-decomposition modes Not use / Gemstone / below 1, 2, 3 tier. — [strategy][g-strat], [noob][g-noob] — **H**
- [ ] One active buff per consumable family (Scroll, Tome, Elixir, Flask); re-use replaces and resets the timer; HP and MP potions independent. — [buffs][g-buff] — **M**
- [ ] Alchemy grades D–S; A needs fort Alchemy 2, S needs 3. — [definitive][g-def], client — **H**
- [ ] Courage and Rise sets craft-only. — [dungeons][g-dng] comments — **M**

## Economy

- [ ] NPC buy price = base × multiplier (seen 7.92 for gold items, 1.1 for Dimensional Energy); sell = base × 6.3; sent in 0x452. — images vs client — **M**
- [ ] Auction: 5% commission at listing, 6-day term, price shown in gold and jewels (1 jewel = 1,000 gold). — [noob][g-noob] — **H**
- [ ] Daily quests reset 00:00, weekly Monday 00:00; Monster Hunt daily 50 → 100,000 EXP + 1 bronze medal; weekly 250 → 10 Dimensional Energy + 1 silver medal. — [noob][g-noob] image — **M**
- [ ] Free gacha every 12 h; paid gacha Artifact 1,000 / Weapon 2,000 / Innocence 2,000 jewels (and 10,000 versions); items T1–T3. — [noob][g-noob] image, [definitive][g-def] — **M**
- [ ] Purple jewels only from real money; yellow from achievements/quests/players; both buy gacha. — [Turkish][g-tr] — **H**
- [ ] Medal shop prices (Athan) as in the economy page. — [noob][g-noob] image — **M**
- [ ] Shop Mall +5% drop-rate item. — [Turkish][g-tr] — **M**

[g-dng]: https://steamcommunity.com/sharedfiles/filedetails/?id=1344219430
[g-noob]: https://steamcommunity.com/sharedfiles/filedetails/?id=1345368744
[g-buff]: https://steamcommunity.com/sharedfiles/filedetails/?id=1354427871
[g-es-gear]: https://steamcommunity.com/sharedfiles/filedetails/?id=1431688611
[g-es-upg]: https://steamcommunity.com/sharedfiles/filedetails/?id=1431875497
[g-def-es]: https://steamcommunity.com/sharedfiles/filedetails/?id=1459898274
[g-def]: https://steamcommunity.com/sharedfiles/filedetails/?id=1459948573
[g-strat]: https://steamcommunity.com/sharedfiles/filedetails/?id=1460486971
[g-tr]: https://steamcommunity.com/sharedfiles/filedetails/?id=1460533609
[g-ptbr]: https://steamcommunity.com/sharedfiles/filedetails/?id=1544645226
[g-crush-basics]: https://steamcommunity.com/sharedfiles/filedetails/?id=780459080

## Added from patch notes (see [[gameplay/patch-history]])

- [ ] Event schedule (server time): War of Warmonger every 2 h, Battle Arena 06/18, Holy Things 07/19, Sunday 20:00 Civil War (WM 1107). — announcements — **M**
- [ ] War of Warmonger filled with up to 15 bots per side; Battle Arena max 5 per team. — WM 1107 / 0719 — **M**
- [ ] Failed reinforcement drops one level and consumes materials; Reinforcing Adjuvant prevents it. — WM 0412 — **M**
- [ ] Dungeon level measured from the nation's Main Fortress; border-area unlock levels 0/20–27. — WM 0726 / 0615 — **M**
- [ ] Safety factor ticks every 30 min (distance-scaled); ≤30 gives an 80% invasion chance; <0 = monster-owned; dungeon clear +5. — WM 0726 — **M**
- [ ] Fort shields recover in 3 h with 1 h invulnerability after each loss. — WM 0705 — **M**
- [ ] Transformation cooldown 120 s; hero gets 35–100% of gear stats by gear tier. — WM 0621 / 0628 — **M**

## Added from the numbers pass (see [[gameplay/reinforce-and-runes]], [[gameplay/events-and-schedules]])

Format: rule — value — source — confidence.

### Runes and gear

- [ ] Rune upgrade cost per step: crystals + Red Passion (+ one Shining/Mysterious/Brilliant/Amplifying from mid-tier steps) — read client `JewelSocketMake` (row = rune item 7002–7211, `next_item`) — WM 0920 image = client, exact — **H**
- [ ] Rune tiers: T1 Attack/AP/Armor/MR/HP/MP/HP regen/MP regen/AS%; T2 ArPen/MRPen/Life Steal/Spell Vamp/Move%/CDR/Crit%; T3 ArPen%/MRPen%/PvP Attack/PvP Armor/Crit Damage — client `JewelSocketMake` groups — **H**
- [ ] Rune max level — +9 (launch +5) — WM 0613 / 0726 — **H**
- [ ] Rune stat per level — client `Item_Jewel` (server-only). The patch caps (Armor 45, MR 60, AP 60, AD 45, MP regen 102 at +9) are older and lower — WM 0412/0420 vs client — **H** (client) / **L** (patch values)
- [ ] Rune success rate falls with level, starting at +6–7 (rarity 1), +5–6 (rarity 2), +4–5 (rarity 3); single-digit % drop per level; overall raised in 0920; exact rates unknown (server-side) — WM 0404/0406/0920 — **L**
- [ ] Runes and gear stats get the PvP stat correction in PvP and War of Warmonger — WM 1107 — **M**
- [ ] Max item tier T4+15; T4 tier-up needs Brilliant Passion as well as Orange — WM 0920 — **M**
- [ ] Rainbow Reinforcing Stone (641–646) works only on items of its own rarity — WM 0420 — **M**
- [ ] Crafted gear and weapons have a small chance to become superior — WM 0726 / 0920 — **M** (chance unknown)
- [ ] Normal gear and T1 runes craftable with yellow jewels standing in for missing materials (cost scales with the shortfall) — WM 0824 — **M**
- [ ] Boss/fame set bonuses at 3/5/8 pieces, values per client `SetBounsItem` — WM 0809 = client — **H**
- [ ] Elixir of Health / Flask of Mana C–S regen +2/4/6/8 (client buffs 2109–2116) — WM 0124 = client — **H**
- [ ] Time Energy T1/T2/T3 = drop and EXP +10/20/30% for 10 min; Drop Chance Potion +40% for 1 h — WM 0726 = client buffs 2134–2137 — **H**
- [ ] Brilliant Passion 5 silver or 1 gold medal; Amplifying 5 silver or 3 gold; costumes 10 gold / 25 silver medals — WM 0920 — **M**
- [ ] Fame shop (Mertris): Blue gemstone 10, Yellow gemstone 50 accumulated fame ("Contribution") — WM 0712 / 0920 — **M**

### PvP, events, forts

- [ ] Fame per result: Gaia PvP win 200 / lose 40; siege win 1,000 / lose 200; per medal gold 1,500 / silver 250 / bronze 50; fame only if you stay to the end — WM 0712 images, 0713 hotfix — **M**
- [ ] Battle Arena and War of Warmonger: win 500 / lose 100 (unit unclear), WoW ranking points +2 / +1, medals ×2; WoW ranking pays medals weekly and yellow jewels monthly — WM 0712 image 2 — **M**
- [ ] Weekend multipliers: global drop ×1.5 and/or PvP medals ×2 for a time window (see the dated list) — WM event posts — **H**
- [ ] Double Event Field: weaker nation only, one per hour, near its border, ×2 medals when taken — WM 0628 — **M**
- [ ] Event notice 5 min before start — WM 0712 — **M**
- [ ] Fort inviolable time by nation fort count (final: 2 forts 30 min, 3 forts 5 min, 4 none); fort invincibility removed once a nation has more than one fort — WM 0726 / 0817 / 0920 — **M**
- [ ] Fort floor-1 nexus HP 90,000, armor 540; no crits on buildings; Heart of Magic down = guardian/Crusader stops regenerating — WM 0809 / 0503 / 0628 — **M**
- [ ] Fort Guardian kill: up to 15 killers each get one drop from {6 essences ×1, 100 D-fragment Blue, 100 D-fragment Red, 25 of each crystal} — WM 0817 image — **M**
- [ ] New fort's mastery level = building legion's level — WM 0817 — **M**
- [ ] Defenders' gear bonus capped at T3+5, larger for nations with fewer forts; 3 s invincibility on internal fort portals — WM 0621 / 0628 / 0705 — **M**
- [ ] Shaia Blessing: pool max 10,000; town/offline gain 5 per min up to 1,000 (was 2,000); item +2,000 (was 1,000); −10 per monster (was 5), −100 per boss; tiers 1–2,000 (+20% hunt EXP/drop) and 2,001–10,000 (+30%, war 130%) — WM 0809 image / 1107 — **M**
- [ ] Shaia Legion donations: 200,000 gold/day per player (+1 donation per 100 jewels); 7 weekly tiers 3/6/10/15/25/35/45 M gold → Shaia +10/10/10/20/20/20/30% and cores (Recovery Shot, Fire Support, Reinforce Nexus, Battlefield Summoner, Powerful Remote Bomb, Twisted Dimension) — WM 1128 image — **M**
- [ ] TP skills: costs and cooldowns per client `Skill_TP` — WM 1018 image = client — **H**
- [ ] Jungle: medium jungle mob spawns at PvP start; Troll/Ogre at 36:00, respawn 4 min; Bear at 35:00, respawn 5 min — WM 0830, blog — **M**
- [ ] Lord of the Land reward box costs 200,000 gold to open (was 300,000); buff needs ≥1 medal in the fight — WM 0920 / 0426 — **M**
- [ ] Hero durability 240; transformation scroll 5 min; Innocence Crystal durability 1,500, −5/s while transformed, no level limit — WM 0402 / 0503 / 1107 — **M**
- [ ] Mysterious World: Death's Rest (132) 2 and Sinking Nest (133) 4 Dimensional Energy (client); Sinking Nest 3 h limit — client + WM 0124 — **H** (cost) / **M** (limit)

### Economy and misc

- [ ] Mail 1,000 gold (with package 10,000); no mail between nations — WM 0404 / 0802 — **M**
- [ ] Costume duration counts only while worn (2,610 min for timed costumes) — WM 0406 — **M**
- [ ] Haley teleport 20 yellow jewels; premium Teleport Scroll (913) in the cash mall — WM 0110 — **M**
- [ ] Daily gacha 10 rewards incl. yellow-jewel packs 100/200/1,000 and T1–3 gear/weapons — WM 0726 — **M**
- [ ] Gacha pools by price (1,000 gear / 2,000 weapon / 2,000 innocence / 4,000 gear T2–3 / 5,000 weapon T2–3), odds unknown — WM 1018 image — **M**
- [ ] Monthly Boss Hunt quest 50 bosses — WM 1107 — **M**
- [ ] Character MR per level: Punisher +3, Saint +4, Guardian +6 (90/120/150 at Lv 30) — WM 0420 — **M** (check `Level_Table` / class base stats)
- [ ] Nexus attack range just above 750 — WM 0124 — **M**

## Added from the Crush Online forum (see [[gameplay/crush-mechanics]], [[gameplay/crush-patch-notes]])

Crush Online (2016–17) values are history; where Warmonger differs, use the Warmonger value.

- [ ] Fame ranks from `Level_Table` (thresholds ×3.1 per step) — CO forum 1123 + client — **H**
- [ ] Lords of the Land: 5 stacks of 120 min (`WinAffect`); gained by destroying the enemy nexus or killing the land boss; lost on fleeing or defeat; reward boxes 1023–1028 — CO 1222 + client — **H**
- [ ] Holding a tower gives 8 TP per 10 s; destroying a tower gives 50 TP — CO 1123 / 1201 — **M**
- [ ] Civil War stake is never refunded; the winner takes the fort with its cores and taxes; taxes claimable until Sunday 24:00 — CO 1215 / 1222 — **M**
- [ ] Character delete: the slot is reusable 24 h later — CO 1108 — **M**
- [ ] Life Saviour heals 30 % / 50 % of max HP; cooldown per client (15 s; CO had 120 s) — **M**
- [ ] Dungeon level order per `FieldNames` (Tow Canyon 5, Ghost Fortress 6; CO had them swapped) — **H**
- [ ] Legion level-up gold per `Level_Table_Guild` — **H**

## Added from the source hunt (see [[gameplay/sources|Sources and gaps]])

- [ ] Crush mode only: every worn item costs EP; total EP ≤ maximum (14,000 on channel 5; 15,000 at Striker 6; 17,000 at Striker 7; +500 from legion mastery). — [[gameplay/gear-stats]] §3, forum — **L**
- [ ] Crush mode only: items have 3 SP levels (D rank) costing EP ÷ 5 each. SP is earned per zone, starts at 0 and is full for fort defenders. Full stats = base + SP bonus. — [[gameplay/gear-stats]] §1 — **L**
- [ ] Damage reduction from armour and MR = value ÷ (100 + value), until the real formula is known. — [[gameplay/stat-values]] §2 — **L**
- [ ] Consumable buffs come from `Skill_Buff` 2060–2132 (C/B/A/S steps). The sheet confirms the S values for crit 20%, AoE 20%, cooldown 12%, attack speed 40 and tenacity 40. — client + sheet — **H**
- [ ] Dungeon levels follow `FieldNames` (125 Tow = Lv 5, 124 Ghost = Lv 6, 142 Dragon Island = Lv 9), not the 2016 order. — client — **H**
- [ ] Dungeon materials: Skull Temple 802/812; Chepa 818/820; Cemetery and Tsunami 814/804/822/824; Swamps 816/826/828; Ghost 808/818/820; Tow and Thorn's Hell 806/822/824; Demon Hell 810/826/828. — [[gameplay/dungeon-drops]] — **H**
- [ ] Each dungeon boss can drop its essence (1930–1935), its horn (2701–2709) and its sealed weapon (2751–2759), as listed in `DungeonAdmission`; rates unknown. — client — **M**
- [ ] Arena monthly ranking pays jewels: 1st 20,000 / 2nd 10,000 / 3rd 5,000 / 4–10 1,000 / 11–50 200 / 51–100 100, paid after month end. — [[gameplay/arena-ranking-rewards]] (2016 image) — **M**
- [ ] Arena weekly payment by SYSTEM mail "Weekly arena payments"; rank 51–100 = 10 × item 1007 Medal : Arena; other rank bands unknown. — same — **M**
- [ ] Mail box object (unit 218) has 10,000 HP (+500) in the Fortress, overriding the client value of 1080. — same — **L**
- [ ] Lords of the Land stack: +1 for a grey-land war win or a successful defence, 0 for an enemy-land conquest, −1 for losing or leaving a war; claiming a box resets it to 0; buff lasts 120 min (`WinAffect`: stacks 0–6 → buff 3029–3034, box 1023–1028). — [[gameplay/lords-of-the-land]] — **H**
- [ ] Buff tiers (2016): +4% AD/AP; −5% cooldown and respawn wait; +6 SP gain; 5% damage reduction reflected as bonus damage; +20 heal/MP regen and the whole buff doubles. Later client text: +10 AD/AP, −5% respawn, +4% Armor/MR, +4% AD/AP, doubles at tier 5. — same — **M**
- [ ] Quests 117/763/764/765 from Kelsey (unit 210): conquer 2/3/4/5 NPC lands, then claim box N; rewards 100k/1.5M/1.5M/1.5M exp plus box 1024/1025/1026/1027. — same — **H**
- [ ] Contents of the Gaia boxes (1023–1028) are not known; they are not in `RandomBox`, so we need another source. — same — **L**
- [ ] Potion = buff on use (Item_Base opt1 301 → Skill_Buff 2050–2072); 16 s; HP and MP potions run independently. — [potion ticks](potion-regen.md), client — **H**
- [ ] Potion payout: either faithful (buff value × 3.2 per regen tick inside 16 s, so 3–4 ticks: S HP +240 ×4, S MP +60 ×3, S Health Mana +120 HP/+24 MP ×4) or as the tooltip says (buff value × 16 in total). Pick one. — [thread post 4290](https://web.archive.org/web/20170722131713/http://crush-game.com/forum/threads/potions-recovering-incorrect-amount.932/), [img](http://i.imgur.com/mhuVgPw.png) — **M**
- [ ] Potion bonus is flat, added on top of base regen each tick and not scaled by it; base regen tick about 6 s (one hand timing). — same source — **M**
- [ ] Artifact step cost: SP per step = EP cost ÷ 5; up to 5 steps; the action bar shows the next step's price or "Max". — [img A](https://i.imgur.com/biw1gJI.jpg), [img B](https://i.imgur.com/h9eBKr6.jpg) — **M**
- [ ] Skull set (3011–3018) Crush Online bonuses: 3 pieces Atk +30; 5 pieces Atk +20 and AS +8%; 8 pieces Atk +20, LS +8% and Crit +5%. Each tier applies once, then the Attack cap of 1,000. — [thread](https://web.archive.org/web/20170302000227/http://www.crush-game.com/forum/threads/skull-artifact-set-3-piece-bonus.928/) — **M**
- [ ] The EP budget at Lv 30 is 15,000. An item that does not fit shows its EP cost in red and cannot be equipped (guess). — [img A](https://i.imgur.com/biw1gJI.jpg) — **M**
- [ ] Precept shop on Freya (unit 200, shop 289): D 4,650 / C 9,300 / B 18,600 gold (2016), vs client prices 10k/25k/50k. Choose one. — [img](http://i.imgur.com/ST4OtVY.jpg) + Item_Base — **M**
- [ ] Precept scroll starts a random "Rank[X] Crafting" quest. Only one active at a time; dropping it allows a re-roll; probably level 30 or higher (pre1 type 4, a=30 is a guess). — thread #1/#4 + Quest 800–813 — **M**
- [ ] Precept rewards: 1–5 medals (D bronze 1000 / C silver 1001 / B gold 1002) and 20–150 Spellstone D, vs the client's fixed 601/611 fragments. Choose one. — thread #1 — **M**
- [ ] The "territorial war" objective counts only attacks or defences against another nation, not grey lands. — thread #6 — **L**
- [ ] Abyss is fields 99–114 (Lv 1–5 per ZoneDB), one 256-unit segment each; each nation enters from its Training Camp (gates 1503/1504/1505 → 99/100/101 gates 1500/1501/1502) — [[gameplay/abyss-map]] — **H**
- [ ] Abyss portal graph as in the portal table (18 client gates plus about 19 from the image at the standard corner spots); routes reach 113 then 114 in 4 jumps — [[gameplay/abyss-map]] — **H**
- [ ] Fortress teleporter "Abyss" (free) lands in field 103/105/107 by nation (Teleport_List 1901–1903) — *client + guess* — **M**
- [ ] Fields 110 Prison and 112 Death's Rest: no portals known; leave closed until a source turns up — *guess* — **L**
