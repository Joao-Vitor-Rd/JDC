from textual.app import ComposeResult
from .base_screen import BaseScreen
from .problem_sections import ProblemsSections
from textual.widgets import Label, ListItem, ListView

class SectionsScreen(BaseScreen):

    CSS_PATH = "../css/sections_screen.css"

    def compose(self) -> ComposeResult:
        yield from super().compose()
        yield ListView(
            ListItem(Label("One"), id="q1"),
            ListItem(Label("Two"), id="q2"),
            ListItem(Label("Three"), id="q3"),
        )

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        self.app.push_screen(ProblemsSections())

    
