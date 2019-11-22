from bottle import route
from bottle import run


@route("/hello/")
def hello_world():
    return "Hello, World!"


@route("/upper/<param>")
def upper(param):
    return param.upper()


if __name__ == '__main__':
    run(host="localhost", port=8080, debug=True)