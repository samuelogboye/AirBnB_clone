#!/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    def test_default_values(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
        
    def test_attributes(self):
        text = "I love the arena"
        user_id = "1122"
        place_id = "4492"
        
        review = Review(text=text, user_id=user_id, place_id=place_id)
        
        self.assertEqual(review.text, text)
        self.assertEqual(review.place_id, place_id)
        self.assertEqual(review.user_id, user_id)
        
    def test_inheritance(self):
        review = Review()
        self.assertIsInstance(review, BaseModel)
    
    def test_long_name(self):
        """Test if the class handles long names properly"""
        name = "A" * 100
        review = Review(name=name)
        self.assertEqual(review.name, name[:255])     
   
    
if __name__ == '__main__':
    unittest.main()
