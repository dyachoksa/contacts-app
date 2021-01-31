import json
from unittest import TestCase

from app.json_encoder import ContactAwareJSONEncoder
from app.models import Contact


class TestContactAwareJSONEncoder(TestCase):
    def test_encode(self):
        """ContactAwareJSONEncoder should correctly encode Contact model"""

        contact = Contact("Test User", "user@test.com")

        result = json.dumps(contact, cls=ContactAwareJSONEncoder)

        expected_result = '{"name": "Test User", "email": "user@test.com"}'

        self.assertEqual(result, expected_result)
