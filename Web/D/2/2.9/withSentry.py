import sentry_sdk

from bottle import Bottle, run
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://8a9946ca5bb44bac8ee186f0a67b564d@sentry.io/4645088",
    integrations=[BottleIntegration()]
)

app = Bottle()


@app.route('/')
def index():
    raise RuntimeError("There is an error!")
    return


app.run(host='localhost', port=8080)


