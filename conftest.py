import pytest

from config.settings import app_settings
from core.logger import logger
from core.request_manager import RequestManager
from domains.teams.team_endpoints import TeamEndpoints


@pytest.fixture(scope="session", autouse=True)
def setup_session():
    """
    Before/After Session Hook:

    Automatically executed once per test execution.
    Initializes the HTTPX client and loads the application configuration.
    """

    logger.info("=== Starting Test Session ===")

    req_manager = RequestManager()

    req_manager.initialize(
        base_url=app_settings.clickup_api_url,
        token=app_settings.clickup_api_token,
    )

    yield req_manager

    logger.info("...... Finishing Test Session........")

    req_manager.close()



@pytest.fixture(scope="session")
def global_team_id(setup_session):
    """
    Dynamically retrieves the user's primary Workspace ID.

    Executed only once per test session.
    """

    team_api = TeamEndpoints()

    response = team_api.get_teams()

    assert response.status_code == 200, (
        "Failed to retrieve global Team ID"
    )

    data = response.json()
    teams = data.get("teams", [])

    assert len(teams) > 0, (
        "The ClickUp account does not have any associated Workspaces"
    )

    return teams[0]["id"]