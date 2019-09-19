#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created on 9/19/19 by Pat Daburu
"""
.. currentmodule:: synolo_flask.exports
.. moduleauthor:: Pat Daburu <pat@daburu.net>

This module contains the "export" endpoints.
"""
from pathlib import Path
import tempfile
from typing import List
from flask import current_app as app
from flask_restplus import Namespace, Resource, fields, reqparse
from flask_restplus.model import Model
from jsendit import response, JSendStatus
from werkzeug.datastructures import FileStorage
from .. import __version__

api = Namespace('exports', description='Export data.')


#: `ExportGisResource` filter arguments
export_gis_filter_parser = reqparse.RequestParser()
export_gis_filter_parser.add_argument('urn', required=False, action='append')


def allowed_file(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in \
           app.config['UPLOAD_EXTENSIONS']


@api.route('/gis/')
class ExportRegionalGisResource(Resource):

    @api.doc('Export the regional GIS data set.')
    def get(self):
        return response(
            status=JSendStatus.SUCCESS,
            message="Success."
        )


@api.route('/gis/<string:urn>')
class ExportLocalGisResource(Resource):

    @api.doc('Export the local GIS data set.')
    def get(self, urn: str):
        return response(
            status=JSendStatus.SUCCESS,
            message=urn if urn else 'No URN'
        )


@api.route('/gis/')
class ExportFilteredGisResource(Resource):

    @api.doc('Export a filtered GIS data set.')
    def post(self):
        # Parse the arguments.
        args = export_gis_filter_parser.parse_args()
        # Get the filter URNs.
        _urn = args.get('urn')
        # The incoming argument may be a string, a list, or nothing.  Let's
        # figure it out now.
        urns = (
            {_urn} if isinstance(_urn, str)
            else set(_urn)
        ) if _urn else []

        return response(
            status=JSendStatus.SUCCESS,
            message=','.join(urns)
        )
