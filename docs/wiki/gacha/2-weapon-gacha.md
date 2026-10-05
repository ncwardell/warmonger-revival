---
title: "Weapon gacha"
type: "gacha"
id: 2
status: "stub"
missing: ["odds"]
sources: ["client: Gacha_02.cdb", "client strings: GUI_Herobind_GachaText_2", "contract: items.yaml hero_gacha 0x4aa, server_rules gacha_odds", "docs: [[gameplay/events-and-schedules]] §10 (WM 1018 image 2: card prices in jewels; pool-to-card match inferred from contents and GUI_Herobind_GachaText_N)"]
pool: 2
contents:
  - {"item": 10011, "grade": 3}
  - {"item": 10017, "grade": 3}
  - {"item": 10002, "grade": 3}
  - {"item": 10000, "grade": 3}
  - {"item": 10001, "grade": 3}
  - {"item": 15004, "grade": 3}
  - {"item": 15007, "grade": 3}
  - {"item": 20001, "grade": 3}
  - {"item": 20011, "grade": 3}
  - {"item": 10003, "grade": 2, "c3": 1}
  - {"item": 10015, "grade": 2, "c3": 1}
  - {"item": 10020, "grade": 2, "c3": 1}
  - {"item": 15000, "grade": 2, "c3": 1}
  - {"item": 15001, "grade": 2, "c3": 1}
  - {"item": 15002, "grade": 2, "c3": 1}
  - {"item": 15006, "grade": 2, "c3": 1}
  - {"item": 15008, "grade": 2, "c3": 1}
  - {"item": 20020, "grade": 2, "c3": 1}
  - {"item": 20021, "grade": 2, "c3": 1}
  - {"item": 20002, "grade": 2, "c3": 1}
  - {"item": 20003, "grade": 2, "c3": 1}
  - {"item": 20015, "grade": 2, "c3": 1}
  - {"item": 641, "grade": 2, "c3": 1}
  - {"item": 643, "grade": 2, "c3": 1}
  - {"item": 10004, "grade": 1, "c3": 2}
  - {"item": 10005, "grade": 1, "c3": 2}
  - {"item": 10014, "grade": 1, "c3": 2}
  - {"item": 15009, "grade": 1, "c3": 2}
  - {"item": 20014, "grade": 1, "c3": 2}
  - {"item": 20004, "grade": 1, "c3": 2}
  - {"item": 641, "grade": 3, "c3": 2}
  - {"item": 643, "grade": 3, "c3": 2}
  - {"item": 11000, "grade": 1, "c3": 2}
  - {"item": 11001, "grade": 1, "c3": 2}
  - {"item": 11002, "grade": 1, "c3": 2}
  - {"item": 11003, "grade": 1, "c3": 2}
  - {"item": 11011, "grade": 1, "c3": 2}
  - {"item": 11015, "grade": 1, "c3": 2}
  - {"item": 11017, "grade": 1, "c3": 2}
  - {"item": 11020, "grade": 1, "c3": 2}
  - {"item": 16000, "grade": 1, "c3": 2}
  - {"item": 16001, "grade": 1, "c3": 2}
  - {"item": 16002, "grade": 1, "c3": 2}
  - {"item": 16004, "grade": 1, "c3": 2}
  - {"item": 16006, "grade": 1, "c3": 2}
  - {"item": 16007, "grade": 1, "c3": 2}
  - {"item": 16008, "grade": 1, "c3": 2}
  - {"item": 21001, "grade": 1, "c3": 2}
  - {"item": 21002, "grade": 1, "c3": 2}
  - {"item": 21003, "grade": 1, "c3": 2}
  - {"item": 21011, "grade": 1, "c3": 2}
  - {"item": 21015, "grade": 1, "c3": 2}
  - {"item": 21020, "grade": 1, "c3": 2}
  - {"item": 21021, "grade": 1, "c3": 2}
  - {"item": 30002, "grade": 1, "c3": 2}
  - {"item": 35002, "grade": 1, "c3": 2}
  - {"item": 35009, "grade": 1, "c3": 2}
  - {"item": 40014, "grade": 1, "c3": 2}
  - {"item": 15005, "grade": 1, "c3": 2}
