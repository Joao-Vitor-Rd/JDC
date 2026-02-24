from ..modules.evaluation.infrastructure.repositories.section_repository import SectionRepository
from ..modules.evaluation.application.use_cases.show_sections import ShowSectionsUseCase
from ..modules.evaluation.presentation.controllers import SectionController

def build_section_controller():

    repo = SectionRepository()
    use_case = ShowSectionsUseCase(repo)

    return SectionController(use_case)