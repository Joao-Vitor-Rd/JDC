from .section_container import build_section_controller
from .problem_container import build_problem_controller

from ..ui import AppContext

def build_app_context() -> AppContext:

    section_controller = build_section_controller()
    problem_controller = build_problem_controller()

    return AppContext(
        section_controller,
        problem_controller
    )