from core.request_manager import RequestManager


class ListEndpoints:
    def __init__(self):
        self.req = RequestManager()

    def create_list(self, parent_id: str, payload: dict, is_folderless: bool = False):
        """
        Creates a list.
        By default, it is created inside a Folder.
        If is_folderless is True, it is created directly in the Space.
        """
        if is_folderless:
            return self.req.send_request(
                "POST",
                f"/space/{parent_id}/list",
                payload=payload
            )

        return self.req.send_request(
            "POST",
            f"/folder/{parent_id}/list",
            payload=payload
        )

    def get_list(self, list_id: str):
        return self.req.send_request("GET", f"/list/{list_id}")

    def delete_list(self, list_id: str):
        return self.req.send_request("DELETE", f"/list/{list_id}")