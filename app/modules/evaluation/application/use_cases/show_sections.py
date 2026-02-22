from ...infrastructure.repositories import SectionRepository

class ShowSectionsUseCase:
    @staticmethod
    def execute() -> list:
        repository = SectionRepository()
        return repository.get_all_sections()

        
