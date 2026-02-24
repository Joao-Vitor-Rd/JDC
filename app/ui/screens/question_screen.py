from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Static
from textual.app import ComposeResult
from .base_screen import BaseScreen
import asyncio

class QuestionScreen(BaseScreen):

    CSS_PATH = "../css/question_screen.css"

    def __init__(self, problem_id: int):
        super().__init__()
        self.problem_id = problem_id
        self.animation_frame = 0
        self.animation_handle = None
        
        self.controller = self.context.problem_controller

        self.problem = self.controller.get_problem(problem_id)
        
    def compose(self) -> ComposeResult:
        yield from super().compose()
        yield Vertical(
            Static(self.problem.title),
            Static(self.problem.description),
            Static(self._get_status_display(), id="status_display", classes="status_box"),
            Horizontal(
                Button("Voltar", id="btn_voltar", variant="primary"),
                Button("Code", id="code", variant="primary"),
                Button("Submit", id="submit", variant="success"),
                id="buttons_container",
            ),
        )
    
    def _get_status_display(self) -> str:
        status_text = self.problem.submission_result
        correct = self.problem._total_of_correct_outputs
        total = len(self.problem._expected_outputs)
        
        return f"Status: {status_text}\nAcertos: {correct}/{total}"
    
    async def _execute_in_worker(self) -> None:
        try:
            self._start_animation()
            await asyncio.to_thread(self.controller.evaluate_code, self.problem)
            self._stop_animation()
            self._update_after_submission()
        except Exception as e:
            self._stop_animation()
            self._show_error_message(f"Erro: {str(e)}")
    
    def _show_error_message(self, message: str) -> None:
        status_widget = self.query_one("#status_display", Static)
        status_widget.update(f"ERRO\n{message}")
    
    def _update_after_submission(self) -> None:
        status_widget = self.query_one("#status_display", Static)
        status_widget.update(self._get_status_display())
        
        submit_btn = self.query_one("#submit", Button)
        submit_btn.disabled = False

    
    def _start_animation(self) -> None:
        self.animation_frame = 0
        frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        
        def update_animation():
            try:
                status_widget = self.query_one("#status_display", Static)
                frame = frames[self.animation_frame % len(frames)]
                status_widget.update(f"Executando {frame}")
                self.animation_frame += 1
            except:
                pass
        
        self.animation_handle = self.set_interval(0.1, update_animation)
    
    def _stop_animation(self) -> None:
        """Para a animação de loading"""
        if self.animation_handle:
            self.animation_handle.stop()
            self.animation_handle = None
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn_voltar":
            self.app.pop_screen()
        if event.button.id == "code":
            self.controller.edit_code(self.problem.id)
        if event.button.id == "submit":
            self.run_worker(self._execute_in_worker()) 
    
