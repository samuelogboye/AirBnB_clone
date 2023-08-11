#!/usr/bin/python3
"""Defines a City class"""

from models.base_model import BaseModel

class City(BaseModel):
    """The class that defines City object inherited from Basemodel"""
    state_id = ""
    name = ""