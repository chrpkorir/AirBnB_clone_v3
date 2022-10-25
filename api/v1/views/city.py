#!/usr/bin/python3
"""handle API functions on the city object"""

from api.v1.views import app_views
from flask import Flask, Request, request, abort, jsonify, make_response
from models.city import City
from models import storage


@app_views.route('/states/,state_id>/cities')
def all_cities(state_id):
    """
    returns all the city objects
    """
    state = storage.get('State', state_id)
    if state is None:
        abort(404)
    cities_response = [city.to_dict() for city in state.cities]

    return jsonify(cities_response)


@app_views.route('/cities/<city_id>')
def list_cities(city_id):
    """
    returns a single city object
    """
    cities = storage.get('City', city_id)
    if cities is None:
        abort(404)

    cities_response = cities.to_dict()
    return jsonify(cities_response)


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """
    deletes a city object using it's id
    """
    city = storage.get('City', city_id)
    if city is None:
        abort(404)

    storage.delete(city)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/cities/<city_id>', method=['POST'])
def add_city(state_id):
    """
    post a city object
    """
    if not Request.json:
        abort(400, "Not a JSON")
    data = Request.json
    if 'name' not in data.keys():
        abort(400, "Missing name")

    state = storage.get("State", state_id)
    if state is None:
            abort(404)
    data['state_id'] = state_id
    instance = City(**data)
    storage.new(instance)
    storage.save()
