from abc import ABC, abstractmethod

class ISectionRepository(ABC):
    @abstractmethod
    def get_all_sections() -> list:
        pass