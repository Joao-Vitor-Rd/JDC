from .app import MeuAppCLI

def start():
    app = MeuAppCLI()
    app.run()

if __name__ == "__main__":
    start()