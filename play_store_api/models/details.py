from flask_restplus import fields

import play_scraper


histogram_model = {
    '1': fields.Integer(
        title='1 star',
        description='Total of 1 star ratings on Play Store',
        example=4829,
        readOnly=True,
    ),
    '2': fields.Integer(
        title='2 stars',
        description='Total of 2 stars ratings on Play Store',
        example=2850,
        readOnly=True,
    ),
    '3': fields.Integer(
        title='3 stars',
        description='Total of 3 stars ratings on Play Store',
        example=1027,
        readOnly=True,
    ),
    '4': fields.Integer(
        title='4 stars',
        description='Total of 4 stars ratings on Play Store',
        example=402831,
        readOnly=True,
    ),
    '5': fields.Integer(
        title='5 stars',
        description='Total of 5 stars ratings on Play Store',
        example=9385028,
        readOnly=True,
    ),
}


details_model = {
    'app_id': fields.String(
        title='App ID',
        description='App package name',
        example='com.android.chrome',
        readOnly=True,
    ),
    'category': fields.List(
        fields.String(
            title='Category',
            description='App category on Play Store',
            example='COMMUNICATION',
            readOnly=True,
        ),
    ),
    'content_rating': fields.List(
        fields.String(
            title='Content rating',
            description='App content rating assigned on Play Store',
            example='Everyone',
            readOnly=True,
        ),
    ),
    'description': fields.String(
        title='Description',
        description='App description on Play Store',
        example='Google Chrome is a fast and secure web browser',
        readOnly=True,
    ),
    'description_html': fields.String(
        title='Description HTML',
        description='App description using HTML markup',
        example='<p>Google Chrome is a fast and secure web browser</p>',
        readOnly=True,
    ),
    'developer': fields.String(
        title='Developer',
        description='App developer screenname',
        example='Google LLC',
        readOnly=True,
    ),
    'developer_address': fields.String(
        title='Developer address',
        description='Developer postal address',
        example='1600 Amphitheatre Parkway, Mountain View 94043',
        default='',
        readOnly=True,
    ),
    'developer_email': fields.String(
        title='Developer email',
        description='Developer support email',
        example='apps-help@google.com',
        default='',
        readOnly=True,
    ),
    'developer_id': fields.String(
        title='Developer ID',
        description='Developer ID on Play Store',
        example='5700313618786177705',
        readOnly=True,
    ),
    'developer_url': fields.String(
        title='Developer URL',
        description='Developer Play Store URL',
        example='https://www.google.com/chrome/android',
        readOnly=True,
    ),
    'editors_choice': fields.Boolean(
        title='Editors choice',
        description='If the app is editors choice on Play Store',
        example=False,
        readOnly=True,
    ),
    'histogram': None,
    'iap': fields.Boolean(
        title='IAP',
        description='If the app have in app purchases',
        example=False,
        default=False,
        readOnly=True,
    ),
    'iap_range': fields.String(
        title='IAP range',
        description='Range of prices for in app purchases',
        example='$0.99-$9.99',
        default='',
        readOnly=True,
    ),
    'icon': fields.String(
        title='Icon',
        description='App icon URL',
        example='https://lh3.googleusercontent.com/nYhPnY2I',
        readOnly=True,
    ),
    'installs': fields.String(
        title='Installs',
        description='Total of installations',
        example='1,000,000,000+',
        readOnly=True,
    ),
    'interactive_elements': fields.List(
        fields.String(
            title='Interactive elements',
            description='If the developer report interactive elements',
            example='Unrestricted Internet',
            readOnly=True,
        ),
    ),
    'price': fields.String(
        title='Price',
        description='App price on Play Store, if is 0 the app is free',
        example='0',
        readOnly=True,
    ),
    'recent_changes': fields.String(
        title='Recent changes',
        description='recent changes for the app last version',
        example='We\'ve also included stability and performance improvements.',
        default='',
        readOnly=True,
    ),
    'required_android_version': fields.String(
        title='Required Android version',
        description='Specifications for supported Android versions',
        example='Varies with device',
        readOnly=True,
    ),
    'reviews': fields.Integer(
        title='Reviews',
        description='Total reviews for the app on Play Store',
        example=9289408,
        default=0,
        readOnly=True,
    ),
    'score': fields.String(
        title='Score',
        description='total ratings score for the app',
        example='4.7',
        default='',
        readOnly=True,
    ),
    'screenshots': fields.List(
        fields.String(
            title='Screenshots',
            description='App screenshots URLs',
            example='https://lh3.googleusercontent.com/lKPDNfs',
            readOnly=True,
        ),
    ),
    'size': fields.String(
        title='Size',
        description='App download size',
        example='Varies with device',
        readOnly=True,
    ),
    'title': fields.String(
        title='Title',
        description='App title',
        example='Google Chrome: fast and secure',
        readOnly=True,
    ),
    'updated': fields.String(
        title='Updated',
        description='App last updated date',
        example='May 10, 2019',
        default='',
        readOnly=True,
    ),
    'url': fields.String(
        title='URL',
        description='App URL on Play Store',
        example='https://play.google.com/store/apps/details?id=com.android.chrome',
        readOnly=True,
    ),
    'video': fields.String(
        title='Video',
        description='App video URL',
        example='https://youtube.com/watch?v=1839Hdu817D',
        default='',
        readOnly=True,
    ),
}


class AppDetails(object):
    def __init__(self, data=None):
        if data:
            data['histogram'] = Histogram(data['histogram'])
            for key in data:
                setattr(self, key, data[key])

    def get_by_id(self, app_id, lang, country):
        status = 200
        try:
            response = play_scraper.details(app_id, lang, country)
        except ValueError:
            response = None
            status = 404
        if 200 == status:
            return AppDetails(response)
        return response


class Histogram(object):
    def __init__(self, histogram):
        for key in histogram:
            setattr(self, str(key), histogram[key])
