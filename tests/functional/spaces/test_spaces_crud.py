import pytest
import pytest_check as check
from domains.spaces.space_endpoints import SpaceEndpoints
from domains.spaces.space_payloads import SpacePayloads
from domains.spaces.space_schemas import SpaceSchema


@pytest.mark.functional
def test_create_and_validate_space(shared_e2e_space, worker_id):
    """Verifies the creation state using the already created shared space to avoid limits."""
    api = SpaceEndpoints()
    
    response = api.get_space(shared_e2e_space)
    assert response.status_code == 200

    data = response.json()
    SpaceSchema.model_validate(data)

    check.equal(data["name"], f"Shared_E2E_Root_{worker_id}")
    check.is_false(data["private"])


@pytest.mark.functional
def test_get_space(shared_e2e_space):
    """Verifies reading an existing Space (Read) using the shared space."""
    api = SpaceEndpoints()
    response = api.get_space(shared_e2e_space)

    assert response.status_code == 200
    data = response.json()
    SpaceSchema.model_validate(data)
    check.equal(data["id"], shared_e2e_space)


@pytest.mark.functional
def test_update_space(shared_e2e_space):
    """Verifies updating an existing Space (Update) using the shared space."""
    api = SpaceEndpoints()
    payload = SpacePayloads.build_update_space_payload()

    response = api.update_space(shared_e2e_space, payload)
    assert response.status_code == 200

    data = response.json()
    SpaceSchema.model_validate(data)
    check.equal(data["name"], payload["name"])


@pytest.mark.functional
def test_delete_space(global_team_id):
    """Verifies deletion of a Space (Delete)."""
    api = SpaceEndpoints()
    payload = SpacePayloads.build_create_space_payload()

    create_res = api.create_space(global_team_id, payload)
    assert create_res.status_code == 200
    space_id = create_res.json()["id"]

    delete_res = api.delete_space(space_id)
    assert delete_res.status_code == 200

    get_res = api.get_space(space_id)
    check.equal(get_res.status_code, 404)