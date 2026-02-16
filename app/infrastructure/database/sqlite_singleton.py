import sqlite3
import threading
from pathlib import Path

class SQLiteDatabase:
    _instance = None
    _lock = threading.Lock()  

    def __new__(cls, db_name="test_db"):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(SQLiteDatabase, cls).__new__(cls)
                cls._instance._db_name = db_name
                cls._instance._initialized = False
        return cls._instance

    def get_connection(self):
        conn = sqlite3.connect(self._db_name)
        conn.row_factory = sqlite3.Row
        return conn

    def setup(self):
        if self._initialized:
            return
        
        with self.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sections'")
            if cursor.fetchone() is not None:
                self._initialized = True
                return
            
            sql_file = Path(__file__).parent.parent.parent.parent / "test_db.sql"
            
            if sql_file.exists():
                with open(sql_file, 'r', encoding='utf-8') as f:
                    sql_script = f.read()
                    cursor.executescript(sql_script)
            
            conn.commit()
            self._initialized = True
