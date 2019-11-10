import random
"""
secret = random.randint(1, 100)

for attempt in range(10, 0, -1):
    guess = input('Will you know my num? You have {} tries\n'.format(attempt))
    guess_number = int(guess)
    if guess_number == secret:
        print("Yeah, right")
        break
    elif guess_number < secret:
        print("My number's is greater then your")
    else:
        print("My number is lesser then your")"""

# task 2.8.1
print("")
user_ids = [33, 1, 15, 42, 24, 22, 20, 38]
print(random.choice(user_ids))
