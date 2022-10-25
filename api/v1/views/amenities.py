#!/usr/bin/python3
""" handles API calls to the amenity """

from api.v1.views import app_views
from flask import abort, jsonify, make_response
from models.amenity import Amenity
from models import storage


@app_views.route('/amenities', methods=['GET'])
def amenity_objs():
    """Retrieves the list of all Amenity Objects"""
    amenities_objs = storage.all(Amenity).values()
    amenities_response = [obj.to_dict() for obj in amenities_objs]
    return jsonify(amenities_response)


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def amenity_by_id(amenity_id=None):
    """Retrieves an Amenity object by its id"""
    amenity_obj = storage.get(Amenity, amenity_id)
    if amenity_obj:
        return jsonify(amenity_obj.to_dict())
    abort(404)


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id=None):
    """Deletes an Amenity object by its id"""
    amenity_objs = storage.get(Amenity, amenity_id)
    if amenity_objs:
        storage.delete(amenity_objs)
        storage.save()
        return make_response(jsonify({}), 200)
    abort(404)
