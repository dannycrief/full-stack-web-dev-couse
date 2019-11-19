# Fizz if % 3 == 0


def fizz_or_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return "FUCK"


for i in range(100):
    print("Number is: " + str(i), fizz_or_buzz(i))
# task 1.1
total = 0
print("\nTask 1.1:")
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)
# task 1.2
total = 0
print("\nTask 1.2:")
for i in range(10000):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        total += i
print(total)

# tasks 2
# Fibonacci numbers
print("\nTask 2:")


def fibonacci():
    my_list = [1, 2]
    a = 1
    b = 2
    global c
    even_total = 0
    while a + b < 4000000:
        for _ in range(3):
            c = a + b
            a, b = b, c
            my_list.append(c)
    for i in my_list:
        if i % 2 == 0:
            even_total += i
    return c, even_total


print(fibonacci())
