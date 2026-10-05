---
title: "Dungeon drops (ores and herbs)"
---

# Dungeon drops (ores and herbs)

For each border-area dungeon level: its name, the client field id, the boss with its `UnitDB` ids, the ore/herb materials with their `Item_Base` codes, and what the client's dungeon window advertises. The base is the **Ore/Herb** tab of the player spreadsheet **Crush Share** ([gid 504563500][t-ore]), checked against the client tables (`FieldNames`, `UnitDB`, `Item_Base`, `DungeonAdmission`, `ObjectList`). Tags: *sheet*, *guide*, *client*, *guess*. Dungeon layouts, entry costs, respawn and gear drops are in [[gameplay/maps-and-dungeons|Maps and dungeons]].

> [!note]
> The Ore/Herb tab is word for word the "Dungeons" section of the Steam guide [Crush Online basics][g-crush] (Agouha, 2016). It is **Crush Online era**. The ore/herb lists also agree with the 2018 Warmonger [dungeons guide][g-dng], so the materials did not change. What did change is the **level number of Ghost Fortress and Tow Canyon** (§2). The Lv 3 row of the tab also carries an unrelated chat note ("WTS Silver medal / EoD"). It is not data.

## 1. Per dungeon level

| Sheet Lv | Sheet name → client field (`FieldNames`) | Boss in sheet → `UnitDB` ids | Ores / herbs in sheet (`Item_Base` code) | Client "rewards" icons (`DungeonAdmission`) |
|---|---|---|---|---|
| 1 | Temple of the Skull → **121** "[Lv 1] Skull Temple" | Deathhead → King Deathhead **672**; Tough King Deathhead 804; 1501 | Garnet **802**, Red Bloodstone **812** | Blue Passion Frag [D] 601, Gem Stone: Blue 693, Essence of Darkness 1930, DeathHead Horn 2701, Death Head's Sealed Weapon 2751 |
| 1 | Chepa Village → **127** "[Lv 1] Chepa Village" | Chepa Sorcerer → **870** / 950 | Lavender **818**, Peppermint **820** | Red Passion Frag [D] 611, 601, 693, Essence of Wind 1931, Drop of Chepa Sorcerer 2709, Chepa Sorcerer's Sealed Weapon 2759 |
| 2 | Cemetery of the Skull → **128** "[Lv 2] Skull Cemetery" | Death Knight → Dark Knight Skull **673**; 809, 1205, 1504 | Topaz **814**, Blue Bloodstone **804**, Rosemary **822**, Jasmine **824** | 611, 693, Essence of Darkness 1930, Skull Horn 2702, Dark Knight's Sealed Weapon 2752 |
| 3 | Lake of the tsunami → **122** "[Lv 3] Tsunami Lake" | Tempest Fisher → **674**; 733, 1209 | Topaz 814, Blue Bloodstone 804, Rosemary 822, Jasmine 824 | Red Passion Piece [D] 612, Blue Passion Piece [D] 602, 693, Essence of Water 1933, Fin of Fisher 2703, Tempest Fisher's Sealed Weapon 2753 |
| 4 | Swamps of the Snake Warrior → **123** "[Lv 4] Swamps of Snake Warrior" | Slayer Komodo → **675**; 736, 1213 | Onyx **816**, Borage **826**, Spartium **828** | 612, 602, 693, Essence of Fire 1932, Horn of Komodo 2704, Slayer Komodo's Sealed Weapon 2754 |
| 5 *(client: 6)* | Fortress of Ghost → **124** "[Lv 6] Ghost Fortress" | Great Summoner Spectre → **676**; 743, 1218 | Moonstone **808**, Lavender 818, Peppermint 820 | 612, 693, Gem Stone: Yellow 694, Essence of Earth 1934, Bone of Spector 2705, Wizard Spector's Sealed Weapon 2755 |
| 6 *(client: 5)* | Canyon of Tow → **125** "[Lv 5] Tow Canyon" | War chief Garon → War Chief Garon **677**; 822, 1223 | Emerald **806**, Rosemary 822, Jasmine 824 | 602, 693, Essence of Light 1935, Horn of Garon 2706, War hammer Garon's Sealed Weapon 2756 |
| 7 | Hell of Demon → **126** "[Lv 7] Demon Hell" | Akasha/Reviathan → Reviatan Shadow **678** / 740, Commander Reviatan 739, Reviatan 972 | Diamond **810**, Borage 826, Spartium 828 | 612, Red Passion Frag [C] 613, 693, 694, Essence of Light 1935, Horn of Leviathan 2707, Devil commander Leviathan's Sealed Weapon 2757 |
| 8 | Thorns Hell → **129** "[Lv 8] Thorn's Hell" | Akasha/Reviathan → Akasha **849** | Emerald 806, Rosemary 822, Jasmine 824 | 602, Blue Passion Frag [C] 603, 693, 694, Gem Stone: Red 695, Essence of Fire 1932, Horn of Akasha 2708, Arch devil Akasha's Sealed Weapon 2758 |
| – *(client: 9)* | not in sheet → **142** "[Lv 9] Dragon Island" | ? | ? | 613, 603, 694, 695, Essences 1930–1935 (all six) |

