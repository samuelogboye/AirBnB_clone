#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    def test_default_values(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        
    def test_attributes(self):
        name = "table"
        
        amenity = Amenity(name=name)
        
        self.assertEqual(amenity.name, name)
        
    def test_inheritance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
    
    def test_long_name(self):
        """Test if the class handles long names properly"""
        name = "A" * 100
        amenity = Amenity(name=name)
        self.assertEqual(amenity.name, name[:255])     
   
    
if __name__ == '__main__':
    unittest.main()
