from helpers.random_generator import generate_random_name


class ListPayloads:
    @staticmethod
    def build_create_list_payload(name: str = None, content: str = "Automated List") -> dict:
        return {
            "name": name or generate_random_name("List"),
            "content": content
        }
