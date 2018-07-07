"""
File: settings.py
Author: Me
Email: yourname@email.com
Github: https://github.com/yourname
Description:
"""


class Config(object):
    """
    doc
    """
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'


class DevelopmentConfig(Config):
    """
    doc
    """
    DEBUG = True
    TESTING = True
    DATABASE_URI = 'sqlite://:memory:'


class ProductionConfig(Config):
    """
    doc
    """
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'
