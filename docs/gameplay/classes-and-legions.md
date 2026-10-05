---
title: "Classes, nations and legions"
---

# Classes, nations and legions

From the player guides listed in [[gameplay/README|Gameplay]], checked against client tables where possible. Tags: **client**, **guide(s)**, **image**, **guess**.

## 1. Classes

Three classes. Each carries **two weapons** and swaps between them (Space = weapon change, X = transform); the **weapon decides the skills** (4 skills per weapon: Q W E R). *guides + image* [definitive guide][g-def] §Classes, [noob guide][g-noob] key settings screenshot. Client: `WeaponBase` gives each weapon 4 normal + 4 hero skill ids (see [[spec/skills]]).

| Class | Weapons | Role | Difficulty shown at creation |
|---|---|---|---|
| **Punisher** | Daggers, Bows | Physical (AD) damage dealer; best tower/nexus damage; stealth skills; low defence | Low |
| **Saint** | Flying Blades, Dual Guns, Wands | Mage (AP); the only class with heals (also on allies); lots of area damage; slowest; AP Saints are weak against towers, AD Saint (guns) possible | High |
| **Guardian** | Maces, Cannons | Tank; most crowd control (stuns); can also deal AD or AP damage | Middle (in-game); "Low" in the Turkish guide |

Sources: [Turkish guide][g-tr] §Sınıflar (weapon lists), [definitive guide][g-def] §Classes, [strategy guide][g-strat] §Classes, [PT-BR guide][g-ptbr] §Classes; creation screen *image* in [strategy guide][g-strat] (each class shows a radar of Attack / Ability Power / Magic Resist / Movement Speed / Attack Speed / Armor).

- The first weapon is chosen at creation; later crafted weapons of the same family have **the same stats, only different skills** at the same tier. *guide* [definitive guide][g-def] §Choosing Weapons. (Contradicted in part by item screenshots, where "Magical" weapons have small stat differences; treat as approximate.)
- Weapon families seen in crafting lists: Punisher — Magical Frost/Shadow/Sniping/Vision Bow, Magical Judge/Blood/Hiding Dagger, Skeleton King's Magic Dagger (superior); Saint — Magical Crystal Wand, Skeleton King's Magic Gun; Guardian — Magical Demolition/Dash/Crush/Protect Hammer, Skeleton King's Magic Hammer/Cannon. *image + client (Item_Base 20001–21020)*.
- Two damage types plus true damage: AD (Attack) is resisted by Armor, AP (Ability Power) by Magic Resist. *guide* [strategy guide][g-strat].
- Character sheet of a level-30 Punisher in T3+15 gear (*image*, [strategy guide][g-strat]): HP 9,817 (regen 34), MP 1,051 (regen 8), Attack 2,826, AP 67, Armor 863, MR 721, Armor Pen 32/3%, Life Steal 15%, Crit Damage 100%, Crit Chance 5.0%, Attack Speed 665, Movement Speed 680; other stats on the sheet: Magic Pen, Spell Vamp, Reduced Critical Damage, Reduced Area Damage, Toughness, Cooldown Reduction. The sheet also shows **Nation, Legion, Rank (e.g. "Officer [5]"), Fame (81,500 of 107,110) and "Warmonger" points (24 P)**.
- Hero transformation: a hero ("transform") is unlocked from gacha **hero pieces** and is usable only at **max level 30**. *guides* [Turkish guide][g-tr] §Gacha, [definitive guide][g-def] §Tip. Client: `HeroData` (22 heroes, 10 skills each).

## 2. Nations

- Three nations: **Arslan (red)**, **Erion (blue)**, **Armia (green)**. In 2018 Armia was **disabled** — not selectable, 0 lands, 0 forts. *guides* [definitive guide][g-def] §How to start, [PT-BR guide][g-ptbr]; *image* Nation Information panel.
- The nation is chosen **per account**: all characters on the account share it (to stop spying). It can be changed later at the castle, which moves the whole account. *guides* [noob guide][g-noob] §Getting started, [strategy guide][g-strat] §Classes.
- Nation choice "makes no difference" except through which fort masteries your nation has unlocked. *guide* [definitive guide][g-def].
- The Nation Information panel shows: a notice board (editable — "Change" button), total nation power bar (lands and forts per nation), channel information (each fort: owner legion, land, mastery levels in six categories, cores installed), a **Legion Rank** table (rank, legion, fame, weekly reward estimate) and a **"Next Council: N days"** countdown. *image* [strategy guide][g-strat]. Client: nation `Policy` / `PolicyActive` tables exist server-side only (3 levels of value/cost) — the council probably elects who sets policies (*guess*).
- Legion reward estimates in that screenshot fall in bands: rank 1 ≈ 7.68 M, rank 2 ≈ 6.14 M, ranks 3–9 ≈ 2.05 M, 10–14 ≈ 1.02 M, 15–19 ≈ 0.51 M (gold, presumably). *image* — so rewards are paid by rank bracket, not linearly by fame.

