from __future__ import annotations
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from models.address import Address
    from models.student import Student

from models.person import Person


class Professor(Person):
    def __init__(self, name: str, phone_number: str, email_address: str, address: Address,
                 staff_number: int, years_of_service: int = 0):
        super().__init__(name, phone_number, email_address, address)
        self._staff_number = staff_number  # Protected
        self.__years_of_service = years_of_service  # Private
        self.number_of_classes = 0  # Public
        self._salary = 0  # Protected
        self._supervising_students: List[Student] = []  # Protected
        
        self._calculate_salary()

    def _calculate_salary(self) -> None:
        base_salary = 5_000_000
        experience_bonus = self.__years_of_service * 500_000
        self._salary = base_salary + experience_bonus

    @property
    def salary(self) -> int:
        return self._salary

    @property
    def staff_number(self) -> int:
        return self._staff_number

    @property
    def years_of_service(self) -> int:
        return self.__years_of_service

    def add_student(self, student: Student) -> bool:
        if len(self._supervising_students) >= 5:
            return False  # Max 5 students
        if student not in self._supervising_students:
            self._supervising_students.append(student)
            return True
        return False

    def remove_student(self, student: Student) -> bool:
        if student in self._supervising_students:
            self._supervising_students.remove(student)
            return True
        return False

    def get_supervising_students(self) -> List[Student]:
        return self._supervising_students.copy()

    def update_years_of_service(self, years: int) -> None:
        self.__years_of_service = years
        self._calculate_salary()

    def add_class(self) -> None:
        self.number_of_classes += 1

    def remove_class(self) -> None:
        if self.number_of_classes > 0:
            self.number_of_classes -= 1

    def get_professor_info(self) -> str:
        base_info = super().get_person_info()
        return (f"{base_info} | Staff Number: {self.staff_number} | "
                f"Years of Service: {self.years_of_service} | Classes: {self.number_of_classes} | "
                f"Salary: Rp{self.salary:,} | Supervising: {len(self._supervising_students)} students")

    def __str__(self) -> str:
        return self.get_professor_info()

    def __repr__(self) -> str:
        return (f"Professor(name='{self.name}', phone_number='{self.phone_number}', "
                f"email_address='{self.email_address}', address={repr(self.address)}, "
                f"staff_number={self.staff_number}, years_of_service={self.years_of_service}, "
                f"number_of_classes={self.number_of_classes}, salary={self.salary})")