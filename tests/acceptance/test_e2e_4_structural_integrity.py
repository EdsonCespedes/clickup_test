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
def test_e2e_structural_integrity(shared_e2e_space):
    """HLTC 4: Structural Integrity (Renaming Folder does not break Tasks)."""
    f_api = FolderEndpoints()
    l_api = ListEndpoints()
    t_api = TaskEndpoints()

    f_res = f_api.create_folder(
        shared_e2e_space,
        FolderPayloads.build_create_folder_payload(name="Integrity_Folder")
    )
    folder_id = f_res.json()["id"]

    l_res = l_api.create_list(
        folder_id,
        ListPayloads.build_create_list_payload()
    )
    list_id = l_res.json()["id"]

    task_ids = []

    for i in range(3):
        res = t_api.create_task(
            list_id,
            TaskPayloads.build_create_task_payload(name=f"Bulk Task {i + 1}")
        )
        task_ids.append(res.json()["id"])

    logger.info("Renaming parent Folder")

    f_api.update_folder(
        folder_id,
        {"name": "Folder_Renamed_E2E"}
    )

    # Assert: Tasks remain accessible
    for t_id in task_ids:
        t_res = t_api.get_task(t_id)
        check.equal(t_res.status_code, 200)
