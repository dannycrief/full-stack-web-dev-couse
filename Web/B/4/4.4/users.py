import json
import os
import uuid

USER_DATA_FILE_PATH = "users.json"
LOG_DATA_FILE_PATH = "last_seen_log.json"

class Users:
    def __init__(self):
        self.users = self.read()

    def read(self):
        if not os.path.exists(USER_DATA_FILE_PATH):
            return []
        with open(USER_DATA_FILE_PATH) as fd:
            users = json.load(fd)
        return users

    def save(self):
        with open(USER_DATA_FILE_PATH) as fd:
            json.dump(self.users, fd)

    def find(self):
        for user in self.users:
            if user["first_name"] == name:
                return user["id"]

    def add_user(self, user_data):
        self.users.append(user_data)
        self.save()

    def valid_email(self, email):
        if email.count('@') == 1:
            if len(email.split('@')) > 1 and '.' in email.split('@')[-1]:
                return True
            else:
                return False
        else:
            return False

    def request_data(self):
        print("Hello, I need to know you")
        first_name = input("What's your name? ")
        last_name = input("What's your surname? ")
        email = valid_email(input("Email: "))
        user_id = str(uuid.uuid4())
        user = {
            "id": user_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email
        }
        return user


def main():
    """
    Осуществляет взаимодействие с пользователем, обрабатывает пользовательский ввод
    """
    users = Users()
    # просим пользователя выбрать режим
    mode = input("Выбери режим.\n1 - найти пользователя по имени\n2 - ввести данные нового пользователя\n")
    # проверяем режим
    if mode == "1":
        # выбран режим поиска, запускаем его
        name = input("Введи имя пользователя для поиска: ")
        user_id = users.find(Users.name)
        if user_id:
            print("Найден пользователь с идентификатором: ", user_id)
        else:
            print("Такого пользователя нет.")
    elif mode == "2":
        user_data = Users.request_data()
        # добавляем нового пользователя в список всех пользователей
        users.add_user(user_data)
        print("Спасибо, данные сохранены!")
    else:
        print("Некорректный режим:(")



