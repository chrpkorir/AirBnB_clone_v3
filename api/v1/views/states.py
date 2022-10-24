#!/usr/bin/python3
"""
handles all default RESTFul API actions to states
"""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models.state import State
from models import storage


@app_views.route('/states')
def all_states():
    """
    returns all the states
    """
    get_states = storage.all('State').values()
    states = []
    for obj in get_states:
        states.append(obj.to_dict())

    return jsonify(states)


@app_views.route('/states/<state_id>')
def list_state(state_id):
    """
    returns a single state object

    Args::
        state_id: the state object's id
    """
    get_state = storage.get('State', state_id)
    if get_state is None:
        abort(404)
    else:
        state_response = get_state.to_dict()

    return jsonify(state_response)


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """
    deletes a state object using its id

    Args::
        state_id: the id of the state object
    """
    get_state = storage.get('State', state_id)
    if get_state is None:
        abort(404)
    else:
        storage.delete(get_state)
        storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/states/<state_id>', methods=['POST'])
def add_state():
    """
    add a new state using POST request
    """
    if not request.json:
        abort(400, "Not a JSON")
    else:
        state_data = request.json
        if 'name' not in state_data.keys():
            abort(400, "Missing name")
        state_instance = State(**state_data)
        storage.new(state_instance)
        storage.save()

        state_response = state_instance.to_dict()

    return make_response(jsonify(state_response), 201)
