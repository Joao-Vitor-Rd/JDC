from abc import ABC, abstractmethod

class IProblemRepository(ABC):
    @abstractmethod
    def get_all_problems(self) -> list:
        pass