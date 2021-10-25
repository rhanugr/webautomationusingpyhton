import logging


logger = logging.getLogger(__name__)
logger.addHandler()   #File handler object

logger.debug("Debug statement has been executed")
logger.info("Information statement")
logger.warning("Something in Warning mode")
logger.error("A Major Error")
logger.critical("Critical issues")
