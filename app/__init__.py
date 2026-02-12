from .app import JDC
from .util import dir

def start():
    dir.Dir.create_data_dir()
    app = JDC()
    app.run()

if __name__ == "__main__":
    start()