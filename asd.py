import logging

logger = logging.getLogger("First Logger")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug('Logged Debug Message')
logger.info('Logged Info Message')
logger.warning('Logged Warning Message')
logger.error('Logged Error Message')
