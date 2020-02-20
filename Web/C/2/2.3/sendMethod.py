from random import random


def counter(up_to):
    i = 0
    while i < up_to:
        yield i
        i += 1


# enumerate([2, 12, 85, 6]) == (0, 2), (1, 12), (2, 85), (3, 6)


my_counter = counter(10)
for i, element in enumerate(my_counter):
    if i < 5:
        continue
    print(element)

print('next one')


def counterOne(up_to):
    i = 0
    while i < up_to:
        val = (yield i)
        if val is None:
            i += 1
        else:
            i = val


cnt = counterOne(10)
print(next(cnt))
print(next(cnt))
print(next(cnt))
print(next(cnt))
print(next(cnt))
print(next(cnt))
print(next(cnt))
print(next(cnt))
print(next(cnt))
print(next(cnt))


# print(next(cnt))

# task 1:
# cnt = counter(10)
# cnt.send(4)
# answer: TypeError

# task 2:
def my_odd_random():
    while True:
        x = 0
        while x % 2 != 1:
            x = random.randint(1, 99)
            print(x)
        yield x

# answer: 1) True; 2) %
