"""class User:
    def __init__(self):
        print("Создаю пользователя")
        self.name = "Гелиозавр"


u1 = User()
u2 = User()

u2.name = "Орнитишийлар"
print(u1.name, u2.name)


class User:
    def __init__(self):
        print("Создаю пользователя")
        self.name = "Гелиозавр"

    def __str__(self):
        return self.name


u1 = User()
print(u1)
"""


"""class User:
    def __init__(self, email, name="Гелиозавр"):
        self.email = email
        self.name = name

    def __str__(self):
        return "%s <%s>" % (self.name, self.email)


u1 = User("text@example.com")
u2 = User(name="Орнитишийлар", email="zakusi@pet.ru")
print(u1, u2)"""


class User:
    def __init__(self, email, name="Гелиозавр"):
        self.email = email
        self.name = name

    def __str__(self):
        return "%s <%s>" % (self.name, self. email)

    def __eq__(self, other):
        return self.email.lower() == other.email.lower()


u1 = User(name="Гелиозавр", email="RAWR@mail.ru")
u2 = User(name="Орнитишийлар", email="rawr@mail.ru")

print(u1, u2)
print("Is it the same user?", u1 == u2)
