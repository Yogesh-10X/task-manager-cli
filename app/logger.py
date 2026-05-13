import logging
from config import config
logger = logging.getLogger("task_manager")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(
    config["log_file"],
    encoding="utf-8"
)
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)
if not logger.handlers:
    logger.addHandler(file_handler)