from flask_restplus import Resource

from play_store_api.controllers.health import health


@health.route('')
class Health(Resource):
    @health.doc(responses={200: 'OK', 500: 'The API is down'})
    def get(self):
        return 'OK'
