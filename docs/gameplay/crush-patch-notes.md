---
title: "Crush Online patch notes 2016–17"
---

# Crush Online patch notes 2016–17

The full Crush Online (**CO**) change log as the archived official forum (crush-game.com/forum, Oct 2016 – Mar 2017) and the CO Steam news (appid 475630) record it. Each change has its before → after value where one was given. Tables are in our own words. The thread link is next to each patch heading; the link list is at the bottom.

**Read this as history.** The client we have is the **late Warmonger (WM) build**. It replaced CO's weapon grades (D…SS, levels 1–30), Equipment Points (EP), the Striker level and the artifact system with tiers (T1–T3 +0…+15) and runes. Where a CO number can be checked against the decoded client tables (`data/tables/*.tsv`, see [[spec/data-tables]]) or a WM patch note, the **WM / client** column says whether it still holds. The server follows the client unless a page says otherwise ([[gameplay/server-rules]]). WM-era notes are in [[gameplay/patch-history]].

Tags: *staff* = posted by the CO team · *player* = forum player or moderator report · *image* = read off a screenshot · *client* = decoded client table · *guess*.

> [!note] Lost images
> The CO team put most of its tables in images on `crush-game.com/sites/57f2b2e8…/assets/…`. The Wayback Machine never saved any of them: a CDX query on `crush-game.com/sites/` finds only the site's own design images. So these tables are **gone**: the 21 Oct weapon balancing (all three classes), the 27 Oct boss balancing, the 23 Nov TP-skill and rank tables, the 15 Dec loot-box and spell-stone drop tables and the weapon/skill-stone renaming, the 22 Dec weapon coefficients, SP/TP distance penalty and Land-of-the-Lord box, the Season 2 stat-scaling charts, the 21 Feb artifact step/reinforce tables, and the 2 Mar TP-skill old/new and socket tables. Player screenshots on imgur still load (used below and in [[gameplay/lords-of-the-land]], [[gameplay/precept-shop]], [[gameplay/potion-regen]], [[gameplay/arena-ranking-rewards]]). Gyazo, Discord and forum attachments do not.

## Timeline

| Date | Patch / event | Headline |
|---|---|---|
| 2016-06-29 – 09-08 | Closed beta (CBT 1–3), then open beta from 8 Sep | Steam news only |
| 2016-10-10 | Launch on Steam | client 10087 on 11 Oct, 10090 by 13 Oct, 10102 by ~23 Oct ([t29], [t348]) |
| 10-11 | Patch 20161011 | legion cap, slot prices, costumes |
| 10-12 | Patch 20161012 | last-fort safety buff |
| 10-13 | Patch 20161013 | anti-cheat, black crystals |
| 10-14 | Patch 20161014 | premium core "Sacred Area" |
| 10-17 | Patch 20161017 | connection-point cap 480 |
| 10-19 | Patch 20161019 | "For Honor" nation buff |
| 10-21 | Patch 20161021 | full weapon rebalance, medals back |
| ~10-21 | 1st National Council | system forts removed, kings |
| 10-27 | Patch 20161027 | Halloween, legion fixes, boss balancing |
| ~11-01 | Weapon rollback | fast-levelled weapons downgraded |
| 11-03 | Patch 20161103 | starter channel, 3 artifacts, many values |
| 11-07/08 | Legion reset; patch 20161108 | legions to level 1; LotL winners only; 24 h re-create |
| 11-17 | Patch 20161117 | crafting and reinforcement prices |
| 11-23 | Patch 20161123, **Season 1** | 3 channels, ranks, Life Saviour, LotL buffs |
| 11-25 | Gift | 4,500 jewels per account |
| 12-01 | Patch 20161201 | tower TP, siege nexus |
| 12-02 | Nation change disabled | 10:00 CET |
| 12-15 | Patch 20161215, **Civil War** | civil war, boss summons, legion cost |
| 12-22 | Patch 20161222 | weapon coefficients, VIP, costumes |
| 2017-02-02 | Patch 20170202, **Season 2** | daily quests, artifact rescale, weapon alchemy |
| 02-21 | Patch 20170221 | artifact steps by grade, SP potions |
| 03-01 | Shutdown notice | Steam version offline 1 May 2017 |
| 03-02 | Patch 20170302 | sockets, TP ranks, intrusion, 15-player wars |

---

## 2016-10-11 ([t29]; Turkish copy [t48])

