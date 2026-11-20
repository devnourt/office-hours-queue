import pytest

from fees import make_invoice
from grades import GradeBook


@pytest.fixture
def student():
    book = GradeBook("2023001")
    book.add_grade("SET312", 3)
    book.add_grade("SET472", 3)
    return book


@pytest.mark.parametrize(
    "kind, expected",
    [
        ("regular", 7200),
        ("scholarship", 3600),
        ("international", 17000),
    ],
)
def test_invoice_total(student, kind, expected, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert make_invoice(student, kind) == expected


class FakeWriter:
    def __init__(self):
        self.saved = {}

    def write(self, student_id, text):
        self.saved[student_id] = text


def test_invoice_uses_injected_writer(student):
    fake = FakeWriter()
    make_invoice(student, "regular", writer=fake)
    assert fake.saved["2023001"] == "Invoice for 2023001: 7200 EGP"


def test_unknown_kind_is_rejected(student):
    with pytest.raises(KeyError):
        make_invoice(student, "visitor")
