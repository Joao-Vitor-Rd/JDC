from ....application.use_cases import ProblemSubmissionUseCase
from ....domain.evaluation.entities import Problem

class ProblemController:
    
    def evaluate_code(self, code_path: str, problem: Problem):
        return ProblemSubmissionUseCase.execute(code_path=code_path, problem=problem)