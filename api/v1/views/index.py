#!/usr/bin/python3
"""
returns a json object; the status
"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """
    returns the status of the request
    """
    return jsonify({"status": "OK"})
