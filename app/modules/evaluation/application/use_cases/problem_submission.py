from ...domain.interfaces import CodeExecutor
from ...domain.entities import Problem 
from .....shared.utils.dir import Dir
from ...domain.repositories import IProblemRepository

class ProblemSubmissionUseCase:

    def __init__(
      self,
      repository: IProblemRepository, 
      executor:   CodeExecutor
    ):
        self.repository = repository
        self.executor = executor

    def execute(self, problem: Problem):

        code_path = Dir.get_problem_path(problem.id)

        code_outputs = self.executor.execute(
            code_path=code_path, 
            inputs=problem._inputs,
            time_limit= problem.time_limit
        )

        problem.evaluate_submission(code_outputs)
        
        self.repository.save_submition_result(problem)