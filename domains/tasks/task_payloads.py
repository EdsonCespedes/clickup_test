from helpers.random_generator import generate_random_name

class TaskPayloads:
    @staticmethod
    def build_create_task_payload(name: str = None, description: str = "Test Description") -> dict:
        return {
            "name": name or generate_random_name("Task"),
            "description": description,
            "status": "to do"
        }

    @staticmethod
    def build_update_task_payload(new_status: str) -> dict:
        return {
            "status": new_status
        }