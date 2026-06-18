import pytest
import pytest_check as check

from core.logger import logger
from domains.teams.team_endpoints import TeamEndpoints
from domains.teams.team_schemas import GetTeamsResponse


@pytest.mark.smoke
def test_get_teams_successfully():
    """
    Verify that the user can successfully retrieve their Workspaces (Teams).

    Validates:
    - HTTP status code
    - Response data integrity
    - Pydantic schema validation
    """

    # 1. Arrange
    team_api = TeamEndpoints()

    # 2. Act
    response = team_api.get_teams()

    # 3. Assert: Status Code
    assert response.status_code == 200, (
        f"Expected status code 200, but received {response.status_code}"
    )

    # 4. Assert: Schema Validation
    data = response.json()
    validated_data = GetTeamsResponse.model_validate(data)

    # 5. Assert: Data Integrity
    check.is_true(
        len(validated_data.teams) > 0,
        "The user does not have any assigned team/workspace",
    )

    if validated_data.teams:
        team_id = validated_data.teams[0].id

        logger.info(
            "Test completed successfully. Main Team ID: %s",
            team_id,
        )

        check.is_not_none(
            team_id,
            "The Team ID should not be null",
        )
