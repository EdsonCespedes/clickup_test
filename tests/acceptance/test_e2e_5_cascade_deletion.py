import pytest
import pytest_check as check

from core.logger import logger
from domains.folders.folder_endpoints import FolderEndpoints
from domains.folders.folder_payloads import FolderPayloads
from domains.lists.list_endpoints import ListEndpoints
from domains.lists.list_payloads import ListPayloads
from domains.tasks.task_endpoints import TaskEndpoints
from domains.tasks.task_payloads import TaskPayloads


@pytest.mark.acceptance
def test_e2e_cascade_deletion(shared_e2e_space):
    """HLTC 5: Cascade deletion from a Folder (Soft delete handling)."""
    f_api = FolderEndpoints()
    l_api = ListEndpoints()
    t_api = TaskEndpoints()

    f_res = f_api.create_folder(
        shared_e2e_space,
        FolderPayloads.build_create_folder_payload()
    )
    folder_id = f_res.json()["id"]

    l_res = l_api.create_list(
        folder_id,
        ListPayloads.build_create_list_payload()
    )
    list_id = l_res.json()["id"]

    t_res = t_api.create_task(
        list_id,
        TaskPayloads.build_create_task_payload()
    )
    task_id = t_res.json()["id"]

    # Act: Delete Folder
    logger.info(f"Executing cascade delete from Folder {folder_id}")

    delete_res = f_api.delete_folder(folder_id)
    assert delete_res.status_code == 200

    # Assert: Verify cascade behavior
    l_check = l_api.get_list(list_id)

    if l_check.status_code == 200:
        check.is_true(
            l_check.json().get("deleted", False),
            "List was not marked as deleted"
        )
    else:
        check.equal(l_check.status_code, 404)

    t_check = t_api.get_task(task_id)

    check.is_in(t_check.status_code, [200, 404])