| Change | Before → after | WM / client |
|---|---|---|
| Legion member cap at legion level 1 | 20 → **60** (60 is also the overall cap) *staff* | `Level_Table_Guild` column @08 reads 200, 400 … 2,000 per level; its meaning is unconfirmed. *client* |
| Inventory/warehouse slot prices | raised; first warehouse slot 10 → **40 jewels** *player*; last warehouse steps 500 / 750 / 1,000 *player* ([t109]) | `ExpandSlot` cost2 (currency 13) runs 40, 80, 250, 500, 750, 1,000, 1,250 … 5,000, so it matches. *client* |
| Shop costumes | Punisher Athletic and Military sets added *staff* | – |
| Auction mail | lost AH deliveries resent by mail *staff* | – |

## 2016-10-12 ([t85])

| Change | Detail |
|---|---|
| Last-fortress safety buff | When a nation has **one** fort left on a channel, 4 safety zones around it cannot be attacked *staff* |
| Slot prices | lowered again after complaints *staff* |
| HP/MP potion sell price | adjusted (no number) *staff* |

## 2016-10-13 ([t115])

| Change | Detail |
|---|---|
| Anti-cheat | harsher punishment for speed hacks (trial) *staff* |
| Black crystals | lower decompose yield; gemstones holding black crystals drop in more high-level areas *staff* |

## 2016-10-14 ([t146])

Premium core **Sacred Area**, sold in the Auction House and craftable at Arion (core smith) with the right labs *staff*:

| Property | Value |
|---|---|
| Needs | a fortress |
| Conquers | up to **3** adjacent territories (while the protection buff is on) |
| Protects | up to **4** territories for the next **20 h**; enemies cannot enter |
| Binding | not character-bound |

## 2016-10-17 ([t234])

| Change | Value |
|---|---|
| Connection points | stop stacking at **480**; spend them and they stack again until the 00:00 CEST reset *staff* |
| Speed-hack penalty | raised again *staff* |

WM: the client's `ConnectReward` is 6 play-time steps (30, 60, 120, 180, 240, 300 min), not a point shop. *client*

## 2016-10-19 ([t290]; German [t291])

| Change | Value |
|---|---|
| "For Honor" channel buff | a nation with **< 8 territories** on a channel gets **+20 %** HP, MP, damage, spell power, armor and MR, in PvP only; it switches off once the nation holds more than 8 *staff* |
| Fame/medal bug, potion and crystal bugs, nation-change item loss | fixed *staff* |
| Legion mastery "Acquisition" | drop rate fixed *staff* (client `GuildMastery` 8 "Acquisition": 5/10/15/20/25) |
| Political system | switched on automatically *staff* (German copy) |

## 2016-10-21 ([t350], overview [t450])

| Change | Before → after |
|---|---|
| All weapons rebalanced; per-class tables in images (lost) | – *staff* |
| Skeleton King's Cannon attack speed | **780 → 640** *staff*. A wrong value briefly gave 160–180; fixed in client 10102 *staff* ([t348]) |
| Punisher daggers | all daggers now share one attack speed (players read 611–640, Skeleton dagger once 226) *player* |
| Crit cap | about 40 % → ~33–36 % seen; per-weapon caps reported as 20 % (Justice, Mutilation daggers) and 25 % (Skeleton dagger) *player* ([t348], [t350]) |
| Gun of Execution AP | 21 → 10.85 (from the lost image) *player* |
| Base magic resist | raised *player* |
| Medals | re-enabled with a new, stricter rate; Precept quests suggested for silver/gold meanwhile *staff* |
| Disconnects/freezes | fixed after "2.5 bad days" (Steam 21 Oct) *staff* |

## About 2016-10-21: first National Council ([t317])

| Rule | Value *staff* |
|---|---|
| System fortresses | removed; only legion forts remain |
| Legions allowed a fort | top **20** with a positive legion-gold balance |
| Forts moved by legion rank | ch1: ranks 1–4 · ch2: 5–8 · ch3: 9–12 · ch4: 13–16 · ch5: 17–20 |
| King vote | top **3** legion masters nominated; masters ranked **4–20** vote; reign **30 days**; next council 19 Nov 00:01–24:00 CET |
| Labs | the king may place **20** laboratories next to each fort ([t158]) |

## 2016-10-27: Halloween ([t453]; costumes [t355])

| Change | Value |
|---|---|
| Quest "Trick or Treat" | NPC Corpse Bride in the nation castle; hunt Jack O'Lantern in PvE; reward box with skill stone "Creep Jack" *staff*. Players say the stone has only **120** spell charges *player* |
| Halloween costumes | **10,000 jewels** each, until 7 Nov 2016 *staff* |
| Legion fame | now resets at every National Council (next 19 Nov) *staff* |
| Legion wages | paid **Saturday 04:00 CEST** *staff* |
| Quest items | can no longer go into the warehouse *staff* |
| Boss balancing | most bosses changed (table image lost) *staff* |
| Unlisted | red-ether gatherer fixed; Eternal Lake no longer computes as a T8 dungeon; Guardian damage up (~+50 AD, one report); Bracelet of Temptation now 3,900 EP, 780 SP per step, buff 400 HP ×3 / 48 MR ×2 *player* |

