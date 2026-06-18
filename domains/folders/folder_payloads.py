from helpers.random_generator import generate_random_name


class FolderPayloads:
    @staticmethod
    def build_create_folder_payload(name: str = None) -> dict:
        return {"name": name or generate_random_name("Folder")}
