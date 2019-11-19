def say_hello(name):
    return "Hello, " + name

say_hi = say_hello

print(say_hi("Traveller"))


def say_hi(name):
    def get_intro(lang='ru'):
        lang = lang.lower()
        return {
            "ru": "Привет, ",
            "en": "Hello, "
        }[lang]
    message = get_intro() + name
    return message

print(say_hi("SOME NAME"))
