from ...infrastructure.service.python_code_executor import PythonCodeExecutor
from ...domain.evaluation.entities import Problem 
from ...util.dir import Dir

class ProblemSubmissionUseCase:
    @staticmethod
    def execute(problem: Problem):
        executor = PythonCodeExecutor()
        code_path = Dir.concat_JDC_path(problem._title)
        code_outputs = executor.execute(code_path=code_path, inputs=problem._inputs, time_limit=1)
        problem.evaluate_submission(code_outputs=code_outputs)
