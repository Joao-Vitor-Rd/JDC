from textual.app import App
from .ui.screens.main_screen import MainScreen
from .ui import AppContext
from .container.app_container import build_app_context

class JDC(App):

    context: AppContext 

    def on_mount(self) -> None:
        self.context = build_app_context()
        self.push_screen(MainScreen())
        
