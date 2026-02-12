from textual.widgets import Footer


class FooterApp(Footer):
    """Footer customizado para a aplicação."""
    
    DEFAULT_CSS = """
    FooterApp {
        background: #444444;
    }
    """
