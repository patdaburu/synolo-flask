#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created on 9/18/19 by Pat Blair
"""
.. currentmodule:: synolo_flask.info
.. moduleauthor:: Pat Daburu <pat@daburu.net>

This module contains resources that provide general information about the API.
"""
from flask_restplus import Namespace, Resource, fields
from flask_restplus.model import Model
from .. import __version__

api = Namespace('info', description='Information About the API')

InfoModel: Model = api.model(
    'Info',
    {
        'version': fields.String(
            readOnly=True,
            description='the API version'
        )
    }
)  #: the information model


@api.route('/')
class InfoResource(Resource):
    """Get general information about the API."""
    @api.doc('get_info')
    @api.marshal_with(InfoModel, envelope='info')
    def get(self):
        """Get general information about the API"""
        return {
            'version': __version__
        }
