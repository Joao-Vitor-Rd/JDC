from textual.app import ComposeResult
from .base_screen import BaseScreen
from .question_screen import QuestionScreen
from textual.widgets import Label, ListItem, ListView

class SectionScreen(BaseScreen):

    CSS_PATH = "../css/section_screen.css"

    def compose(self) -> ComposeResult:
        yield from super().compose()
        yield ListView(
            ListItem(Label("One"), id="q1"),
            ListItem(Label("Two"), id="q2"),
            ListItem(Label("Three"), id="q3"),
        )

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        item_id = event.item.id
        if item_id in ["q1", "q2", "q3"]:
            self.app.push_screen(QuestionScreen())

    
