from ...domain.repositories import IProblemRepository

class ShowProblems:

    def __init__(
        self,
        repository: IProblemRepository, 
    ):
        self.repository = repository

    def execute(self, section_id: int) -> list:
        return self.repository.get_all_problems(section_id)
