from .....shared.utils.dir import Dir

class EditCode:
    
    def execute(self, problem_id: str):
        Dir.open_vscode_in_code(problem_id)