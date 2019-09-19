#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created on 9/18/19 by Pat Daburu
"""
.. currentmodule::synolo_flask.api
.. moduleauthor:: Pat Daburu <pat@daburu.net>

This is the
"""
from flask_restplus import Api
from .. import __version__
from .exports import api as exports
from .info import api as info
from .uploads import api as uploads

API_ROOT: str = '/api'  #: the common root for API routes

# Create the API object.
api = Api(
    title='Synolo REST API',
    version=__version__,
    description='This is the Synolo REST API'
    # Add other API metadata here.
)

# Add the namespaces.
api.add_namespace(info, path='/info')
api.add_namespace(exports, path='/exports')
api.add_namespace(uploads, path='/uploads')
