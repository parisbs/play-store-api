from flask import Flask
from flask_restplus import Api

from config import get_config_environment

from play_store_api.controllers import namespaces


def _register_namespaces(api):
    for namespace in namespaces:
        api.add_namespace(namespace)


def create_api(config=None):
    app = Flask(__name__)

    if config:
        app.config.from_object(config)
    else:
        app.config.from_object(get_config_environment())

    api = Api(
        app=app,
        title=app.config['API_NAME'],
        version=app.config['API_VERSION'],
        description=app.config['API_DESCRIPTION'],
        prefix='/v{}'.format(app.config['API_VERSION']),
        doc='/docs',
        catch_all_404s=True,
        contact='Paris N. Baltazar Salguero',
        contact_url='https://github.com/parisbs/play-store-api',
        contact_email='sieg.sb@gmail.com',
    )

    _register_namespaces(api)

    return app
