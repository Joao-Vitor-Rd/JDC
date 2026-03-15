from ...domain.repositories import IProblemRepository
from .....shared.database.sqlite_singleton import SQLiteDatabase
from ..mappers import ProblemMapper
from ...domain.entities import Problem 

class ProblemRepository(IProblemRepository):
    def __init__(self):
        self.db = SQLiteDatabase()
    
    def get_all_problems(self, section_id: int) -> list:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()

            sql = """
                SELECT id, title 
                FROM problems 
                WHERE section_id = ?
            """

            params = (
                section_id,
            )

            cursor.execute(sql,params)
            rows = cursor.fetchall()
            
            return ProblemMapper.to_brief_dtos(rows)
        
    def get_problem(self, problem_id: int) -> Problem:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()

            sql = """
                SELECT * 
                FROM problems 
                WHERE id = ?
            """

            params = (
                problem_id,
            )
            
            cursor.execute(sql, params)
            row = cursor.fetchone()
            
            if not row:
                return None
            
            cursor.execute(
                "SELECT input_value, expected_output FROM test_cases WHERE problem_id = ?",
                (problem_id,)
            )
            test_cases = cursor.fetchall()
            test_cases_list = [dict(tc) for tc in test_cases]
            
            return ProblemMapper.to_problem(dict(row), test_cases_list)
        
    def save_submition_result(self, problem: Problem):
        with self.db.get_connection() as conn:
            cursor = conn.cursor()

            sql = """
                UPDATE problems
                SET submission_result = ?, 
                    total_of_correct_outputs = ? 
                WHERE id = ?
            """

            params = (
                problem.submission_result.value, 
                problem.total_of_correct_outputs,
                problem.id,
            )

            cursor.execute(sql, params)
            rows = cursor.fetchall()
            