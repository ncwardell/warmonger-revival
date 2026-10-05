---
title: "Warmonger forum (2018)"
---

# Warmonger forum (2018)

What the archived `warmonger-game.com/forum` holds, and the numbers in it that the wiki did not have yet. Grouped by system and cited. Most of the board was already mined through its older `crush-game.com` copies ([[gameplay/crush-mechanics]], [[gameplay/crush-patch-notes]], [[gameplay/dungeon-drops]], [[gameplay/stat-values]]). This page adds only what those pages lack and points to them for the rest.

Tags: *forum* = player post · *staff* = CO team or moderator · *client* = decoded WM client table (`data/tables/`) · *guess*. Almost everything here is **Crush Online (CO, Oct 2016 – Apr 2017)**. Where the WM client agrees or differs, that is stated.

## 1. What the archive is

| Fact | Value | Source |
|---|---|---|
| What it is | The **Crush Online XenForo board, frozen** and moved to the new domain. Every page title still reads "Crush Online - Forum" and every post is from Oct 2016 – Sep 2017. Only **one** post was written after the move: a 13 May 2018 request to change the Warmonger account linked to Steam (post 4389, thread 961) | [w961], [w422] *forum* |
| Captures | 281 forum URLs, 31 Mar 2018 – 2 Jan 2019: 196 × 200, 57 × 301, 15 × 404, 10 × 403 (login walls), 2 × 303, 1 × 405 | [CDX listing](https://web.archive.org/cdx/search/cdx?url=warmonger-game.com/*&output=json&collapse=urlkey&limit=20000) |
| Threads saved | 49 thread pages (incl. page 2 of threads 109, 679 and 247), 13 `posts/` and 25 `goto/post` redirects (most are "page not found"), 25 section index pages and 13 section RSS feeds | this sweep |
| Section RSS feeds | Each feed carries the **first post** (truncated) of the newest ~20 threads per section. This is the only copy of about 100 threads, among them bug reports and German news posts | e.g. [rss-bugs], [rss-faq] |
| Non-forum pages | none with content. The 2018 official site left only 301-redirected media (class videos `guardian_720`, `punisher_720`, `saint_720`, `crush_web`; `screen_1–6.jpg`; `Weekend_Madness_3.jpg`). From Sep 2019 the domain is a Thai casino spam blog (WordPress) | [CDX listing](https://web.archive.org/cdx/search/cdx?url=warmonger-game.com/*&output=json&collapse=urlkey&limit=20000) |
| Attachments, images | `forum/attachments/*` are 403 login walls. The CO staff table images (`crush-game.com/sites/…/assets/…`: VIP level plan, boss-balancing table of 27 Oct 2016, weapon coefficients of 22 Dec 2016) were **never archived** (CDX empty, direct fetch 404) | this sweep |

## 2. Dungeon drops (Season 2, Feb 2017)

Full list of artifacts found per dungeon level after Season 2 made monster drops roll durability and additional effects. The wiki had only four examples ([[gameplay/crush-mechanics]] §9). EP = Equipment Points cost; volume = season tag (Basic stays every season, Nightmare = Season 1 item, now drop-only; Bless = Season 2, craft-only). *forum* [w904]

| Dungeon level | Artifact (volume, EP) |
|---|---|
| 1 | Bone Necklace (Nightmare, 2,400); Bracelet of Wrath (Basic, 800); Stone of Mana (Basic, 250); Bead of Spirit (Basic); Stone of Health (added by a reply) |
| 2 | Wooden Quiver (Basic, 600); Absorption of Bandolier; Fabric Armor (Basic, 300); Ring of Magic (Basic, 400); Cape (Basic, 300) |
| 3 | Mana's Orb (Nightmare, 1,000); Gloves of Swordsman (Basic, 1,600); Earrings of Magic (Basic, 2,000); Bracelet of Wrath (Basic, 800) |
| 4 | Leather Cape (900); Plate Armor (1,500); Ring of Emission (1,200); Ring of Swordsman (1,700); Ring of Rise (1,600), all Basic |
| 5 | Helmet of Protection (Nightmare, 1,800); White Gloves (Nightmare, 1,600); Bracelet of Spirit (Basic, 2,400); Thief's Gloves (Basic, 2,100); Necklace of Transcendency (Basic, 1,850) |
| 6 | Cape of Odin (Basic, 1,500); Ring of Fighter (Basic, 1,600); Primal Quiver (Basic, 2,600); Thick Cape (Nightmare, 1,700) |
| 7 | Earrings of Life (2,400); Ultimate Gloves (2,625); Limited Gloves (2,000); Gloves of Raven (2,350); Gloves of Zealot (3,600), all Basic |
| 8 | Cape of Sun (Nightmare, 2,250); Ring of Glacier (Nightmare, 3,600); Huge Belt (Basic, 1,500); Armor of Spirit (Basic, 1,500); Ring of Life (Basic, 2,400) |
| Field / Abyss only | Ring of Wizard (Lv 1), Timeworn Cape (Lv 1), Ruby of Health (Lv 2–3), High-quality Sapphire (Lv 2–3), Ring of Rush (Lv 4 or the last Abyss room), Chain Armor (Lv 4), Ring of Abyss (Lv 4) |

- A Saint guide from the same week confirms six of these sources (White Gloves and Necklace of Transcendency T5, Thick Cape T6, Earrings of Life T7, Cape of Sun and Huge Belt T8) and says White Bracelet (Nightmare) could then be neither dropped nor crafted *forum* [w907].
- The dungeon level is "T" in player speech; level 7 = 7 lands away from a fort; dungeons do not spawn on channel 3 *staff* [w71].
- None of these CO artifact names exist in the WM client strings (`StringAll_Eng`). WM drops tiered gear instead; use this list only as a model for "each dungeon level has its own loot table, with a few field-only items". *client*

## 3. Bosses, essences and the Tow quest

| Rule | Value | Source |
|---|---|---|
| When a dungeon boss exists | only when the map is **monster-invaded** (black skull over the land on the world map) | *forum* [w71] |
| Essence of Darkness from T1/T2 bosses | the T1/T2 dungeon boss is blocked by shields unless the nation has **more than one fort** on the channel; the other source is the officers in the T8 field | *forum* [w680] |
| Solo farming | Lv 1–2 bosses (Deathhead, Death Knight) can be soloed with base gear and potions; one pair killed Death Knight about 40 times without an essence, and players reported a lower rate after patches | *forum* [w361] |
| Tow Chief (Abyss) loot | only three drops: reinforcement stones, spell-stone patterns, Essence of Darkness (very rare); must be killed by a level 15–20 (or 25) character | *forum* [w361] |
| Essence weapon route (Punisher) | Skeleton King's Dagger + "Knight" skill stone = **2 Essence of Darkness + 200 silver medals** | *forum* [w680] |
| Abyss Tow quest (CO) | in the Abyss field next to the starting zone that has your nation's guards: kill **10 Tow, 10 Elite Tow, 1 boss** → **5 Shining Stones + 10 D reinforcement stones**; 5–10 minutes. Shining Stones (NPC price 5 copper) go into three Guardian weapons (5 / 5 / 15) | *forum* [w691] |
| Same quest in WM | quest ids **80–82** "Support the Abyss expedition": kill 10 × unit 10001, 10 × unit 10002 and 1 × unit **826 Tow Chief** in field **108** (The land of Greed) → **220,000 EXP** plus a class weapon (80: Magical Life Wand 10002 + Magical Wrath Blade 10017; 81: Magical Judge Dagger 15007; 82: Magical Demolition Hammer 20001). Quest 17 (same title, prerequisite) gives 198,000 EXP + 100 C health and mana potions (885, 889) | `Quest.tsv`, `StringAll_Eng` *client* |
| WM Land of Greed repeatable | quests 749 and 1101: 50 × unit 10001 + 50 × unit 10002 in field 108 → 50,000 EXP, 50,000 (reward type 4, probably gold) and 50 Blue Passion Fragments [D] (601) | `Quest.tsv` *client* |

## 4. Levelling and medals

| Rule | Value | Source |
|---|---|---|
| Refined Oils repeatable | unlocks after the Odin quest (collect 2 Garnet and 2 Bloodstone) | *forum* [w621] |
| Level 28–29 stall | blue repeatables are triggered by finishing certain purple quests (boss kills, NPC lands + box). Hand in blue repeatables first and keep the purple ones until no blue is left | *forum* [w680], [w422] |
| Freya precept quests | give **no EXP** | *forum* [w422] |
| Silver from precepts | B scroll "kill Tempest Fisher" → **4 silver**; B scroll "kill 10/10 Tow" → **2 silver**; C scroll "occupy territory 10/10" or "kill players" (Abyss kills count) → silver | *forum* [w680] |
| Bronze | conquering NPC territory gives bronze medals; new players needed 100–200 bronze per weapon | *forum* [w361] |
| Season 2 medals | wars gave mostly bronze, silver very rarely; after Season 2 every weapon cost bronze only, and 13.5k-EP sets came from quests | *forum* [w900] |

## 5. Legions and forts

Legion stats per level (the guide only knew levels 1–2) *forum* [w426]:

| Level | Members max | EXP to next | Legion gold to next | Stock max | Mastery points |
|---|---|---|---|---|---|
| 1 | 60 | 30,000 | 100,000 | 100 | 1 |
| 2 | 60 | 204,000 | 220,000 | 400 | 3 |

WM `Level_Table_Guild` keeps the gold (100,000 / 220,000) but not the EXP; see [[gameplay/crush-mechanics]] §8. *client*

Fort cores: durability starts at **100** and drops **1 per hour**; each core also pays legion fame per hour, and active cores cost durability per use *forum* [w426]:

| Core | Effect | Fame / hour | Per use: durability, fame |
|---|---|---|---|
| Increasing Barrier | max shields +2 (cap 10) | 20 | passive |
| Recharging Barrier | shield recharge −20 % (1 shield / 30 min → 24 min) | 200 | passive |
| Preserving Barrier | keeps shields when the fort moves | 20 | passive (the guide's per-use line here is garbled) |
| Moving the Fortress | move up to 2 lands | 20 | 10, 200 |
| Increasing Seal | enlarges the fort; safety +10 around it | 10 | 50, 500 |
| Add-on: Reinforce Nexus | stronger nexus (HP, armour, damage) on a chosen land | 20 | 100, 2,000 |
| Add-on: Gathering Red Ether | gatherer on a chosen land; usable 30 min after placing; then 1 (blue) ether every 30 min | 40 | 100, 4,000 |
| Vitality of the Fortress | full SP in wars within 3 lands of the fort | 50 | 20, 1,000 |
| Reserved Time | resets all core cooldowns | 10 | 100, 1,000 |
| Dimension Movement (needs a lab) | moves the fort to another channel | 10 | 50, 500 |

- 5 [Low] cores sold by NPC **Arion** for 192,000 personal gold; crafted cores (**28** kinds) are installed at **Hadrian** *forum* [w426].
- Dimension Movement lands on a **random** owned land; never channel 3, never a channel that already has 4 forts *forum* [w763].
- At most **4 forts per nation per channel**; channel 3 holds system forts only; only top-20 legions may build; Civil War bids on Saturday, the war follows on Monday *staff/forum* [w763].
- Best standing set: Increasing Barrier + [Low] Increasing Barrier + [Low] Recharging Barrier = **+3 shields, 10 % faster** recharge *forum* [w866].
- Moving a fort onto a land with an add-on destroys the add-on *forum* [w866].
- Fighting on a channel where your legion owns a fort gives **+50 % fame** *forum* [w866].
- A legion with negative gold cannot invite; leaders can summon members into a running battle from the member list *forum* [w866].
- System forts kept their shields even when the nation had other forts on the channel; players hid gatherers under them (bug report, Feb 2017) *forum* [rss-bugs].
- A player built forts with an alt of the enemy nation to lock that nation out of its level 5–8 dungeons *forum* [rss-faq].
- Fort siege: each Heart destroyed removes one guard respawn (2 guards killed with 1 Heart down → 1 comes back) *forum* [w426].

## 6. War and arena (CO, as described by players in 2017)

| Rule | Value | Source |
|---|---|---|
| Respawn point | dead players respawn **inside** their nexus; a nexus push turns into spawn-killing (players asked for a ring around the nexus) | *forum* [w900], [w910] |
| Tower rush | towers were weak enough that Punishers could dive them alone; players asked for much stronger towers | *forum* [w893], [w910] |
| Strong TP-skill pairs | Healing Circle + Artillery Fire to take a nexus; Revive + Portal | *forum* [w900] |
| Arena map | one lane plus jungle camps (more than 4 per side, since a player asked to cut them to 4 *guess*), a centre zone that grants SP over time, the arena nexus does **not** heal players; empty queues gave matches against bots | *forum* [w893], [w910] |
| Arena rewards | coins and boxes, called useless; monthly and weekly leaderboard rewards existed (see [[gameplay/arena-ranking-rewards]]) | *forum* [w910], *staff* [w941] |
| Reward credit | war reward points came from kills only; towers, jungle, healing and defence did not count | *forum* [w900] |

## 7. Stats, regen and crafting

| Rule | Value | Source |
|---|---|---|
| Mana regen example (Saint, A-grade weapons) | base **10** per tick + Gaia buff 20 + Flask of Mana 16 + two S artifacts 12 each = **70 per tick**; S mana and HP/MP potions = 400 mana per 16 s; together about 36 mana/s (player assumes a 6 s tick) | *forum* [w907] |
| Armour target | 350–400 armour cuts 75–80 % of physical damage; 50 more armour gains only 1–2 % | *forum* [w866] (formula in [[gameplay/stat-values]]) |
| Additional-effect totals at A grade | 4 × 44 armour = 176; 4 × 24 attack = 96; 8 × (14 attack + 24 armour) = 112 / 192; 8 × attack-only = 192 | *forum* [w866], [w803] |
| Higher-grade reinforcement stone | using a stone above the item's grade raises the success chance | *forum* [w866] |
| Spell stones | use the weapon's own grade; higher grades work but are wasted | *forum* [w866] |
| Craft failures | Thorns Armor failed up to 11 times in a row for one player; Thorns Armor, Necklace of Despair and Invincible Armor 7–10+ fails were common; a failed Skull-weapon alchemy lost an A30 weapon and a boss horn | *forum* [w803], [w895], [w900] |
| Bulk crafting | about 2–3 s per item and a click every 100 items; 100 S reinforcement stones need 12,800 D stones (≈ 576 M gold at 45,000 gold per D) | *forum* [w916] |
| Crushing shop items | 50 items → about 20–25 blue crystals, about 700k profit when sold | *forum* [w866] |

Punisher artifact stats at 14,000 EP (helmet to ring, 25 items with EP and main stats) are in [w803]; the same items with sheet values are in [[gameplay/gear-stats]].

## 8. VIP and account

| Rule | Value | Source |
|---|---|---|
| VIP thresholds | jewels bought in the last 30 days. The staff example (10,000 → VIP 2; 30,000 → VIP 3; 40,000 → VIP 4) bounds them: VIP 2 ≤ 10,000 < VIP 3 ≤ 30,000 < VIP 4 ≤ 40,000; staff confirmed VIP 4 needs 40,000 jewels **every** 30 days | *staff* [w679]; exact thresholds were in a lost image; bounds are a *guess* from the example |
| VIP ticket | 6,000,000 gold or 2,000 jewels at Cathy; with gold only VIP 1 is reachable | *staff* [w679], *forum* [w422] |
| Warehouse expansion | the last steps cost 500 / 750 / 1,000 jewels (one more step after that) | *forum* [w679] |
| Free gift | 4,500 jewels to every account that existed on 23 Nov 2016 | *staff* [rss-news8] |
| Weekend Madness (2–5 Dec 2016) | +25 % weapon XP; +50 % drop rate for monsters of level 1–5 | *staff* [rss-news8] |
| Server address (CO, Oct 2016) | the support guide had players trace 5.196.252.200 | *staff* [w108] |
| Steam end | Steam version off on 1 May 2017; the standalone client kept running into 2017 (only channel 1 worked by Sep 2017) | *staff* [rss-news8], *forum* [rss-disc] |

## 9. Threads listed on index pages but never archived

The section indexes name threads whose pages exist in no capture on either domain. They would have filled gaps 1–4 in [[gameplay/sources]] §9: **List of all Grind locations 11/7/2016** (598), **Monster Drop Rate: In Progress** (636), **[Patch 2016-10-27] Boss Monster Balancing** (473, a table image), **Upgrading Weapons from A to S** (633), **Nation Overview** (538), **Forts & Channel Movement** (532), **Lord of the lands buff** (846), **PvP Motivation/Medals** (891), **Siege minion, war, and Strat panel** (860, the old crush-game copy exists, see [[gameplay/sources]] §8). Sources: [idx-guides2], [idx-sugg2].

## Threads read

From `warmonger-game.com/forum` (Wayback, 2018): 71, 108, 109 (+p2), 207, 247 (+p2), 261, 361, 422, 426, 528, 621, 679 (+p2), 680, 691, 719, 763, 803, 838, 866, 868, 876, 888, 889, 893, 894, 895, 900, 904, 906, 907, 909, 910, 916, 924, 925, 926, 927, 938, 941, 943, 944, 945, 948, 961; 13 RSS feeds (first posts of about 170 threads); 25 section and category indexes. New facts above come mainly from 426, 680, 691, 866, 893, 900, 904, 907, 910 and the feeds.

[w71]: https://web.archive.org/web/20180406072259/http://warmonger-game.com/forum/threads/dungeon-ore-plants-drop-location-boss-location.71/
[w108]: https://web.archive.org/web/20180406065225/http://warmonger-game.com/forum/threads/technical-diagnostic-tools.108/
[w361]: https://web.archive.org/web/20180715012142/http://www.warmonger-game.com/forum/threads/how-to-get-essence-of-darkness-reinforcement-stones.361
[w422]: https://web.archive.org/web/20180331215519/http://warmonger-game.com/forum/threads/beginners-guide.422
[w426]: https://web.archive.org/web/20180331215534/http://warmonger-game.com/forum/threads/legions-and-fortresses.426
[w621]: https://web.archive.org/web/20180406065032/http://warmonger-game.com/forum/threads/guide-to-leveling-how-to-avoid-getting-stuck.621/
[w679]: https://web.archive.org/web/20180406064925/http://warmonger-game.com/forum/threads/guide-vip-connection-rewards-system.679/
[w680]: https://web.archive.org/web/20180406072506/http://warmonger-game.com/forum/threads/secrets-of-gearing-up-lets-get-strong.680/
[w691]: https://web.archive.org/web/20180406072456/http://warmonger-game.com/forum/threads/free-shining-stones-x5-bind-on-pickup.691/
[w763]: https://web.archive.org/web/20180406072627/http://warmonger-game.com/forum/threads/fort-cores-guide.763/
[w803]: https://web.archive.org/web/20180406065210/http://warmonger-game.com/forum/threads/punisher-build-guide.803/
[w866]: https://web.archive.org/web/20180331215552/http://warmonger-game.com/forum/threads/tips-tricks-and-cookies.866
[w893]: https://web.archive.org/web/20180406072617/http://warmonger-game.com/forum/threads/arena.893/
[w895]: https://web.archive.org/web/20180406072643/http://warmonger-game.com/forum/threads/upgrade-crafting-system.895/
[w900]: https://web.archive.org/web/20180406072314/http://warmonger-game.com/forum/threads/season-2-impressions.900/
[w904]: https://web.archive.org/web/20180331215529/http://warmonger-game.com/forum/threads/items-drop-list-guide.904
[w907]: https://web.archive.org/web/20180331215539/http://warmonger-game.com/forum/threads/quick-guide-to-saints.907
[w910]: https://web.archive.org/web/20180406072228/http://warmonger-game.com/forum/threads/war-arena-etc.910/
[w916]: https://web.archive.org/web/20180406072638/http://warmonger-game.com/forum/threads/instant-craft-create-for-many.916/
[w941]: https://web.archive.org/web/20180406065327/http://warmonger-game.com/forum/threads/some-ideas.941/
[w961]: https://web.archive.org/web/20180801104243/http://www.warmonger-game.com/forum/threads/change-the-warmonger-account-linked-to-steam.961
[rss-bugs]: https://web.archive.org/web/20180406064903/http://warmonger-game.com/forum/forums/bugs-reports.13/index.rss
[rss-faq]: https://web.archive.org/web/20180406072552/http://warmonger-game.com/forum/forums/general-question-faq.12/index.rss
[rss-disc]: https://web.archive.org/web/20180406072429/http://warmonger-game.com/forum/forums/general-discussion.14/index.rss
[rss-news8]: https://web.archive.org/web/20180406065147/http://warmonger-game.com/forum/forums/news.8/index.rss
[idx-sugg2]: https://web.archive.org/web/20180403051822/http://warmonger-game.com/forum/forums/game-suggestions.82/page-2
[idx-guides2]: https://web.archive.org/web/20180403051827/http://warmonger-game.com/forum/forums/guides.15/page-2
