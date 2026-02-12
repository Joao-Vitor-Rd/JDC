from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Button, Static, OptionList, Header
from textual.widgets.option_list import Option
from textual.widget import Widget
from textual.screen import Screen
from typing import TYPE_CHECKING
from ..widget.footer_app import FooterApp
from textual.app import ComposeResult
import subprocess
from pathlib import Path

if TYPE_CHECKING:
    from .base_screen import BaseScreen

QUESTION = "Prefix Sum"

class QuestionScreen(Screen):

    CSS_PATH = "../css/question_screen.css"
    BINDINGS = [("q", "quit_app", "Sair")]

    def __init__(self, questao_data):
        super().__init__()
        self.questao_data = questao_data
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Static(self.questao_data.get("titulo", "Questão"), classes="titulo"),
            Static(self.questao_data.get("conteúdo", "")),
            Horizontal(
                Button("Voltar", id="btn_voltar", variant="primary"),
                Button("Code", id="code", variant="primary"),
                id="buttons_container",
            ),
        )
        yield FooterApp()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn_voltar":
            self.app.pop_screen()
        if event.button.id == "code":
            folder = Path.home() / "jdc_data"
            (folder / "q1.c").touch()
            subprocess.Popen(f'code "{folder}/q1.c"', shell=True)
    
    def action_quit_app(self) -> None:
        self.app.pop_screen()


    
