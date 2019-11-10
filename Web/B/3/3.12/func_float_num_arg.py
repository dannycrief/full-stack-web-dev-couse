import os

print(os.path.join("some", "folder"))

print(os.path.join("some", "other", "folder"))


def f(a, b):
    pass


print(f(4, 2))
# print(f(4, 2, 1)) it'll be an error, cause too many arguments were given

print("\nMulti func")

# *args it means that we can give
def multi(*args):
    res = 1
    for elements in args:
        res *= elements
    return res


print(multi(1, 2, 4, 0))
print(multi(2, 5, 7, 2, 4))
