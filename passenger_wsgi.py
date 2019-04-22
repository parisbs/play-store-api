#!/home/blindoap/virtualenv/play-store-api/3.6/bin/python

from flup.server.fcgi import WSGIServer
from play_store_api import create_api

if __name__ == '__main__':
    api = create_api()
    WSGIServer(api).run()
