import os
from os.path import join, dirname

from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


PROJECT = 'play-store-api'
VERSION = '2'


def get_config_environment():
    config = dict()
    config['development'] = Development
    config['production'] = Production
    environment = os.environ.get('ENVIRONMENT_CONFIG', 'development').lower()
    return config.get(environment, Development)


class Config(object):
    API_NAME = PROJECT
    API_VERSION = VERSION
    API_DESCRIPTION = 'Retrieve app details from Play Store'
    DEBUG = False
    TESTING = False


class Test(Config):
    DEBUG = True
    TESTING = True


class Development(Config):
    API_VERSION = '{}-dev'.format(VERSION)
    DEBUG = True


class Production(Config):
    pass
