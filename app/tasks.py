from app.storage import load_tasks, save_tasks
from config import config
from logger import logger
tasks = load_tasks()
def add_task(title, priority=config["default_priority"]):
    if not title or title.strip() == "":
        logger.warning("Attempted to add empty task")
        return None
    if priority not in ["low", "medium", "high"]:
        logger.warning(f"Invalid priority given: {priority}, defaulting")
        priority = config["default_priority"]
    global tasks
    if tasks:
        new_id = max(task["id"] for task in tasks) + 1
    else:
        new_id = 1
    task = {
        "id": new_id,
        "title": title,
        "completed": False,
        "priority": priority
    }
    tasks.append(task)
    logger.info(f"Task added: {title}")
    save_tasks(tasks)
    return task
def get_tasks():
    return tasks
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    logger.info(f'Task deleted: {task_id}')
def mark_complete(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            logger.info(f'Task completed: {task_id}')
            return task
    return None
