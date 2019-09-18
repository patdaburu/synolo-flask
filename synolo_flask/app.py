#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created on 9/18/19 by Pat Daburu
"""
.. currentmodule:: synolo_flask.app
.. moduleauthor:: Pat Daburu <pblair@daburu.net>

This is the entry point for the `Flask <http://flask.pocoo.org/>`_
application.
"""
import logging
import os
from flask import Blueprint, Flask
from flask_cors import CORS
from . import config
from .apis import api, API_ROOT


__logger__: logging.Logger = logging.getLogger(__name__)  #: the module logger


# Determine which configuration set we're using.
_config = config.get_object_name()
__logger__.info(
    f"The application is using the "
    f"'{config.get_name()}' configuration ({_config})."
)

# Create the Flask application.
app = Flask(__name__, static_url_path='')  #: the core Flask application
app.config.from_object(_config)
blueprint = Blueprint('api', __name__, url_prefix=API_ROOT)
api.init_app(blueprint)
app.register_blueprint(blueprint)
CORS(app)

# Set up special handling for static files.
if 'STATIC_FOLDER' in os.environ:
    app.static_folder = os.environ.get('STATIC_FOLDER')


@app.route('/')
def root():
    """Serve the default file."""
    return app.send_static_file('index.html')
