#!/usr/bin/python3
"""
Contains the TestDbStorage classes and TestDBStorageDocs
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Ameninty
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place, 
           "Review": Review, "State": State, "User": User}

