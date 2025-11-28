from datetime import datetime


class Author:
    def __init__(self, name: str, birth_year: int):
        self.name = name
        self.birth_year = birth_year

    def get_age(self, current_year: int = None) -> int:
        if current_year is None:
            current_year = datetime.now().year
        
        if self.birth_year > current_year:
            raise ValueError("Birth year cannot be in the future")
        
        return current_year - self.birth_year

    def display_info(self) -> str:
        try:
            age = self.get_age()
            return f"Author: {self.name} (Born: {self.birth_year}, Age: {age})"
        except ValueError:
            return f"Author: {self.name} (Born: {self.birth_year})"

    def __str__(self) -> str:
        return self.display_info()

    def __eq__(self, other) -> bool:
        if not isinstance(other, Author):
            return False
        return self.name == other.name and self.birth_year == other.birth_year

    def __repr__(self) -> str:
        return f"Author(name='{self.name}', birth_year={self.birth_year})"