"""
secure_student.py
Secure Student class with encapsulation and validated accessors/mutators.
"""

from typing import Dict


class Student:
    def __init__(self, matric_no: str, name: str, initial_balance: float = 0.0):
        if not matric_no or not isinstance(matric_no, str):
            raise ValueError("matric_no must be a non-empty string")
        if not name or not isinstance(name, str):
            raise ValueError("name must be a non-empty string")
        if initial_balance < 0:
            raise ValueError("initial_balance cannot be negative")

        # Private attributes (convention: underscore-prefixed)
        self._matric_no: str = matric_no
        self._name: str = name
        self._cgpa: float = 0.0
        self._tuition_balance: float = float(initial_balance)
        self._grades: Dict[str, float] = {}

    # Read-only accessors for ID and name
    def get_matric_no(self) -> str:
        return self._matric_no

    def get_name(self) -> str:
        return self._name

    # Sensitive data accessors
    def get_cgpa(self) -> float:
        return float(self._cgpa)

    def get_tuition_balance(self) -> float:
        return float(self._tuition_balance)

    # Controlled mutators
    def add_grade(self, course_code: str, score: float) -> None:
        if not course_code or not isinstance(course_code, str):
            raise ValueError("course_code must be a non-empty string")
        if not isinstance(score, (int, float)) or not (0.0 <= score <= 100.0):
            raise ValueError("score must be a number between 0 and 100")
        self._grades[course_code] = float(score)
        self._recalculate_cgpa()

    def update_cgpa(self, new_cgpa: float) -> None:
        if not isinstance(new_cgpa, (int, float)) or not (0.0 <= new_cgpa <= 4.0):
            raise ValueError("new_cgpa must be between 0.0 and 4.0")
        self._cgpa = float(new_cgpa)

    def _recalculate_cgpa(self) -> None:
        if not self._grades:
            self._cgpa = 0.0
            return
        total = 0.0
        for score in self._grades.values():
            g = max(0.0, min(4.0, (score / 100.0) * 4.0))
            total += g
        self._cgpa = total / len(self._grades)

    def pay_tuition(self, amount: float) -> None:
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self._tuition_balance:
            raise ValueError("payment exceeds outstanding tuition balance")
        self._tuition_balance -= float(amount)

    # Useful representation for tests / debugging
    def to_dict(self) -> Dict[str, object]:
        return {
            "matric_no": self._matric_no,
            "name": self._name,
            "cgpa": self._cgpa,
            "tuition_balance": self._tuition_balance,
            "grades": dict(self._grades),
        }