import pytest
import pytest_check as check

from core.logger import logger
from domains.lists.list_endpoints import ListEndpoints
from domains.lists.list_payloads import ListPayloads
from domains.tasks.task_endpoints import TaskEndpoints
from domains.tasks.task_payloads import TaskPayloads


@pytest.mark.acceptance
def test_e2e_state_tracking(shared_e2e_space):
    """HLTC 2: State tracking (Folderless List -> Task)."""
    list_api = ListEndpoints()
    task_api = TaskEndpoints()

    # List directly in the Space
    l_res = list_api.create_list(
        shared_e2e_space,
        ListPayloads.build_create_list_payload(name="State_Tracking_List"),
        is_folderless=True
    )
    assert l_res.status_code == 200
    list_id = l_res.json()["id"]

    # Act: Create initial Task
    task_payload = TaskPayloads.build_create_task_payload(name="Tracking Task")
    task_res = task_api.create_task(list_id, task_payload)
    task_id = task_res.json()["id"]

    # Act: Update Status
    logger.info(f"Updating task status {task_id}")

    update_res = task_api.update_task(
        task_id,
        TaskPayloads.build_update_task_payload(new_status="complete")
    )
    assert update_res.status_code == 200

    updated_data = update_res.json()
    check.equal(updated_data["status"]["status"], "complete")
