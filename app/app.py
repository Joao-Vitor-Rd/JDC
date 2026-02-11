from textual.app import App, ComposeResult
from textual.widgets import Footer, Button, Static
from textual.containers import Vertical
from textual.screen import Screen
from .ui.header_app_title import HeaderApp
from textual.widgets.option_list import Option
from .ui.first_section import FirstSection


class MeuAppCLI(App):
    
    BINDINGS = [("q", "quit", "Sair")]
    ENABLE_COMMAND_PALETTE = False

    def compose(self) -> ComposeResult:
        yield HeaderApp()
        yield FirstSection()
        


    def action_mudar_tema(self) -> None:
        self.dark = not self.dark
