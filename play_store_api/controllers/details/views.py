import re

from flask_restplus import fields, Resource

from play_store_api.controllers.details import details
from play_store_api.models.details import AppDetails, details_model, histogram_model


histogram = details.model('Histogram', histogram_model)
details_model['histogram'] = fields.Nested(histogram)
app_details_model = details.model('AppDetails', details_model)


@details.route('/<string:app_id>')
@details.doc(responses={404: 'App not found'})
@details.param('app_id', description='App ID as package name', example='com.android.chrome')
class Details(Resource):
    @details.doc('get_details')
    @details.response(400, 'Invalid app ID format')
    @details.marshal_with(app_details_model)
    def get(self, app_id, lang='en', country='us'):
        regex = re.compile(r'^[A-Za-z0-9_-]+\.[A-Za-z0-9\._-]+$')
        if not regex.match(app_id):
            details.abort(400, "Invalid app ID format, must be like com.android.chrome")
        app_details = AppDetails()
        response = app_details.get_by_id(app_id, lang, country)
        if response:
            return response
        details.abort(404, 'The app {} no exists'.format(app_id))
