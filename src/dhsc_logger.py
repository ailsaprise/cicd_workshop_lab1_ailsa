import logging
import logging.config
from pathlib import Path

import colorama


class ColouredFormatter(logging.Formatter):
    """
    A custom logging formatter to add colours to log messages based on level.
    Attributes:
        RESET (str): ANSI escape code to reset color formatting.
        COLORS (dict): Mapping of log levels to their corresponding ANSI colour codes.
    Methods:
        format(record):
            Formats the specified record as text, adding colour based on the log level.
    """

    RESET = "\033[0m"
    COLOURS = {
        "DEBUG": "\033[94m",  # Blue
        "INFO": "\033[92m",  # Green
        "WARNING": "\033[93m",  # Yellow
        "ERROR": "\033[91m",  # Red
        "CRITICAL": "\033[95m",  # Magenta
    }

    def format(self, record):
        message = super().format(record)
        return f"{self.COLOURS.get(record.levelname, self.RESET)}{message}{self.RESET}"


def configure_dhsc_logger(filepath: Path = Path("outputs", "log.txt")):
    """
    Configure logging to use nicer DHSC defaults. Logging will write
    to both stdout and to file.

    Args:
        filepath (Path): Path to save log file. Defaults to "./outputs/log.txt"
    """

    colorama.init()

    LOGGER_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "detailed": {
                "class": "logging.Formatter",
                "format": "%(asctime)s [%(levelname)s] %(message)s (%(name)s)",
            },
            "pretty": {
                "class": f"{__name__}.ColouredFormatter",
                "format": "[%(levelname)s] %(message)s",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "pretty",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": filepath,
                "formatter": "detailed",
            },
        },
        "loggers": {
            "": {
                "level": "INFO",
                "handlers": ["file", "console"],
            }
        },
    }

    logging.config.dictConfig(LOGGER_CONFIG)
