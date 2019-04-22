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
    @details.marshal_with(app_details_model)
    def get(self, app_id, lang='en', country='us'):
        app_details = AppDetails()
        return app_details.get_by_id(app_id, lang, country)
