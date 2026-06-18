import pytest
import pytest_check as check

from core.logger import logger
from domains.spaces.space_endpoints import SpaceEndpoints
from domains.spaces.space_payloads import SpacePayloads
from domains.spaces.space_schemas import SpaceSchema


@pytest.fixture(scope="function")
def space_lifecycle(global_team_id):
    """
    Setup and cleanup fixture.

    Creates a Space before the test execution and deletes it after completion.
    """

    api = SpaceEndpoints()
    payload = SpacePayloads.build_create_space_payload()

    # SETUP: Create resource
    response = api.create_space(
        global_team_id,
        payload,
    )

    assert response.status_code == 200, (
        "Setup failed: Unable to create Space"
    )

    space_data = response.json()
    space_id = space_data["id"]

    yield {
        "api": api,
        "space_id": space_id,
        "initial_data": space_data,
        "team_id": global_team_id,
    }

    # Delete resource
    logger.info(
        "Cleaning resources: Deleting Space %s",
        space_id,
    )

    api.delete_space(space_id)


@pytest.mark.functional
def test_create_and_validate_space(global_team_id):
    """
    Verify successful Space creation (Create).
    """

    api = SpaceEndpoints()

    payload = SpacePayloads.build_create_space_payload(
        name="Framework_Test_Space"
    )

    response = api.create_space(
        global_team_id,
        payload,
    )

    # Hard Assertion: Status Code
    assert response.status_code == 200

    data = response.json()

    # Schema Validation
    SpaceSchema.model_validate(data)

    # Soft Assertions: Data Integrity
    check.equal(
        data["name"],
        payload["name"],
        "Space name does not match",
    )

    check.is_false(
        data["private"],
        "Space should not be private by default",
    )

    # Manual cleanup for this specific test
    api.delete_space(data["id"])


@pytest.mark.functional
def test_get_space(space_lifecycle):
    """
    Verify retrieval of an existing Space (Read).
    """

    api = space_lifecycle["api"]
    space_id = space_lifecycle["space_id"]
    initial_name = space_lifecycle["initial_data"]["name"]

    response = api.get_space(space_id)

    assert response.status_code == 200

    data = response.json()

    SpaceSchema.model_validate(data)

    check.equal(
        data["id"],
        space_id,
    )

    check.equal(
        data["name"],
        initial_name,
    )


@pytest.mark.functional
def test_update_space(space_lifecycle):
    """
    Verify update of an existing Space (Update).
    """

    api = space_lifecycle["api"]
    space_id = space_lifecycle["space_id"]

    payload = SpacePayloads.build_update_space_payload()

    response = api.update_space(
        space_id,
        payload,
    )

    assert response.status_code == 200

    data = response.json()

    SpaceSchema.model_validate(data)

    check.equal(
        data["name"],
        payload["name"],
        "Space name was not updated",
    )


@pytest.mark.functional
def test_delete_space(global_team_id):
    """
    Verify Space deletion (Delete).
    """

    api = SpaceEndpoints()

    # 1. Create a temporary Space to delete
    payload = SpacePayloads.build_create_space_payload()

    create_response = api.create_space(
        global_team_id,
        payload,
    )

    assert create_response.status_code == 200

    space_id = create_response.json()["id"]

    # 2. Delete the Space
    delete_response = api.delete_space(space_id)

    assert delete_response.status_code == 200

    check.equal(
        delete_response.json(),
        {},
        "Delete response body should be empty",
    )

    # 3. Verify the resource no longer exists
    get_response = api.get_space(space_id)

    check.equal(
        get_response.status_code,
        404,
        "Deleted Space should return 404 Not Found",
    )

    check.is_in(
        "Space not found",
        get_response.text,
    )