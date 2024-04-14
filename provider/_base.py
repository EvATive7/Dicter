class Provider:
    def __init__(self, config: dict) -> None:
        self.config = config

    def get(self) -> list[str]:
        raise NotImplementedError()