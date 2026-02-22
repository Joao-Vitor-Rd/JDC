from ...application.use_cases.show_sections import ShowSectionsUseCase

class SectionController:
    
    def show_all_sections(self) -> list:
        return ShowSectionsUseCase.execute()
