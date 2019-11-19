def make_russian(number):
    ten_mod = number % 10
    hundr_mod = number % 100
    if ten_mod == 1 and hundr_mod != 11:
        return str(number) + " студент"
    elif ten_mod in [2, 3, 4] and hundr_mod not in [12, 13, 14]:
        return str(number) + " студента"
    else:
        return str(number) + " студентов"


for number in range(1, 5001):
    print(make_russian(number))
