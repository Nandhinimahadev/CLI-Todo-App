import json
import argparse
import os

TODO_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print(f"✅ Task added: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{idx}. {status} {task['description']}")

def mark_done(index):
    tasks = load_tasks()
    try:
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"✔️ Task {index} marked as done.")
    except IndexError:
        print("❗ Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Deleted task: {removed['description']}")
    except IndexError:
        print("❗ Invalid task number.")

def main():
    parser = argparse.ArgumentParser(description="📋 CLI Todo App")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Task description")

    # List command
    subparsers.add_parser("list", help="List all tasks")

    # Done command
    parser_done = subparsers.add_parser("done", help="Mark a task as done")
    parser_done.add_argument("index", type=int, help="Task number")

    # Delete command
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("index", type=int, help="Task number")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        mark_done(args.index)
    elif args.command == "delete":
        delete_task(args.index)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
