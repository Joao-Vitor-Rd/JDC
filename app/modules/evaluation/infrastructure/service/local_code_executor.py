from ...domain.interfaces import CodeExecutor
from ...domain.enums import EvaluationFlags
import subprocess

class LocalCodeExecutor(CodeExecutor):

    def execute(self, code_path: str, inputs: list, time_limit: float) -> list:
        code_outputs = []

        try:
            with open(code_path, "r") as f:
                pass

        except Exception:
            return [EvaluationFlags.CE_FLAG]
        
        for input_value in inputs:
            try:
                result = subprocess.run(
                    ["python3", code_path],
                    input=str(input_value),
                    capture_output=True,
                    text=True,
                    timeout=time_limit
                )
                
                if result.returncode != 0:
                    code_outputs.append(EvaluationFlags.RE_FLAG)
                else:
                    output = result.stdout.strip()
                    code_outputs.append(output)
                
            except subprocess.TimeoutExpired:
                code_outputs.append(EvaluationFlags.TL_FLAG)
                break
                
            except Exception:
                code_outputs.append(EvaluationFlags.RE_FLAG)
        
        return code_outputs