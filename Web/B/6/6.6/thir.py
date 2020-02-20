def fib(n):
    a, b = 1, 1
    for x in range(n):
        yield a
        a, b = b, a + b


def run_iterator(iterator):
    items = []
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        else:
            items.append(item)
    return items


fibonacci_sequence = fib(5)
for item in run_iterator(fibonacci_sequence):
    print(item)


