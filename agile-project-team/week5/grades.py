"""Grade book for the TDD kata.

A student records grades for courses, each with a credit-hour value.
"""

MAX_CREDITS = 18


class GradeError(Exception):
    """Raised when a grade cannot be added or removed."""


class GradeBook:
    """A student's recorded grades."""

    def __init__(self, student_id):
        self.student_id = student_id
        self.courses = {}

    @property
    def total_credits(self):
        """Return the sum of credit hours for all recorded grades."""
        return sum(self.courses.values())

    def add_grade(self, code, hours):
        """Record a grade for a course, enforcing the credit limit."""
        if code in self.courses:
            raise GradeError(f"{code} is already registered")
        if self.total_credits + hours > MAX_CREDITS:
            raise GradeError("credit-hour limit is 18")
        self.courses[code] = hours

    def remove_grade(self, code):
        """Remove a recorded grade for a course."""
        if code not in self.courses:
            raise GradeError(f"{code} is not registered")
        del self.courses[code]
