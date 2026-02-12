from textual.app import App
from .ui.screens.main_screen import MainScreen

class JDC(App):

    def on_mount(self) -> None:
        self.push_screen(MainScreen())
        
