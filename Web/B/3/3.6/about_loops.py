# break
for i in range(len(user_list)):
    huge_holiday_discount = caclculate_complicated_operation(i)
    add_huge_holiday_discount(user_id=i)
    if i == 70:
        print(i)
        break

for event in events:
    if event["refer"] == "https://b24-mu3bxs.bitrix24.shop//katalog/clothes/t-shirts/":
        print(event["item_id"])
        break

# continue
visited_items = []

for event in events:
    if event["referer"] == "https://b24-mu3bxs.bitrix24.shop//katalog/clothes/t-shirts/":
        continue
    item = {"id": event["item_id"], "price": event["item_price"]}
    visited_items.append(item)
