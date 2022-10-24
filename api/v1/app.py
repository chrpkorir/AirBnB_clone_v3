#!/usr/bin/python3
"""returns the status of the API"""

from os import getenv
from models import storage
from api.v1.views import app_views
from flask import Flask

"""Host and port env variables"""
host_env = getenv('HBNB_API_HOST') or '0.0.0.0'
port_env = getenv('HBNB_API_PORT') or 5000


app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down_db(error):
    """closes the sdb session"""
    storage.close()


if __name__ == "__main__":

    app.run(
            host=host_env, port=port_env,
            threaded=True
            )
