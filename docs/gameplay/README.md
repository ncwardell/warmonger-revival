---
title: "Gameplay"
---

# Gameplay

What Warmonger was like to play, collected from player guides and other sources and matched to the client's own ids where possible. Every fact cites its source and says how sure we are (*client*, *guide*, *guides*, *image*, *guess*). Add what you know — see [[wiki-style]].

## Pages

- [[gameplay/sources|Sources and gaps]] — every source found (sheets, archives, screenshots, videos) and the numbers still missing
- [[gameplay/maps-and-dungeons|Maps and dungeons]] — Gaia, nations' lands, dungeon tiers, bosses and drops
- [[gameplay/classes-and-legions|Classes, nations and legions]]
- [[gameplay/items-and-crafting|Items and crafting]] — materials, upgrades, gear sources
- [[gameplay/progression-and-economy|Progression and economy]] — levels, quests, currencies
- [[gameplay/pvp-and-matches|PvP and matches]] — land wars, forts, matches
- [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]] — rune and tier-up material tables, caps, fail rules, set bonuses
- [[gameplay/events-and-schedules|Events, schedules and PvP rewards]] — hourly schedules, fame/medal rewards, weekend events, forts, Shaia, gacha pools
- [[gameplay/patch-history|Patch notes and other sources]] — official announcements 2016–19, blog, archived wiki and forum
- [[gameplay/server-rules|Server rules checklist]] — concrete rules a server must implement, with sources
- [[gameplay/crush-patch-notes|Crush Online patch notes]], [[gameplay/crush-mechanics|Crush Online mechanics]] — the original game's forum, Oct 2016 – Mar 2017, with Crush vs Warmonger differences
- [[gameplay/npc-locations|NPC and point-of-interest locations]] — where the server must place town NPCs, portals, quest NPCs and gathering nodes, per map
- [[gameplay/consumables|Consumables and clickables]] — potions, scrolls, elixirs and their recipes, buff values and durations
- [[gameplay/video-tutorial-walkthrough|Video notes: the tutorial]] — all 32 tutorial steps with quest ids, NPC positions and rewards; new characters start in Training Ground (field 89)
- [[gameplay/video-character-creation-and-tutorial|Video notes: character creation]] — classes, appearance options, starting weapons and skills, starting stats, the tutorial after the June 2018 relaunch
- [[gameplay/videos|Videos]] — 86 gameplay videos by topic, with timestamps; start here for the tutorial
- [[gameplay/gear-stats|Gear stats]], [[gameplay/dungeon-drops|Dungeon drops]], [[gameplay/stat-values|Stat values]] — from the Crush Share player spreadsheet
- [[gameplay/abyss-map|Abyss map and portals]], [[gameplay/lords-of-the-land|Lords of the Land]], [[gameplay/skull-artifact-set|Skull artifact set]], [[gameplay/potion-regen|Potion regeneration]], [[gameplay/arena-ranking-rewards|Arena ranking rewards]], [[gameplay/precept-shop|Precept shop]] — from player screenshots

## Sources

Steam guides for Warmonger (app 718790) and Crush Online (app 475630):

