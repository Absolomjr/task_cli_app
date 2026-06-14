from utils import now


def create_task(task_id, description):
    return {
        "id": task_id,
        "description": description,
        "status": "todo",
        "created_at": now(),
        "updated_at": now()
    }