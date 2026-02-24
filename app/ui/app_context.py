from ..modules.evaluation.presentation.controllers import ProblemController
from ..modules.evaluation.presentation.controllers  import SectionController

class AppContext:

    def __init__(
        self,
        section_controller: SectionController,
        problem_controller: ProblemController,
    ):
        self.section_controller = section_controller
        self.problem_controller = problem_controller