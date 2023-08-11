#!/usr/bin/python3
"""Defines a User class"""

from models.base_model import BaseModel

class Place(BaseModel):
    """The class that defines User object inherited from Basemodel"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []