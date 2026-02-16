from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Static
from textual.app import ComposeResult
from .base_screen import BaseScreen
from pathlib import Path
from ...presentation.controllers.evaluation import ProblemController 
from ...domain.evaluation.entities import Problem
from ...util.dir import Dir

QUESTION = "Prefix Sum"

class QuestionScreen(BaseScreen):

    CSS_PATH = "../css/question_screen.css"

    def __init__(self, questao_data=None):
        super().__init__()
        self.questao_data = questao_data or {}
        self.controller = ProblemController()

        self.problem = Problem(
            id=1,
            title="Contar de 1 até N",
            description="Dado um número n, imprima de 1 até n, cada número em uma linha",
            inputs=[5, 10, 1],
            expected_outputs=["1\n2\n3\n4\n5", "1\n2\n3\n4\n5\n6\n7\n8\n9\n10", "1"],
            submission_result=Problem.STATUS_UNSOLVED,
            total_of_correct_outputs=0
        )
        
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
    
    def _get_status_display(self) -> str:
        status_text = self.problem.submission_result
        correct = self.problem._total_of_correct_outputs
        total = len(self.problem._expected_outputs)
        
        return f"Status: {status_text}\nAcertos: {correct}/{total}"
    
    async def _execute_in_worker(self, code_path: str) -> None:
        try:
            self._while_evaluate()
            self.controller.evaluate_code(code_path=code_path, problem=self.problem)
            self._update_after_submission()
        except Exception as e:
            self._show_error_message(f"Erro: {str(e)}")
    
    def _show_error_message(self, message: str) -> None:
        status_widget = self.query_one("#status_display", Static)
        status_widget.update(f"ERRO\n{message}")
    
    def _update_after_submission(self) -> None:
        status_widget = self.query_one("#status_display", Static)
        status_widget.update(self._get_status_display())
        
        submit_btn = self.query_one("#submit", Button)
        submit_btn.disabled = False

    def _while_evaluate(self):
        status_widget = self.query_one("#status_display", Static)
        status_widget.update("Executando...")
            
        submit_btn = self.query_one("#submit", Button)
        submit_btn.disabled = True
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn_voltar":
            self.app.pop_screen()
        if event.button.id == "code":
            Dir.open_vscode_in_code("q1.py")
        if event.button.id == "submit":
            self.run_worker(self._execute_in_worker(Dir.concat_JDC_path("q1.py"))) 
    
