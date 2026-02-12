from textual.containers import Container
from textual.widgets import Button, Static, OptionList
from textual.widgets.option_list import Option
from textual.app import ComposeResult
from .base_screen import BaseScreen
from .question_screen import QuestionScreen

QUESTION = "Prefix Sum"

QUESTOES = {
    "op1": {"titulo": "Soma de Prefixos", "conteúdo": "Explicação da questão 01..."},
    "op2": {"titulo": "Two Pointers", "conteúdo": "Explicação da questão 02..."},
    "op3": {"titulo": "Sliding Window", "conteúdo": "Explicação da questão 03..."},
}

class FirstSection(BaseScreen):
    """Tela da primeira seção da aplicação."""

    def compose(self) -> ComposeResult:
        yield from super().compose()
        
        yield Container(
            Static(QUESTION, classes="question"),
            OptionList(
                Option("Questão 01", id="op1"),
                Option("Segunda Opção", id="op2"),
                Option("Terceira Opção", id="op3"),
                id="menu_selecao"
            ),
            id="dialog",
        )
    
    def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        questao_data = QUESTOES.get(event.option_id)
        self.app.push_screen(QuestionScreen(questao_data))

    
