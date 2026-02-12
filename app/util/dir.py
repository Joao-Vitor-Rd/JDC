import os
import shutil
from pathlib import Path

class Dir():
    @staticmethod
    def create_data_dir():
        pasta = Path.home() / "jdc_data"
        pasta.mkdir(exist_ok=True)
        return pasta