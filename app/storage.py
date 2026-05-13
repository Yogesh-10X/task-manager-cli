import json
from config import config
from app.logger import logger

FILE_PATH = config["data_file"]

def load_tasks():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        logger.warning("Tasks file not found. Returning empty list.")
        return []
    except json.JSONDecodeError:
        logger.error("Tasks JSON file is corrupted.")
        return []

def save_tasks(tasks):
    try:
        with open(FILE_PATH, "w") as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        logger.error(f"Failed to save tasks: {e}")