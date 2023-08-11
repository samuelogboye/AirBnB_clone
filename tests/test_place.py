#!/usr/bin/python3
import unittest
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    def test_default_values(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])
        
        
    def test_attributes(self):
        name = "Abuja"
        user_id = "1122"
        city_id = "4492"
        description = "Serene"
        number_rooms = "42"
        number_bathrooms = "42"
        max_guest = "4"
        price_by_night = "44944"
        latitude = "4.4"
        longitude = "2.2"
        amenity_ids = [333, 555, 666]
        
        place = Place(name=name, user_id=user_id, city_id=city_id,
                      description=description, number_rooms=number_rooms,
                      number_bathrooms=number_bathrooms, max_guest=max_guest,
                      price_by_night=price_by_night, latitude=latitude,
                      longitude=longitude, amenity_ids=amenity_ids)
        
        self.assertEqual(place.name, name)
        self.assertEqual(place.city_id, city_id)
        self.assertEqual(place.user_id, user_id)
        self.assertEqual(place.description, description)
        self.assertEqual(place.number_rooms, number_rooms)
        self.assertEqual(place.number_bathrooms, number_bathrooms)
        self.assertEqual(place.max_guest, max_guest)
        self.assertEqual(place.price_by_night, price_by_night)
        self.assertEqual(place.latitude, latitude)
        self.assertEqual(place.longitude, longitude)
        self.assertEqual(place.amenity_ids, amenity_ids)
        
    def test_inheritance(self):
        place = Place()
        self.assertIsInstance(place, BaseModel)
    
    def test_long_name(self):
        """Test if the class handles long names properly"""
        name = "A" * 100
        place = Place(name=name)
        self.assertEqual(place.name, name[:255])     
   
    
if __name__ == '__main__':
    unittest.main()
