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
def test_e2e_hierarchy_creation_flow(shared_e2e_space):
    """HLTC 1: End-to-end hierarchical creation flow (Folder -> List -> Task)."""
    f_api = FolderEndpoints()
    l_api = ListEndpoints()
    t_api = TaskEndpoints()

    # 1. Folder
    f_res = f_api.create_folder(
        shared_e2e_space,
        FolderPayloads.build_create_folder_payload(name="E2E_Folder")
    )
    assert f_res.status_code == 200
    folder_id = f_res.json()["id"]

    # 2. List
    l_res = l_api.create_list(
        folder_id,
        ListPayloads.build_create_list_payload(name="E2E_List")
    )
    assert l_res.status_code == 200
    list_id = l_res.json()["id"]

    # 3. Task
    t_res = t_api.create_task(
        list_id,
        TaskPayloads.build_create_task_payload(name="E2E_Final_Task")
    )
    assert t_res.status_code == 200

    task_data = t_res.json()

    check.equal(task_data["name"], "E2E_Final_Task")
    check.is_in("id", task_data)