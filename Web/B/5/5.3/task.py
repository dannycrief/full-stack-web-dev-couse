def compose_hello_func(name):
    get_intro = lambda: "Hello, " + name + "!"
    return get_intro


def decorate(tag, klass=None):
    if klass:
        wrap = lambda text: "<{0} class='{2}'></{0}>".format(tag, text, klass)
    else:
        wrap = lambda text: "<{0}>{1}</{0}>".format(tag, text)
    return wrap


greeting = compose_hello_func("Stepan")
print(decorate("div", "container")(decorate("h2")(greeting())))
