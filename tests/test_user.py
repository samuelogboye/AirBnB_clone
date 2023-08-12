#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def test_default_values(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attributes(self):
        email = "test@example.com"
        password = "password123"
        first_name = "John"
        last_name = "Doe"
        user = User(email=email, password=password,
                    first_name=first_name, last_name=last_name)
        self.assertEqual(user.email, email)
        self.assertEqual(user.password, password)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)

    def test_inheritance(self):
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_long_name(self):
        """Test if the class handles long names properly"""
        first_name = "A" * 100
        last_name = "B" * 100
        user = User(first_name=first_name, last_name=last_name)
        self.assertEqual(user.first_name, first_name[:255])


if __name__ == '__main__':
    unittest.main()
