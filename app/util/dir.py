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
    def open_vscode_in_code(problem_name: str):
        subprocess.Popen(f'code "{Dir.JDC_PATH}/{problem_name}"', shell=True)

    @staticmethod
    def concat_JDC_path(to_concat: str) -> str:
        return Dir.JDC_PATH / to_concat