from itertools import chain, product, accumulate, combinations, permutations, zip_longest, takewhile
import operator

iterator = iter([1, 2, 3])
print(iterator.__next__())  # 1
print(iterator.__next__())  # 2
print(iterator.__next__())  # 3

l1 = range(0, 10)
l2 = range(10, 20)
l3 = range(20, 30)
all = chain(l1, l2, l3)
print(list(all))

for i in chain(l1, l2, l3):
    if i % 3 == 0:
        print(i)

l = range(0, 5)
print(list(combinations(l, 3)))  # [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 3), (0, 2, 4), (0, 3, 4), (1, 2, 3), (1, 2,
# 4), (1, 3, 4), (2, 3, 4)]


for i in permutations('ABCD', 3):
    print(i)

# ('A', 'B', 'C')
# ('A', 'B', 'D')
# ('A', 'C', 'B')
# ('A', 'C', 'D')
# ('A', 'D', 'B')
# ('A', 'D', 'C')
# ('B', 'A', 'C')
# ('B', 'A', 'D')
# ('B', 'C', 'A')
# ('B', 'C', 'D')
# ('B', 'D', 'A')
# ('B', 'D', 'C')
# ('C', 'A', 'B')
# ('C', 'A', 'D')
# ('C', 'B', 'A')
# ('C', 'B', 'D')
# ('C', 'D', 'A')
# ('C', 'D', 'B')
# ('D', 'A', 'B')
# ('D', 'A', 'C')
# ('D', 'B', 'A')
# ('D', 'B', 'C')
# ('D', 'C', 'A')
# ('D', 'C', 'B')

"""
То есть в permutations кортежи ('A', 'B', 'C') и ('A', 'C', 'B') будут считаться разными, а в combinations — одинаковыми.
"""

print(list(product('ABCDEFGH', '12345678')))  # [('A', '1'), ('A', '2'), ('A', '3'), ('A', '4'), ('A', '5'), ('A',
# '6'), ('A', '7'), ('A', '8'), ('B', '1'), ('B', '2'), ('B', '3'), ('B', '4'), ('B', '5'), ('B', '6'), ('B', '7'),
# ('B', '8'), ('C', '1'), ('C', '2'), ('C', '3'), ('C', '4'), ('C', '5'), ('C', '6'), ('C', '7'), ('C', '8'), ('D',
# '1'), ('D', '2'), ('D', '3'), ('D', '4'), ('D', '5'), ('D', '6'), ('D', '7'), ('D', '8'), ('E', '1'), ('E', '2'),
# ('E', '3'), ('E', '4'), ('E', '5'), ('E', '6'), ('E', '7'), ('E', '8'), ('F', '1'), ('F', '2'), ('F', '3'), ('F',
# '4'), ('F', '5'), ('F', '6'), ('F', '7'), ('F', '8'), ('G', '1'), ('G', '2'), ('G', '3'), ('G', '4'), ('G', '5'),
# ('G', '6'), ('G', '7'), ('G', '8'), ('H', '1'), ('H', '2'), ('H', '3'), ('H', '4'), ('H', '5'), ('H', '6'), ('H',
# '7'), ('H', '8')]

"""OR"""
for i in 'ABCDEFGH':
    for j in range(1, 9):
        print(i, j)

ll = [1, 3, 5, 7, 9]
print(list(accumulate(ll)))  # [1, 4, 9, 16, 25] IT MEANS: 1+3=4; 4+5=9;...

print(list(accumulate(ll, func=operator.mul)))  # [1, 3, 15, 105, 945]

l = [1, 2, 3, 9, 8, 7]
print(list(
    accumulate(l, func=max))
)  # [1, 2, 3, 9, 9, 9] IT MEANS: everything that are after max value will be max value
print(list(accumulate(l, func=min)))  # [1, 1, 1, 1, 1, 1]
"""ZIP_LONGEST"""
a = zip_longest('ABCDEFGH', range(1, 10), fillvalue='*')
print(list(a))  # [('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5), ('F', 6), ('G', 7), ('H', 8), ('*', 9)]
"""takewhile"""
l = [1, 2, -3, 3, 4]
t = takewhile(lambda x: x > 0, l)
print(list(t))  # [1, 2]
print(list(filter(lambda x: x < 0, [1, 2, -1, 4]))[0])  # -1
print(next(filter(lambda x: x < 0, [1, 2, -1, 4]), None))  # -1

range_ = range(0, 5)
range_a = len(list(combinations(range_, 3)))
print(range_a)

l = [2, -2, -3, 3, 4]
print(list(takewhile(lambda x: x % 2 == 0, l)))
