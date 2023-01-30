from flask import Response, jsonify, request
from flask_restful import Resource
from database.models import Ad

class AdApi(Resource):
    def get(self):
        ads = Ad.objects().to_json()
        return Response(ads, mimetype="application/json", status=200)

    def post(self):
        data=request.get_json()
        print(data)
        ad = Ad(**data).save()
        return {'id':str(ad.id)},200
