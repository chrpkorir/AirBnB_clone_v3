#!/usr/bin/python3
"""handle API functionson the city object"""

from api.v1.views import app_views
from flask import Flask, abort, jsonify
from models.city import City
from models import storage


@app_views.route('/states/,state_id>/cities')
def all_cities(state_id):
    """
    returns all the city objects
    """
    get_state = storage.get('State', state_id)
    if get_state is None:
        abort(404)
    cities_response = [city.to_dict() for city in get_state.cities]

    return jsonify(cities_response)
