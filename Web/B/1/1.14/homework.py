new_sepal = []
flowers = {
    "iris_setosa": {
        "sepal_length": [3.6, 4.9, 4.8, 4.7],
        "sepal_width": [2.9, 3.3, 3.2, 3.1],
        "petal_length": [1.3, 1.2, 1.5, 1.4],
    },
    "iris_virginica": {
        "sepal_length": [7.2, 7.0, 7.9],
        "sepal_width": [3.1, 2.7, 2.8],
        "petal_length": [5.5, 5.5, 6.5],
    },
    "iris_versicolor": {
        "sepal_length": [6.5, 6.0, 6.1, 6.2, 6.3],
        "sepal_width": [2.8, 2.9, 2.4, 2.7, 2.7],
        "petal_length": [4.8, 4.7, 5.0, 4.9, 4.8],
    },
}


"""def goByRows(first_row, second_row, third_row):
    for FirstRowElement in first_row:
        new_sepal.append(FirstRowElement)
    for SecondRowElement in second_row:
        new_sepal.append(SecondRowElement)
    for ThirdRowElement in third_row:
        new_sepal.append(ThirdRowElement)
    return new_sepal


# общее среднее значение для sepal_length:
def sepal_length(first_row, second_row, third_row):
    total = 0
    goByRows(first_row, second_row, third_row)
    for totalSumElement in new_sepal:
        total += totalSumElement
    return round(total/len(new_sepal), 1)


# общее среднее значение для sepal_width:
def sepal_width(first_row, second_row, third_row):
    total = 0
    goByRows(first_row, second_row, third_row)
    for totalSumElement in new_sepal:
        total += totalSumElement
    return round(total / len(new_sepal), 1)


# общее среднее значение для petal_length:
def petal_length(first_row, second_row, third_row):
    total = 0
    goByRows(first_row, second_row, third_row)
    for totalSumElement in new_sepal:
        total += totalSumElement
    return round(total / len(new_sepal), 1)


def callUser():
    print("Введите что хотите узнать")
    print("1. Общее среднее значение для sepal_length")
    print("2. Общее среднее значение для sepal_width")
    print("3. Общее среднее значение для petal_length")
    ask = input("Выберите число:\n")
    while ask != '1' or ask != '2' or ask != '3':
        if ask == '1':
            first_row = flowers['iris_setosa']['sepal_length']
            second_row = flowers['iris_virginica']['sepal_length']
            third_row = flowers['iris_versicolor']['sepal_length']
            return sepal_length(first_row, second_row, third_row)
        elif ask == '2':
            first_row = flowers['iris_setosa']['sepal_width']
            second_row = flowers['iris_virginica']['sepal_width']
            third_row = flowers['iris_versicolor']['sepal_width']
            return sepal_width(first_row, second_row, third_row)
        elif ask == '3':
            first_row = flowers['iris_setosa']['petal_length']
            second_row = flowers['iris_virginica']['petal_length']
            third_row = flowers['iris_versicolor']['petal_length']
            return petal_length(first_row, second_row, third_row)
        else:
            return callUser()


print(callUser())
"""

# This is the answer

sepal_lengths = []
sepal_widths = []
petal_lengths = []
for flower, data in flowers.items():
    for length in data['sepal_length']:
        sepal_lengths.append(length)

    for width in data['sepal_width']:
        sepal_widths.append(width)

    for length in data['petal_length']:
        petal_lengths.append(length)


# общее среднее значение для sepal_length:
mean_sepal_length = sum(sepal_lengths) / len(sepal_lengths)
print(round(mean_sepal_length, 1))

# общее среднее значение для sepal_width:
mean_sepal_width = sum(sepal_widths) / len(sepal_widths)
print(round(mean_sepal_width, 1))

# общее среднее значение для petal_length:
mean_petal_length = sum(petal_lengths) / len(petal_lengths)
print(round(mean_petal_length, 1))