WM / client: unit 2000 "Jack O' Lantern", item 763 "Scroll of Transform: [Jack]", item 1056 Halloween reward box, costumes 2043–2045 and item 2549 "Jack's Pumpkin" are all still there. *client*

## About 2016-11-01: weapon rollback ([t494])

Weapons that had been levelled through an exploit were downgraded, "mostly S → A and A → B", to level 1 of the lower grade. Not every player was hit; it depended on the other weapon grades and the legion level. The exact rule was not published *staff*. Players report S1 → A1 and A22 → B1 *player*.

## 2016-11-03 ([t534]; Steam 7 Nov)

**Starter channel** (the old channel 5) *staff*:

| Rule | Value |
|---|---|
| Who | new players **below level 25**, moved there the first time they use a Gaia Scroll |
| Gear in war | only grade **D or C** weapons and artifacts |
| PvE wars | only a few regular monsters |
| Fort defence | legions with a fort there get more legion fame for defending it |
| Dungeons | up to **level 3** only |
| Gaia Scroll during a war | takes the player to a safe zone |
| EP cap there | 14,000 (vs 15,000 at Striker 6) *player* ([t603]) |

**New artifacts** *staff*:

| Artifact | Slot | EP | SP per step | Base | Steps 1–5 |
|---|---|---|---|---|---|
| Necklace of Blade | necklace | 2,500 | 500 | Attack +16 | Atk +21 / ArPen% +4 / Atk +21 / ArPen% +4 / Atk +21 |
| Sharp Necklace | necklace | 3,100 | 620 | Attack speed +16 | AS +21 / ArPen% +4 / AS +21 / ArPen% +4 / AS +21 |
| Sting Bracelet | bracelet | 2,800 | 560 | Attack speed +20 | Atk +26 / ArPen% +4 / Atk +26 / ArPen% +4 / Atk +26 |

**Other changes**:

| Change | Before → after |
|---|---|
| Destroyed lab | its effect now stops *staff* |
| Repeatable-quest reward | 20 blue crystals → **1,000 gold** *staff* |
| Fortress guards | can now be healed by players *staff* |
| SP from player kills | **× 1/5** *staff* |
| Medal formula | more medals, deaths punished less *staff* |
| Nation owning **< 10** fields | more medals for a win *staff* |
| Cores | the same core can no longer be installed twice in one fort *staff* |
| Legion level, EXP, mastery | reset *staff* |
| Battle Arena | invitation shown even during war; held **once an hour** if a channel has more than **100** players (was a fixed daily time) *staff* |
| Yellow ether as legion reward | only **10 %** of the pool is paid out, split 1st 30 % · 2nd 15 % · 3rd 12 % · 4–10th 4 % each · 11–15th 2 % each · 16–20th 1 % each *staff* |
| VIP ticket (gold) | 6,000,000 → **9,000,000** *player* |
| High Reinforcing Adjuvant | 2,500,000 → **7,500,000** gold *player* |
| Fortress construction kit | 12,000,000 → **18,000,000** gold *player* |
| New character stats | Armor Penetration % and Magic Penetration % *player* |

A medal bug the same day gave single players up to 255 gold medals; staff told them to sell or destroy them ([t534]).

## 2016-11-07/08 ([t524], [t609])

| Change | Value |
|---|---|
| Legions | all reset to **level 1** (some had out-levelled the intended curve on day 1) *staff* |
| Lords of the Land | only the **winning** team gets the buff and reward box (11-07 had already changed how it is gained) *staff* |
| Character deletion | **24 h** wait before a new character can be made on that slot *staff* |

## 2016-11-17 ([t681])

Crafting price by item grade *staff*:

| Grade | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Before | 1,000 | 2,000 | 3,000 | 5,000 | 10,000 | 20,000 | 30,000 |
| After | 2,000 | 4,000 | 10,000 | 20,000 | 50,000 | 100,000 | 240,000 |

Reinforcement price *staff*:

| Step | D→C | C→B | B→A | A→S | S→SS |
|---|---|---|---|---|---|
| Before | 1,000 | 5,000 | 10,000 | 16,000 | 25,000 |
| After | 1,000 | 5,000 | 10,000 | **30,000** | **60,000** |

