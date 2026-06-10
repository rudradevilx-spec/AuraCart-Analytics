import logging
from pathlib import Path

from app.utils.constants import (
    DEFAULT_LOG_FILE
)


class AuraLogger:

    _logger = None

    @classmethod
    def get_logger(cls):

        if cls._logger:

            return cls._logger

        Path("logs").mkdir(
            exist_ok=True
        )

        logger = logging.getLogger(
            "AuraCart"
        )

        logger.setLevel(
            logging.INFO
        )

        if not logger.handlers:

            file_handler = (
                logging.FileHandler(
                    DEFAULT_LOG_FILE,
                    encoding="utf-8"
                )
            )

            formatter = (
                logging.Formatter(
                    "%(asctime)s | "
                    "%(levelname)s | "
                    "%(message)s"
                )
            )

            file_handler.setFormatter(
                formatter
            )

            logger.addHandler(
                file_handler
            )

        cls._logger = logger

        return logger