Sources: sheet columns *sheet* ([Ore/Herb][t-ore]). Field names, unit ids and item codes *client*. The `DungeonAdmission` icon list is what the dungeon-entry window *shows* as possible rewards. It is not a drop table and has no rates (rates are server-side). *client*

- "Akasha/Reviathan" is listed for both Lv 7 and Lv 8 in the sheet. The client splits them: Demon Hell's rewards show the **Leviathan** horn and weapon, Thorn's Hell's show **Akasha**'s. *client*
- "Death Knight" (sheet) is "Dark Knight Skull" in the client. The client's sealed weapon is also "Dark Knight". *client*
- Each boss's **Essence** matches the Crush forum: "Essence of Darkness just drops from the Tier 1 dungeon boss" ([Crush forum][f-secrets] post 1) fits Skull Temple / Skull Cemetery showing 1930. *guide + client*
- Amounts per run (e.g. Garnet ×4) are not in the sheet. The 2018 guide's counts are in [[gameplay/maps-and-dungeons|Maps and dungeons]] §2. *guide*

## 2. Where the sheet disagrees with the client

| Point | Sheet (Crush 2016) | Client (Warmonger final) | Use |
|---|---|---|---|
| Level of Fortress of Ghost / Canyon of Tow | Ghost = Lv 5, Tow = Lv 6 | `FieldNames` 124 "[Lv 6] Ghost Fortress", 125 "[Lv 5] Tow Canyon". `Dungeon.tsv` order …123, **125, 124**, 126…. `DungeonAdmission` entry cost 125 = 7/9, 124 = 8/12 | client |
| Dragon Island (Lv 9) | absent | field 142, cost 10 / 23 Dimensional Energy | client |
| Boss names | Deathhead, Death Knight, Akasha/Reviathan | King Deathhead, Dark Knight Skull, Reviatan (Lv 7) / Akasha (Lv 8) | client |

The 2018 [dungeons guide][g-dng] already uses the client's order (Tow 5, Ghost 6). *guide*

## 3. The materials

The 14 ore/herb materials, their alchemy powder (Owen grinds 10 per craft, see [[gameplay/items-and-crafting|Items and crafting]] §4), NPC sell price and the gathering-node model. All *client* (`Item_Base` sell_price, currency 2 = gold; `ObjectList` gathering models). Dungeons are from the sheet.

| Material | Code | Powder | Sell (gold) | Gather node model (`ObjectList`) | Dungeons (sheet Lv) |
|---|---:|---:|---:|---|---|
| Garnet | 802 | 803 | 20 | 1085 Mineral_Garnett | 1 Skull Temple |
| Blue bloodstone | 804 | 805 (Bloodstone powder) | 20 | 1081 Mineral_Bloodstone_Blue | 2, 3 |
| Emerald | 806 | 807 | 40 | 1084 Mineral_Emerald | 6 Tow, 8 Thorns |
| Moonstone | 808 | 809 | 30 | 1086 Mineral_Moonstone | 5 Ghost |
| Diamond | 810 | 811 | 40 | 1083 Mineral_Diamond | 7 Demon |
| Red bloodstone | 812 | 813 | 20 | 1082 Mineral_Bloodstone_Red | 1 Skull Temple |
| Topaz | 814 | 815 | 30 | 1088 Mineral_Topaz | 2, 3 |
| Onyx | 816 | 817 | 30 | 1087 Mineral_Onyx | 4 Swamps |
| Lavender | 818 | 819 | 30 | 3013 Flower_Lavender | 1 Chepa, 5 Ghost |
| Peppermint | 820 | 821 | 30 | 3015 Flower_Peppermint | 1 Chepa, 5 Ghost |
| Rosemary | 822 | 823 | 20 | ? | 2, 3, 6, 8 |
| Jasmine | 824 | 825 | 20 | ? | 2, 3, 6, 8 |
| Borage | 826 | 827 | 10 | ? | 4, 7 |
| Spartium | 828 | 829 | 10 | ? | 4, 7 |

- The client has four more flower models (3011 Anika, 3012 FireFlower, 3014 MoonFlower, 3016 Whisper). They probably stand for Rosemary, Jasmine, Borage and Spartium, which have no model of their own. *guess*
- Minerals sit on the **blue diamond** minimap icons and herbs on the **green leaf** icons inside each dungeon ([[gameplay/maps-and-dungeons|Maps and dungeons]] §2, *image*). The node positions inside each dungeon map are not recovered yet. They should be in the dungeon map files (`data/map`). *guess*

[t-ore]: https://docs.google.com/spreadsheets/d/1nDMzbRY59x-ZcVXyQ22yrkPLDhwprgPD7AVJpirYWUY/edit#gid=504563500
[g-crush]: https://steamcommunity.com/sharedfiles/filedetails/?id=780459080
[g-dng]: https://steamcommunity.com/sharedfiles/filedetails/?id=1344219430
[f-secrets]: https://web.archive.org/web/20161206171243/http://www.crush-game.com:80/forum/threads/secrets-of-gearing-up-lets-get-strong.680/
