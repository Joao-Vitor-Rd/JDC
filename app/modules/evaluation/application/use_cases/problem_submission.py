from ...infrastructure.service.python_code_executor import PythonCodeExecutor
from ...domain.entities import Problem 
from .....shared.utils.dir import Dir

class ProblemSubmissionUseCase:
    @staticmethod
    def execute(problem: Problem):
        executor = PythonCodeExecutor()
        code_path = Dir.get_problem_path(problem.id)
        code_outputs = executor.execute(code_path=code_path, inputs=problem._inputs, time_limit=1)
        problem.evaluate_submission(code_outputs=code_outputs)
