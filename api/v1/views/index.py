#!/usr/bin/python3
"""
returns a json object; the status
"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def status():
    """
    returns the status of the request
    """
    api_status = {"status": "OK"}
    return jsonify(api_status)


@app_views.route('/stats')
def stats():
    """
    retrieves the number of each objects by type
    """
    objects = {
            "amenities": storage.count("Amenity"),
            "cities": storage.count("City"),
            "places": storage.count("Place"),
            "reviews": storage.count("Review"),
            "states": storage.count("State"),
            "users": storage.count("User")
            }

    return jsonify(objects)
