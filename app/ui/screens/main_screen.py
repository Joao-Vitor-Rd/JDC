from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Button, Static, OptionList, Header
from textual.app import ComposeResult
from .base_screen import BaseScreen
from .first_section import FirstSection

class MainScreen(BaseScreen):
    
    is_root = True
    
    def compose(self) -> ComposeResult:
        yield from super().compose()
        yield Vertical(
            Button("Modules", id="modules", variant="primary"),
            Button("Configs", id="configs", variant="primary"),
            id="buttons_container",
        )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "modules":
            self.app.push_screen(FirstSection())

