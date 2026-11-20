"""Fee policies for student invoices.

Each student type has its own policy class, so adding a new type needs no
change to make_invoice (Open/Closed Principle).
"""

# Strategy classes intentionally expose a single fee() method.
# pylint: disable=too-few-public-methods

FEE_PER_HOUR = 1200


class RegularPolicy:
    """Default fee: a fixed rate per credit hour."""

    def fee(self, hours):
        """Return the fee for the given credit hours."""
        return hours * FEE_PER_HOUR


class ScholarshipPolicy:
    """Half of the regular fee."""

    def fee(self, hours):
        """Return the discounted fee for the given credit hours."""
        return hours * FEE_PER_HOUR * 0.5


class InternationalPolicy:
    """Higher rate plus a one-off service fee."""

    RATE = 2000
    SERVICE_FEE = 5000

    def fee(self, hours):
        """Return the fee for the given credit hours."""
        return hours * self.RATE + self.SERVICE_FEE


POLICIES = {
    "regular": RegularPolicy(),
    "scholarship": ScholarshipPolicy(),
    "international": InternationalPolicy(),
}


class FileWriter:
    """Write invoice text to a file on disk."""

    def write(self, student_id, text):
        """Save the invoice text for a student."""
        with open(f"invoice_{student_id}.txt", "w", encoding="utf-8") as f:
            f.write(text)


def make_invoice(student, kind, writer=None):
    """Calculate and write an invoice, returning the total fee."""
    policy = POLICIES[kind]
    total = policy.fee(student.total_credits)
    text = f"Invoice for {student.student_id}: {int(total)} EGP"
    (writer or FileWriter()).write(student.student_id, text)
    return total
