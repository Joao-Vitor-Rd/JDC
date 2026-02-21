from ...util.dir import Dir

class EditCode:
    def execute(problem_id: str):
        Dir.open_vscode_in_code(problem_id)