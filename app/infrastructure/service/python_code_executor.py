from ...domain.repositories.code_executor import CodeExecutor
import subprocess
import sys

TLE_FLAG = "@TL@"
COMPILER_ERROR_FLAG = "@CE@"

class PythonCodeExecutor(CodeExecutor):

    def execute(self, code_path: str, inputs: list, time_limit: int) -> list:

        code_outputs = []

        for input_value in inputs:
            try:
                input_str = str(input_value)
                
                result = subprocess.run(
                    [sys.executable, code_path],
                    input=input_str,
                    capture_output=True,
                    text=True,
                    timeout=time_limit
                )
                
                output = result.stdout.strip()
                code_outputs.append(output)
                
            except subprocess.TimeoutExpired:
                code_outputs.append(TLE_FLAG)
                
            except Exception as e:
                code_outputs.append(COMPILER_ERROR_FLAG)
        
        return code_outputs

