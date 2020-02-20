my_list = [i * 4 for i in range(10)]

my_generator = (i * 4 for i in range(10))

for element in my_list:
    print(element)

for element in my_generator:
    print(element)

print('something new...')


def counter(up_to):
    i = 0
    yield 'START'
    while i < up_to:
        yield i
        i += 1
    yield 'END'


def sample_sequence():
    yield 2
    yield 12
    yield 85
    yield 'Ноль'
    yield 6


my_count = counter(5)
for element in my_count:
    print(element)

print('next one')

seq = sample_sequence()
for _ in range(3):
    print(next(seq))
print('...')
print(next(seq))
print(next(seq))
# print(next(seq))


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print('one more')

sequencer = fib()
for _ in range(20):
    print(next(sequencer))