| Change | Value |
|---|---|
| Artifact SP cost | no longer drops as the grade rises; a fixed cost per item *staff* |
| New consumables | 2 at the Merits NPC, 1 in the AH, 2 for HP and 1 for TP *staff*. Players list: Life Saviour (2,000 HP instantly), 100 for 1,000 jewels; a fame Life Saviour (1,000 HP) for 1,000 fame; Potion of Brisk A, 1 gold medal, +2,000 SP *player*. The jewel potion was pulled the same week *staff* |
| Negative fame | for **losing a fort siege** (stops fake attacks). It also hit normal battles by mistake; that was removed *staff* |
| After-battle info | extra result screen *staff* |

WM / client: `ItemSancMet` charges a flat 1,000 / 3,000 / 5,000 / 10,000 gold per table row, and `Item_Make` gold is 0 for 369 of 465 recipes, 150–450 for the rest. The CO grade price tables do not survive. Potion of Brisk [A]/[B]/[C] cost 1 gold/silver/bronze medal and give 2,000/1,000/500 SP (`Item_Base` 880–882, opt 503). *client*

## 2016-11-23: Season 1 ([t714]; Steam 23 Nov)

| Change | Value |
|---|---|
| Lords of the Land | now also from killing the territory **boss** in PvE *staff* |
| Channels | 5 → **3**: ch1 a King's fortress per nation; ch2 a system fortress per nation that falls once players build their own; ch3 beginner channel with no player forts. Displaced fort owners refunded *staff* |
| Marshals | 20 → **8** from the next council *staff* |
| TP skills | open to more ranks (table image lost) *staff* |
| Life Saviour (HP potion) | not usable in the Battle Arena; cooldown **120 s** *staff* |
| Premium Life Saviour | bundle of 25 for **1,000 jewels**; heals **50 %** of max HP (2,000 cap mentioned) *staff* |
| Fame Life Saviour | **1,000 fame** at the Merits merchant; heals **30 %** of max HP *staff* |
| Invincible Armor / Gloves of Ghost | effect now only on the wearer; duration 5 s → **3 s** *staff* (5 s before: [t295]) |
| Holding a tower in war | **8 TP** per tower every **10 s** *staff* |
| AH prices | High Reinforcing Adjuvant 2,000 jewels / 10,000,000 gold · VIP 30 days 2,500 jewels / 12,500,000 gold · Fortress construction 4,500 jewels / 22,500,000 gold *staff* |
| Monster invasions | chance now set mainly by the Safety Factor, then by the total land a nation holds on the channel *staff* |
| Costume preview | added *staff* |

Rank structure *staff*:

| Rank | Who |
|---|---|
| King | 1 per nation |
| Marshal | 20 (8 after the next council); from 15 Dec every fort owner |
| Imperator | individual ranking 1–3 |
| General | individual ranking 4–25 |
| Officer | individual ranking 25–73 |
| Veteran | 55,411 – 5,117,346 personal fame |
| Soldier | 600 – 55,410 personal fame |

Lords of the Land buff tiers *staff*; the launch values are from a 11 Oct screenshot ([t24], *image*):

| Stack | At launch | From 23 Nov 2016 | WM client (`Skill_Buff` 3029–3034) |
|---|---|---|---|
| 1 | AD and AP +4 % | AD and AP **+10** | AD and AP +10 |
| 2 | cooldown and respawn wait −5 % | same | respawn wait −5 % (no cooldown) |
| 3 | SP gain +6 | same | **Armor and MR +4 %** |
| 4 | take 5 % less damage, deal it back as bonus damage | **AD and AP +4 %** | AD and AP +4 % |
| 5 | heal and mana regen +20, whole buff doubled | same | whole buff doubled (no +20) |

WM / client: the fame thresholds are **exactly** the CO numbers: `Level_Table` fame_threshold 600 → 1,860 → 5,766 → 17,875 → **55,411** → … → **5,117,346** → 15,863,773 (×3.1 per step), and `FameRank` names Novice, Soldier 1–4, Veteran 1–5, Officer 1–5, General, Imperator, Senator, Marshal, King. Life Saviour items 1801/1802 heal 50 % / 30 % (`Skill_Base` 5276/5275 eff 121/120), and the fame one costs 1,000 fame. The client cooldown field is **15,000 ms**, not 120 s. Each LotL stack lasts 120 min (`WinAffect`). *client*

## 2016-11-25 ([t723]; Steam 25 Nov)

Every account created before 23 Nov 23:59 CET got **4,500 jewels** *staff*.

## 2016-12-01 ([t747])

