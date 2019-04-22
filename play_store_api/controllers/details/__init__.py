# flake8: noqa
# pylint: disable=wildcard-import
from flask_restplus import Namespace


details = Namespace('details', description='Get specific app details')


from .views import *
