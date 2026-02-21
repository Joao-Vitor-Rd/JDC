from ...domain.evaluation.entities import Problem  
from ...infrastructure.repositories.evaluation import ProblemRepository
class ShowProblem:
    @staticmethod
    def execute(problem_id: int) -> Problem:
        repository = ProblemRepository()
        return repository.get_problem(problem_id)