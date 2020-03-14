import logging
import os

handler = logging.FileHandler(filename='test.log')
handler.setLevel(logging.DEBUG)

logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.debug("[{}] Debug test message".format(os.path.basename(__file__)))
logger.info("Info test message")
logger.warning("Warning test message")
logger.error("Error test message")
logger.critical("Critical test message")
