import random

def say_hello(name):
    return "Hello, " + name

def do_action(function):
    random_name = random.choice(["Edgar, Arsen"])
    return function(random_name)

print(do_action(say_hello))


def compose_hello_func(name):
    def get_intro():
        return "Привет, " + name + "!"

    return get_intro

say_hi = compose_hello_func("Арсений")
print(say_hi())

# or

def compose_hello_func(name):
    get_intro = lambda: "Привет, " + name + "!"
    return get_intro
