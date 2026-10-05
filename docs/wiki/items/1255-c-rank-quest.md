---
title: "C Rank Quest"
type: "item"
id: 1255
status: "complete"
missing: []
sources: ["client: Item_Base.cdb id 1255", "image: [[gameplay/precept-shop]] §1 (Crush Online Oct 2016: Freya sold Rank[C] precepts at 9,300 gold and Rank[B] at 18,600; client ids grouped per rank on that page)"]
name_key: "ItemName_1202"
kind: 44
kind_name: "Quest precept"
classes: "all"
bind: "on_pickup"
price: {"currency": 2, "currency_name": "Gold", "buy": 25000}
cost_pair:
  - {"currency": 2, "amount": 25000}
stats: []
icon: {"file": "Items_07.png", "index": 37}
obtained_from:
  - {"how": "shop_crush_2016", "npc": 200, "price": 9300, "currency": "gold"}
---
<!-- generated:start -->
<!-- generated-keys: title=d00e38 type=d36ca9 id=cc6f6e sources=e788d5 name_key=ba6b34 kind=98fbc4 kind_name=b94918 classes=92d079 bind=883bf8 price=2080a7 cost_pair=0f9a23 stats=97d170 icon=df3f62 obtained_from=97d170 -->
|  |  |
|---|---|
|  | ![C Rank Quest](wiki/assets/items/1255.png) |
| **Item id** | `1255` |
| **Kind** | Quest precept (44) |
| **Classes** | all |
| **Bind** | on pickup |
| **Buy price** | 25,000 Gold |
| **Icon** | `ui/icons/Items_07.png` cell 37 |

### Tooltip

> Build a nexus at the monster occupation and win
>
> Limit : 30 Lv, Belong to legion

### Where to get it

- how shop_crush_2016, npc 200, price 9300, currency gold (hand-entered)

### Mentioned in

- [[gameplay/precept-shop|Precept shop and precept quests]]
<!-- generated:end -->

## Notes

Freya sold the Rank[C] precept for **9,300 gold** in October 2016 ([[gameplay/precept-shop|Precept shop]] §1, *image*); the client's base price is 25,000.

## Behaviour

<!-- hand-written: add what you know, with a source -->

## Sources

- image: [[gameplay/precept-shop]] §1 (Crush Online Oct 2016: Freya sold Rank[C] precepts at 9,300 gold and Rank[B] at 18,600; client ids grouped per rank on that page)

## Open questions

The client's shop 289 sells only 1251–1253 for rank C, and this precept points to quest 815, which is not in `Quest.tsv` ([[gameplay/precept-shop|Precept shop]] §1). So it was probably not sold in the final game.

<!-- credit:start -->
---
*Game content © GAMESinFLAMES / Joyimpact; reproduced for preservation and reference.*
<!-- credit:end -->
