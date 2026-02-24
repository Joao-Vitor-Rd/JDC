from ...application.use_cases.show_sections import ShowSectionsUseCase

class SectionController:

    def __init__(self, show_sections_use_case: ShowSectionsUseCase):
        self.show_sections_use_case = show_sections_use_case

    def show_all_sections(self) -> list:
        return self.show_sections_use_case.execute()