import os
import random

from bottle import route, run

import sayings


def generate_message():
    phrase = ''
    for i in (sayings.beginnings, sayings.subjects, sayings.verbs, sayings.actions, sayings.ends):
        phrase += random.choice(i) + ' '
    return phrase


@route("/")
def index():
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Генератор утверждений</title>
  </head>
  <body>
    <div class="container">
      <h1>Коллеги, добрый день!</h1>
      <p>{}</p>
      <p class="small">Чтобы обновить это заявление, обновите страницу</p>
    </div>
  </body>
</html>
""".format(
        generate_message()
    )
    return html


@route("/api/roll/<some_id:int>")
def example_api_response(some_id):
    return {"requested_id": some_id, "random_number": random.randrange(some_id)}


@route('/api/generate/')
def get_message():
    return {'message': generate_message()}


@route('/api/generate/<num:int>')
def get_message_num(num):
    return {'messages': [generate_message() for i in range(num)]}


if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
