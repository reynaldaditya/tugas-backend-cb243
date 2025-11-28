from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.address import Address

from models.person import Person


class Student(Person):
    """
    Class representing a student, inherits from Person.
    
    Attributes:
        student_number (int): Unique student identifier
        average_mark (int): Student's average academic mark (0-100)
    """
    
    def __init__(self, name: str, phone_number: str, email_address: str, address: Address, 
                 student_number: int, average_mark: int = 0):
        super().__init__(name, phone_number, email_address, address)
        self.student_number = student_number
        self.average_mark = average_mark
        self._seminars_taken = 0  # Private attribute

    def is_eligible_to_enroll(self, course: str) -> bool:
        """
        Check if student is eligible to enroll in a course.
        
        Args:
            course (str): Course name to check eligibility for
            
        Returns:
            bool: True if eligible, False otherwise
        """
        # Simple eligibility logic based on course type and average mark
        if "advanced" in course.lower():
            return self.average_mark >= 80
        else:
            return self.average_mark >= 70

    def get_seminars_taken(self) -> int:
        """
        Get the number of seminars taken by the student.
        
        Returns:
            int: Number of seminars taken
        """
        return self._seminars_taken

    def take_seminar(self) -> None:
        """Register the student for one seminar."""
        self._seminars_taken += 1

    def update_average_mark(self, new_mark: int) -> None:
        """
        Update the student's average mark.
        
        Args:
            new_mark (int): New average mark (0-100)
            
        Raises:
            ValueError: If mark is not between 0 and 100
        """
        if 0 <= new_mark <= 100:
            self.average_mark = new_mark
        else:
            raise ValueError("Average mark must be between 0 and 100.")

    def get_student_info(self) -> str:
        """Return detailed student information."""
        base_info = super().get_person_info()
        return (f"{base_info} | Student Number: {self.student_number} | "
                f"Average Mark: {self.average_mark} | Seminars Taken: {self._seminars_taken}")

    def __str__(self) -> str:
        return self.get_student_info()

    def __repr__(self) -> str:
        return (f"Student(name='{self.name}', phone_number='{self.phone_number}', "
                f"email_address='{self.email_address}', address={repr(self.address)}, "
                f"student_number={self.student_number}, average_mark={self.average_mark}, "
                f"seminars_taken={self._seminars_taken})")