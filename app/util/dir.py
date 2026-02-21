from pathlib import Path
import subprocess

class Dir():

    JDC_PATH =  Path.home() / "jdc_data"

    @staticmethod
    def create_data_dir():
        pasta = Path.home() / "jdc_data"
        pasta.mkdir(exist_ok=True)
        return pasta
    
    @staticmethod
    def get_jdc_path() -> str:
        return Dir.JDC_PATH
    
    @staticmethod
    def open_vscode_in_code(problem_id: str):
        problem_path = f"q{problem_id}.py"
        subprocess.Popen(f'code "{Dir.JDC_PATH}/{problem_path}"', shell=True)

    @staticmethod
    def get_problem_path(problem_id: int) -> str:
        problem_path = f"q{problem_id}.py"
        return str(Dir.JDC_PATH / problem_path)
    
    @staticmethod
    def concat_JDC_path(to_concat: str) -> str:
        return Dir.JDC_PATH / to_concat