def div(x, y):
    return x / y


try:
    d = div(4, 0)
    print("And we have ", d)
except ZeroDivisionError as err:
    print("There is an error:", err)
print("\n")
try:
    alist = [1, 2, 3]
    d =div(3, alist)
    print("Result: ", d)
except (ZeroDivisionError, TypeError) as err:
    print("Error:", err)
print("\n")
try:
    alist = [1, 2, 3]
    d = div(4, alist)
    print("Result of division is ", d)
except ZeroDivisionError:
    print("You cand divide by zero.")
except TypeError as err:
    print("Unsupported parameters:", err)
