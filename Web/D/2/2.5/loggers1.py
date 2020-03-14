import logging
import os

logger = logging.getLogger()

logging.basicConfig(filename='test.log')

logger.debug("Debug test message")
logger.info("Info test message")
logger.warning("[{}] Warning test message".format(os.path.basename(__file__)))
logger.error("Error test message")
logger.critical("Critical test message")
