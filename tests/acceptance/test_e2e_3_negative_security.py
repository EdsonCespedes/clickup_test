import pytest
import pytest_check as check

from core.request_manager import RequestManager
from domains.tasks.task_endpoints import TaskEndpoints
from domains.tasks.task_payloads import TaskPayloads


@pytest.mark.acceptance
def test_e2e_negative_and_security(global_team_id):
    task_api = TaskEndpoints()

    # Scenario A: Security
    req_manager = RequestManager()
    original_token = req_manager._headers["Authorization"]
    req_manager._headers["Authorization"] = "invalid_token_123"

    try:
        res_401 = task_api.get_task("any_id")
        check.equal(res_401.status_code, 401)

    finally:
        req_manager._headers["Authorization"] = original_token

    # Scenario B: Non-existent resource / Unauthorized access
    fake_list_id = "9999999999"
    res_error = task_api.create_task(
        fake_list_id,
        TaskPayloads.build_create_task_payload()
    )

    assert res_error.status_code in [401, 404]
