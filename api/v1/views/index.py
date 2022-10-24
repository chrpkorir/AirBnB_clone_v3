#!/usr/bin/python3
"""
returns a json object; the status
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'])
def status():
    """
    returns the status of the request
    """
    api_status = {"status": "OK"}
    return jsonify(api_status)


@app_views.route('/stats', methods=['GET'])
def stats():
    """
    retrieves the number of each objects by type
    """
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)
