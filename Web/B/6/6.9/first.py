from bottle import route, HTTPError, run, request


@route("/add")
def add():
    try:
        x = int(request.query.x)
        y = int(request.query.y)
    except ValueError:
        result = HTTPError(400, "Uncorrect parameter")
    else:
        s = x + y
        result = "The sum of {} and {} is {}".format(x, y, s)
    return result


if __name__ == '__main__':
    run(host="localhost", port=8080, debug=True)


"""
answers:
1-&
2-?
3-request
"""