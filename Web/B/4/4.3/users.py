import json
import os
import uuid

DATA_FILE_PATH = "users.json"


def read():
    if not os.path.exists(DATA_FILE_PATH):
        return []

    with open(DATA_FILE_PATH) as fd:
        users = json.load(fd)
    return users


def save(users):
    with open(DATA_FILE_PATH, "w") as fd:
        json.dump(users, fd)


def find(users):
    name = input("Введи имя пользователя для поиска: ")
    for user in users:
        if user["first_name"] == name:
            return user["id"]


def valid_email(email):
    if email.count('@') == 1:
        if len(email.split('@')) > 1 and '.' in email.split('@')[-1]:
            return True
        else:
            return False
    else:
        return False


def request_data():
    print("Привет! Я запишу твои данные!")
    first_name = input("Введи своё имя: ")
    last_name = input("А теперь фамилию: ")
    email = valid_email(input("Мне еще понадобится адрес твоей электронной почты: "))
    user_id = str(uuid.uuid4())
    user = {
        "id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }
    return user


def main():
    users_list = read()
    mode = input("Выбери режим.\n1 - найти пользователя по имени\n2 - ввести данные нового пользователя\n")
    if mode == "1":
        user_id = find(users_list)
        if user_id:
            print("Найден пользователь с идентификатором: ", user_id)
        else:
            print("Такого пользователя нет.")
    elif mode == "2":
        user = request_data()
        users_list.append(user)
        save(users_list)
        print("Спасибо, данные сохранены!")
    else:
        print("Некорректный режим:(")


if __name__ == "__main__":
    main()
