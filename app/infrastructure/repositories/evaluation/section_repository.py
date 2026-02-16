from ....domain.evaluation.repositories import ISectionRepository
from ....infrastructure.database.sqlite_singleton import SQLiteDatabase
from ....infrastructure.mappers.section_mapper import SectionMapper

class SectionRepository(ISectionRepository):
    def __init__(self):
        self.db = SQLiteDatabase()
    
    def get_all_sections(self) -> list:
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome FROM sections")
            rows = cursor.fetchall()
            
            return SectionMapper.to_entities(rows)