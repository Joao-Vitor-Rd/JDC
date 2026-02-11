from textual.widgets import Header

class HeaderApp(Header):

    DEFAULT_CSS = """
    HeaderApp {
        height: 3;
        background: $surface;
    }
    """
    
    VERSION = "1.0"

    def __init__(
        self,
        title: str = "JDC",
        subtitle: str = "Version 0.1",
        show_clock: bool = True,
        *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.custom_title = title
        self.custom_subtitle = subtitle
        self.show_clock = show_clock

    def on_mount(self) -> None:
        self.app.title = self.custom_title
        self.app.sub_title = self.custom_subtitle
