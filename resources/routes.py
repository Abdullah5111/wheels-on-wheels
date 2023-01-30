from resources.resources import AdApi

def initialize_routes(api):
    api.add_resource(AdApi, "/api/ads")