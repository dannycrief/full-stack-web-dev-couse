"""
FILTER FUNCTION
"""
alist = [1, 2, 3, 4, 5, 6]


def event_number(number):
    """Returns True if number % 2 == 0, otherwise - False"""
    return number % 2 == 0


for number in filter(event_number, alist):
    print(number)


def my_filter(function, iterable):
    result = []
    for item in iterable:
        if function(item):
            result.append(item)
    # or
    filtered_list = [item for item in iterable if function(item)]
    return result


"""
MAP  FUNCTION 
"""
print("MAP  FUNCTION")


def sqr(number):
    return number ** 2


for item in map(sqr, alist):
    print(item)


def my_map(function, iterable):
    result = []
    for item in iterable:
        value = function(item)
        result.append(value)
    # or
    mapped_list = [function(item) for item in iterable]
    return result


"""
LAMBDA  FUNCTION 
"""
print("LAMBDA  FUNCTION")

sqr = lambda number: number ** 2
event_number = lambda number: number % 2 == 0


# than
print("than")
for number in filter(lambda number: number % 2 == 0, alist):
    print(number)
print("and")
for number in map(lambda number: number ** 2, alist):
    print(number)


"""
Tasks
"""
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Task 1")
for number in filter(lambda number: number % 5 == 0, numbers_list):
    print(number)
print("Task 2")
for number in map(lambda number: number ** 5, numbers_list):
    print(number)
print("Task 3")
words = ["Monty", "Python's", "flying", "circus"]


def short_word(word):
    """Returns True if length words is <= 5, otherwise - Fasle"""
    return len(word) <= 5

short_words = filter(short_word, words)

for short_word in short_words:
    print(short_word)
