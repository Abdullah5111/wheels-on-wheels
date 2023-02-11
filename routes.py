from resources import AdApi, SparePartAdApi, SellerApi, AdApiById, SparePartAdApiById, UserApi,LoginApi

def initialize_routes(api):
    api.add_resource(AdApi, "/api/ads")
    api.add_resource(SparePartAdApi, "/api/spare-parts")
    api.add_resource(AdApiById, "/api/ad/<id>")
    api.add_resource(SparePartAdApiById, "/api/spare-part/<id>")
    api.add_resource(SellerApi, "/api/sellers")
    api.add_resource(UserApi,"/api/User")
    api.add_resource(LoginApi, '/api/Login')