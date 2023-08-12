#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def test_default_values(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_attributes(self):
        name = "Lagos"
        state_id = "1122"

        city = City(name=name, state_id=state_id)

        self.assertEqual(city.name, name)
        self.assertEqual(city.state_id, state_id)

    def test_inheritance(self):
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_long_name(self):
        """Test if the class handles long names properly"""
        name = "A" * 100
        city = City(name=name)
        self.assertEqual(city.name, name[:255])


if __name__ == '__main__':
    unittest.main()
