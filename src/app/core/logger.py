import logging


def init_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(levelname)s:     %(name)s     %(message)s')
    consoleHandler.setFormatter(formatter)
    logger.addHandler(consoleHandler)
