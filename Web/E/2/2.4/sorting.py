import operator

"""Clear function"""
ll = [33, 41, 22, 45]
print(sorted(ll))  # [22, 33, 41, 45]
print(ll)  # [33, 41, 22, 45]


def key_func(x: list) -> int:
    return len(x)


ll = ['a', 'aa', 'b', 'bbb', 'c']
print(list(sorted(ll, key=key_func)))  # ['a', 'b', 'c', 'aa', 'bbb']


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


a = Point(1, 3)
b = Point(2, 3)
c = Point(1, 4)
l = [a, b, c]

f = operator.attrgetter('x')

print(f(a))  # 1
print(f(b))  # 2

print(list(sorted(l, key=f)))  # [<__main__.Point object at 0x7fad52f94580>, <__main__.Point object at 0x7fad52f65d00>,
# <__main__.Point object at 0x7fad52f65ca0>]

print(list(sorted(l, key=f))[0].x)  # 1

"""Map function"""
ll = ['a', 'aa', 'b', 'bbb', 'c']
print(list(map(len, ll)))  # [1, 2, 1, 3, 1]

l = [1, 2, 3]


def square(x):
    return x * x


print(list(map(square, l)))  # [1, 4, 9]

not_true = [False, False, False]
maybe = [False, True, False]
true = [True, True, True]

print(any(not_true))  # False
print(any(maybe))  # True
print(all(not_true))  # False
print(all(maybe))  # False
print(all(true))  # True

ll = [-1, -2, 3, 4, -22]


def is_positive(x):
    return x > 0


print("Testing any:", any(map(is_positive, ll)))  # Testing any: True
print("Testing all:", all(map(is_positive, ll)))  # Testing any: False

ll = [1, 2, 3, 4, 55]
print(max(ll))  # 55
print(min(ll))  # 1

"""Filter function"""


def division_by_three(number):
    return number % 3 == 0


ll = [1, 2, 3, 4, 5, 6, 233]
print(list(filter(division_by_three, ll)))  # [3, 6]

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
print(list(zip(l1, l2)))  # [(1, 'a'), (2, 'b'), (3, 'c')]
print(dict(zip(l1, l2)))  # {1: 'a', 2: 'b', 3: 'c'}

ll = ["A", "B", "C"]
print(enumerate(ll))  # <enumerate object at 0x7f7c01b7d180>
for i in enumerate(ll):
    print(i)  # (0, 'A') (1, 'B') (2, 'C')

"""Exercises"""
print(list(enumerate("EDFI")))  # [(0, 'E'), (1, 'D'), (2, 'F'), (3, 'I')]


def is_digit(input):
    return input.isdigit()


ll = ['a', 'b', '32', '33']
print(list(filter(is_digit, ll)))  # ['32', '33']
