import json
import os
import sys

def load_tasks():
    if not os.path.exists("tasks.json"):
        return []

    with open("tasks.json", "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)

def add_tasks(tasks, text):
    task = {
        "text": text,
        "done": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f'Added task: "{text}"')

def complete_task(tasks, task_number):
    index = task_number - 1
    
    if index < 0 or index >= len(tasks):
        print("Invalid task number. Double check your input based on the list of tasks.")
        return

    tasks[index]["done"] = True
    save_tasks(tasks)
    print(f'Marked task {task_number} as complete.')


def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    
    for index, task in enumerate(tasks, start=1):
        status="X" if task["done"] else " "
        print(f"{index}. [{status}] {task['text']}")



def main():
    tasks = load_tasks()
    if len(sys.argv) < 2:
        list_tasks(tasks)
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python todo.py add \"Task decription\"")
            return

        task_text = " ".join(sys.argv[2:])
        add_tasks(tasks, task_text)

    elif command == "complete":
        if len(sys.argv) != 3:
            print("Usage: python3 todo.py complete <task_number>")
            return

        try:
            task_number = int(sys.argv[2])
        except ValueError:
            print("Task number must be an integer.")
            return

        complete_task(tasks, task_number)


    else:
        print(f"Unknown command: {command}")



    

if __name__== "__main__":
    main()