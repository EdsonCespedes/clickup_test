from helpers.random_generator import generate_random_name


class SpacePayloads:
    """Payload builder for Space-related API requests."""

    @staticmethod
    def build_create_space_payload(name: str = None) -> dict:
        return {
            "name": name or generate_random_name("Space_Auto"),
            "multiple_assignees": True,
            "features": {
                "due_dates": {
                    "enabled": True,
                    "start_date": False,
                    "remap_due_dates": True,
                },
                "time_tracking": {
                    "enabled": False,
                },
            },
        }

    @staticmethod
    def build_update_space_payload(new_name: str = None) -> dict:
        return {
            "name": new_name or generate_random_name("Space_Updated"),
            "color": "#FFCC00",
        }