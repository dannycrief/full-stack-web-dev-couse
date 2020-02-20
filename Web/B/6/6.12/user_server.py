import json

from bottle import route, run, HTTPError, request


def save_user(user_data):
    first_name = user_data["first_name"]
    last_name = user_data["last_name"]
    filename = "{}-{}.json".format(first_name, last_name)

    with open(filename, "w") as fd:
        json.dump(user_data, fd)
    return filename


@route("/user", method="POST")
def user():
    user_data = {
        "first_name": request.forms.get("first_name"),
        "last_name": request.forms.get("last_name"),
        "birthdate": request.forms.get("birthdate")
    }
    resource_path = save_user(user_data)
    print("User saved ad: ", resource_path)

    return "Your data has been successfully saved."


if __name__ == '__main__':
    run(host="localhost", port=8080, debug=True)