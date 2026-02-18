from ....application.use_cases import ProblemSubmissionUseCase
from ....application.use_cases import EditCode
from ....domain.evaluation.entities import Problem

class ProblemController:
    
    def evaluate_code(self, problem: Problem):
        ProblemSubmissionUseCase.execute(problem)
    
    def edit_code(self, problem_name: str):
        EditCode.execute(problem_name)