| Change | Before → after |
|---|---|
| TP for destroying a tower | **8 → 50** *staff* |
| Fortress-siege nexus HP | **5,000 → 15,000** *staff* |
| Nexus armor / MR | **30 → 40** *staff* |
| Nexus attack | 6 % → **10 %** of the target's health; hits now slow *staff* |
| Nexus attack interval | 8,000 → 10,000 (units not given, probably ms) *staff* |
| Towers | detect invisible enemies *staff* |
| Match Info UI | reworked; shows TP-skill holders *staff* |
| Negative legion gold | legions that could not cover it with ether reset to 0 *staff* |
| Training Camp spell stones | lower drop rate *staff* |
| Highest dungeon tier | **T8** *staff* |
| Bow of Frost "Hail of Arrows" | tooltip fixed: hits at most **3** enemies *staff* |
| Reinforcing while dead | disabled *staff* |
| Skill stone "Timewarp" | PvP only *staff* |
| Rank "Grand Marshall" | renamed King *staff* |

WM: first-floor nexus 90,000 HP, armor 540 (WM 0809, [[gameplay/patch-history]]). Client `Skill_Base` 5114 Hail of Arrows has max_targets **5**. *client*

## 2016-12-02 ([t749]; [t748](https://web.archive.org/web/20161206154730/http://www.crush-game.com/forum/threads/nation-change-disabled-and-the-future-of-this-feature.748/))

Nation change disabled from **2 Dec 2016 10:00 CET**, because players kept moving to the winning nation *staff*. Weekend event 2–5 Dec: weapon XP **+25 %**, drop rate **+50 %** for monsters of level 1–5 *staff* ([t755]).

Unannounced, early December: VIP could no longer be bought with gold; the gold VIP ticket had gone to 12.5 M before that *player* ([t773], [t780]).

## 2016-12-15: Civil War ([t816]; Steam 15 Dec)

**Civil War** *staff* (corrected in the replies and on 22 Dec):

| Rule | Value |
|---|---|
| Size | up to **15 v 15**, legion against legion of the same nation |
| Bids | Saturday 00:00–23:59 CET, by legion masters/sub-masters at fortress administrator Hadrin, staking legion gold |
| Several bidders | the highest legion-gold stake fights. Players: an equal later bid takes the slot; a legion that lost its slot cannot bid again *player* ([t827]) |
| Battle | **Sunday 20:00 CET**; both legions wait in the fort's territory (players: inside the fort) |
| Outcome | challengers lose or draw → defenders keep the stake; challengers win → they take the fort. A second fort becomes a System Fort |
| From 22 Dec | the stake is not refunded either way; the winner takes cores and taxes if the fort is on the same channel; fort taxes (from buying, selling and crafting in the fort) are collected as gold during the week and can be claimed as legion ether until **Sunday 24:00 CET**; no Civil War on channel 3 |

**Fortress siege** *staff*:

| Rule | Value |
|---|---|
| Attackers' nexus | stands on floor 1; if it falls the attackers lose |
| Ether plunder | 3 capture bars: bar 1 = **4 %**, bar 2 = **10 %**, bar 3 = **20 %** of the defending legion's total ether |

**Other changes** *staff*:

| Change | Before → after |
|---|---|
| Boundary-area boss summon | dungeon elites drop a scroll that summons one extra boss, **once** per boss: DeathHead, Chepa Sorcerer, Dark Knight, Tempest Fisher, Komodo, Spector, Garon, Leviathan, Akasha |
| Xmas costumes | 3, **5,000 jewels** each, until 9 Jan 2017 |
| VIP window | new UI showing current level and what the next needs |
| Box loot | all boxes changed (image lost) |
| Magic Crafting Stone | removed from the merchant; only from the **[Diamond] Medal Reward Box** |
| Senator rank | new, for top legion leaders; Marshal = every fort owner |
| Changing TP skills during war | allowed; locked for **180 s** afterwards |
| Mailbox slots | unlocked for all players |
| Creating a legion | **1,000,000 → 10,000,000** gold |
| Warehouse | filter added |
| Core "Dimension Move" | removed |
| Spell stones | can be split; **D** spell-stone drops raised in boundary areas, all higher-grade spell-stone drops removed |
| Weapon and skill-stone names | changed (image lost) |
| New quests | to reach level 30 without getting stuck (moderator post) |

WM / client: the summon items are `Item_Base` 2585–2589 "The Death Head's / Dark Knight's / Tempest Fisher's / Slayer Komodo's / Chepa Sorcerer's Pipe". Medal Reward Boxes 1051–1055 ([Bronze] for 4 bronze medals, [Silver] 3 silver, [Gold] 2 gold, [Mithril] 1 mithril, [Diamond]) are still there. The client's weapons carry the **renamed** forms ("Magical Wrath Blade", "Skeleton King's Magic Dagger/Cannon", "Magical Frost Bow", "Magical Demolition Hammer"), which players were already using in early 2017 ([t906]). *client*

