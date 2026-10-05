---
title: "Crush Online mechanics from the forum"
---

# Crush Online mechanics from the forum

Rules and numbers about Crush Online (**CO**, Oct 2016 – Apr 2017) that the archived official forum gives **outside** the patch notes: guides, FAQ answers, staff replies in bug threads, and player measurements. Grouped by system and cited. The dated change log is [[gameplay/crush-patch-notes]]. Warmonger-era (**WM**) rules are in [[gameplay/server-rules]] and [[gameplay/patch-history]].

Tags: *staff* = CO team or forum moderator speaking for the devs · *player* = player post · *image* = read off a screenshot · *client* = decoded WM client table (`data/tables/`, [[spec/data-tables]]) · *guess*. Many player numbers are from the first weeks and may have changed later.

> [!warning] CO is not WM
> The WM client dropped CO's weapon grades (D, C, B, A, S, SS with levels 1–30), Equipment Points (EP), Striker levels, SP-unlocked artifact steps and "additional effect" rolls. Use those sections as background only. Rules marked **still in client** below are the ones that carry over.

## 1. Levels and quests

| Rule | Value | Source |
|---|---|---|
| Level cap | 30. Levelling to 30 is "the tutorial"; the real game starts after it | *player* [t315]; client `Level_Table` ends at 30 (42,350,740 exp) *client* |
| EXP source | quests only; monster kills give little or nothing | *player* [t156] |
| Repeatable "blue" quests | appear only while the nation holds lands far enough out (around level 28 you need level 6+ dungeons). Do them before the yellow/purple quests or you can stall at level 28–29 | *player* [t156], [t621], [t680] |
| Rough turn-in counts | levels 10–20: ~81 medical herbs; 21–26: ~51 refined oils; 28.5–29: ~9–12 Ointment of Spirit; 29.5–30: sulphur until it stops | *player* [t621] |
| Fast route | a fresh character reaches 30 in about 4 h and 2–3 M gold | *player* [t621] |
| Precept scrolls | random repeatable quests sold by Freya; D/C/B scrolls cost **4,650 / 9,300 / 18,600** gold (Oct 2016); D gives mostly bronze, C silver, B gold medals, **1–5** medals plus **20–150** D spell stones; drop a bad roll and buy another. Details: [[gameplay/precept-shop]] | *image* / *player* [t97] |
| Precept B examples | "take 1 territory" → 3 gold medals + 150 spell stones; "2 NPC territories" → 2 gold + 150 | *player* [t680] |
| Character delete | 24 h before the slot can be reused (from 8 Nov 2016) | *staff* [t609] |

## 2. EP, Striker level and weapon grades (CO only)

| Rule | Value | Source |
|---|---|---|
| Equipment Points (EP) | every artifact has an EP cost; total worn EP is capped | *player* [t422] |
| Raising the EP cap | level 30, Striker (ST) level from the 5 equipped weapons, legion mastery "Elite Warrior" | *player* [t91] |
| ST6 | all 5 weapons at A22 (560 STP) → **15,000 EP** | *player* [t252], [t868] |
| ST7 | 900 STP = 5 weapons at **SS30** → **17,000 EP**; +500 from maxed Elite Warrior → **17,500** | *player* [t252], [t603] |
| Starter channel cap | 14,000 EP | *player* [t603] |
| Weapon upgrade value | A22 → S15 added only ~13 attack; ST5 → ST6 about +600 HP | *player* [t278] |
| Drops vs crafts (before Season 2) | dropped gear had **0 durability** and no additional effect, so it could not be reinforced past its grade; durability only limits upgrades, gear still works at 0 | *staff* [t98], *player* [t868] |

Still in client: `GuildMastery` 14 "Elite Warrior" gives 100/200/300/400/500 at levels 1–5, the same +500. *client*

## 3. Artifacts: additional effects, crafting, reinforcing

