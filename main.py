from app.tasks import add_task, get_tasks, delete_task, mark_complete
import argparse
def handle_args():
    parser = argparse.ArgumentParser(description="Task Manager CLI")

    parser.add_argument("command", nargs="?", help="Command (add, list, delete, complete)")
    parser.add_argument("value", nargs="?", help="Task title or ID")
    parser.add_argument("--priority", default="medium", help="Task priority")

    args = parser.parse_args()

    return args
def show_menu():
    print("\n==== Task Manager ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task Complete")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter task title: ")
            priority = input("Enter priority (low/medium/high): ").lower()
            if priority not in ["low", "medium", "high"]:
                print("Invalid priority. Defaulting to medium.")
                priority = "medium"
            add_task(title, priority)
            print("Task added!")
        elif choice == "2":
            tasks = get_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                for task in tasks:
                    status = "✔" if task["completed"] else "✘"
                    print(f'{task["id"]}. {task["title"]} [{status}] (Priority: {task.get("priority", "medium")})')
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
                print("Task deleted!")
            except:
                print("Invalid ID")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to mark complete: "))
                result = mark_complete(task_id)
                if result:
                    print("Task marked as complete!")
                else:
                    print("Task not found.")
            except:
                print("Invalid ID")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    args = handle_args()

    if args.command:

        if args.command == "add":
            add_task(args.value, args.priority)
            print("Task added!")

        elif args.command == "list":
            tasks = get_tasks()
            for task in tasks:
                status = "✔" if task["completed"] else "✘"
                print(f'{task["id"]}. {task["title"]} [{status}] (Priority: {task.get("priority", "medium")})')

        elif args.command == "delete":
            delete_task(int(args.value))
            print("Task deleted!")

        elif args.command == "complete":
            mark_complete(int(args.value))
            print("Task completed!")

        else:
            print("Unknown command")

    else:
        main()

