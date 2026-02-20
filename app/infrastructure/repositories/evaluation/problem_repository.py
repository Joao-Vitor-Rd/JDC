from ....domain.evaluation.repositories import IProblemRepository
from ....infrastructure.database.sqlite_singleton import SQLiteDatabase
from ....infrastructure.mappers import ProblemMapper

class ProblemRepository(IProblemRepository):
    def __init__(self):
        self.db = SQLiteDatabase()
    
    def get_all_problems(self, section_id: int) -> list:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title FROM problems WHERE section_id = ?", (section_id,))
            rows = cursor.fetchall()
            
            return ProblemMapper.to_brief_dtos(rows)