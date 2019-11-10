import json
# for user
file_object = open('user.txt')
user = json.load(file_object)
file_object.close()
print(user)
print(user['age'])
print(user['name'])
print(user['gender'])

# for costumers
print("")
file_object = open("customers.txt")
customers = json.load(file_object)
file_object.close()
print(customers)
print(customers[0])
for customer in customers:
    if customer['gender'] == "female":
        print(customer)
# dump user
print("")
user = {
    'name': 'Monty Python',
    'gender': 'male',
    'age': 24
}
file_object = open('user1.txt', 'w')
json.dump(user, file_object)
file_object.close()

# next dump costumers
print("")
customers = [{"name": "Alice", "gender": "female", "email": "alice@example.com"}, {"name": "Bob", "gender": "male", "email": "bob24@exa.net"}, {"name": "John", "gender": "female", "email": "john@johnjefferson.org"}]
file_object = open('customers.txt', 'w')
json.dump(customers, file_object)
file_object.close()

# trying find the user
print("")
fp = open('users.txt')
users = json.load(fp)
first_user = None
for user in users:
    if first_user is None or user['registered'] < first_user['registered']:
        first_user = user

print(first_user)

# some types of load & dump
# one more load type
print("")
json_decoded_string = '{"name": "Alice", "age": 27}'
user = json.loads(json_decoded_string)
print(user)
print(user["name"])

# one more dump type
print("")
user = {'name': 'Alice', 'age': 27}
json_decoded_user_string = json.dumps(user)
print(json_decoded_user_string)

# find the user_id that was registered at last
print("")
open_file = open('users.txt')
users = json.load(open_file)
last = None
for user in users:
    if first_user is not None or user['id'] > last['id']:
        last = user
print(last)

# task B2.7.2
print("")
fp = open('user_addresses.txt')
users_list = json.load(fp)
print(users_list[0]['address']['city'])
