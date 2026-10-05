---
title: "Patch notes and other sources"
---

# Patch notes and other sources

Rules and numbers from the official Steam announcements (Warmonger 2018–19 = **WM**, Crush Online 2016–17 = **CO**), the Spanish blog guide, archived warwiki.net, the archived official CO forum and Steam discussions. Paraphrased; the date tag links the announcement. Later patches override earlier ones, and the client data (final build) overrides all of them. The full text of every announcement is in the Steam news API: `https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=718790&count=300&maxlength=0` (and `appid=475630`).

## Dungeons and world

- Unlock level per border area (WM [0615](https://steamcommunity.com/games/718790/announcements/detail/2842216343262999426)): Chepa 0, Skull Temple 20, Skull Cemetery 21, Tsunami Lake 22, Swamps 23, Tow Canyon 24, Ghost Fortress 25, Demon Hell 26, Thorn's Hell 27.
- Hard-mode entry moved from Time Energy to Dimensional Energy in WM [0726](https://steamcommunity.com/games/718790/announcements/detail/2462791699369817744) (normal 2/3/3/5/6/7/8/9/10, hard 4/6/8/10/13/16/20/24/29; event dungeons 5 normal, hard 10/10/10/20/20). Earlier Time Energy fees: WM [0426](https://steamcommunity.com/games/718790/announcements/detail/2394103650887775295).
- Time Energy then became buffs: T1/T2/T3 = drops and EXP +10/20/30% for 10 min; Drop Chance Potion +40% drops for 1 h (WM 0726).
- Dungeon open time 20 → 15 min (WM [0402](https://steamcommunity.com/games/718790/announcements/detail/2383968106583377018)); with more than 2 users monsters respawn after 5 min (WM [0404](https://steamcommunity.com/games/718790/announcements/detail/2394101748794304355)). Dimensional Energy once cut to 2,000 gold (WM [0328](https://steamcommunity.com/games/718790/announcements/detail/2365953485470992984)).
- Since WM 0726, dungeon level is measured from the nation's **Main Fortress** (its highest-level fort).
- Safety factor (WM 0726): drops every 30 min in proportion to distance from the fort; at ≤30 there is an 80% chance per tick of monster invasion; below 0 the land is captured by monsters; clearing a field dungeon gives +5; legion-owned fields are exempt from the extra time-based reduction.
- Dragon Island (field 142) is reached only through a field dimension gate (WM [0920](https://steamcommunity.com/games/718790/announcements/detail/2450411965551395652)). "Mysterious World" border area via the fortress gate, tabs Death's Rest (Passion) and Sinking Nest (WM [0110](https://steamcommunity.com/games/718790/announcements/detail/2417771014047971842)); Sinking Nest changed to crystals/gemstones with a 3-hour limit (WM [0124](https://steamcommunity.com/games/718790/announcements/detail/2425653583381829617)). These are client fields 132/133.
- Scattered Troops and Avenue of Spirit open to both nations (WM [0412](https://steamcommunity.com/games/718790/announcements/detail/2394102381817542359)). Abyss: lower drop rate, kills don't count for the daily kill quest, 5 s immunity on moving, later a non-PK area (WM 0329/0404/[0511](https://steamcommunity.com/games/718790/announcements/detail/3822871998312896536)).
- CO bosses were summonable once per dungeon with a scroll from elite monsters (CO [1215](https://steamcommunity.com/games/475630/announcements/detail/4249665521684533034)); highest dungeon tier T8.

## Items

- Max tier rose to **T4+15** (WM 0920); runes **+9** from WM 0726 (+5 at launch, WM [0613](https://steamcommunity.com/games/718790/announcements/detail/2431262783620368792)).
- From WM 0412 a failed upgrade no longer destroys the item: it drops one level and materials are used; "Reinforcing Adjuvants" prevent the drop.
- Crystal cost per level and tier (WM [0420](https://steamcommunity.com/games/718790/announcements/detail/2758894130315567397), image table, after the patch): T1 Blue 20/30/40/60/80/100/120 then Yellow 20/30/40; T2 Yellow 20–80 then Red 20–80; T3 Red 30–80 then Black 20–120. The table has 10 rows (0–9), so these are almost certainly **rune** levels, not gear steps; before/after tables are in [[gameplay/reinforce-and-runes]] §2.
- Rune materials +1…+9 for T1–T3 and item crafting costs in Orange/Shining/Brilliant Passion (WM 0920, image tables); Brilliant Passion 5 silver or 1 gold medal. The rune table matches the client's `JewelSocketMake` exactly; both tables are transcribed in [[gameplay/reinforce-and-runes]].
- Rune caps at +9: Armor 45, MR 60, AP 60, AD 45, Mana regen 102 (WM 0412/0420). Runes take the PvP stat correction (WM [1107](https://steamcommunity.com/games/718790/announcements/detail/2423394805992652770)).
- Boss sets (Death Head, Skull, Fisher, Komodo, Spector, Garon, Fame Knight, Fame Warrior) with 3 bonus steps (WM [0809](https://steamcommunity.com/games/718790/announcements/detail/2454911758739952435)); essences for them drop from fort guardians.
- HP/MP regen tick 5 s → 1 s (WM 0420). Normal gear and T1 runes craftable with yellow jewels replacing missing materials (WM [0824](https://steamcommunity.com/games/718790/announcements/detail/2444779293804741322)). All gear can roll up to 3 sockets.
- CO crafting price by grade 1–7: 2,000 / 4,000 / 10,000 / 20,000 / 50,000 / 100,000 / 240,000 gold (archived forum, patch notes 2016-11-17).

## PvP, events, forts

- Schedule (server time), WM [0712](https://steamcommunity.com/games/718790/announcements/detail/2838841185432966428): War of Warmonger 02/08/14/20, Battle Arena 04/06/10/12/16/18/22/24, Holy Thing 07/19, Sunday 20:00 Civil War. WM 1107: War of Warmonger every 2 h except 06/18 (Battle Arena), Holy Things 07/19.
- War of Warmonger: up to 15 bots per side, nexus 70,560 HP (WM 1107). Battle Arena max 5 per team (WM [0719](https://steamcommunity.com/games/718790/announcements/detail/2412125660633804214)). Rewards: win 500 / lose 100 (+2 / +1 points), double medals (WM 0712). Fame: Gaia PvP win/lose 200/40, siege 1000/200; fame per gold/silver/bronze medal 1500/250/50.
- TP skill changes (WM [1018](https://steamcommunity.com/games/718790/announcements/detail/2403126706515770404)): Siege Minion 1000 TP cd 100→60 s, Fortified cd 180→120, Fire Support 2500→2000, I'll be back! 2000→1500, Blind/Portal/Freeze 2500→1500. Matches the client `Skill_TP`.
- Defenders get +100% medals in land battles (WM 0412); 3-minute protection after a won war (WM 0329); leaving a war early resets Lords of the Land and costs fame (WM 0426); "Gear Bonus" catch-up for weaker defenders up to T3+5.
- Forts: shields recover in 3 h with 1 h invulnerability after each loss (WM [0705](https://steamcommunity.com/games/718790/announcements/detail/2499943313680174373)); first-floor nexus HP 90,000, armor 540 (WM 0809); fort guardian drops for up to 15 killers (WM [0817](https://steamcommunity.com/games/718790/announcements/detail/2444779293764867295)).
- Shaia legion donations: 200,000 gold/day per player, 7 tiers 3M…45M unlocking cores (WM [1128](https://steamcommunity.com/games/718790/announcements/detail/2415515408464895311)). Shaia Blessing point pool (cap 10,000) boosting fame/medals/hunting (WM 0809/0817/1107).
- CO civil war: up to 15 v 15; holding a tower gave 8 TP per 10 s; a third nation could intrude on a war (archived forum). Nation King elected monthly (CO).

## Heroes

- Transformation cooldown 10 → 120 s (WM [0621](https://steamcommunity.com/games/718790/announcements/detail/2499943313629707204)); share of gear stats a hero gets: 35% at T1+0 up to 100% at T3+15 (WM [0628](https://steamcommunity.com/games/718790/announcements/detail/2499943313654890838)). Innocence Crystal: durability 1,500, drains 5/s while transformed (WM 1107).

## Economy and timeline

- Yellow jewels tradable 24 h after receipt; auction price of a yellow jewel fixed at 500 gold (WM [0503](https://steamcommunity.com/games/718790/announcements/detail/2394104285094559240)); mail 1,000 gold (WM 0404). Fame shop (WM 0712). Teleport by Haley 20 yellow jewels (WM 0110).
- Gacha pools by price (WM 1018): 1000 gear T1–3, 2000 weapon / innocence; daily gacha 5 → 10 rewards (WM 0726).
- Early Access 27 Mar 2018; launch wipe 14 Jun 2018 (WM [0605](https://steamcommunity.com/games/718790/announcements/detail/2396358622015638297)); closure announced 12 Mar 2019, servers off 1 Apr 2019 (WM [0312](https://steamcommunity.com/games/718790/announcements/detail/2530366080613548634)). Crush Online's Steam servers closed 1 May 2017 (CO [0301](https://steamcommunity.com/games/475630/announcements/detail/4249665521684531476)).

## Numbers pass (October 2026)

A second read of all 57 Warmonger and 30 Crush Online announcements (the CO feed lists each one twice) and every image in them. The tables and detailed values are in:

- [[gameplay/reinforce-and-runes]]: rune upgrade materials (0920, = client `JewelSocketMake`), older rune crystal tables (0420 before/after), rune caps and fail-rate notes, gear failure penalty, tier-up Orange/Brilliant Passion table (0920), boss-set bonuses (0809, = client `SetBounsItem`), consumable changes (elixirs/flasks 0124 = client buffs).
- [[gameplay/events-and-schedules]]: the 0712 and 1107 hour-by-hour schedules, match rewards and fame tables (0712, 0511), all weekend drop/medal events with dates, Double Event Field, fort/siege values, Fort Guardian drop list (0817), Shaia Blessing points (0809/1107), Shaia Legion donation tiers (1128), TP skill table (1018), gacha pools (1018), Crush Online ranks, prices and events.
- [[gameplay/classes-and-legions]] §5: weapon, hero and class balance numbers per patch, and the Skeleton King's Vision Bow (0110, = client skills 5491–5494).

Per-patch numbers not repeated in those pages:

- **0328**: Dimensional Energy price cut to 2,000 gold (later 5,000 base again in the client); character creation wait 24 h → 1 h; decomposition and premium scroll gold prices lowered.
- **0329**: tower and nexus attack/defence raised; tower range raised; NPC invasion chance raised; 3 repeatable Abyss quests at Athan; Abyss drop rate lowered; no item drops in the training ground.
- **0402**: party bonus and kills only count on the same map; hero durability 24 → 240.
- **0404**: weekly maintenance on Thursdays; cash top-up needs a minimum level; cash-mall items bind on pickup; Pyrotechnics sold for gold at Wren.
- **0511**: Abyss made non-PK; new characters get beginner helmet, armour, gloves and shoes; Legion Core battleground summon.
- **0615**: border-area unlock levels (0/20–27), see Dungeons above.
- **0726**: daily-quest panel shown automatically above Lv 27; more jewels and fame from daily quests; returning-player reward package.
- **0920**: monster drop chances on Gaia fields and in dungeons changed; boss-material drop rates from fort guardians and dungeon bosses raised; "cumulative fame" renamed **Contribution**.
- **1107**: Nation Support Fund now needs Gaia field battles; sieges add to it; daily/weekly/monthly Monster Area Wars quests also count War of Warmonger.
- **0110**: normal-rarity gear no longer bound (tradeable); repeatable quests moved to "Free Quests" on the quest board and mission quests to "War Quests" (Lv 30+). **0124** removed Free Quests from the board again.
- **0124**: daily Kill Player gives a little EXP and gold; mana-draining toggle skills keep draining at full mana.

## Other sources

- **guia-warmonger.blogspot.com** (Overdose, ES) — still online. It has **10 static pages and no posts** (the posts feed is empty): warmonger-espanol, como-empezar, dungeons, mejorar-tu-equipo, runas, alquimia, pvp-jcj, lista-armasarmaduras, links-oficiales, ayudanos-mejorar. All were read and their ~22 images viewed. New numbers: jungle mobs 1,500 TP each, tower 500 TP, 3-player dungeon respawn 5 min then every 1 min, Dimensional Energy 5,500 gold; its dungeon cost table is the same image as WM 0726. Its gear-list page only links to warwiki's *normal-gear* article.
- **warwiki.net** — dead and barely archived. The Wayback CDX for `warwiki.net/*` (and `www.`) lists about 70 captures: the homepage (2010–2018, the pre-2018 ones are an unrelated WordPress site), `/feed/`, `/comments/feed/` (empty) and theme files. **None of the ~35 article pages** (normal-gear, superior-gear, rare-gear, each slot, each weapon type, the three rune pages, upgrading/crafting, dungeons, fortress-management …) and none of the uploaded images were captured; all return 404 from the archive (checked Oct 2026). The only text left is the RSS feed (`https://web.archive.org/web/20181117140931/http://warwiki.net/feed/`, 10 items dated 22–30 Jul 2018), of which three have bodies: Currency, Maps and Farming Mechanics, Customising the Game. Their numbers are already in the wiki: Avenue of Spirit and Scattered Troops 3 bronze Time Energy + 5 Dimensional Energy, Gollam/Siren/Nas 10; safety −5 per abandoned war; respawn after 9 min in a party.
- **Archived CO forum** — `https://web.archive.org/web/2016*/http://www.crush-game.com/forum/threads/*` (about 370 threads: patch notes, dungeon/boss lists, legions and forts, civil war, VIP).
- **Steam discussions** — `https://steamcommunity.com/app/718790/discussions/` (440 topics, General only).
- CO artifact EP/stat sheet (Google Sheets): https://docs.google.com/spreadsheets/d/1nDMzbRY59x-ZcVXyQ22yrkPLDhwprgPD7AVJpirYWUY
- Nothing usable on namu.wiki, Reddit, fandom, mmorpg.com or mmobomb; warmonger-game.com was not archived.
