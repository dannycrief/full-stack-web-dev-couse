import sentry_sdk
import os
from bottle import route, run
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://a369267ec27543ac82652b80d8d7e417@sentry.io/5167644",
    integrations=[BottleIntegration()]
)


@route('/')
def index():
    html = """
    <!doctype html>
    <html lang="en">
      <head>
        <title>Heroku Logs</title>
      </head>
      <body>
        <div class="container">
            <h1>Usage:</h1>
            <p class="small">To see success page click <a href="https://glacial-sea-00294.herokuapp.com/success">here</a></p>
            <p class="small">To see error page click <a href="https://glacial-sea-00294.herokuapp.com/fail  ">here</a></p>
        </div>
      </body>
    </html>
    """
    return html


@route('/success')
def success():
    return


@route('/fail')
def fail():
    raise RuntimeError("There is an RunTimeError!")


if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
