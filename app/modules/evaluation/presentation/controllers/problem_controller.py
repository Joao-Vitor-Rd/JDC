from ...application.use_cases import ProblemSubmissionUseCase
from ...application.use_cases import ShowProblems
from ...application.use_cases import ShowProblem
from ...application.use_cases import EditCode
from ...domain.entities import Problem
from ...application.dtos import ProblemBriefDTO

class ProblemController:
    
    def __init__(
        self,
        submission_use_case: ProblemSubmissionUseCase,
        edit_code_use_case: EditCode,
        show_problems_use_case: ShowProblems,
        show_problem_use_case: ShowProblem
    ):
        self.submission_use_case = submission_use_case
        self.edit_code_use_case = edit_code_use_case
        self.show_problems_use_case = show_problems_use_case
        self.show_problem_use_case = show_problem_use_case

    def evaluate_code(self, problem: Problem):
        self.submission_use_case.execute(problem)

    def edit_code(self, problem_id: str):
        self.edit_code_use_case.execute(problem_id)

    def show_all_problems(self, section_id: int) -> list[ProblemBriefDTO]:
        return self.show_problems_use_case.execute(section_id)

    def get_problem(self, problem_id: int) -> list[ProblemBriefDTO]:
        return self.show_problem_use_case.execute(problem_id)
