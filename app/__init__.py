from .app import JDC
from .shared.utils import dir
from .shared.database import SQLiteDatabase

def start():
    dir.Dir.create_data_dir()
    
    db = SQLiteDatabase()
    db.setup()
    
    app = JDC()
    app.run()

if __name__ == "__main__":
    start()