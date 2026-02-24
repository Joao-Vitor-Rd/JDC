from abc import ABC, abstractmethod

class CodeExecutor(ABC):
    @abstractmethod
    def execute(self, code_path: str, inputs: list, time_limit: int) -> list:
        pass
