class TaskData:
    """Static data and assertion constants for the Tasks domain."""

    INVALID_STATUSES = ["nonexistent_status", "12345", "!@#$%"]

    EXPECTED_ERRORS = {
        "not_found": "Task not found",
        "invalid_list": "List not found",
        "unauthorized": "OAuth token is not valid"
    }