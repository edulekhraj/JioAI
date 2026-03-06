import logging
import os

def get_logger():

    logger = logging.getLogger("AutomationLogger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)

        file_handler = logging.FileHandler(f"{log_dir}/test.log")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger