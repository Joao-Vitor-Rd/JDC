from ...domain.repositories.code_executor import CodeExecutor
from ...infrastructure.service.python_code_executor import PythonCodeExecutor
from ...domain.entities.problem import Problem 

class ProblemSubmissionUseCase:
    @staticmethod
    def execute(code_path: str, problem: Problem):
        executor = PythonCodeExecutor()
        code_outputs = executor.execute(code_path=code_path, inputs=problem._inputs, time_limit=5)
        problem.evaluete_submission(code_outputs=code_outputs)
