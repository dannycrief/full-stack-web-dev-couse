from bottle import route
from bottle import run


def fib(n):
    a, b = 1, 1
    for x in range(n):
        a, b = b, a + b
    return a


@route("/fib/<n:int>")
def fib_handler(n):
    result = fib(n)
    return str(result)


if __name__ == '__main__':
    run(host="localhost", port=8080, debug=True)