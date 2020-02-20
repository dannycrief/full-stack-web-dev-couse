def html_wrap(tag):
    def decorator(func):
        def wrap(param):
            return "<{0}>{1}</{0}>".format(tag, func(param))
        return wrap
    return decorator


@html_wrap("2h")
def say_hi(name):
    return "Hello, " + name + name.capitalize()


print(say_hi("Stepan"))