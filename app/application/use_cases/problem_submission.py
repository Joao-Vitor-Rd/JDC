from ...infrastructure.service.python_code_executor import PythonCodeExecutor
from ...domain.evaluation.entities import Problem 

class ProblemSubmissionUseCase:
    @staticmethod
    def execute(code_path: str, problem: Problem):
        executor = PythonCodeExecutor()
        code_outputs = executor.execute(code_path=code_path, inputs=problem._inputs, time_limit=5)
        problem.evaluete_submission(code_outputs=code_outputs)
