#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created on 9/18/19 by Pat Daburu
"""
.. currentmodule:: synolo_flask.config
.. moduleauthor:: Pat Daburu <pat@daburu.net>

This is the primary application configuration.
"""
from pathlib import Path
import os
from typing import Any


class Defaults:
    DEBUG = False
    TESTING = False
    UPLOAD_PATH = Path.cwd().resolve() / 'uploads'
    UPLOAD_EXTENSIONS = {'zip', 'rar', '7z', 'gz', 'json'}


# def get_value(name: str, default: Any = None) -> Any:
#     """
#     Get a configuration value from the default configuration sources.
#
#     :param name: the configuration name
#     :param default: the value to return if no value is found within the
#         configuration sources
#     :return: the value
#     """
#     try:
#         return os.environ[name]
#     except KeyError:
#         return getattr(Defaults, name, default)


class Config(object):
    """
    This is the base class for configuration objects.
    """
    DEBUG = True if os.environ.get('DEBUG') == 'True' else False
    TESTING = True if os.environ.get('TESTING') == 'True' else False
    UPLOAD_PATH = os.environ.get('UPLOAD_PATH', Defaults.UPLOAD_PATH)
    UPLOAD_EXTENSIONS = Defaults.UPLOAD_EXTENSIONS


class ProductionConfig(Config):
    """
    This is the production configuration.
    """
    DEBUG = False


class StagingConfig(Config):
    """
    This is the staging configuration.
    """
    DEBUG = True


class DevelopmentConfig(Config):
    """
    This is the development configuration.
    """
    DEBUG = True


class TestingConfig(Config):
    """
    This is the testing configuration.
    """
    DEBUG = True


def get_name() -> str:
    """
    Get the simple name of the current configuration environment.

    :return: the simple name (*e.g.* 'production', or 'development', *etc.*)
    """
    return os.environ.get('FLASK_ENV', 'production')


def get_object_name() -> str:
    """
    Get the name of the configuration object.

    :return: the fully-qualified name of the configuration object
    """
    return f"{__name__}.{get_name().title()}Config"
