def tell_even(num):
    if num % 2 == 0:
        print(num, '-- is even')
    else:
        print(num, '-- is odd')


def greet(name, gender):
    if gender == 'male':
        print("Hello, Mrs. ", name)
    else:
        print("Hello, Miss. ", name)


print(greet('Stepan Kozurak', 'male'))


def sum_numbers(x, y):
    result = x + y
    return result