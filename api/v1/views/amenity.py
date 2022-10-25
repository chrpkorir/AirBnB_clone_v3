#!/usr/bin/python3
""" handles API calls to the amenity """

from api.v1.views import app_views
from flask import jsonify
from models.amenity import Amenity
from models import storage


@app_views.route('/amenities', methods=['GET'])
def amenity_objs():
    """Retrieves the list of all Amenity Objects"""
    amenities_objs = storage.all(Amenity).values()
    amenities_response = [obj.to_dict() for obj in amenities_objs]
    return jsonify(amenities_response)
