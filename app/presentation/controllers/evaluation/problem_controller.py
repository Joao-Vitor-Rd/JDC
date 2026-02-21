from ....application.use_cases import ProblemSubmissionUseCase
from ....application.use_cases import ShowProblems
from ....application.use_cases import ShowProblem
from ....application.use_cases import EditCode
from ....domain.evaluation.entities import Problem
from ....application.dtos import ProblemBriefDTO

class ProblemController:
    
    def evaluate_code(self, problem: Problem):
        ProblemSubmissionUseCase.execute(problem)
    
    def edit_code(self, problem_id: str):
        EditCode.execute(problem_id)

    def show_all_problems(self, section_id: int) -> list[ProblemBriefDTO]:
        return ShowProblems.execute(section_id)
    
    def get_problem(self, problem_id: int) -> list[ProblemBriefDTO]:
        return ShowProblem.execute(problem_id)
    
