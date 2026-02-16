from textual.app import ComposeResult
from .base_screen import BaseScreen
from .problem_sections import ProblemsSections
from textual.widgets import Label, ListItem, ListView
from ...presentation.controllers.evaluation import SectionController

class SectionsScreen(BaseScreen):

    CSS_PATH = "../css/sections_screen.css"

    def compose(self) -> ComposeResult:
        yield from super().compose()
        
        controller = SectionController()
        sections = controller.show_all_sections()
        
        list_items = [
            ListItem(Label(section.title), id=f"section_{section.id}")
            for section in sections
        ]
        
        yield ListView(*list_items)

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        self.app.push_screen(ProblemsSections())

    