Steam news 16 Dec: weekend drop event **+25 %**, and "magic stone chances increased significantly" that morning *staff*.

## 2016-12-22 ([t835]; Steam 22 Dec)

| Change | Value |
|---|---|
| Weapon coefficients | changed so that high grades are stronger, but by less than before (table image lost; Steam text) *staff* |
| SP/TP penalty | the farther a fight is from the nation's fort, the bigger the TP/SP penalty (image lost) *staff* |
| VIP daily jewels | must be claimed by hand; **basic** VIP now also gets **5 jewels** *staff* |
| Blacksmith Farrel | now buys and sells items *staff* |
| Skill stones for Striker rank 1–2 | sold for gold, no crafting; rank 3+ still crafted (price image lost) *staff* |
| Land of the Lord buff | gained by destroying the enemy **nexus** (PvP) or killing the territory **boss** (PvE); lost by **fleeing** or **losing** *staff* |
| Land of the Lord reward box | new contents (image lost) *staff* |
| Drop Chance Potion | **+20 %** drops for **1 h**; 500 jewels, or 10 for 4,500 *staff* |
| Xmas drop costume | +10 % drop chance, 14 days, 3,800 jewels, gone from the AH on 9 Jan; older Xmas costumes stay permanent with no drop bonus *staff* |
| Shop costumes | all limited to **14 days**; Halloween sets removed *staff* |
| Costume prices (jewels) | Summer 2,000 · Dragon Slayer 2,500 · Athlete 2,000 · Maid 2,000 · Military 2,000 · Goosebam 2,500 · Christmas 3,800 *staff* |
| Make a costume permanent ("carve") | **10,000,000 gold** at the Merits Costume Merchant; becomes the default skin, effects and timer removed *staff* |
| Costume Remover | **425,000 gold**; hides the costume and keeps its stats *staff* |

WM / client: Drop Chance Potion (item 764 → buff 2134) gives **+40 %** (WM 0726 agrees), not 20 %. Costume Remover (item 1999) costs **50,000** gold. The LotL description matches the 22 Dec rule: given when the attacker earns a medal, reset by running away or defeat. *client*

Events: 28 Dec – 2 Jan **+25 %** weapon XP and drops ([t855]); 13–16 Jan the same (Steam).

## 2017-02-02: Season 2 ([t898]; German copy t897; Steam 2 Feb)

| Change | Value |
|---|---|
| Daily quest system | up to **3** daily, **4** weekly and **5** monthly quests a day, plus bonus rewards for clear counts; about **13,000 jewels** a month if all are done *staff* |
| Artifacts | base stats and scaling cut; monster abilities cut **15–20 %** to match (players measured artifact cuts of 30–56 %) *staff* / *player* |
| Monster drops | dropped items now roll stats and durability like crafted ones (before: 0 durability, no additional effect, [t868]) *staff* |
| Content | **55** new artifacts, weapons and skill stones (e.g. Ring of Death, Mithril Earrings, Brilliant Vision Bow); items carry a **Volume** (season): "Nightmare" (S1), "Bless" (S2); "Basic" items stay the same every season *staff* / *player* ([t904]) |
| Artifact sets | collectable sets with set bonuses (14k and 17k EP sets, [t906] player) *staff* |
| Weapon alchemy | combine a **level 30** weapon with materials; a higher-grade input weapon raises the success chance; on failure **all** materials are lost; Skull weapons now only from alchemy *staff* |
| Council dates | shown in the UI *staff* |
| Fixes | fort core "Increased Luck" now adds drop rate; Add-on "Twisted Dimension" scales dungeon level properly; Gloves of Raven craftable again (T7 drop) *staff* |
| Announced | fortress upgrade system (later: WM fort levels/masteries) *staff* |

Events: 3–6 Feb drop chance **+25 %** ([t902]); 14–15 Feb 14:02–14:02 CET **double** drops and weapon XP ([t913]).

WM: the client has 9 set bonuses (`SetBounsItem`) and WM 0809 boss sets, but none of the CO artifacts (Necklace of Blade, Thorns Armor, Huge Belt…) and no EP field in `Item_Base`. *client*

## 2017-02-21 ([t922]; Steam 21 Feb)

| Change | Value |
|---|---|
| Medal boxes | contents changed to drop more medals *staff* |
| Costume | "Family Bear" set *staff* |
| Set items | can be reinforced up to **SS** *staff* |
| Artifact steps | reinforcing to a higher grade now unlocks the steps **permanently**; SP no longer has to be spent in battle (table image lost) *staff* |
| Artifact reinforce chance | depends on the artifact's tier; lower tiers succeed more often (image lost) *staff* |
| SP potions | cooldown removed *staff* |

