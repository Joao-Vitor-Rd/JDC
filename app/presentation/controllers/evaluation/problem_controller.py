from ....application.use_cases import ProblemSubmissionUseCase
from ....application.use_cases import ShowProblems
from ....application.use_cases import EditCode
from ....domain.evaluation.entities import Problem
from ....application.dtos import ProblemBriefDTO

class ProblemController:
    
    def evaluate_code(self, problem: Problem):
        ProblemSubmissionUseCase.execute(problem)
    
    def edit_code(self, problem_name: str):
        EditCode.execute(problem_name)

    def show_all_problems(self, section_id: int) -> list[ProblemBriefDTO]:
        return ShowProblems.execute(section_id)
