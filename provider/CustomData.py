from ._base import Provider
from util import *

class CustomData(Provider):
    def __init__(self, config: dict) -> None:
        super().__init__(config)
        self.path = config['path']

    def get(self) -> list[str]:
        return read_list_from_folder(self.path)