from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Static
from textual.app import ComposeResult
import subprocess
from .base_screen import BaseScreen
from pathlib import Path
from ...application.use_cases.problem_submission import ProblemSubmissionUseCase
from ...domain.evaluation.entities import Problem
from threading import Thread

QUESTION = "Prefix Sum"

class QuestionScreen(BaseScreen):

    CSS_PATH = "../css/question_screen.css"

    def __init__(self, questao_data=None):
        super().__init__()
        self.questao_data = questao_data or {}

        self.problem = Problem(
            id=1,
            title="Contar de 1 até N",
            description="Dado um número n, imprima de 1 até n, cada número em uma linha",
            inputs=[5, 10, 1],
            expected_outputs=["1\n2\n3\n4\n5", "1\n2\n3\n4\n5\n6\n7\n8\n9\n10", "1"],
            submission_result=Problem.STATUS_UNSOLVED,
            total_of_correct_outputs=0
        )
    
    def _get_status_display(self) -> str:
        status_map = {
            Problem.STATUS_UNSOLVED: "US",
            Problem.STATUS_ACCEPTED: "AC",
            Problem.STATUS_WRONG_ANSWER: "WA",
            Problem.STATUS_TIME_LIMIT_EXCEED: "TL",
            Problem.STATUS_COMPILER_ERROR: "CE"
        }
        
        status_text = status_map.get(self.problem.submission_result, "?")
        correct = self.problem._total_of_correct_outputs
        total = len(self.problem._expected_outputs)
        
        return f"Status: {status_text}\nAcertos: {correct}/{total}"
    
    def _execute_submission(self, code_path: str) -> None:
        ProblemSubmissionUseCase.execute(code_path=code_path, problem=self.problem)
    
    def _on_submission_complete(self) -> None:
        status_widget = self.query_one("#status_display", Static)
        status_widget.update(self._get_status_display())
    
    def _execute_and_update(self, code_path: str) -> None:
        try:
            ProblemSubmissionUseCase.execute(code_path=code_path, problem=self.problem)
        except Exception as e:
            self.app.call_from_thread(lambda: self._show_error_message(f"Erro: {str(e)}"))
        finally:
            self.app.call_from_thread(self._update_after_submission)
    
    def _show_error_message(self, message: str) -> None:
        status_widget = self.query_one("#status_display", Static)
        status_widget.update(f"ERRO\n{message}")
    
    def _update_after_submission(self) -> None:
        status_widget = self.query_one("#status_display", Static)
        status_widget.update(self._get_status_display())
        
        submit_btn = self.query_one("#submit", Button)
        submit_btn.disabled = False
    
    def compose(self) -> ComposeResult:
        yield from super().compose()
        yield Vertical(
            Static(self.questao_data.get("titulo", "Questão"), classes="titulo"),
            Static(self.questao_data.get("conteúdo", "")),
            Static(self._get_status_display(), id="status_display", classes="status_box"),
            Horizontal(
                Button("Voltar", id="btn_voltar", variant="primary"),
                Button("Code", id="code", variant="primary"),
                Button("Submit", id="submit", variant="success"),
                id="buttons_container",
            ),
        )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn_voltar":
            self.app.pop_screen()
        if event.button.id == "code":
            folder = Path.home() / "jdc_data"
            (folder / "q1.py").touch()
            subprocess.Popen(f'code "{folder}/q1.py"', shell=True)
        if event.button.id == "submit":
            path = Path.home() / "jdc_data" / "q1.py"
            
            status_widget = self.query_one("#status_display", Static)
            status_widget.update("Executando...")
            
            submit_btn = self.query_one("#submit", Button)
            submit_btn.disabled = True
            
            thread = Thread(target=self._execute_and_update, args=(path,), daemon=True)
            thread.start()
        
    


    