## 3. Legions (guilds)

All from the [Turkish guide][g-tr] §Lejyon Yönetimi unless marked (that section reads as a translation of an official FAQ):

- **Legion fame / EXP** comes from clearing monster invasions (purple skulls), taking neutral PvE lands, and defending/attacking the other nation. More legion members on the same map → more fame, up to a cap.
- **Level up** is manual: when the legion has enough EXP, the leader presses Level Up in the admin tab, which also costs **legion gold**. Client: `Level_Table_Guild` (10 levels), `GuildMastery` (14 entries), `GuildMissionReward`.
- **Legion gold** pays wages, levelling, legion warehouse expansion, and Civil War bids.
- **Ether**: owning a land produces ether automatically over time; **1 ether sells for 700 legion gold**. Buying ether has no real use.
- **Owning a land**: build a **War Nexus** for **500 legion fame** (needs permission set in G → Admin → Authority). A legion that owns a fort can also place a **Reinforced Nexus, Amplification Ether, Twisted Dimension or No-Entrance core** on an unowned land.
- **Wages**: part of legion gold is paid out **every Saturday 04:00**; the total depends on legion gold + ether.
- Legion warehouse via the legion NPC. *guide* [noob guide][g-noob].
- A "Join & Create Legion" quest (return to Kesley) exists. *image* [noob guide][g-noob].

## 4. Forts (castles)

From the [Turkish guide][g-tr] §Kale Yönetimi unless marked:

