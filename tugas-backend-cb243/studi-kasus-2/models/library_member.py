from typing import List
from models.library_item import LibraryItem


class LibraryMember:
    def __init__(self, member_id: int, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_items: List[LibraryItem] = []

    def borrow_item(self, item: LibraryItem) -> None:
        if item in self.borrowed_items:
            raise ValueError(f"Item '{item.title}' is already borrowed by {self.name}")
        
        self.borrowed_items.append(item)
        print(f"✅ {self.name} successfully borrowed '{item.title}'")

    def return_item(self, item: LibraryItem) -> None:
        if item not in self.borrowed_items:
            raise ValueError(f"Item '{item.title}' is not borrowed by {self.name}")
        
        self.borrowed_items.remove(item)
        print(f"✅ {self.name} successfully returned '{item.title}'")

    def get_borrowed_items(self) -> List[LibraryItem]:
        return self.borrowed_items.copy()

    def display_borrowed_items(self) -> None:
        if not self.borrowed_items:
            print(f"📚 {self.name} has no borrowed items")
            return
        
        print(f"📚 {self.name}'s borrowed items ({len(self.borrowed_items)} items):")
        for i, item in enumerate(self.borrowed_items, 1):
            print(f"  {i}. {item.title} (ID: {item.item_id})")

    def calculate_total_late_fees(self, days_late_dict: dict) -> float:
        total_fee = 0.0
        
        for item in self.borrowed_items:
            days_late = days_late_dict.get(item.item_id, 0)
            if days_late > 0:
                fee = item.calculate_late_fee(days_late)
                total_fee += fee
                print(f"   - '{item.title}': {days_late} days late = Rp {fee:,.0f}")
        
        return total_fee

    def get_member_info(self) -> str:
        """Get member information as string."""
        return f"Member {self.member_id}: {self.name} ({len(self.borrowed_items)} items borrowed)"

    def __str__(self) -> str:
        return self.get_member_info()

    def __repr__(self) -> str:
        return f"LibraryMember(member_id={self.member_id}, name='{self.name}')"