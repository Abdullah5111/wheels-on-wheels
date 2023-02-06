from resources import AdApi, SellerApi, AdApiById,UserApi,LoginApi

def initialize_routes(api):
    api.add_resource(AdApi, "/api/ads")
    api.add_resource(AdApiById, "/api/ad/<id>")
    api.add_resource(SellerApi, "/api/sellers")
    api.add_resource(UserApi,"/api/User")
    api.add_resource(LoginApi, '/api/Login')