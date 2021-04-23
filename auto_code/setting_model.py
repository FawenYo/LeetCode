from typing import List

from rich.console import Console

console = Console()


class Setting:
    def __init__(self) -> None:
        self.QUESTIONS: List[str] = [""]
        self.FETCH_FROM_SERVER: bool = True
        self.SHOW_QUESTIONS: bool = True

        self.DATE = "2021-04-25"
        self.OPTIONAL = True
