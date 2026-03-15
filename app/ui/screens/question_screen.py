from textual.containers import Vertical
from textual.widgets import Static
from textual.app import ComposeResult
from textual.binding import Binding
from .base_screen import BaseScreen
from ...modules.evaluation.domain.enums import EvaluationResult
import asyncio

class QuestionScreen(BaseScreen):

    CSS_PATH = "../css/question_screen.css"

    BINDINGS = BaseScreen.BINDINGS + [
        Binding(key="e", action="edit_code", description="Edit Code", show=True),
        Binding(key="enter", action="submit", description="Submit Code", show=True),
    ]

    def __init__(self, problem_id: int):
        super().__init__()
        self.problem_id = problem_id
        self.animation_frame = 0
        self.animation_handle = None
        self.is_submitting = False
        
        self.controller = self.context.problem_controller

        self.problem = self.controller.get_problem(problem_id)
        
    def compose(self) -> ComposeResult:
        yield from super().compose()
        yield Vertical(
            Static(self.problem.title),
            Static(self.problem.description),
            Static(self._get_status_display(), id="status_display", classes="status_box"),
        )
    
    def _get_status_display(self) -> str:
        status_text = self.problem.submission_result.value
        correct = self.problem.total_of_correct_outputs
        total = len(self.problem.expected_outputs)
        
        return f"Status: {status_text}\nAcertos: {correct}/{total}"

    def _status_widget(self) -> Static:
        return self.query_one("#status_display", Static)
    
    def _show_error_message(self, message: str) -> None:
        self._status_widget().update(f"ERRO\n{message}")
    
    def _update_after_submission(self) -> None:
        self._status_widget().update(self._get_status_display())

    def _start_animation(self) -> None:
        self.animation_frame = 0
        frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        
        def update_animation():
            try:
                frame = frames[self.animation_frame % len(frames)]
                self._status_widget().update(f"Executando {frame}")
                self.animation_frame += 1
            except:
                pass
        
        self.animation_handle = self.set_interval(0.1, update_animation)
    
    def _stop_animation(self) -> None:
        if self.animation_handle:
            self.animation_handle.stop()
            self.animation_handle = None

    def _begin_submit(self) -> None:
        self.is_submitting = True
        self._start_animation()

    def _end_submit(self) -> None:
        self._stop_animation()
        self.is_submitting = False

    def action_edit_code(self) -> None:
        self.controller.edit_code(self.problem.id)

    def action_submit(self) -> None:
        if self.is_submitting:
            return

        self._begin_submit()
        self.run_worker(self._submit_in_worker(), exclusive=True)

    async def _submit_in_worker(self) -> None:
        try:
            await asyncio.to_thread(self.controller.evaluate_code, self.problem)
            self._update_after_submission()
        except Exception as e:
            self._show_error_message(f"Erro: {str(e)}")
        finally:
            self._end_submit()

    
