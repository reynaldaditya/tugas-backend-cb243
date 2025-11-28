from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.address import Address


class Person:
    def __init__(self, name: str, phone_number: str, email_address: str, address: Address):
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address
        self.address = address

    def purchase_parking_pass(self) -> str:
        return f"{self.name} has purchased a parking pass."

    def update_contact_info(self, phone_number: str = None, email_address: str = None) -> None:
        if phone_number:
            self.phone_number = phone_number
        if email_address:
            self.email_address = email_address

    def set_address(self, address: Address) -> None:

        self.address = address

    def get_person_info(self) -> str:
        address_info = self.address.get_full_address() if self.address else "No address"
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email_address}, Address: {address_info}"

    def __str__(self) -> str:
        return self.get_person_info()

    def __eq__(self, other) -> bool:
        if not isinstance(other, Person):
            return False
        return (self.name == other.name and
                self.phone_number == other.phone_number and
                self.email_address == other.email_address and
                self.address == other.address)

    def __repr__(self) -> str:
        return (f"Person(name='{self.name}', phone_number='{self.phone_number}', "
                f"email_address='{self.email_address}', address={repr(self.address)})")