**Additional-effect rolls** on a crafted D-rank artifact (two lines; if both lines roll the same stat, it shows as one larger line) *player* [t163], [t838](https://web.archive.org/web/20180406072223/http://warmonger-game.com/forum/threads/max-additional-effect-on-artifact.838/):

| Stat | One line (low / mid / high) | Max single (two lines added) |
|---|---|---|
| Attack | 2 / 4 / 8 | 12 (16 claimed) |
| Armor | 4 / 8 / 12 | 20 (24 claimed) |
| Magic resist | 3 / 6 / 9 | 15 (18 claimed) |
| Health | 10 / 20 / 30 | 50 (60 claimed) |
| HP regen | 4 / 8 / 12 | 20 (24 claimed) |
| Mana | 5 / 10 / 15 | 25 (30 claimed) |
| MP regen | 2 / 4 / 6 | 10 (12 claimed) |

- Each grade up adds a fixed amount: single Armor +8 (max D 20 → C 28 → B 36 → A 44 → S 52), single Attack +4 (D 12 → S 28); a double Attack+Armor line adds +2/+4 (D 8+12 → S 16+28) *player* [t163].
- No AP, cooldown or life-steal lines exist *player* [t163].
- **Magic Crafting Stone** from merchant Wren re-rolls the lines and costs durability *player* [t163]. Its price moved with the economy: 37,000 → 48,000, then 42,500 gold; Scroll of Return 72 → 96. Staff (via a moderator): NPC prices are a "dynamic gold economy" tied to the land a nation holds *staff* [t177]. From 15 Dec 2016 the stone came only from the Diamond medal box ([[gameplay/crush-patch-notes]]).
- **Crushing** an item costs **1,000 gold** on top of its price; the yield is random *staff* [t170]. Example: an armor bought for 2,880 gave 18 blue crystals *player*. 50 shop items crushed give about 20–25 blue crystals *player* [t866].
- **Crafting can fail** for top items (Thorns Armor, Invincible Armor, transform stones, Skull weapons via alchemy); the materials are lost. No protection item exists *player* [t159](https://web.archive.org/web/20161017065206/http://www.crush-game.com/forum/threads/about-crafting.159/), [t923].
- **Reinforcing**: three slots: item, reinforcement stone, and an optional **adjuvant**. The adjuvant should raise the success chance (players doubted it worked) and stops the durability loss. Adjuvants came from the premium AH (also for gold) and for **Mithril medals** at Merits merchant Athan *player* [t576]. One player estimates B+ upgrades at about 5 % without an adjuvant and 10–20 % with one *player, guess* [t430].
- **Stack size** 255 for crystals and stones *image* ([imgur kAQdUc2](http://i.imgur.com/kAQdUc2.png), [t224](https://web.archive.org/web/20161020061732/http://www.crush-game.com/forum/threads/devs-how-to-proceed.224/)).

Still in client: `Item_Base` 1100 "Reinforcing adjuvants" is bought with currency 16 (Mithril medal), price 1. *client*

## 4. Combat stats and formulas

| Rule | Value | Source |
|---|---|---|
| Armor/MR damage reduction | fits `reduction = A / (100 + A)`: 100 → 50 %, 200 → 66.7 %, 400 → 80 % | *player, guess* [t528] |
| Attack cap | **1,000** attack (the Skeleton/Justice dagger R buff scales to the cap and no further) | *player* [t265], [t456] |
| Attack-speed cap | **1,000** | *player* [t429], [t348] |
| Crit-chance items | "+x %" crit on items adds x % **of** current crit, not x points (Necklace of Luck +18 % gave +2 %); one player calls it a bug, another the intended design | *player* [t760], [t732] |
| Stat rounding | the UI hides decimals; parts round separately, so totals can be 1 off (0.5 + 15.5 = 16, but 1 + 16 = 17 shown) | *staff* [t734] |
| Thorns Armor | reflects about **30 %** of the attacker's AD, not reduced by armor | *player* [t528], [t543] |
| Tenacity | Tenacity potion 40 %; Guardian talent 15 % | *player* [t539] |
| CC chaining | no diminishing returns; players report 20 s+ chains | *player* [t367], [t631](https://web.archive.org/web/20170419074441/http://www.crush-game.com/forum/threads/the-state-of-balance.631/) |
| Recommended HP | base ~1,160 HP; 4,200–5,250 for PvP (Oct 2016) | *player* [t528] |
| Cooldown reduction sources | Boots of Sage 8 %, Scroll of Cooldown S 12 %, Ring of Glacier 8 %, mastery Icy Chills 9 % | *player* (German) [t261] |
| Saint AP bug | Saints had +75 % AP they should not have (Nov 2016); a moderator said a fix was coming | *staff* [t733] |

Potion ticks (S grade, March 2017): mana 60 per tick × 3 ticks = 180 of the 300 shown; health 240 × 4 = 960 of 1,200; HP/MP 120 + 24 × 4 = 480/96 of 600/120. A tick is about 6 s; each potion runs 16 s *player/image* [t932]. Full analysis in [[gameplay/potion-regen]].

## 5. Notable items and skills

| Item / skill | Numbers | Source |
|---|---|---|
| Invincible Armor | 4,000 EP; 800 SP per step at D (2,400 total); **5 s** invulnerable and no CC; 90 s cooldown; recipe C-grade Thorns Armor + 28 black crystals + 20 Amplifying spell stones (400 gold medals); two separate crafts can fail. From 23 Nov 2016: self only, 3 s | *player* [t295] |
| Gloves of Ghost | 6,100 EP; 1,220 SP per step (3,660); **5 s** invisible, broken by skills; 80–90 s cooldown; +12 % crit damage; recipe B-grade Ultimate Gloves + 53 black crystals + 10 Amplifying stones (200 gold medals) | *player* [t295] |
| Cape of Space | 1,900 EP; 380 SP per step; short blink every **30 s**; recipe 14 blue + 18 red crystals + 5 Worked Topaz (25 topaz) | *player* [t389] |
| Transform stones "Sacred Power" (Crusader Cherubim) / "Wrath of the Knight" (Dark Knight Skull) | 5 Essence of Light or Darkness + 5 Brilliant spell stones (100 silver medals) + 5 D reinforcement stones; can fail; swap the QWER bar | *player* [t254] |
| Earrings of Amplification | step 3: 100 damage + 25 % of current HP, about 60 s cooldown, works on bosses | *player* [t365], [t330] |
| Soul Infestation (Guardian hammer) | turns autoattacks into AoE magic damage while active; 14 s cooldown | *player* [t774], [t391] |
| Bracelet of Temptation | AP +10 % of armor | *player* [t261] |
| Skull artifact set | 3-piece bonus bugged (about 1,000 attack instead of ~20), Feb 2017; see [[gameplay/skull-artifact-set]] | *player* [t928] |

Client check: `Skill_Base` cooldowns are Soul Infestation **19 s** (5036), Petrification 16 s, Death from Above 70 s, Blink like Wind 12 s, Rapid Dash 20 s, Hail of Arrows 15 s with **5** targets. The CO numbers above are older. *client*

## 6. War, territories, TP, safety

| Rule | Value | Source |
|---|---|---|
| War length | **40:00** (timer read 39:24) | *image* ([imgur gqWSZJQ](http://i.imgur.com/gqWSZJQ.jpg), [t24]) |
| Win by TP | **10,000** TP (HUD "TP 0/10000"), or kill the NPC boss on grey land | *image* [t24], *player* [t15] |
| NPC land times (Oct 2016) | levels 1–3 a few minutes; level 4 about 20 min with a good group; 5+ needs organisation | *player* [t15] |
| TP from mobs on NPC land | 15–30 per mob; the weaker nation got 100+ per mob, the dominant one about 10 | *player* [t367], [t278] |
| Strategy (TP) panel | goes to the **first** players to enter the war (up to 3 holders); can be passed on, often bugged. Siege Minion costs 500 TP in that panel | *player* [t433](https://web.archive.org/web/20161028132714/http://www.crush-game.com/forum/threads/suggestions-tweaks-and-maybe-bugs.433/), [t26] |
| Portal bug | destroying an enemy portal set your own TP to 0 until the next TP gain | *player* [t848] |
| Fort lands | wars on a fort's land let the fort side bring unlimited players; players above 15 got no reward (bug) | *player* [t392] |
| Fortress floor 2 | strategy skills cannot be used; detection wards are the answer to invisible attackers (dev reply) | *staff* [t593] |
| War teleport | 1 jewel to jump to a war from the pop-up; teleport to any fort for a small fee | *player* [t162] |
| Dungeon level | distance from your nation's fort: **1 map = 1 level** | *player* [t156] |
| Safety factor | killing the **transmission gate** raises safety by **5**, but only if you left and re-entered after the boss died. Killing the boss alone does not change safety | *player* [t674] |
| Monster invasion | forced when a nation holds **too many lands**, whatever their safety (100+ safety lands still flipped) | *player* [t701]; matches the 23 Nov 2016 note |
| Lords of the Land | +1 stack per NPC land won or fort defence, none for enemy land, −1 for losing or leaving; 5 stacks, 6 boxes. See [[gameplay/lords-of-the-land]] | *player/image* [t24] |

## 7. Medals, contribution, arena

| Rule | Value | Source |
|---|---|---|
| War contribution | at launch only **last hits** on mobs and players counted; no contribution, no medals | *player* [t83], [t286](https://web.archive.org/web/20161022142514/http://www.crush-game.com/forum/threads/medal-bug.286/) |
| Medals per war (Oct 2016) | usually 1–2 bronze; best seen 1 silver + 4 bronze in a 15 v 15; the D–SS rating did not set the medal type | *player* [t438] |
| Before the Oct 21 nerf | up to 5 gold per war, 1–2 gold for a good win | *player* [t666](https://web.archive.org/web/20170320013921/http://crush-game.com/forum/threads/reasons-why-i-stay-just-to-troll.666/) |
| Arena rewards | monthly 1st 20,000 / 2nd 10,000 / 3rd 5,000 / 4–10th 1,000 / 11–50th 200 / 51–100th 100 jewels; weekly rank 51–100 = 10 medals. See [[gameplay/arena-ranking-rewards]] | *image* [t231], [t343] |
| Precept removal | early 2017 players say precepts were removed and silver/gold became hard to get; a moderator floated bronze → silver → gold exchange | *player* / *staff* [t901](https://web.archive.org/web/20170305042127/http://www.crush-game.com/forum/threads/precept-quest.901/) |

Still in client: medal items 999–1002 (Mithril, Bronze, Silver, Gold; sell 45 / 5 / 10 / 30 gold), 1007 Arena medal, and the medal reward boxes 1051–1055. *client*

## 8. Legions, forts, cores, kings

| Rule | Value | Source |
|---|---|---|
| Create a legion | 1,000,000 gold at Kelsey (10,000,000 from 15 Dec 2016); character-bound | *player* [t426], [t149](https://web.archive.org/web/20161017065216/http://www.crush-game.com/forum/threads/creating-your-own-legion.149/) |
| Legion level 1 → 2 | 30,000 legion EXP + 100,000 legion gold; stock cap 100; 1 mastery point | *player* [t426] |
| Legion level 2 → 3 | 204,000 EXP + 220,000 gold; stock cap 400; 3 mastery points | *player* [t426] |
| Max legion level | 10 | *player* [t426] |
| Legion gold | needed to recruit and to pay taxes; **5 missed tax payments in a row suspend the legion**; yellow ether sells for legion gold in the admin panel | *staff* [t740] |
| Fortress | built with a Fortress Construction Kit from the premium AH; only the top 20 legions; at most **4 forts per channel**; cannot be captured at first, only destroyed (before Civil War) | *player* [t200], [t154](https://web.archive.org/web/20161017065226/http://www.crush-game.com/forum/threads/guild-forts.154/) |
| Shields | winning a war on a fort's land removes 1 shield; at 0 a siege opens | *player* [t426], [t385] |
| Siege | capture cores to weaken the guardian; destroying a Heart stops one guard respawn; kill the guardian to win; defenders start at full SP | *player* [t426] |
| [Low] cores | 5 types at **192,000** gold each (personal gold): Increasing/Recharging/Preserving Barrier, Moving the Fortress, Increasing Seal; half the crafted value | *player* [t426] |
| Core durability | 100, −1 per hour; each use costs durability and gives legion fame (e.g. Moving: −10 and 200 fame per use) | *player* [t426] |
| Increasing Barrier | max shields +2 (cap 10); [Low] +1 | *player* [t426], [t763], [t385] |
| Recharging Barrier | shield recharge −20 % (one shield per 30 min → 24 min); [Low] −10 % | *player* [t426], [t763] |
| Preserving Barrier | keeps shields when the fort moves (otherwise they reset to 0) | *player* [t763] |
| Moving the Fortress | up to **2** territories away | *player* [t426] |
| Legion Conquest | 100 durability, 2 uses, 60 min cooldown; takes a random enemy land, even a shielded one | *player* [t763] |
| [Low] Increasing Seal | probably lets 25 defenders fight 15 attackers | *player, guess* [t763] |
| Spell Barrier of the Seal | stops the safety factor from dropping, but fewer bosses spawn on the channel | *player* [t763] |
| Amplified Legion | +20 % legion fame from battles | *player* [t763] |
| Magic No Entrance | no-entry zone for all nations, 35 min | *player* [t763] |
| Twisted Dimension | +2 levels to a zone near the fort (fixed in Season 2) | *player* [t763] |
| Vitality of the Fortress | full SP in wars within 3 territories of the fort | *player* [t426] |
| Craftsman's Knowledge / weapon-XP cores | shown as 20 %, gave 10 % | *player* [t763], [t762] |
| Ether gatherers | craft Increasing + Recharging Barrier → Reinforce Nexus → Gathering core; red ether any time, blue needs a resource lab, black needs a spell lab; the red gatherer gave blue ether until 27 Oct | *player* [t431](https://web.archive.org/web/20161203205658/http://www.crush-game.com/forum/threads/forts-ether.431/), [t426] |
| Ether value | ~100,000 ether < 100 M gold (Nov 2016) | *player* [t487](https://web.archive.org/web/20161102124955/http://www.crush-game.com/forum/threads/legion.487/) |
| King and labs | only the king places labs (20 per fort); the king is elected monthly at the National Council | *staff* [t158], *player* [t200] |
| Core materials | core stones (Mysterious, Brilliant, Amplifying) are only needed for cores; ~100 of each is enough | *player* [t196](https://web.archive.org/web/20161019135336/http://www.crush-game.com/forum/threads/what-to-do-with-core-stone.196/) |

Client check: `Level_Table_Guild` level-up gold is **100,000** (→ level 2) and **220,000** (→ level 3), the same as the CO guide. Its EXP column (5,000; 150,000) does **not** match the CO guide (30,000; 204,000), and column @08 (200, 400…) matches the CO stock cap at level 2 (400) but not at level 1 (100). WM fort masteries replaced the CO cores and labs (`FortMastery`). *client*

## 9. Dungeons, bosses, farming

Dungeon list as the CO forum gave it (Oct 2016) *player* [t71]:

| Level | Dungeon | Boss | Gathering |
|---|---|---|---|
| 1 | Temple of the Skull | Deathhead | Garnet, Red Bloodstone |
| 1 | Chepa Village | Chepa Sorcerer | Lavender, Peppermint |
| 2 | Cemetery of the Skull | Death Knight (Dark Knight Skull) | Topaz, Blue Bloodstone, Rosemary, Jasmine |
| 3 | Lake of the Tsunami | Tempest Fisher | Topaz, Blue Bloodstone, Rosemary, Jasmine |
| 4 | Swamps of the Snake Warrior | Slayer Komodo | Onyx, Borage, Spartium |
| 5 | Fortress of Ghost | Great Summoner Spectre | Moonstone, Lavender, Peppermint |
| 6 | Canyon of Tow | War Chief Garon | Emerald, Rosemary, Jasmine |
| 7 | Hell of Demon | Akasha / Leviathan | Diamond, Borage, Spartium |
| 8 | Thorns Hell | Akasha / Revenant | Emerald, Rosemary, Jasmine |

> [!important] Levels 5 and 6 are swapped in WM
> CO had **Ghost Fortress = level 5** and **Tow Canyon = level 6**. Players reported quest markers and map placement mixed up between the two ([t402], [t765]). The WM client names field 125 "[Lv 5] Tow Canyon" and field 124 "[Lv 6] Ghost Fortress" (`FieldNames`), and the WM unlock levels are Tow 24, Ghost 25. Use the client order. *client*

| Rule | Value | Source |
|---|---|---|
| Essences | every boss (dungeon or world map) can drop every essence; Essence of Darkness/Light sold for 15–20 M gold | *player* [t71], [t361], [t866] |
| Tow Chief (Abyss) | drops reinforcement stones, spell-stone patterns and (rarely) Essence of Darkness; must be killed by a level 15–20/25 character | *player* [t361] |
| Group scaling | a dungeon spawns more monsters per player and loot scales with them; a solo player gets about 1/5 of a full group's loot | *player* [t339](https://web.archive.org/web/20161030033934/http://www.crush-game.com/forum/threads/change-dungeon-behaviour.339/), [t419] |
| Party size | 5 per dungeon instance | *player* [t814](https://web.archive.org/web/20161218064723/http://www.crush-game.com/forum/threads/christmas-event-everyone-can-join.814/) |
| Instance bug | players entering one portal sometimes got separate instances (fixed 1 Dec 2016) | *player* [t203](https://web.archive.org/web/20161019135223/http://www.crush-game.com/forum/threads/suggestions-bugs-miscellaneous.203/) |
| Timeout | when the dungeon timer runs out nothing drops; you are teleported out | *staff* [t427](https://web.archive.org/web/20161026223426/http://www.crush-game.com/forum/threads/dungeon-timeout.427/) |
| Abyss AFK farm | 250–360 D spell stones an hour (12–18 A after conversion) | *player* [t327] |
| T7 / T8 | T7: B spell stones, A/B gemstones, items to sell. T8 elites (not normal mobs) drop B reinforcement stones worth ~350,000 gold; artifacts sell for 50–70k | *player* [t327], [t278] |
| Season 2 drop list | artifacts per dungeon level with EP cost, e.g. L1 Bone Necklace 2,400, L5 Helmet of Protection 1,800, L7 Gloves of Zealot 3,600, L8 Ring of Glacier 3,600 | *player* [t904] |
| Double-drop meaning | "double drop" doubles the number of loot rolls (e.g. 50 spell stones **and** a fragment), not the stack size | *player* [t913] |

Client check: units 672 King Deathhead, 673 Dark Knight Skull, 674 Tempest Fisher, 675 Slayer Komodo, 676 Great Summoner Spectre, 677 War Chief Garon, 849 Akasha, 950 Chepa Sorcerer, 825 Crusader Cherubim and 826 Tow Chief are in `UnitDB`. *client*

## 10. Economy, VIP, cash shop

| Rule | Value | Source |
|---|---|---|
| Connection points | 1 per minute online, VIP or not; cap **480**; kept on logout; reset 00:00 CET; spent on spell and reinforcement stones | *staff* [t109] |
| VIP levels | 4 levels from the jewels **bought in the last 30 days** (thresholds in a lost image); each purchase counts for 30 days. Example: 10,000 jewels = VIP 2, +30,000 two weeks later = VIP 4, then VIP 3 for 15 more days | *staff* [t109] |
| VIP benefits | daily jewels (1,000–20,000 per 30 days by level); daily spell stones (VIP 1 D … VIP 4 A; 7,200 D to the equivalent of 240,000 D per 30 days); daily red reinforcement stones (D…A; 240 D to the equivalent of 5,760 D); **+200** movement speed out of combat; mail attachment slots, up to 5 at VIP 4 | *staff* [t109] |
| Equivalence implied | 240,000 D spell stones ≈ 5,500 A (about 44:1); 5,760 D reinforcement ≈ 180 A (32:1) | *staff* [t109], *guess* (ratio) |
| VIP ticket | 30 days; 6,000,000 gold or 2,000 jewels from Cathy (auction manager) at launch; later 9 M, then 12.5 M, then jewels only | *staff* [t109]; see [[gameplay/crush-patch-notes]] |
| Real-money VIP | about €5 → VIP 1, €60 → VIP 4 | *player* [t54](https://web.archive.org/web/20161014095013/http://www2.crush-game.com/forum/threads/how-do-you-get-vip-status-for-crush-online.54/) |
| Jewel packs | two Steam packs (€12 and €24) | *player* [t468](https://web.archive.org/web/20161031223013/http://www.crush-game.com/forum/threads/buying-jewels-via-steam-live.468/) |
| Auto-create | stops before it would spend jewels on a missing material | *staff* [t789](https://web.archive.org/web/20161210215052/http://www.crush-game.com/forum/threads/auto-create-to-lost-jewellery.789/) |
| Reinforcement stone prices | 1 D reinforcement stone ≈ 45,000 gold (AH, Feb 2017); 100 S stones need 12,800 D | *player* [t923] |
| Nation change | at the castle NPC; resets personal fame; the warehouse looked empty afterwards (per-nation bank?); disabled from 2 Dec 2016 | *player* [t156], [t201], *staff* [t749] |

Client check: WM `ExpandSlot` jewel costs start at 40 and run up to 5,000, which fits the CO prices ([[gameplay/crush-patch-notes]]). `ConnectReward` is a 30–300 min ladder. `PrimiumShop` has no VIP ticket. *client*

## 11. Conduct rules (staff)

- **One client per PC** is allowed, because multiboxing cannot be detected reliably. Macros or bots that drive several characters, or any automation, are **forbidden** *staff* [t871].
- **Fame farming** with alt characters is forbidden; the fame logic was to be changed *staff* [t713].
- The anti-cheat sent suspected speed-hackers to **Prison** for about 3–5 min. It also caught laggy honest players, and one was banned for "third-party programs" *player* [t199], [t219](https://web.archive.org/web/20161030033939/http://www.crush-game.com/forum/threads/clicked-my-w-e-r-combo-for-punisher-in-pvp-and-got-sent-to-prison.219/).
- Bug reports in English only; support mail, with a separate German address and a payments address *staff* [t67](https://web.archive.org/web/20161024100026/http://www.crush-game.com/forum/threads/how-to-report-support-email.67/).

## 12. Crush vs Warmonger: differences that matter for the server

| Topic | CO (forum) | WM (client / notes) | Use |
|---|---|---|---|
| Dungeon levels 5/6 | Ghost Fortress 5, Tow Canyon 6 | Tow Canyon 5, Ghost Fortress 6 | WM |
| Fame-rank thresholds | 600 / 55,411 / 5,117,346 | the same in `Level_Table` | same |
| Lords of the Land tiers 2, 3, 5 | CD and respawn −5 %; SP +6; +20 regen | respawn −5 %; Armor/MR +4 %; doubling only | WM |
| Life Saviour cooldown | 120 s | 15 s (`Skill_Base` 5275/5276) | client, check in play |
| Drop Chance Potion | +20 %, 1 h | +40 % (buff 2134, WM 0726) | WM |
| Costume Remover | 425,000 gold | 50,000 gold | WM |
| Hail of Arrows targets | 3 | 5 | WM |
| Soul Infestation cooldown | 14 s | 19 s | WM |
| Connection reward | 1 pt/min, cap 480, point shop | 6 time steps, 30–300 min | WM |
| Legion level-up gold | 100k, 220k | 100k, 220k | same |
| Legion EXP curve | 30k, 204k | 5k, 150k | WM |
| Gear system | grades D–SS, levels 1–30, EP, Striker, additional effects | tiers T1–T3 +0…+15, runes, sockets | WM |
| Players per war | 15 v 15 (then "15" from Mar 2017) | 15 per side with bots (WM 1107) | WM |
| Win condition | nexus, or 10,000 TP, or NPC boss | same gauge | same |

[t15]: https://web.archive.org/web/20161020061825/http://www.crush-game.com/forum/threads/psa-npc-territory.15/
[t24]: https://web.archive.org/web/20161015064613/http://www.crush-game.com/forum/threads/psa-land-lord-quest.24/
[t26]: https://web.archive.org/web/20161020061802/http://www.crush-game.com/forum/threads/suggestion-npc-lands-strategy-skills.26/
[t71]: https://web.archive.org/web/20161017183204/http://www.crush-game.com/forum/threads/dungeon-ore-plants-drop-location-boss-location.71/
[t83]: https://web.archive.org/web/20161026122911/http://www.crush-game.com/forum/threads/contribution-for-war.83/
[t91]: https://web.archive.org/web/20161027194122/http://www.crush-game.com/forum/threads/how-to-raise-ep.91/
[t97]: https://web.archive.org/web/20161017183216/http://www.crush-game.com/forum/threads/psa-precept-quest-medals-and-spellstones.97/
[t98]: https://web.archive.org/web/20161018142050/http://www2.crush-game.com/forum/threads/items-durability.98/
[t109]: https://web.archive.org/web/20161017183210/http://www.crush-game.com/forum/threads/guide-vip-connection-rewards-system.109/
[t265]: https://web.archive.org/web/20161022145541/http://www.crush-game.com/forum/threads/punisher-dagger-weapons.265/
[t156]: https://web.archive.org/web/20161017065036/http://www.crush-game.com/forum/threads/iso-help-no-repeatable-quests-and-i-am-lv28.156/
[t158]: https://web.archive.org/web/20161017065056/http://www.crush-game.com/forum/threads/quick-guide-about-kings-fortresses-laboratories.158/
[t162]: https://web.archive.org/web/20161017065111/http://www.crush-game.com/forum/threads/suggestion.162/
[t163]: https://web.archive.org/web/20161018031653/http://www.crush-game.com/forum/threads/all-the-additional-effect-stats.163/
[t170]: https://web.archive.org/web/20161018173701/http://www.crush-game.com/forum/threads/crush-is-way-to-random.170/
[t177]: https://web.archive.org/web/20161018173816/http://www.crush-game.com/forum/threads/npc-d-magic-crafting-stone-price-bugged.177/
[t199]: https://web.archive.org/web/20161019114353/http://www.crush-game.com/forum/threads/prison-for-no-reason.199/
[t200]: https://web.archive.org/web/20161019135003/http://www.crush-game.com/forum/threads/guild-fortress.200/
[t201]: https://web.archive.org/web/20161022021607/http://www.crush-game.com/forum/threads/cheest-bank-clear.201/
[t231]: https://web.archive.org/web/20161022005000/http://www.crush-game.com/forum/threads/is-there-a-way-to-stop-battle-arena-weekly-monthly-reward.231/
[t252]: https://web.archive.org/web/20161021234056/http://www.crush-game.com/forum/threads/bonus-striker-status.252/
[t254]: https://web.archive.org/web/20161022145703/http://www.crush-game.com/forum/threads/crusader-cherubim-dark-knight-skull-skill-stones.254/
[t261]: https://web.archive.org/web/20170209233403/http://crush-game.com/forum/threads/meine-meinung-zum-saint-nach-100-stunden.261/
[t278]: https://web.archive.org/web/20161022141400/http://www.crush-game.com/forum/threads/suggestion-game-so-far.278/
[t295]: https://web.archive.org/web/20161025042755/http://www.crush-game.com/forum/threads/invincible-armor-gloves-of-ghost-information.295/
[t315]: https://web.archive.org/web/20161024100126/http://www.crush-game.com/forum/threads/increasing-max-level.315/
[t327]: https://web.archive.org/web/20161025044734/http://www.crush-game.com/forum/threads/the-grind.327/
[t343]: https://web.archive.org/web/20161024091444/http://www.crush-game.com/forum/threads/arena-monthly-reward.343/
[t348]: https://web.archive.org/web/20161024085844/http://www.crush-game.com/forum/threads/skeleton-dagger-attack-speed-lowered.348/
[t361]: https://web.archive.org/web/20161024100021/http://www.crush-game.com/forum/threads/how-to-get-essence-of-darkness-reinforcement-stones.361/
[t365]: https://web.archive.org/web/20161024100151/http://www.crush-game.com/forum/threads/psa-weapon-nerfs-were-necessary.365/
[t367]: https://web.archive.org/web/20161024100053/http://www.crush-game.com/forum/threads/suggestions-few-of-them.367/
[t330]: https://web.archive.org/web/20161024100037/http://crush-game.com/forum/threads/saint-is-a-mage-or-a-support.330/
[t385]: https://web.archive.org/web/20161027182334/http://www.crush-game.com/forum/threads/forts-barriers.385/
[t389]: https://web.archive.org/web/20161028132643/http://www.crush-game.com/forum/threads/cape-of-space.389/
[t391]: https://web.archive.org/web/20161025044624/http://www.crush-game.com/forum/threads/guardian-too-powerful.391/
[t392]: https://web.archive.org/web/20161025044819/http://www.crush-game.com/forum/threads/war-under-fortress-bug.392/
[t402]: https://web.archive.org/web/20161026230614/http://www.crush-game.com/forum/threads/war-chief-garon-great-summoner-spectre-quests.402/
[t419]: https://web.archive.org/web/20161027182320/http://www.crush-game.com/forum/threads/bosses-are-unrewarding-and-mostly-boring.419/
[t422]: https://web.archive.org/web/20161028132535/http://www.crush-game.com/forum/threads/beginners-guide.422/
[t422]: https://web.archive.org/web/20161028132535/http://www.crush-game.com/forum/threads/beginners-guide.422/
[t426]: https://web.archive.org/web/20161104045956/http://www.crush-game.com/forum/threads/legions-and-fortresses.426/
[t429]: https://web.archive.org/web/20161028132638/http://www.crush-game.com/forum/threads/1-speed-hacker.429/
[t430]: https://web.archive.org/web/20161028112405/http://www.crush-game.com/forum/threads/serriously.430/
[t438]: https://web.archive.org/web/20161030092114/http://www.crush-game.com/forum/threads/medals.438/
[t456]: https://web.archive.org/web/20161227111857/http://www.crush-game.com/forum/threads/skele-dagger-2nd-r-trigger-no-dmg-shield-still-active-since-the-haloween-patch.456/
[t528]: https://web.archive.org/web/20161130042453/http://www.crush-game.com/forum/threads/google-spreadsheet-with-gear-info.528/
[t539]: https://web.archive.org/web/20161107135353/http://www.crush-game.com/forum/threads/game-balance-thoughts.539/
[t543]: https://web.archive.org/web/20170211150702/http://crush-game.com/forum/threads/best-in-slot-guardian-11-3-2016-15-000-ep.543/
[t576]: https://web.archive.org/web/20161112011503/http://www.crush-game.com/forum/threads/frage-zum-verstaerken-der-waffen.576/
[t593]: https://web.archive.org/web/20161210202710/http://www.crush-game.com/forum/threads/fortress-bug.593/
[t603]: https://web.archive.org/web/20161129115247/http://www.crush-game.com/forum/threads/channel-5-guide-to-being-notorious-how-to-twink-your-gear-ep-13500.603/
[t609]: https://web.archive.org/web/20170701033345/http://crush-game.com/forum/threads/patchlog-20161108.609/
[t621]: https://web.archive.org/web/20161229073102/http://www.crush-game.com/forum/threads/guide-to-leveling-how-to-avoid-getting-stuck.621/
[t674]: https://web.archive.org/web/20170426151457/http://crush-game.com/forum/threads/how-to-keep-lands-and-best-setups-for-t8-farming.674/
[t680]: https://web.archive.org/web/20161206171243/http://www.crush-game.com/forum/threads/secrets-of-gearing-up-lets-get-strong.680/
[t701]: https://web.archive.org/web/20161208110156/http://www.crush-game.com/forum/threads/all-red-area-spawn-boss-even-100-safety.701/
[t713]: https://web.archive.org/web/20161213161039/http://www.crush-game.com/forum/threads/fame-abuse.713/
[t732]: https://web.archive.org/web/20161129115344/http://www.crush-game.com/forum/threads/necklace-of-luck.732/
[t733]: https://web.archive.org/web/20161130042631/http://www.crush-game.com/forum/threads/nerf-saints-already.733/
[t734]: https://web.archive.org/web/20161218184636/http://www.crush-game.com/forum/threads/wrong-stats-number-on-weapon-character.734/
[t740]: https://web.archive.org/web/20170419074320/http://www.crush-game.com/forum/threads/legion-gold-ether.740/
[t749]: https://web.archive.org/web/20161209162833/http://www.crush-game.com/forum/threads/nation-change-disabled-by-02-12-16-10-00-cet.749/
[t760]: https://web.archive.org/web/20161215092518/http://www.crush-game.com/forum/threads/critical-strike-not-working.760/
[t762]: https://web.archive.org/web/20161206072718/http://www.crush-game.com/forum/threads/weapon-xp.762/
[t763]: https://web.archive.org/web/20161206072826/http://www.crush-game.com/forum/threads/fort-cores-guide.763/
[t765]: https://web.archive.org/web/20161206033128/http://www.crush-game.com/forum/threads/lvl-5-6-dungeon-bug.765/
[t774]: https://web.archive.org/web/20161206171139/http://www.crush-game.com/forum/threads/guardian-hammer-of-souls-soul-infestation.774/
[t848]: https://web.archive.org/web/20161227202518/http://www.crush-game.com/forum/threads/strategy-skill-portal.848/
[t866]: https://web.archive.org/web/20170103111611/http://www.crush-game.com/forum/threads/tips-tricks-and-cookies.866/
[t868]: https://web.archive.org/web/20170210140704/http://crush-game.com/forum/threads/general-guide-to-gearing-up-and-getting-started.868/
[t871]: https://web.archive.org/web/20170111201223/http://www.crush-game.com/forum/threads/multiclient-clarification.871/
[t904]: https://web.archive.org/web/20170211151046/http://crush-game.com/forum/threads/items-drop-list-guide.904/
[t913]: https://web.archive.org/web/20170217201456/http://www.crush-game.com/forum/threads/valentines-day-special-event.913/
[t923]: https://web.archive.org/web/20170227130036/http://www.crush-game.com/forum/threads/impossible-to-craft-cursed-gloves.923/
[t928]: https://web.archive.org/web/20170302000227/http://www.crush-game.com/forum/threads/skull-artifact-set-3-piece-bonus.928/
[t932]: https://web.archive.org/web/20170418235408/http://crush-game.com/forum/threads/potions-recovering-incorrect-amount.932/
