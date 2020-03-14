import logging

logger = logging.getLogger('my-logger')
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")
handler.setFormatter(formatter)

logger.setLevel(logging.DEBUG)
handler.setLevel(logging.DEBUG)

logger.addHandler(handler)

logger.debug("Verifying that DEBUG messages are processed by both the logger and the handler")
logger.info("INFO Level Test Message")
logger.error("Another message, but already ERROR")
