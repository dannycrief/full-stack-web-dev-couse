def func(a, b=4):
    """This function add two numbers"""
    return a + b


print(func(14))
print(func.__defaults__)
func.__defaults__ = (17, )
print(func(14))
print(func.__doc__)
func.__doc__ += ", but you don't need you enter the second one."
print(func.__doc__)
