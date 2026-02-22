from textual.app import ComposeResult
from .base_screen import BaseScreen
from .section_problems_screen import ProblemsSections
from textual.widgets import Label, ListItem, ListView
from ...modules.evaluation.presentation.controllers import SectionController

class SectionsScreen(BaseScreen):

    CSS_PATH = "../css/sections_screen.css"

    def compose(self) -> ComposeResult:
        yield from super().compose()
        
        controller = SectionController()
        sections = controller.show_all_sections()

        self.section_titles = {section.id: section.title for section in sections}
        
        list_items = [
            ListItem(Label(section.title), id=f"section_{section.id}")
            for section in sections
        ]
        
        yield ListView(*list_items)

    def on_list_view_selected(self, event: ListView.Selected) -> None:

        section_id = int(event.item.id.split("_")[1])
        self.app.push_screen(ProblemsSections(section_id, self.section_titles[section_id]))

    
