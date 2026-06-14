from storage import load_tasks, save_tasks
from models import create_task
from utils import now


def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def add_task(description):
    tasks = load_tasks()

    task = create_task(get_next_id(tasks), description)

    tasks.append(task)
    save_tasks(tasks)

    print(f"Task added successfully (ID: {task['id']})")


def update_task(task_id, description):
    tasks = load_tasks()
    task = find_task_by_id(tasks, task_id)

    if task is None:
        print("Error: Task not found")
        return

    task["description"] = description
    task["updated_at"] = now()

    save_tasks(tasks)
    print("Task updated successfully")


def delete_task(task_id):
    tasks = load_tasks()
    task = find_task_by_id(tasks, task_id)

    if task is None:
        print("Error: Task not found")
        return

    tasks.remove(task)
    save_tasks(tasks)

    print("Task deleted successfully")


def mark_task(task_id, status):
    tasks = load_tasks()
    task = find_task_by_id(tasks, task_id)

    if task is None:
        print("Error: Task not found")
        return

    task["status"] = status
    task["updated_at"] = now()

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
            f"Created: {task.get('created_at', 'N/A')} "
            f"Updated: {task.get('updated_at', 'N/A')}"
        )