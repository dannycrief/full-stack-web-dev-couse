class Number:
	value = 4
num = Number()
setattr(num, "value", 6)
print(getattr(num, "value"))
		
class User: pass

user1 = [
	"Peter",
	"32",
	"peterrobinson@mail.com",
	["Egg", "Spam", "Hat", "Knife", "Shield", "Book of Knight secrets"],
]

attrs = ["name", "age", "email", "purcases"]
user_instance = User()
for attr, val in zip(attrs, user1):
    setattr(user_instance, attr, val)
    print(getattr(user_instance, attr))
