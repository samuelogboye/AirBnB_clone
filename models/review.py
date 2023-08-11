#!/usr/bin/python3
"""Defines a Review class"""

from models.base_model import BaseModel

class Review(BaseModel):
    """The class that defines User object inherited from Basemodel"""
    place_id = ""
    user_id = ""
    text = ""
    