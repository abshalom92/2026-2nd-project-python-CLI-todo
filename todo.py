import argparse
from storage import load_tasks
from commands import list_tasks, add_task, complete_task

def create_parser():
    parser = argparse.ArgumentParser(
        description = "Simple command-line to-do application"
    )

    subparsers = parser.add_subparsers(dest = "command", required = True)

    #list command

    subparsers.add_parser("list", help="List all tasks")

    #add command

    add_parser = subparsers.add_parser("add", help="Add a task")
    add_parser.add_argument("text", nargs = "+", help="Task description")

    #complete command

    complete_parser = subparsers.add_parser(
        "complete", help="Mark a task as complete"
    )
    complete_parser.add_argument(
        "task_number", type=int, help="Task number to complete"
    )

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    tasks = load_tasks()

    if args.command == "list":
        list_tasks(tasks)

    elif args.command == "add":
        task_text = " ".join(args.text)
        add_task(tasks, task_text)

    elif args.command == "complete":
        complete_task(tasks, args.task_number)

if __name__ == "__main__":
    main()