| Guide | Language | Covers |
|---|---|---|
| [Definitive Guide for Warmonger](https://steamcommunity.com/sharedfiles/filedetails/?id=1459948573) | EN | most systems |
| [Guía definitiva de Warmonger](https://steamcommunity.com/sharedfiles/filedetails/?id=1459898274) | ES | Spanish edition of the above |
| [How to Warmonger.... a Strategy Guide](https://steamcommunity.com/sharedfiles/filedetails/?id=1460486971) | EN | strategy, farming, world map |
| [A Noob's Guide to Warmonger by Punisher](https://steamcommunity.com/sharedfiles/filedetails/?id=1345368744) | EN | progression, dungeons |
| [Dungeons: Bosses, Materials and Gear drop](https://steamcommunity.com/sharedfiles/filedetails/?id=1344219430) | EN | dungeons, bosses, drops |
| [Using the crafting materials to your advantage](https://steamcommunity.com/sharedfiles/filedetails/?id=1354427871) | EN | crafting materials, buffs |
| [TIPs: Como y donde conseguir tu equipo](https://steamcommunity.com/sharedfiles/filedetails/?id=1431688611) | ES | where to get gear |
| [TIPs 2: Como mejorar armas y equipo](https://steamcommunity.com/sharedfiles/filedetails/?id=1431875497) | ES | upgrades, special dungeons |
| [WARMONGER REHBER](https://steamcommunity.com/sharedfiles/filedetails/?id=1460533609) | TR | general, forts and dungeon tiers |
| [Guia Básico - Warmonger](https://steamcommunity.com/sharedfiles/filedetails/?id=1544645226) | PT-BR | classes, legions |
| [Crush Online basics](https://steamcommunity.com/sharedfiles/filedetails/?id=780459080) | EN | wars, conquering lands |
| [All The Additional Effect Stats](https://steamcommunity.com/sharedfiles/filedetails/?id=814958862) | EN | Crush Online random item add-on stats, old shop prices |

Authors, in table order: Zombids (from Overdose's blog guia-warmonger.blogspot.com), Zombids, corentyn1 ("Dracoco"), Kayne, InDeed, fissehans, Zombids, Zombids, boboboom.d, Baylor, Agouha, Made In Heaven. The guide listings for both apps hold only these twelve (page 2 of the 718790 list repeats page 1).

All ~250 screenshots in these guides were viewed (world maps, dungeon minimaps, boss and loot screens, shop, crafting, reinforce, rune, quest, gacha, auction and nation-info windows). Their contents are described in our own words in the topic pages; none are copied here. The guide comment threads were read too (the dungeon guide's comments add facts on sockets and craft-only sets).

Client tables used for cross-checks: `FieldNames`, `Dungeon`, `DungeonAdmission`, `Event_Dungeon`, `UnitDB`, `Item_Base`, `Item_Make`, `Skill_TP`, `FortMastery`, `Level_Table` (all in `data/tables/`).

## Other sources (numbers pass, Oct 2026)

| Source | What was used | Pages |
|---|---|---|
| Steam announcements, Warmonger (app 718790): [list](https://steamcommunity.com/games/718790/announcements), full text via `https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=718790&count=300&maxlength=0` | all 57 announcements (Feb 2018 – Mar 2019), the same set as the [Steam news hub](https://store.steampowered.com/news/app/718790) | [[gameplay/patch-history]], [[gameplay/reinforce-and-runes]], [[gameplay/events-and-schedules]], [[gameplay/classes-and-legions]] |
| Steam announcements, Crush Online (app 475630): [list](https://steamcommunity.com/games/475630/announcements) | 30 announcements (each listed twice in the feed), Jun 2016 – Mar 2017 | [[gameplay/events-and-schedules]] §11 |
| Images in those announcements | 108 image links, 44 distinct. The 29 that carry content were viewed: every table, screenshot and the three table images linked as plain URLs in the 0712, 0920 and 1107 notes. The rest are repeated header banners and small skill or item icons. Data tables transcribed: rune crystals (0420 ×2), schedules (0712, 1107), match/fame/medal rewards (0712 ×3), dungeon entry (0726), Time Energy buffs (0726), Shaia tiers (0809), Fort Guardian drops (0817), tier-up passions (0920), rune materials (0920), TP skills (1018), gacha pools (1018), Shaia Legion tiers (1128), Vision Bow and Mysterious World screens (0110) | [[gameplay/reinforce-and-runes]], [[gameplay/events-and-schedules]] |
| [guia-warmonger.blogspot.com](https://guia-warmonger.blogspot.com/p/como-empezar.html) (Overdose, ES) | all 10 pages (the blog has no posts) and their ~22 images | [[gameplay/events-and-schedules]], [[gameplay/reinforce-and-runes]] |
| warwiki.net via the Wayback Machine | CDX listing; only the homepage and RSS feed were ever archived (3 article bodies). The ~35 gear/weapon/rune articles and all uploaded images were never captured | see [[gameplay/patch-history]] §Other sources |

Client cross-checks in this pass: `JewelSocketMake` (rune costs, exact match), `Item_Jewel` (rune values, differ), `SetBounsItem` (set bonuses, match), `Skill_Buff` (consumables, match), `Skill_Base` (Vision Bow, match; some 2018 cooldown changes missing), `Skill_TP`, `DungeonAdmission`, `ItemSancMet`, `Item_Base` prices.

## Dead or unreachable sources

- **warwiki.net**: the community gear database the definitive guide linked for full T3+15 stats. Its article pages are not in the Wayback Machine (only its feed and homepage are; see above).
- The Google Doc "Overview of clickables" linked from the buffs guide (crafting recipes for consumables).

## Worth a human look

- The world-map screenshots in the [strategy guide](https://steamcommunity.com/sharedfiles/filedetails/?id=1460486971) and the [noob guide](https://steamcommunity.com/sharedfiles/filedetails/?id=1345368744): they show every land name, owner and dungeon tier icon at one moment in 2018, which could seed the initial land ownership.
- The dungeon minimaps in the [dungeons guide](https://steamcommunity.com/sharedfiles/filedetails/?id=1344219430) next to the client's `minimap_z<id>` textures, to place spawns, gather nodes and bosses.
- The "First steps video lvl 1–17" linked from the [definitive guide](https://steamcommunity.com/sharedfiles/filedetails/?id=1459948573) §First Steps (the tutorial and early quest flow).
- **Videos** (YouTube ids; we cannot watch them):
  - fort war: ZonderCoRe 6_z6CUpZj30 (hero form), JPd7TCu-44o (core room); Dackmen E5rqHNAFaz8, BcbszKkUbbQ (nexus boss), iyMgWsBYOxc (legion war)
  - 15 v 15 battles: Dackmen NCHwg0oQVbg, LTZm_Hb3mNA; Guardian mass PvP: VhHADbLm7HE, JngxzCCUc9Q, kU2RuzoNOnc
  - dungeons and farming: Nas Village run eL5hx5C9iZw; AFK Red Passion farm onNr7IVnDu8; rune to +7 dpofIAFX2wM; rush-map conquest JcKtjYFPFfw
  - long sessions: s04CSN16w1s (2.5 h), IQI0yh1S0-Y, CqCY2ULeVGw, cqYz3j59MFI; Spanish basics awKR2rF-3nM, q5lJoBiDwfY
  - Crush Online era: 2umwpYlKAvg (fort battle, guardian boss, lands), yAK2gjqTCrk (tutorial)
- Patch-note table images: transcribed in [[gameplay/reinforce-and-runes]] and [[gameplay/events-and-schedules]]. Two cells are unclear: the 0920 tier-up table has a count of 1 with no item named (2T normal weapon and 2T superior gear rows), and the fifth Shaia Legion core name in 1128 is cut off ("…attlefield summone…").