## 2017-03-01: shutdown notice ([t930]; Steam 1 Mar)

Last day on Steam **30 Apr 2017**, offline **1 May 2017**; payment switched off; all jewel purchases to be refunded in "Crush 2.0" *staff*. A later post told players to keep using the non-Steam client with their GAMESinFLAMES login ([t937](https://web.archive.org/web/20171117094023/http://crush-game.com/forum/threads/en-playing-crush-online-without-steam.937/)).

## 2017-03-02 ([t934])

| Change | Value |
|---|---|
| Period costumes in the AH | now carry stat bonuses; carving (making permanent) removes the bonus *staff* |
| Tooltips | lockable detail view *staff* |
| Crafting menu | shows every needed material, including artifacts *staff* |
| Weapon sockets | Skeleton weapons can open sockets for jewel stones giving Attack, Attack speed, Spell power, Armor, MR, cooldown or ST points. NPC **Alan** sells stones, NPC **Casta** opens sockets and inserts/removes stones. A failed socket opening can **destroy** the weapon; stones must match the weapon grade, one at a time; removing a stone destroys it *staff* |
| Strategy (TP) skills | rank requirements lowered; Officer and General removed as requirements (tables lost) *staff* |
| Skill cooldowns | adjusted (no numbers) *staff* |
| **Intrusion** | a **third nation** may join a war and take the land by last-hitting the boss or reaching **10,000 TP**; intruders have no nexus and no TP skills and are not shown in the war info *staff* |
| Players per war | lowered to **15** (the note does not say per side or in total; before it was 15 v 15, and fort lands let in more, [t392]) *staff* |

WM / client: sockets (`JewelSocket`, NPCs) and the three-nation intrusion survive as WM features. The WM 1107 War of Warmonger caps sides at 15 with bots ([[gameplay/patch-history]]). *client* / *notes*

---

## Coverage

- **Threads read:** 386 thread pages (370 threads) saved by the earlier sweep, all read: English news, guides, general discussion, FAQ, bug reports and suggestions; German news, discussion and legion boards (8); Turkish news and discussion (4). No Polish or French thread page was ever archived: the index pages list 5 French and 1 Polish thread, but none has a capture. Plus the 23 CO Steam news items.
- **Newly fetched:** 0 threads. The 39 "missing" CDX entries are 404/301/403 captures or duplicate ids of threads already saved, and the 105 threads seen only on the 86 forum index pages (fetched for this check) have no Wayback capture. 15 imgur screenshots were fetched; 66 official images were tried and none was archived.

[t15]: https://web.archive.org/web/20161020061825/http://www.crush-game.com/forum/threads/psa-npc-territory.15/
[t24]: https://web.archive.org/web/20161015064613/http://www.crush-game.com/forum/threads/psa-land-lord-quest.24/
[t29]: https://web.archive.org/web/20161015055537/http://www.crush-game.com/forum/threads/patch-notes-20161011.29/
[t48]: https://web.archive.org/web/20161015063056/http://www2.crush-game.com/forum/threads/yama-notlari-2016-10-11.48/
[t85]: https://web.archive.org/web/20161015074715/http://crush-game.com/forum/threads/patch-notes-20161012.85/
[t109]: https://web.archive.org/web/20161017183210/http://www.crush-game.com/forum/threads/guide-vip-connection-rewards-system.109/
[t115]: https://web.archive.org/web/20161017024821/http://www.crush-game.com/forum/threads/patch-notes-20161013.115/
[t146]: https://web.archive.org/web/20161020050128/http://www.crush-game.com/forum/threads/patch-notes-20161014.146/
[t158]: https://web.archive.org/web/20161017065056/http://www.crush-game.com/forum/threads/quick-guide-about-kings-fortresses-laboratories.158/
[t234]: https://web.archive.org/web/20161020051204/http://www.crush-game.com/forum/threads/patch-notes-20161017.234/
[t290]: https://web.archive.org/web/20161022145536/http://www.crush-game.com/forum/threads/patch-notes-20161019.290/
[t291]: https://web.archive.org/web/20161023112324/http://www.crush-game.com/forum/threads/patch-notes-20161019.291/
[t295]: https://web.archive.org/web/20161025042755/http://www.crush-game.com/forum/threads/invincible-armor-gloves-of-ghost-information.295/
[t317]: https://web.archive.org/web/20161024091404/http://www.crush-game.com/forum/threads/1st-national-council-in-crush-online.317/
[t348]: https://web.archive.org/web/20161024085844/http://www.crush-game.com/forum/threads/skeleton-dagger-attack-speed-lowered.348/
[t350]: https://web.archive.org/web/20161025044649/http://www.crush-game.com/forum/threads/patch-notes-20161021.350/
[t355]: https://web.archive.org/web/20161026122218/http://www.crush-game.com/forum/threads/halloween-costumes.355/
[t392]: https://web.archive.org/web/20161025044819/http://www.crush-game.com/forum/threads/war-under-fortress-bug.392/
[t450]: https://web.archive.org/web/20161031223229/http://www.crush-game.com/forum/threads/patch-2016-10-21-overview-weapon-balancing.450/
[t453]: https://web.archive.org/web/20161030053817/http://www.crush-game.com/forum/threads/patch-notes-20161027-halloween-event.453/
[t494]: https://web.archive.org/web/20161102115146/http://www.crush-game.com/forum/threads/weapon-downgrade.494/
[t524]: https://web.archive.org/web/20161107135423/http://www.crush-game.com/forum/threads/legion-level-reset-beginner-channel.524/
[t534]: https://web.archive.org/web/20161106035205/http://www.crush-game.com/forum/threads/patchnotes-20161103.534/
[t603]: https://web.archive.org/web/20161129115247/http://www.crush-game.com/forum/threads/channel-5-guide-to-being-notorious-how-to-twink-your-gear-ep-13500.603/
[t609]: https://web.archive.org/web/20170701033345/http://crush-game.com/forum/threads/patchlog-20161108.609/
[t681]: https://web.archive.org/web/20161124163001/http://www.crush-game.com/forum/threads/updated-patchnotes-20161117.681/
[t714]: https://web.archive.org/web/20161127144545/http://www.crush-game.com/forum/threads/patch-notes-20161123-season-1.714/
[t723]: https://web.archive.org/web/20170419074622/http://www.crush-game.com/forum/threads/a-gift-free-jewels-worth-over-5-euro.723/
[t747]: https://web.archive.org/web/20161204161112/http://www.crush-game.com/forum/threads/patch-notes-20161201.747/
[t749]: https://web.archive.org/web/20161209162833/http://www.crush-game.com/forum/threads/nation-change-disabled-by-02-12-16-10-00-cet.749/
[t755]: https://web.archive.org/web/20161205092239/http://www.crush-game.com/forum/threads/week-end-madness-weapon-xp-drop-rates-event.755/
[t773]: https://web.archive.org/web/20161207081416/http://www.crush-game.com/forum/threads/vip-ticket-12-5kk-now.773/
[t780]: https://web.archive.org/web/20161208105504/http://www.crush-game.com/forum/threads/vip-cant-be-bought-now-using-gold.780/
[t816]: https://web.archive.org/web/20161218074842/http://www.crush-game.com/forum/threads/patch-notes-20161215-civil-war.816/
[t827]: https://web.archive.org/web/20170419000850/http://www.crush-game.com/forum/threads/civil-war-thoughts.827/
[t835]: https://web.archive.org/web/20170119153205/http://crush-game.com/forum/threads/patch-notes-20161222.835/
[t855]: https://web.archive.org/web/20170119153617/http://crush-game.com/forum/threads/new-year-event-25-weapon-xp-and-drop-rate.855/
[t868]: https://web.archive.org/web/20170210140704/http://crush-game.com/forum/threads/general-guide-to-gearing-up-and-getting-started.868/
[t898]: https://web.archive.org/web/20170206152519/http://www.crush-game.com/forum/threads/patchnotes-20170202-season-2-changes.898/
[t902]: https://web.archive.org/web/20170210140527/http://crush-game.com/forum/threads/drop-chance-event-this-weekend_03-02-06-02.902/
[t904]: https://web.archive.org/web/20170211151046/http://crush-game.com/forum/threads/items-drop-list-guide.904/
[t906]: https://web.archive.org/web/20170211151251/http://www.crush-game.com/forum/threads/sealed-stones-15000-ep.906/
[t913]: https://web.archive.org/web/20170217201456/http://www.crush-game.com/forum/threads/valentines-day-special-event.913/
[t922]: https://web.archive.org/web/20170224115748/http://www.crush-game.com/forum/threads/patchnotes-20170221.922/
[t930]: https://web.archive.org/web/20170308155214/http://www.crush-game.com/forum/threads/thank-all-of-you-for-taking-this-journey-with-us.930/
[t934]: https://web.archive.org/web/20170309151333/http://www.crush-game.com/forum/threads/patchnotes-20170302.934/
