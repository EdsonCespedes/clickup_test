import uuid

def generate_random_name(prefix: str = "Test") -> str:
    """
    Generates a unique random suffix to avoid collisions during parallel execution.
    """
    return f"{prefix}_{uuid.uuid4().hex[:8]}"