from ...infrastructure.repositories import ProblemRepository

class ShowProblems:

    @staticmethod
    def execute(section_id: int) -> list:
        repository = ProblemRepository()
        return repository.get_all_problems(section_id)
