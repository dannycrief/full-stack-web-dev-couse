import bottle

import sys

sys.path.insert(0, r'/home/danny/Full-stack Pytho web developer/Web/C/2/2.9/backend')
from appp.server import app


if __name__ == "__main__":
    bottle.run(
        app=app, host=app.config.host, port=app.config.port, server=app.config.server
    )