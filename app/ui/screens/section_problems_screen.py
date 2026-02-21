from textual.containers import Container
from textual.widgets import Static, OptionList
from textual.widgets.option_list import Option
from textual.app import ComposeResult
from .base_screen import BaseScreen
from .question_screen import QuestionScreen
from ...presentation.controllers.evaluation import ProblemController

class ProblemsSections(BaseScreen):

    def __init__(self, section_id: int, name: str):
        super().__init__(name)
        self.section_id = section_id

    def compose(self) -> ComposeResult:
        yield from super().compose()
        controller = ProblemController()

        problems = controller.show_all_problems(self.section_id)

        optionlist = [
             Option(problem.title, id=problem.id)
             for problem in problems
        ]

        yield Container(
            Static(self.name, classes="question"),
            OptionList(*optionlist),
            id="dialog",
        )
    
    def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        problem_id = int(event.option_id)
        self.app.push_screen(QuestionScreen(problem_id))

    
