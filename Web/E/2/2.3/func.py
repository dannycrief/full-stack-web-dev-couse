"""incorrect"""


def delete_last(l):
    l.pop(-1)
    return l


l = [1, 2, 3]
print(delete_last(l))
print(l)


def delete_last_pure(l):
    return l[:-1]


l = [1, 2, 3]
print(delete_last_pure(l))


def add_one(x: int) -> int:
    x += 1
    return x


print(add_one(5))
