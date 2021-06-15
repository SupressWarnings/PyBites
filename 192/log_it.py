import logging
from typing import Callable

LOGGER = logging.getLogger("pybites_logger")

DEBUG = lambda msg: LOGGER.debug(msg)
INFO = lambda msg: LOGGER.info(msg)
WARNING = lambda msg: LOGGER.warning(msg)
ERROR = lambda msg: LOGGER.error(msg)
CRITICAL = lambda msg: LOGGER.critical(msg)


def log_it(level: Callable, msg: str) -> None:
    level(msg)


if __name__ == "__main__":
    log_it(DEBUG, "This is a debug message.")
    log_it(INFO, "This is an info message.")
    log_it(WARNING, "This is a warning message.")
    log_it(ERROR, "This is an error message.")
    log_it(CRITICAL, "This is a critical message.")
