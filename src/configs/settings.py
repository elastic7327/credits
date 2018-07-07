"""
File: settings.py
Author: Me
Email: yourname@email.com
Github: https://github.com/yourname
Description:
"""


class Config(object):  # pylint: disable=too-few-public-methods
    """
    doc
    """
    DEBUG = False
    TESTING = False
    # DATABASE_URI = 'sqlite://'


class DevelopmentConfig(Config):  # pylint: disable=too-few-public-methods
    """
    doc
    """
    DEBUG = True
    TESTING = True
    # DATABASE_URI = 'sqlite://'
    # SQLALCHEMY_DATABASE_URI = 'sqlite://'


class ProductionConfig(Config):  # pylint: disable=too-few-public-methods
    """
    doc
    """
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'
