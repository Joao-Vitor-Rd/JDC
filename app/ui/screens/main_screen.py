from textual.widgets import ListItem, ListView, Label
from textual.app import ComposeResult
from .base_screen import BaseScreen
from .sections_screen import SectionsScreen

class MainScreen(BaseScreen):
    
    is_root = True
    CSS_PATH = "../css/main_screen.css"

    def compose(self) -> ComposeResult:
        yield from super().compose()
        yield ListView(
            ListItem(Label("Sections"), id="sections"),
            ListItem(Label("Configurations"), id="configs"),
        )
    
    def on_list_view_selected(self, event: ListView.Selected) -> None:
        item_id = event.item.id
        if item_id == "sections":
            self.app.push_screen(SectionsScreen())

