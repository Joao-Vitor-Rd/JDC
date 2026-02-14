from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Static
from textual.app import ComposeResult
import subprocess
from .base_screen import BaseScreen
from pathlib import Path

QUESTION = "Prefix Sum"

class QuestionScreen(BaseScreen):

    CSS_PATH = "../css/question_screen.css"

    def __init__(self, questao_data=None):
        super().__init__()
        self.questao_data = questao_data or {}
    
    def compose(self) -> ComposeResult:
        yield from super().compose()
        yield Vertical(
            Static(self.questao_data.get("titulo", "Questão"), classes="titulo"),
            Static(self.questao_data.get("conteúdo", "")),
            Horizontal(
                Button("Voltar", id="btn_voltar", variant="primary"),
                Button("Code", id="code", variant="primary"),
                id="buttons_container",
            ),
        )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn_voltar":
            self.app.pop_screen()
        if event.button.id == "code":
            folder = Path.home() / "jdc_data"
            (folder / "q1.c").touch()
            subprocess.Popen(f'code "{folder}/q1.c"', shell=True)
    


    
