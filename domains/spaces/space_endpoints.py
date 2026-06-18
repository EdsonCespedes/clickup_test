from core.request_manager import RequestManager


class SpaceEndpoints:
    """Handles all HTTP requests related to Spaces."""

    def __init__(self):
        self.req = RequestManager()

    def create_space(self, team_id: str, payload: dict):
        return self.req.send_request(
            "POST",
            f"/team/{team_id}/space",
            payload=payload,
        )

    def get_space(self, space_id: str):
        return self.req.send_request(
            "GET",
            f"/space/{space_id}",
        )

    def update_space(self, space_id: str, payload: dict):
        return self.req.send_request(
            "PUT",
            f"/space/{space_id}",
            payload=payload,
        )

    def delete_space(self, space_id: str):
        return self.req.send_request(
            "DELETE",
            f"/space/{space_id}",
        )
