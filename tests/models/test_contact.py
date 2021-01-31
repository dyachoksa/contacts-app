from unittest import TestCase

from app.models import Contact


class TestContact(TestCase):
    """The contact model tests"""

    def setUp(self):
        self.name = "Test User"
        self.email = "user@test.com"
        self.contact = Contact(self.name, self.email)

    def test_structure(self):
        """Contact model should have all required fields"""
        self.assertEqual(self.contact.name, self.name)
        self.assertEqual(self.contact.email, self.email)

    def test_get_display_value(self):
        """Contact model should generate correct display value"""
        expected_result = f"{self.name} / {self.email}"
        self.assertEqual(self.contact.get_display_value(), expected_result,
                         "Expected to have display value as a '<name> / <email>'")

    def test_has_email(self):
        self.assertTrue(self.contact.has_email())

    def test_to_dict(self):
        expected_result = {"name": self.name, "email": self.email}
        self.assertDictEqual(self.contact.to_dict(), expected_result)
