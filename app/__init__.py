from .app import JDC
from .util import dir
from .infrastructure.database import SQLiteDatabase

def start():
    dir.Dir.create_data_dir()
    
    # Inicializar banco de dados
    db = SQLiteDatabase()
    db.setup()
    
    app = JDC()
    app.run()

if __name__ == "__main__":
    start()