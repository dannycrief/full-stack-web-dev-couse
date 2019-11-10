import collections

d = collections.defaultdict(list)
print(d)

print(d["key"])  # выводим значение по ключу key, оно не определено в словаре, поэтому используется значение по
# умолчанию — пустой список
print(d[42])

d["k"].append(33)
print(d)
print(d["k"])

print("")
print("The end of this. Starts new one.")

FILENAME = 'numbers.txt'
fp = open(FILENAME)
counter = collections.defaultdict(int)

line_number = 1
for line in fp:
    numbers = line.split()
    for number in numbers:
        int_number = int(number)
        counter[line_number] += int_number
    line_number += 1

fp.close()

for line_num, line_sum in counter.items():
    print("{} - {}".format(line_num, line_sum))
