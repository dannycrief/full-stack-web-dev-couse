def html_wrap(tag, klass=None):
    def decorator(func):
        def wrap(param):
            if klass:
                return "<{0} class=\"{2}\">\n   {1}\n</{0}>".format(tag, func(param), klass)
            else:
                return "<{0}>{1}</{0}>".format(tag, func(param))
        return wrap
    return decorator


@html_wrap("div", "container")
@html_wrap("h2")
def say_hi(name):
    return "Hello, " + name.capitalize()


print(say_hi("Stepan"))