from play_store_api import create_api

api = create_api()
# Makes compatible with Passenger WSGI servers
application = api

if __name__ == "__main__":
    api.run()
