from models.library_item import LibraryItem
from models.author import Author


class Book(LibraryItem):
    def __init__(self, item_id: int, title: str, author: Author, isbn: str):
        super().__init__(item_id, title)
        self.author = author
        self.isbn = isbn

    def display_info(self) -> None:
        print(f"Book ID: {self.item_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author.name}")
        print(f"ISBN: {self.isbn}")
        print(f"Author Info: {self.author.display_info()}")

    def calculate_late_fee(self, days_late: int) -> float:
        if days_late < 0:
            raise ValueError("Days late cannot be negative")
        
        rate_per_day = 2000  # Rp 2,000 per day
        return days_late * rate_per_day

    def get_book_info(self) -> str:
        return f"Book '{self.title}' by {self.author.name} (ISBN: {self.isbn})"

    def __str__(self) -> str:
        return self.get_book_info()

    def __repr__(self) -> str:
        return (f"Book(item_id={self.item_id}, title='{self.title}', "
                f"author={repr(self.author)}, isbn='{self.isbn}')")