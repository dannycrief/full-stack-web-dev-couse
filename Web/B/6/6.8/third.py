from bottle import route
from bottle import HTTPError  # Импортируем класс HTTPError
from bottle import run


@route("/modify/<param>/<method>")
def modify(param, method):
    # проверяем переданный модификатор и готовим соответствующий результат
    if method == "upper":
        result = param.upper()
    elif method == "lower":
        result = param.lower()
    elif method == "title":
        result = param.title()
    else:
        result = HTTPError(400, "incorrect `method` value")
    return result


if __name__ == '__main__':
    run(host="localhost", port=8080, debug=True)