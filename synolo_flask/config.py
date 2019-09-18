#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created on 9/18/19 by Pat Daburu
"""
.. currentmodule:: config
.. moduleauthor:: Pat Daburu <pat@daburu.net>

This is the primary application configuration.
"""
import os


class Config(object):
    """
    This is the base class for configuration objects.
    """
    DEBUG = True if os.environ.get('DEBUG') == 'True' else False
    TESTING = True if os.environ.get('TESTING') == 'True' else False


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
    TESTING = True


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
