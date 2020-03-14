import logging
import random


class MyFilter:
    def filter(self, logRecord):
        return logRecord.levelno == logging.INFO


# creating formatter, getting logger and give it DEBUG lvl
formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger('my-logger')
logger.setLevel(logging.DEBUG)

# Configuration for handler to print messages on console
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)

# One more handler to react on INFO lvl messages and write them into info.log
file_handler = logging.FileHandler(filename='info.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
file_handler.addFilter(MyFilter())

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


levels = ['debug', 'info', 'error', 'critical']

for _ in range(10):
    level = random.choice(levels)
    eval('logger.{level}("test message with {level} level")'.format(level=level))
