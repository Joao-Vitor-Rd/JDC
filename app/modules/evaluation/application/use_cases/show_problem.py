from ...domain.entities import Problem  
from ...infrastructure.repositories import ProblemRepository
class ShowProblem:
    @staticmethod
    def execute(problem_id: int) -> Problem:
        repository = ProblemRepository()
        return repository.get_problem(problem_id)