- **Getting a fort**: win a **Civil War** or obtain a **Grabie Fragment** from the Holy Gift event.
- **Civil War**: every **Sunday 20:00**. Legions of the **same nation** fight for a fort. Registration is a **bid of legion gold on Saturday 00:00–23:59**; the highest bidder becomes that fort's **Challenger**. The fight is a normal PvP battlefield inside the fort (destroy the enemy nexus); members must be **inside that fort at 20:00** because they are summoned only once. Applies to both attacker and defender.
- **Fort level / EXP**: from **tax collection or donations**. The EXP gauge has **7 bars**. Any player can donate (convert their own gold to fort EXP) at **Hadrian** (top-left of the fort). When the bar is full, levelling also costs gold from the fort's **tax treasury** (usually **10 M or 20 M**); legion or player gold cannot be used. Client `FortMastery` costs are 10 M / 20 M / 50 M per mastery, matching.
- **Mastery points**: each fort level gives one mastery point. Masteries improve that fort's NPCs and are usable **by everyone in the nation**. Unlocking costs tax-treasury gold.
- Client fort mastery tree (`FortMastery.tsv`, *client*), six categories that match the six icons on the fort panel (Weapon, Gear, Rune, Fort & Core, Alchemy, Util): Weapon → Superior Weapon → Rare Weapon, Red Passion ×2; Gear → Superior Gear → Rare Gear, Blue Passion ×2; Rune → 2 Tier Rune → 3 Tier Rune, Orange Passion ×2; Fort & Core → Magic Core → Addon Core, Fort Shield → Shield maintenance → Shorten shield creation time; Alchemy → A Grade → S Grade; Util → Training Officer → Teleporter; Legion House.
- Crafting in a fort is limited by its mastery: mastery 1 = base weapons, 2 = "advanced" weapons, 3 = superior (green) weapons; the same applies to runes (tier), gear, passion conversion, potions/flasks/scrolls/elixirs and cores. Players travel to the fort with the mastery they need. *guide + image* [strategy guide][g-strat] §How to craft.
- **Taxes**: collectable **Sundays 21:00–23:59**, converted to legion gold. Forts also take a small cut of every NPC sale/service in them. Advice: don't collect until the fort is Lv 4+, since donations alone level it. Because of that cut, players topped up a poor treasury on purpose by buying expensive decomposition hammers from the fort's NPC and selling them back, again and again. *guide*.
- **Losing a fort**: enemies siege it. Killing the guardian **Crusader Cherubim** inside (UnitDB 825) removes **one fort shield** and distributes part of the fort's taxes to the winners. The fort falls when all shields are gone. Default **max 3 shields**, raised by the Fort & Core sub-mastery. Shields regenerate periodically (interval unknown).
- **Fort siege** (from the [strategy guide][g-strat] §How to War): floor 1 — capture **6 cores** and kill the **Heart of Magic** (stops the boss's health regeneration; it respawns); the nexus there is weak and its shield cannot be restored. Floor 2 — a very strong boss that needs **heroes** (transformations) to kill. Client fields 130 *Room of Core* and 131 *Room of the Fortress Keeper* fit the two floors (*guess*).
- Possibly **max 2 forts per nation** (unconfirmed by staff). *guide*.

### Holy Gift event

- **Monday–Saturday, 07:00 and 19:00**: a blue triforce appears on a random land. After **90 minutes** (sometimes extended), the legion that owns that land gets the reward; any nation can win it. *guide* [Turkish guide][g-tr] §2.6.
- Possible rewards (§2.7):
  - **Grabie Fragment** — builds a fort on that land (no fort needed to claim).
  - **Frey Fragment** — **+5% max MP** for the whole nation; claimable only by a fort-owning legion; stacks with other forts.
  - **Ru Fragment** — **+5% max HP**, same rules.
  - **Innus's Fragment** — lets a fort move up to **2 cells**; each move costs **10 durability** and drops the fort's current shields; fort-owning legions only.
- Client: `Item_Base` kind 37 = *Holy Things*, kind 39 = *Establish Fort*, kind 60 = *Legion Core*. *client*.
- Patch changes: from [WM 1107][wm1107] the Holy Thing appears on **one** land only, and getting the same core again raises the tier of the Holy Thing item. [WM 0830][wm0830] and [WM 0110][wm0110] changed where its fort is placed; the first placement has a small random factor. *notes*

## 5. Balance numbers from the patch notes

Weapon, hero and class values changed in the official patch notes, in date order. Multipliers are percent of AD/AP. Cross-checked against client `Skill_Base` (cooldown_ms, cost) where the skill could be found. Tags: *notes*, *client*. More system numbers are in [[gameplay/reinforce-and-runes]] and [[gameplay/events-and-schedules]].

### Classes

- Magic Resist gained per level ([WM 0420][wm0420]): **Punisher +3 (90 at Lv 30), Saint +4 (120), Guardian +6 (150)**. *notes*
- HP/MP regeneration ticks every **1 s** (was 5 s); item regen values were rescaled so total output stayed the same ([WM 0420][wm0420]). *notes*
- The Armor/MR penetration formula was changed to make penetration stronger ([WM 0412][wm0412]); exact formula not given. *notes*

### Weapons

| Patch | Weapon (client item) | Change |
|---|---|---|
| [0329][wm0329] / [0402][wm0402] | Magical Dash Blade, Magical Wrath Blade | Q/W (Dash) and Q/E (Wrath) scaling AD → AP |
| [0412][wm0412] | Magical Life Wand (10002) | R range 8 → 6, recovery 6 → 5 |
| [0412][wm0412] | Magical Storm Wand | E AP multiplier 20 → 40 |
| [0412][wm0412] | Magical Crystal Wand | W bonus attack and move speed 13% → 15%; E armor/MR buff and debuff 10% → 20%; R slow 2 → 4 s |
| [0412][wm0412] | Magical Dash Blade, Magical Wrath Blade | per-level growth AP 2 → 8, AD 8 → 2 |
| [0412][wm0412] | Magical Thunder Wand (10001) | Q AP base 70 → 80; W 90 → 100; "E" cooldown 70 → 60 s (in the client the 60 s skill is the R, *Might of Thunder God*, skill 5007) |
| [0420][wm0420] | Magical Life Wand | W AP 80 → 60; E AP 90 → 60 |
| [0420][wm0420] | Magical Wrath Blade | E AP 120 → 100; R AP 120 → 100, HP multiplier 30 → 20 |
| [0420][wm0420] | Magical Devil Wand (10020) | R cooldown 70 → 60 s, AP 70 → 100 (the client still has *Dark Matter* at 70 s) |
| [0420][wm0420] | Magical Hiding Dagger (15008) | Q cooldown 15 → 19 s, W 20 → 25 s (client: *Backstab* 20 s, *Deception* 25 s) |
| [0426][wm0426] | Magical Wrath Blade | R base damage no longer scales with AP |
| [0426][wm0426] | Magical Judge Dagger | E armor/MR debuff 10% → 20% |
| [0426][wm0426] | Magical Blood Dagger | E gives +100 attack speed for 5 s |
| [0712][wm0712] | Skeleton King's Magic Dagger | E AP → AD; R silence 2 → 3 s |
| [0712][wm0712] | Magical Devil Wand | E cooldown 22 → 15 s (the client has both: *Hush* 5178 at 22 s and 5472 at 15 s) |
| [0712][wm0712] | Skeleton King's Magic Cannon | Q and R AP → AD + AP; per-level growth AD +10 → +8 and AP +2 |
| [0719][wm0719] | Wrath Blade | E max multiplier at T3 1.2 → 0.8 AP |
| [0830][wm0830] | Magical Protect Mace | damage up to ×5 per basic attack |
| [0124][wm0124] | Magical Demolition Hammer | Q *Soul Infestation*: basic attacks deal 10 + 60% AP + 75% AD magic damage (bonus AD 100% → 75%, AP 30% → 60%), hits several targets |

**Skeleton King's Vision Bow** (superior Punisher bow, item 15005; [WM 0110][wm0110] text + image 2): Attack +140, AP +10, range 750 at T1+0. Skills *notes*, matching client skills 5491–5494 exactly *client*:

| Key | Skill | Cooldown | Mana | Effect |
|---|---|---|---|---|
| Q | Mystic Arrow | 5 s | 75 | 85 + 0.8 AD + 0.625 AP; on hit, attack speed up for 6 s |
| W | Vision Explosion | 17 s | 95 | 85 + 0.83 AD + 0.6875 AP around you, plus more per Vision stack used (stacks from basic attacks, max 10, last 7 s) |
| E | Vision Move | 15 s | 125 | teleport to target point |
| R | Essence Wave | 55 s | 330 | 120 + 1.0 AD + 0.875 AP to all hit; +1 Vision stack per enemy hit |

### Heroes

| Patch | Hero | Change |
|---|---|---|
| [0412][wm0412] | Artamos | crit chance 10% → 5% |
| [0412][wm0412] | Sarasbati | HP → AD conversion 10% → 5% |
| [0412][wm0412], [0420][wm0420] | Amaterasu | MP → AP conversion 10% → 15% → back to 10% |
| [0412][wm0412] | Death Head | crit chance 5% → 3% |
| [0420][wm0420] | Tempest Fisher | MR penetration 20 → 10 |
| [0615][wm0615] | Dark Knight | passive cooldown fixed at 300 s |

- Share of gear stats a hero gets ([WM 0628][wm0628]): hero T1+0 **35%**, T1+15 **45%**, T2+10 **65%**, T3+15 **100%**. *notes*
- Transformation cooldown 10 → **120 s** ([WM 0621][wm0621]). *notes*
- Costume "Ninja": dodge +5%, move +5% ([WM 0412][wm0412]). *notes*

[wm0329]: https://steamcommunity.com/games/718790/announcements/detail/2383968106570216224
[wm0402]: https://steamcommunity.com/games/718790/announcements/detail/2383968106583377018
[wm0412]: https://steamcommunity.com/games/718790/announcements/detail/2394102381817542359
[wm0420]: https://steamcommunity.com/games/718790/announcements/detail/2758894130315567397
[wm0426]: https://steamcommunity.com/games/718790/announcements/detail/2394103650887775295
[wm0615]: https://steamcommunity.com/games/718790/announcements/detail/2842216343262999426
[wm0621]: https://steamcommunity.com/games/718790/announcements/detail/2499943313629707204
[wm0628]: https://steamcommunity.com/games/718790/announcements/detail/2499943313654890838
[wm0712]: https://steamcommunity.com/games/718790/announcements/detail/2838841185432966428
[wm0719]: https://steamcommunity.com/games/718790/announcements/detail/2412125660633804214
[wm0830]: https://steamcommunity.com/games/718790/announcements/detail/2447032361187005747
[wm1107]: https://steamcommunity.com/games/718790/announcements/detail/2423394805992652770
[wm0110]: https://steamcommunity.com/games/718790/announcements/detail/2417771014047971842
[wm0124]: https://steamcommunity.com/games/718790/announcements/detail/2425653583381829617

[g-noob]: https://steamcommunity.com/sharedfiles/filedetails/?id=1345368744
[g-def]: https://steamcommunity.com/sharedfiles/filedetails/?id=1459948573
[g-strat]: https://steamcommunity.com/sharedfiles/filedetails/?id=1460486971
[g-tr]: https://steamcommunity.com/sharedfiles/filedetails/?id=1460533609
[g-ptbr]: https://steamcommunity.com/sharedfiles/filedetails/?id=1544645226
