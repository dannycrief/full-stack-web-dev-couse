class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


peter = User("Peter Robertson", "peterrobentson@mail.com")
julia = User("Julia Donaldson", "juliadonaldson@mail.com")

print(peter.name)
print(julia.email)