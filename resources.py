from flask import Response, request
from flask_restful import Resource
from models import Ad, Seller,User, SparePart

class AdApi(Resource):
    def get(self):
        ads = Ad.objects().to_json()
        return Response(ads, mimetype="application/json", status=200)

    def post(self):
        data=request.get_json()
        print("car data is",data)
        ad = Ad(**data).save()
        return {'id':str(ad.id)},200

class SparePartAdApi(Resource):
    def get(self):
        ads = SparePart.objects().to_json()
        return Response(ads, mimetype="application/json", status=200)

    def post(self):
        data=request.get_json()
        print(data)
        ad = SparePart(**data).save()
        return {'id':str(ad.id)},200

class AdApiById(Resource):
    def get(self,id):
        ad=Ad.objects.get(id=id).to_json()
        return Response(ad,mimetype="application/json",status=200)

    def put(self,id):
        body = request.get_json()
        Ad.objects.get(id=id).update(**body)
        return {'id':str(id)},200

    def delete(self,id):
        Ad.objects.get(id=id).delete()

class SparePartAdApiById(Resource):
    def get(self,id):
        ad=SparePart.objects.get(id=id).to_json()
        return Response(ad,mimetype="application/json",status=200)

    def put(self,id):
        body = request.get_json()
        SparePart.objects.get(id=id).update(**body)
        return {'id':str(id)},200

    def delete(self,id):
        SparePart.objects.get(id=id).delete()

class SellerApi(Resource):
    def get(self):
        sellers = Seller.objects().to_json()
        return Response(sellers, mimetype="application/json", status=200)

    def post(self):
        data=request.get_json()
        seller = Seller(**data).save()
        return {'id':str(seller.id)},200

class UserApi(Resource):
    def post(self):
        body=request.get_json()
        try: 
            res=User.objects(email=body["email"]).to_json()
            res1 = User.objects(name=body["uname"]).to_json()
            res=res+res1
            if(len(res)>4):
                return {"error":"User already exists"},200
            else:
                user1 = User(name=body["uname"],email=body["email"],password=body["password"]).save()
                id=user1.id
                return {'id':str(id)},200
        except User.DoesNotExist: 
                user1 = User(name=body["uname"],email=body["email"],password=body["password"]).save()
                id=user1.id
                return {'id':str(id)},200
                
    def get(self):
        usr=User.objects().to_json()
        return Response(usr, mimetype="application/json", status=200)

class LoginApi(Resource):
    def post(self):
        body=request.get_json()
        try:
            usr=User.objects(name=body['uname'] , password=body['password']).to_json()
            if(len(usr)>2):
                return Response(usr, mimetype="application/json", status=200)
            else:
                return {"error":"User dont exists"},200
        except User.DoesNotExist:
            return {"error":"User dont exists"},200