# play-store-api
API to retrieve apps info from Play Store

## Requirements
* Python 3.6.15

## Install environment
1. Copy .env.example file to .env one and change the environment config if is necessary, change the port to a different one, e.g. 5000
2. Run `make install-deps`
3. Run `make run`
4. Go to http://localhost:5000/v2/details/com.android.chrome

## Open Source Libraries
[Google Play Scraper](https://pypi.org/project/google-play-scraper/)
