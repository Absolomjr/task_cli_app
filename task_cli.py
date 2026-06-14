import sys

from task_service import (
    add_task,
    update_task,
    delete_task,
    mark_task,
    list_tasks
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
                return

            status = sys.argv[2]

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