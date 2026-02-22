class Section:

    def __init__(
        self,
        id: int,
        title: str,
    ):
        self._id = id
        self._title = title

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def title(self) -> str:
        return self._title
    
    @id.setter
    def id(self, value: int) -> None:
        self._id = value
    
    @title.setter
    def title(self, value: str) -> None:
        self._title = value