price: {"amount": 2000, "currency": 13, "currency_name": "Jewels (yellow + purple)"}
bag_slots_needed: 10
kind: "gacha_pool"
---
<!-- generated:start -->
<!-- generated-keys: title=98af80 type=0814f8 id=da4b92 sources=85200f pool=da4b92 contents=370f78 price=66fc63 bag_slots_needed=b1d578 kind=a22c27 -->
|  |  |
|---|---|
| **Pool** | `2` (`Gacha_02.cdb`, 0x4aa gacha_type 2) |
| **Card name** | Weapon (`GUI_Herobind_Type2`) |
| **Price** | 2,000 Jewels (yellow + purple) |
| **Bag slots needed** | 10 |
| **Odds** | unknown (server side, never published) |
| **Entries** | 59 (57 distinct items) |

### Card text

> You can earn items between 1 and 3 tiers

### What the 2018 card listed

[[gameplay/events-and-schedules|Events and schedules]] §10 (WM 1018 image): Normal Weapon (1–3), Superior Weapon (1), Rare Weapon (1), Normal / Superior Rainbow stone. The match of this client pool to that card is *inferred* from the tiers and contents.

### Contents

`grade` and `c3` are the table's own columns. In the paid pools grade 3 rows have `c3` 0, grade 2 rows `c3` 1 and grade 1 rows `c3` 2, and the Rainbow stones 641/643 appear once per rarity; so `c3` looks like the rarity (0 normal, 1 superior, 2 rare) and `grade` like a draw class, 3 the commonest (*guess*). Pools 4 and 5 set an unknown column `c4` = 1 on every row.

#### Grade 1 (33)

