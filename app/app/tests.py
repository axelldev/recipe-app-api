"""
Saple tests
"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Tests for the calc module."""

    def test_add_function(self):
        """Tets the addion fuction of 2 numbers."""
        result: int = calc.add(3, 10)
        self.assertEqual(result, 13)

    def test_subtract_function(self):
        """Test the subtraction between 2 numbers."""
        result: int = calc.sub(5, 11)
        self.assertEqual(result, -6)
