import sys
from storage import load_tasks
from commands import list_tasks, add_task, complete_task


def main():
    tasks = load_tasks()

    if len(sys.argv) < 2:
        list_tasks(tasks)
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print('Usage: python todo.py add "Task description"')
            return

        task_text = " ".join(sys.argv[2:])
        add_task(tasks, task_text)

    elif command == "complete":
        if len(sys.argv) != 3:
            print("Usage: python todo.py complete <task_number>")
            return

        try:
            task_number = int(sys.argv[2])
        except ValueError:
            print("Task number must be an integer.")
            return

        complete_task(tasks, task_number)

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()