|  | item | kind | c3 |
|---|---|---|---|
| ![](../assets/items/10004.png) | [[wiki/items/10004-tempest-s-magical-wand\|Tempest's magical wand]] | Weapon (31) | 2 |
| ![](../assets/items/10005.png) | [[wiki/items/10005-magical-blade-shield-flame\|Magical Blade Shield : Flame]] | Weapon (31) | 2 |
| ![](../assets/items/10014.png) | [[wiki/items/10014-skeleton-king-s-magic-gun\|Skeleton king's Magic Gun]] | Weapon (31) | 2 |
| ![](../assets/items/15009.png) | [[wiki/items/15009-skeleton-king-s-magic-dagger\|Skeleton King's Magic Dagger]] | Weapon (31) | 2 |
| ![](../assets/items/20014.png) | [[wiki/items/20014-skeleton-king-s-magic-cannon\|Skeleton King's Magic Cannon]] | Weapon (31) | 2 |
| ![](../assets/items/20004.png) | [[wiki/items/20004-skeleton-king-s-magic-hammer\|Skeleton King's Magic Hammer]] | Weapon (31) | 2 |
| ![](../assets/items/11000.png) | [[wiki/items/11000-magical-storm-wand\|Magical Storm Wand]] | Weapon (31) | 2 |
| ![](../assets/items/11001.png) | [[wiki/items/11001-magical-thunder-wand\|Magical Thunder Wand]] | Weapon (31) | 2 |
| ![](../assets/items/11002.png) | [[wiki/items/11002-magical-life-wand\|Magical Life Wand]] | Weapon (31) | 2 |
| ![](../assets/items/11003.png) | [[wiki/items/11003-magical-cystal-wand\|Magical Cystal Wand]] | Weapon (31) | 2 |
| ![](../assets/items/11011.png) | [[wiki/items/11011-magical-adapted-dual-gun\|Magical adapted Dual Gun]] | Weapon (31) | 2 |
| ![](../assets/items/11015.png) | [[wiki/items/11015-magical-dash-blade\|Magical Dash Blade]] | Weapon (31) | 2 |
| ![](../assets/items/11017.png) | [[wiki/items/11017-magical-wrath-blade\|Magical Wrath Blade]] | Weapon (31) | 2 |
| ![](../assets/items/11020.png) | [[wiki/items/11020-magical-devil-wand\|Magical Devil Wand]] | Weapon (31) | 2 |
| ![](../assets/items/16000.png) | [[wiki/items/16000-magical-shadow-bow\|Magical Shadow Bow]] | Weapon (31) | 2 |
| ![](../assets/items/16001.png) | [[wiki/items/16001-magical-sniping-bow\|Magical Sniping Bow]] | Weapon (31) | 2 |
| ![](../assets/items/16002.png) | [[wiki/items/16002-magical-vision-bow\|Magical Vision Bow]] | Weapon (31) | 2 |
| ![](../assets/items/16004.png) | [[wiki/items/16004-magical-frost-bow\|Magical Frost Bow]] | Weapon (31) | 2 |
| ![](../assets/items/16006.png) | [[wiki/items/16006-magical-blood-dagger\|Magical Blood Dagger]] | Weapon (31) | 2 |
| ![](../assets/items/16007.png) | [[wiki/items/16007-magical-judge-dagger\|Magical judge Dagger]] | Weapon (31) | 2 |
| ![](../assets/items/16008.png) | [[wiki/items/16008-magical-hiding-dagger\|Magical hiding Dagger]] | Weapon (31) | 2 |
| ![](../assets/items/21001.png) | [[wiki/items/21001-magical-demolition-hammer\|Magical Demolition Hammer]] | Weapon (31) | 2 |
| ![](../assets/items/21002.png) | [[wiki/items/21002-magical-dash-hammer\|Magical Dash Hammer]] | Weapon (31) | 2 |
| ![](../assets/items/21003.png) | [[wiki/items/21003-magical-crush-hammer\|Magical Crush Hammer]] | Weapon (31) | 2 |
| ![](../assets/items/21011.png) | [[wiki/items/21011-magical-blast-cannon\|Magical Blast Cannon]] | Weapon (31) | 2 |
| ![](../assets/items/21015.png) | [[wiki/items/21015-magical-protect-mace\|Magical Protect Mace]] | Weapon (31) | 2 |
| ![](../assets/items/21020.png) | [[wiki/items/21020-magical-protect-hammer\|Magical Protect Hammer]] | Weapon (31) | 2 |
| ![](../assets/items/21021.png) | [[wiki/items/21021-magical-protect-cannon\|Magical Protect Cannon]] | Weapon (31) | 2 |
| ![](../assets/items/30002.png) | [[wiki/items/30002-magical-life-wand\|Magical Life Wand]] | Weapon (31) | 2 |
| ![](../assets/items/35002.png) | [[wiki/items/35002-magical-vision-bow\|Magical Vision Bow]] | Weapon (31) | 2 |
| ![](../assets/items/35009.png) | [[wiki/items/35009-skeleton-king-s-magic-dagger\|Skeleton King's Magic Dagger]] | Weapon (31) | 2 |
| ![](../assets/items/40014.png) | [[wiki/items/40014-skeleton-king-s-magic-cannon\|Skeleton King's Magic Cannon]] | Weapon (31) | 2 |
| ![](../assets/items/15005.png) | [[wiki/items/15005-skeleton-king-s-vision-bow\|Skeleton king's Vision Bow]] | Weapon (31) | 2 |

#### Grade 2 (15)

|  | item | kind | c3 |
|---|---|---|---|
| ![](../assets/items/10003.png) | [[wiki/items/10003-magical-cystal-wand\|Magical Cystal Wand]] | Weapon (31) | 1 |
| ![](../assets/items/10015.png) | [[wiki/items/10015-magical-dash-blade\|Magical Dash Blade]] | Weapon (31) | 1 |
| ![](../assets/items/10020.png) | [[wiki/items/10020-magical-devil-wand\|Magical Devil Wand]] | Weapon (31) | 1 |
| ![](../assets/items/15000.png) | [[wiki/items/15000-magical-shadow-bow\|Magical Shadow Bow]] | Weapon (31) | 1 |
| ![](../assets/items/15001.png) | [[wiki/items/15001-magical-sniping-bow\|Magical Sniping Bow]] | Weapon (31) | 1 |
| ![](../assets/items/15002.png) | [[wiki/items/15002-magical-vision-bow\|Magical Vision Bow]] | Weapon (31) | 1 |
| ![](../assets/items/15006.png) | [[wiki/items/15006-magical-blood-dagger\|Magical Blood Dagger]] | Weapon (31) | 1 |
| ![](../assets/items/15008.png) | [[wiki/items/15008-magical-hiding-dagger\|Magical hiding Dagger]] | Weapon (31) | 1 |
| ![](../assets/items/20020.png) | [[wiki/items/20020-magical-protect-hammer\|Magical Protect Hammer]] | Weapon (31) | 1 |
| ![](../assets/items/20021.png) | [[wiki/items/20021-magical-protect-cannon\|Magical Protect Cannon]] | Weapon (31) | 1 |
| ![](../assets/items/20002.png) | [[wiki/items/20002-magical-dash-hammer\|Magical Dash Hammer]] | Weapon (31) | 1 |
| ![](../assets/items/20003.png) | [[wiki/items/20003-magical-crush-hammer\|Magical Crush Hammer]] | Weapon (31) | 1 |
| ![](../assets/items/20015.png) | [[wiki/items/20015-magical-protect-mace\|Magical Protect Mace]] | Weapon (31) | 1 |
| ![](../assets/items/641.png) | [[wiki/items/641-rainbow-reinforcing-stone-weapon\|Rainbow Reinforcing Stone (Weapon)]] | Grede Reinforcing Stone (48) | 1 |
| ![](../assets/items/643.png) | [[wiki/items/643-rainbow-reinforcing-stone-weapon\|Rainbow Reinforcing Stone (Weapon)]] | Grede Reinforcing Stone (48) | 1 |

#### Grade 3 (11)

|  | item | kind | c3 |
|---|---|---|---|
| ![](../assets/items/10011.png) | [[wiki/items/10011-magical-adapted-dual-gun\|Magical adapted Dual Gun]] | Weapon (31) | 0 |
| ![](../assets/items/10017.png) | [[wiki/items/10017-magical-wrath-blade\|Magical Wrath Blade]] | Weapon (31) | 0 |
| ![](../assets/items/10002.png) | [[wiki/items/10002-magical-life-wand\|Magical Life Wand]] | Weapon (31) | 0 |
| ![](../assets/items/10000.png) | [[wiki/items/10000-magical-storm-wand\|Magical Storm Wand]] | Weapon (31) | 0 |
| ![](../assets/items/10001.png) | [[wiki/items/10001-magical-thunder-wand\|Magical Thunder Wand]] | Weapon (31) | 0 |
| ![](../assets/items/15004.png) | [[wiki/items/15004-magical-frost-bow\|Magical Frost Bow]] | Weapon (31) | 0 |
| ![](../assets/items/15007.png) | [[wiki/items/15007-magical-judge-dagger\|Magical judge Dagger]] | Weapon (31) | 0 |
| ![](../assets/items/20001.png) | [[wiki/items/20001-magical-demolition-hammer\|Magical Demolition Hammer]] | Weapon (31) | 0 |
| ![](../assets/items/20011.png) | [[wiki/items/20011-magical-blast-cannon\|Magical Blast Cannon]] | Weapon (31) | 0 |
| ![](../assets/items/641.png) | [[wiki/items/641-rainbow-reinforcing-stone-weapon\|Rainbow Reinforcing Stone (Weapon)]] | Grede Reinforcing Stone (48) | 2 |
| ![](../assets/items/643.png) | [[wiki/items/643-rainbow-reinforcing-stone-weapon\|Rainbow Reinforcing Stone (Weapon)]] | Grede Reinforcing Stone (48) | 2 |

### Odds

Not in the client (`Gacha_NN` has items and grades only). The contract's `gacha_odds` suggestion (uniform within a grade, grade weights 70/25/5) is invented, not original data. Put real odds in `odds:` with a source.

### Seen in

- Seen in [[gameplay/README|Gameplay]], section *Pages*
- Seen in [[gameplay/classes-and-legions|Classes, nations and legions]], section *1. Classes*
- Seen in [[gameplay/events-and-schedules|Events, schedules and PvP rewards]], section *9. Other timers and limits*
- Seen in [[gameplay/items-and-crafting|Items, upgrades and crafting]], section *5. Where gear comes from*
- Seen in [[gameplay/patch-history|Patch notes and other sources]], section *Economy and timeline*
- Seen in [[gameplay/progression-and-economy|Progression and economy]], section *3. Currencies*
- Seen in [[gameplay/reinforce-and-runes|Reinforce, tier-up and rune numbers]], section *4. Gear reinforce and tier-up*
- Seen in [[gameplay/server-rules|Server rules checklist]], section *Economy*
- Seen in [[gameplay/sources|Sources and gaps]], section *9. What is still missing*
- Seen in [[gameplay/videos|Videos]], section *Wars, forts and matches*
<!-- generated:end -->

## Notes

<!-- hand-written: add what you know, with a source -->

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

<!-- hand-written: add what you know, with a source -->

## Open questions

<!-- hand-written: add what you know, with a source -->

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
