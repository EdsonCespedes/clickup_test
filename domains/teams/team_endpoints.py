from core.request_manager import RequestManager

class TeamEndpoints:
    """
    Endpoint handler for all Workspace (Teams) related API requests.
    """

    def __init__(self) -> None:
        self.request_manager = RequestManager()
        self.endpoint = "/team"

    def get_teams(self):
        """
        Retrieve all Workspaces associated with the authenticated user.
        """
        return self.request_manager.send_request(
            "GET",
            self.endpoint,
        )