import pytest

from grades import GradeBook, GradeError


def test_add_grade_records_credits():
    book = GradeBook("2023001")
    book.add_grade("SET312", 3)
    assert book.total_credits == 3


def test_cannot_exceed_18_credits():
    book = GradeBook("2023001")
    book.add_grade("SET312", 15)
    with pytest.raises(GradeError):
        book.add_grade("SET472", 4)
    assert book.total_credits == 15


def test_cannot_add_duplicate_grade():
    book = GradeBook("2023001")
    book.add_grade("SET312", 3)
    with pytest.raises(GradeError):
        book.add_grade("SET312", 3)


def test_remove_grade_clears_credits():
    book = GradeBook("2023001")
    book.add_grade("SET312", 3)
    book.remove_grade("SET312")
    assert book.total_credits == 0


def test_remove_missing_grade_raises():
    book = GradeBook("2023001")
    with pytest.raises(GradeError):
        book.remove_grade("SET312")
