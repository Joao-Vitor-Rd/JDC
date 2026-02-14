from ...domain.repositories.code_executor import CodeExecutor
import subprocess
import sys

TLE_FLAG = "@TL@"
COMPILER_ERROR_FLAG = "@CE@"

class PythonCodeExecutor(CodeExecutor):

    def execute(self, code_path: str, inputs: list, time_limit: int) -> list:

        code_outputs = []

        for it_inputs in inputs:
            try:
                result = subprocess.run(
                    [sys.executable, code_path],
                    input=it_inputs,
                    capture_output=True,
                    text=True,
                    check=True,
                    timeout=time_limit
                )

                output = result.stdout.strip()
                code_outputs.append(output)

            except subprocess.TimeoutExpired:
                code_outputs.append(TLE_FLAG)
            except Exception:
                code_outputs.append(COMPILER_ERROR_FLAG)
        
        return code_outputs
        
