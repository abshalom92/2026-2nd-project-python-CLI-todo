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

def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    
    for index, task in enumerate(tasks, start=1):
        status="X" if task["done"] else " "
        print(f"{index}. [{status}] {task['text']}")



def main():
    tasks = load_tasks()
    list_tasks(tasks)



    

if __name__== "__main__":
    main()