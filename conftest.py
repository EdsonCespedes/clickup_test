import pytest

from config.settings import app_settings
from core.logger import logger
from core.request_manager import RequestManager
from domains.teams.team_endpoints import TeamEndpoints
from domains.spaces.space_endpoints import SpaceEndpoints
from domains.spaces.space_payloads import SpacePayloads


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


@pytest.fixture(scope="session")
def shared_e2e_space(global_team_id, worker_id):
    """
    Creates a single shared Space per worker for E2E tests.
    Using worker_id prevents 'name already exists' conflicts across workers
    and keeps total spaces under the free plan limit.
    """
    logger.info(f"[{worker_id}] === Creating Shared Space for E2E Tests ===")
    
    api = SpaceEndpoints()
    # Name is dynamic per execution thread
    payload = SpacePayloads.build_create_space_payload(name=f"Shared_E2E_Root_{worker_id}")
    
    response = api.create_space(global_team_id, payload)
    
    assert response.status_code == 200, (
        f"Failed to create shared Space: {response.text}"
    )
    
    space_id = response.json()["id"]
    
    # Yield the ID to the tests running on this specific worker
    yield space_id
    
    # Teardown at the end of the session for this worker
    logger.info(f"[{worker_id}] === E2E Cleanup: Deleting Shared Space {space_id} ===")
    api.delete_space(space_id)