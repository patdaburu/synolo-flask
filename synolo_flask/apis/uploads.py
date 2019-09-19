#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created on 9/19/19 by Pat Daburu
"""
.. currentmodule:: upload
.. moduleauthor:: Pat Daburu <pat@daburu.net>

This module contains the "upload" endpoints.
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

api = Namespace('uploads', description='Upload Endpoints')

upload_parser = reqparse.RequestParser()
upload_parser.add_argument(
    'file',
    location='files',
    type=FileStorage,
    required=True,
    action='append'
)


def allowed_file(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in \
           app.config['UPLOAD_EXTENSIONS']


@api.route('/<string:data>/')
class UploadStitchResource(Resource):

    @api.doc('Upload Data')
    @api.expect(upload_parser)
    def post(self, data: str):
        args = upload_parser.parse_args()

        uploads: List[FileStorage] = args.get('file')

        # If no files are being uploaded...
        if not uploads:
            # ...that's a fail on the client's part.
            return response(
                status=JSendStatus.FAIL,
                message='Upload files must be included.'
            )
        # Get a list of any files that aren't supported.
        unsupported_uploads = [
            u for u in uploads
            if not allowed_file(u.filename)
        ]
        # If we found unsupported files, that's a fail from the client.
        if unsupported_uploads:
            return response(
                status=JSendStatus.FAIL,
                message=f'Unsupported files: '
                        f'{[u.filename for u in unsupported_uploads]}'
            )

        # TODO: Implement proper file handling.

        tmpdir = Path('/tmp/upload')
        tmpdir.mkdir(parents=True, exist_ok=True)

        for upload in uploads:
            upload_suffix = Path(upload.filename).suffix
            save_path = Path(tmpdir / data).with_suffix(upload_suffix)
            upload.save(str(save_path))

        return response(
            status=JSendStatus.SUCCESS,
            message='Uploaded succeeded!'
        )


