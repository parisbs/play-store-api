from flask_restplus import fields

from google_play_scraper import app


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
    'appId': fields.String(
        title='App ID',
        description='App package name',
        example='com.android.chrome',
        readOnly=True,
    ),
    'adSupported': fields.Boolean(
        title='Ad supported',
        description='The app ads support',
        example=False,
        readOnly=True,
    ),
    'containsAds': fields.Boolean(
        title='Contains ads',
        description='If the app contains ads or not',
        example=False,
        readOnly=True,
    ),
    'contentRating': fields.String(
        title='Content rating',
        description='App content rating assigned on Play Store',
        example='Everyone',
        readOnly=True,
    ),
    'contentRatingDescription': fields.String(
        title='Content rating description',
        description='The app content rating description',
        example='Mild Fantasy Violence',
        readOnly=True,
    ),
    'currency': fields.String(
        title='Currency',
        description='The price currency',
        example='USD',
        readOnly=True,
    ),
    'description': fields.String(
        title='Description',
        description='App description on Play Store',
        example='Google Chrome is a fast and secure web browser',
        readOnly=True,
    ),
    'descriptionHTML': fields.String(
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
    'developerAddress': fields.String(
        title='Developer address',
        description='Developer postal address',
        example='1600 Amphitheatre Parkway, Mountain View 94043',
        default='',
        readOnly=True,
    ),
    'developerEmail': fields.String(
        title='Developer email',
        description='Developer support email',
        example='apps-help@google.com',
        default='',
        readOnly=True,
    ),
    'developerId': fields.String(
        title='Developer ID',
        description='Developer ID on Play Store',
        example='5700313618786177705',
        readOnly=True,
    ),
    'developerWebsite': fields.String(
        title='Developer website',
        description='Developer Play Store website',
        example='https://www.google.com/chrome/android',
        readOnly=True,
    ),
    'free': fields.Boolean(
        title='Free',
        description='If the app is free or not',
        example=True,
        readOnly=True,
    ),
    'genre': fields.String(
        title='Genre',
        description='The app genre to display',
        example='Communication',
        readOnly=True,
    ),
    'genreId': fields.String(
        title='Genre ID',
        description='The app genre ID',
        example='COMMUNICATION',
        readOnly=True,
    ),
    'headerImage': fields.String(
        title='Header image',
        description='The app header image',
        example='https://play-lh.googleusercontent.com/WPIJiEaY1kOU3...',
        readOnly=True,
    ),
    'histogram': None,
    'offersIAP': fields.Boolean(
        title='Offers IAP',
        description='If the app have in app purchases',
        example=False,
        default=False,
        readOnly=True,
    ),
    'inAppProductPrice': fields.String(
        title='In App Product price range',
        description='Range of prices for in app purchases',
        example='$0.99-$9.99',
        default='',
        readOnly=True,
    ),
    'icon': fields.String(
        title='Icon',
        description='App icon URL',
        example='https://lh3.googleusercontent.com/nYhPnY2I...',
        readOnly=True,
    ),
    'installs': fields.String(
        title='Installs',
        description='Total of installations',
        example='1,000,000,000+',
        readOnly=True,
    ),
    'price': fields.String(
        title='Price',
        description='App price on Play Store, if is 0 the app is free',
        example='0',
        readOnly=True,
    ),
    'privacyPolicy': fields.String(
        title='Privacy policy',
        description='The app privacy policy URL',
        example='http://www.google.com/chrome/intl/en/privacy.html',
        readOnly=True,
    ),
    'recentChanges': fields.String(
        title='Recent changes',
        description='recent changes for the app last version',
        example='We\'ve also included stability and performance improvements.',
        default='',
        readOnly=True,
    ),
    'released': fields.String(
        title='Released',
        description='The released date of the app',
        example='Feb 7, 2012',
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
            example='https://lh3.googleusercontent.com/lKPDNfs...',
            readOnly=True,
        ),
    ),
    'summary': fields.String(
        title='Summary',
        description='App summary',
        example='Fast, simple, and secure. Google Chrome browser for Android phones and tablets.',
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
    'version': fields.String(
        title='Version',
        description='The last app version',
        example='Varies with device',
        readOnly=True,
    ),
    'video': fields.String(
        title='Video',
        description='App video URL',
        example='https://www.youtube.com/embed/DFXbVBFPOOs?ps=play&vq=large&rel=0&autohide=1&showinfo=0',
        default='',
        readOnly=True,
    ),
    'videoImage': fields.String(
        title='Video image',
        description='The app video thumbnail',
        example='https://play-lh.googleusercontent.com/KgDQ...',
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
            response = app(app_id, lang, country)
        except ValueError:
            response = None
            status = 404
        if 200 == status:
            return AppDetails(response)
        return response


class Histogram(object):
    def __init__(self, histogram):
        for idx, value in enumerate(histogram):
            setattr(self, str(idx + 1), histogram[idx])
