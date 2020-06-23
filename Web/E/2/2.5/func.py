from functools import partial

# lambda arguments: function
a = lambda x: x

a = (lambda x: x * x)(3)
print(a)  # 9
a = (lambda x, y: x + y)(2, 3)
print(a)  # 5

ll = ['a', 'aa', 'b', 'bbb', 'c']
print(sorted(ll, key=lambda x: x.upper()))  # ['a', 'aa', 'b', 'bbb', 'c']
l = [1, 2, 3]
print(list(map(lambda x: x * x, l)))  # [1, 4, 9]
ll = [-1, -2, 3, 4, -22]
print(list(filter(lambda x: x > 0, ll)))  # [3, 4]


def linear(a, b, x):
    # print(a, x, b)
    return a * x + b


linear1 = partial(linear, 1, 1)
linear2 = partial(linear, -1, -1)
print(linear1(2))  # 3
print(linear2(2))  # -3


def in_between(a, b, c):
    return a < b < c


ll = [1, 2, 3, 4, 5, 6]
z = list(filter(partial(in_between, 3, c=5), ll))
print(z)


def multiply(x, y):
    return x * y


print(partial(multiply, 2))
