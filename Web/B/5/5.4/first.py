def h1_wrap(func):
    def func_wrapper(param):
        return "<h1>"+func(param) + "</h1>"
    return func_wrapper


@h1_wrap
def say_hi(name):
    return "Hello, " + name.capitalize()


print(say_hi("Stephan"))
