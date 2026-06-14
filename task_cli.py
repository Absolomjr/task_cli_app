import sys
import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exits(FILE_NAME):
        return []
    
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
    
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def now():
    return datetime.now().isoformat(timespec="seconds")

def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

def add_task(description):
    tasks = load_tasks()
    
    task = {
        "id": get_next_id(tasks),
        "description": description,
        "status": "todo",
        "created_at": now(),
        "updated_at": now()
    }
    tasks.append(task)
    save_tasks(tasks)
    
    print(f"Task added successfully (ID: {task['id']})")
    
    
def update_task(task_id, description):
    tasks = load_tasks()
    task = find_task(tasks, task_id)

    if task is None:
        print("Error: Task not found")
        return

    task["description"] = description
    task["updatedAt"] = now()

    save_tasks(tasks)
    print("Task updated successfully")
    

def delete_task(task_id):
    tasks = load_tasks()
    task = find_task(tasks, task_id)

    if task is None:
        print("Error: Task not found")
        return

    tasks.remove(task)
    save_tasks(tasks)
    print("Task deleted successfully")
    
def mark_task(task_id, status):
    tasks = load_tasks()
    task = find_task(tasks, task_id)

    if task is None:
        print("Error: Task not found")
        return

    task["status"] = status
    task["updatedAt"] = now()

    save_tasks(tasks)
    print(f"Task marked as {status}")
    
def list_tasks(status=None):
    tasks = load_tasks()

    if status:
        tasks = [task for task in tasks if task["status"] == status]

    if not tasks:
        print("No tasks found")
        return

    for task in tasks:
        print(
            f"{task['id']}. {task['description']} "
            f"[{task['status']}] "
            f"Created: {task['createdAt']} "
            f"Updated: {task['updatedAt']}"
        )

def show_help():
    print("""
Usage:
  python task_cli.py add "Task description"
  python task_cli.py update <id> "New description"
  python task_cli.py delete <id>
  python task_cli.py mark-in-progress <id>
  python task_cli.py mark-done <id>
  python task_cli.py list
  python task_cli.py list done
  python task_cli.py list todo
  python task_cli.py list in-progress
""")
    
def main():
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1]
    
    try:
        if command == "add":
            if len(sys.argv) < 3:
                print("Error: Task description is required")
                return
            add_task(sys.argv[2])
            
        elif command == "update":
            if len(sys.argv) < 4:
                print("Error: Task ID and new description are required")
                return
            update_task(int(sys.argv[2]), sys.argv[3])
            
        elif command == "delete":
            if len(sys.argv) < 3:
                print("Error: Task ID is required")
                return
            delete_task(int(sys.argv[2]))
            
        elif command == "mark-in-progress":
            if len(sys.argv) < 3:
                print("Error: Task ID is required")
                return
            mark_task(int(sys.argv[2]), "in-progress")
            
        elif command == "mark-done":
            if len(sys.argv) < 3:
                print("Error: Task ID is required")
                return
            mark_task(int(sys.argv[2]), "done")
            
        elif command == "list":
            if len(sys.argv) == 2:
                list_tasks()
            else:
                list_tasks(sys.argv[2])
                if status not in ["todo", "in-progress", "done"]:
                    print("Error: Invalid status")
                    return
                list_tasks(status)
                
        else:
            print("Error: Unknown command")
            show_help()
            
    except ValueError:
        print("Error: Task ID must be an integer")
        
if __name__ == "__main__":
    main()
    
    