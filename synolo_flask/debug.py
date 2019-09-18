#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created on 9/18/19 by Pat Daburu
"""
.. currentmodule:: debug
.. moduleauthor:: Pat Daburu <pat@daburu.net>

You can use this script to debug the REST service.
"""
from synolo_flask.app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4000', debug=True)
