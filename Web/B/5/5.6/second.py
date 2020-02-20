def h1_wrap(func):
    def func_wrapper(param):
        return "<h1>"+func(param)+"</h1>"

    func_wrapper.__name__ = func.__name__
    func_wrapper.__doc__ = func.__doc__
    return func_wrapper

@h1_wrap
def say_hi(name):
    """It says hello to name"""
    return "Hello, " + name.capitalize()


print(say_hi("Stepan"))
print(say_hi.__doc__)
print(say_hi.__name__)