from ...domain.repositories import ISectionRepository

class ShowSectionsUseCase:
    
    def __init__(
        self,
        repository: ISectionRepository, 
    ):
        self.repository = repository

    def execute(self) -> list:
        return self.repository.get_all_sections()

        
