from ..modules.evaluation.infrastructure.repositories.problem_repository import ProblemRepository
from ..modules.evaluation.infrastructure.service.local_code_executor import LocalCodeExecutor

from ..modules.evaluation.application.use_cases.problem_submission import ProblemSubmissionUseCase
from ..modules.evaluation.application.use_cases.show_problems import ShowProblems
from ..modules.evaluation.application.use_cases.show_problem import ShowProblem
from ..modules.evaluation.application.use_cases.edit_code import EditCode

from ..modules.evaluation.presentation.controllers import ProblemController

def build_problem_controller():

    repo = ProblemRepository()
    executor = LocalCodeExecutor()

    submission_uc = ProblemSubmissionUseCase(repo, executor)
    show_problems_uc = ShowProblems(repo)
    show_problem_uc = ShowProblem(repo)
    edit_code_uc = EditCode()

    return ProblemController(
        submission_uc,
        edit_code_uc,
        show_problems_uc,
        show_problem_uc
    )