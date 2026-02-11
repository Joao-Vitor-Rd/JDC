from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Button, Static, OptionList, Header, Footer
from textual.widgets.option_list import Option
from textual.widget import Widget
from textual.screen import Screen
from textual.app import ComposeResult
from textual.message import Message

QUESTION = "Prefix Sum"

class QuestionScreen(Screen):
    """Tela da Questão."""
    
    BINDINGS = [("q", "quit_app", "Sair")]

    def __init__(self, questao_data):
        super().__init__()
        self.questao_data = questao_data
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Static(self.questao_data.get("titulo", "Questão"), classes="titulo"),
            Static(self.questao_data.get("conteúdo", "")),
            Button("Voltar", id="btn_voltar", variant="primary"),
        )
        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn_voltar":
            self.app.pop_screen()
    
    def action_quit_app(self) -> None:
        self.app.pop_screen()

    
