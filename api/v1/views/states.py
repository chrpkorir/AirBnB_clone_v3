#!/usr/bin/python3
"""
handles all default RESTFul API actions to states
"""

from api.v1.views import app_views
from flask import abort, jsonify
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
    """
    state = storage.get('State', state_id)
    if state is None:
        abort(404)
    else:
        state_response = state.to_dict()

    return jsonify(state_response)
