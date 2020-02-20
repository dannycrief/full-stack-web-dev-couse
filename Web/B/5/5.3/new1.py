def compose_hello_func(name):
    def get_intro():
        return "Hello, " + name + "!"
    return get_intro


def decorate(tag):
    def wrap(text):
        lhs = "<" + tag + ">"
        rhs = "</" + tag + ">"
        return lhs + text + rhs
    return wrap


h1_decorator = decorate("h1")
greeting = compose_hello_func("Stepan")

print(h1_decorator(greeting()))

"""
or in new1.2
"""
