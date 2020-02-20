def compose_hello_func(name):
    get_intro = lambda: "Hello, " + name + "!"
    return get_intro


def decorate(tag):
    wrap = lambda text: "<{0}>{1}</{0}>".format(tag, text)
    return wrap


h1_decorator = decorate("h1")
greeting = compose_hello_func("Stepan")
print(h1_decorator(greeting()))