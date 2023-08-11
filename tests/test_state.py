#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    def test_default_values(self):
        state = State()
        self.assertEqual(state.name, "")
        
    def test_attributes(self):
        name = "Lagos"
        
        state = State(name=name)
        
        self.assertEqual(state.name, name)
        
    def test_inheritance(self):
        state = State()
        self.assertIsInstance(state, BaseModel)
    
    def test_long_name(self):
        """Test if the class handles long names properly"""
        name = "A" * 100
        state = State(name=name)
        self.assertEqual(state.name, name[:255])     
   
    
if __name__ == '__main__':
    unittest.main()
