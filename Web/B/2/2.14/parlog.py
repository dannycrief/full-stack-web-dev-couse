import json
import collections

​FILENAME = 'firstfile.json'

lf = open(FILENAME, encoding="utf-8")
log_file = []
for i in lf:
    log_file.append(json.loads(i))
lf.close()
# Part 1
# Task 1
print('Part 1')
print('Task 1')
new = []
for line in log_file:
    browsers = line['userAgentName']
    new.append(browsers)
c = collections.Counter(new)
c = c.most_common()
user_browsers = 0
​
for i in c:
    user_browsers += 1
print(user_browsers)

# Task 2 answer 12641824
print('\nTask 2')
nums_of_shop = 0
for line in log_file:
    if line["eventType"] == "itemBuyEvent":
        if not line["detectedDuplicate"] and not line["detectedCorruption"]:
            nums_of_shop += int(line["item_price"])
print(nums_of_shop)
​
​
# B2.14.3 Второй журнал: браузеры
​
FILENAME = 'data_3000.json'
​
lf = open(FILENAME, encoding="utf-8")
log_file = []
for i in lf:
    log_file.append(json.loads(i))
lf.close()
​
print("\nThe second one\n")
​
new = []
total = 0
for line in log_file:
    browsers = line["userAgentName"]
    new.append(browsers)
my_collection = collections.Counter(new).most_common()
for elem in my_collection:
    total += 1
print(total)
​
print('\nTask 2')
nums_of_shop = 0
for line in log_file:
    if line["eventType"] == "itemBuyEvent":
        if not line["detectedDuplicate"]:
            if not line["detectedCorruption"]:
                nums_of_shop += int(line["item_price"])
print(nums_of_shop)
​
# Part 2
print("\nPart 2")
print("1) B2.14.5 Второй журнал: число избранных")
# starts part 2 task 1
​
​
def open_second_file():
    lf = open('data_3000.json', encoding="utf-8")
    log_file = []
    for i in lf:
        log_file.append(json.loads(i))
    lf.close()
    return log_file
​
​
def saved_elems():
    nums_of_items = 0
    all_items = []
    for line in open_second_file():
        if line["eventType"] == "itemFavEvent":
            if line["item_id"]:
                all_items.append(line["item_id"])
    c = collections.Counter(all_items).most_common()
    for i in c:
        print(i)
        nums_of_items += 1
​
    return "{} -- number of saved items".format(nums_of_items)
​
​
print(saved_elems())
print("\n2) B2.14.6 Число 'лайков' товара")
​
​
def some_items_was_liked():
    item_was_liked = 1359
    all_items = []
    for line in open_second_file():
        if line["eventType"] == "itemFavEvent":
            all_items.append(line["item_id"])
    c = collections.Counter(all_items)
    return c
​
​
print(some_items_was_liked())