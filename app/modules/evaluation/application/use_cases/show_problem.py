from ...domain.entities import Problem  
from ...domain.repositories import IProblemRepository
class ShowProblem:

    def __init__(
        self,
        repository: IProblemRepository, 
    ):
        self.repository = repository

    def execute(self, problem_id: int) -> Problem:
        return self.repository.get_problem(problem_id)