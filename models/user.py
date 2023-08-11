#!/usr/bin/python3
"""Defines a User class"""

from models.base_model import BaseModel

class User(BaseModel):
    """The class that defines User object inherited from Basemodel"""
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
