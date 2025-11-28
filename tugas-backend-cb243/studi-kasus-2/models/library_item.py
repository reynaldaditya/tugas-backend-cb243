from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, item_id: int, title: str):
        self.item_id = item_id
        self.title = title

    @abstractmethod
    def display_info(self) -> None:
        pass

    @abstractmethod
    def calculate_late_fee(self, days_late: int) -> float:
        pass

    def __str__(self) -> str:
        return f"Item {self.item_id}: {self.title}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, LibraryItem):
            return False
        return self.item_id == other.item_id

    def __repr__(self) -> str:
        return f"LibraryItem(item_id={self.item_id}, title='{self.title}')"