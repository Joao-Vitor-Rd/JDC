from textual.app import ComposeResult
from textual.screen import Screen
from textual.binding import Binding
from ..widget.header_app import HeaderApp
from ..widget.footer_app import FooterApp


class BaseScreen(Screen):
    
    is_root: bool = False 
    
    @property
    def context(self):
        return self.app.context
    
    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
        Binding(
            key="question_mark",
            action="help",
            description="Show help screen",
            key_display="?",
        ),
        Binding(key="delete", action="delete", description="Delete the thing"),
        Binding(key="j", action="down", description="Scroll down", show=False),
    ]
    
    def compose(self) -> ComposeResult:
        yield HeaderApp()
        yield FooterApp()
    
    def action_quit(self) -> None:
        if self.is_root:
            self.app.exit()
        else:
            self.app.pop_screen()
    
    def action_help(self) -> None:
        pass
    
    def action_delete(self) -> None:
        pass
    
    def action_down(self) -> None:
        pass
