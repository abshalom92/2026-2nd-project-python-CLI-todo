from storage import save_tasks

def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "X" if task["done"] else " "
        print(f"{index}. [{status}] {task['text']}")


def add_task(tasks, text):
    task = {
        "text": text,
        "done": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f'Added tasks: "{text}"')


def complete_task(tasks, task_number):
    index = task_number - 1

    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return
    
    tasks[index]["done"] = True
    save_tasks(tasks)
    print(f"Marked task {task_number} as complete.")

