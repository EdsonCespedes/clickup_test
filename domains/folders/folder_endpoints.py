from core.request_manager import RequestManager

class FolderEndpoints:
    def __init__(self):
        self.req = RequestManager()

    def create_folder(self, space_id: str, payload: dict):
        return self.req.send_request("POST", f"/space/{space_id}/folder", payload=payload)
        
    def get_folder(self, folder_id: str):
        return self.req.send_request("GET", f"/folder/{folder_id}")

    def update_folder(self, folder_id: str, payload: dict):
        return self.req.send_request("PUT", f"/folder/{folder_id}", payload=payload)

    def delete_folder(self, folder_id: str):
        return self.req.send_request("DELETE", f"/folder/{folder_id}")