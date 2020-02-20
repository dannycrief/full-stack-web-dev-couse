user_peter = {
    "name": "Peter",
    "email": "peterrobertson@mail.com",
    "created_at": "2019-05-05",
    "is_email_verified": True,
    "purchases": ["Egg", "Spam", "Hat", "Knife", "Shield", "Book of Knight secrets"],
}

user_julia = {
    "name": "Julia Donaldson",
    "email": "juliadonaldson@mail.com",
    "created_at": "2019-06-13",
    "is_email_verified": True,
    "purchases": ["Egg", "Spam", "Magic Brush"],
}

product_eggs = {
    "name": "Egg",
    "category": "food",
    "is_available": False,
    "quantity_in_stock": 0,
    "vendor": "Dark Knight LTD",
    "manager": "William The Conqueror",
}


class User:
    number_of_fingers = 5
    number_of_eyes = 2


peter = User()
peter.name = "Peter Robertson"

julia = User()
julia.name = "Julia Donaldson"

lancelot = User()

print(peter.name)
print(julia.name)
print(lancelot.number_of_fingers)
