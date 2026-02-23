from abc import ABC, abstractmethod
from ..entities import Problem

class IProblemRepository(ABC):
    @abstractmethod
    def get_all_problems(self) -> list:
        pass

    @abstractmethod
    def get_problem(self, problem_id: int) -> Problem:
        pass

    @abstractmethod
    def save_submition_result(self, problem: Problem):
        pass
