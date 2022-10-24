#!/usr/bin/python3
"""
handles all default RESTFul API actions to states
"""

from api.v1.views import app_views
from flask import jsonify
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
