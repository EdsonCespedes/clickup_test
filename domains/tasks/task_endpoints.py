from core.request_manager import RequestManager

class TaskEndpoints:
    def __init__(self):
        self.req = RequestManager()

    def create_task(self, list_id: str, payload: dict):
        return self.req.send_request("POST", f"/list/{list_id}/task", payload=payload)
        
    def get_task(self, task_id: str):
        return self.req.send_request("GET", f"/task/{task_id}")

    def update_task(self, task_id: str, payload: dict):
        return self.req.send_request("PUT", f"/task/{task_id}", payload=payload)
        
    def delete_task(self, task_id: str):
        return self.req.send_request("DELETE", f"/task/{task_id}")