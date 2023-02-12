from db import db

class Ad(db.Document):
    company=db.StringField(required=True)
    model=db.StringField(required=True)
    price=db.StringField(required=True)
    registered_year=db.StringField(required=True)
    registered_loc=db.StringField(required=True)
    current_loc=db.StringField(required=True)
    engine_cap=db.StringField(required=True)
    km_driven=db.StringField(required=True)
    transmission=db.StringField(required=True)
    image1=db.StringField(required=True)
    image2=db.StringField(required=True)
    image3=db.StringField(required=True)
    image4=db.StringField(required=True)
    creator=db.StringField(required=True)
    status=db.StringField(required=True)

class SparePart(db.Document):
    category=db.StringField(required=True)
    price=db.StringField(required=True)
    location=db.StringField(required=True)
    phone_number=db.StringField(required=True)
    image=db.StringField(required=True)
    creator=db.StringField(required=True)
    status=db.StringField(required=True)

class Seller(db.Document):
    username=db.StringField(required=True)
    c_name=db.StringField(required=True)
    email=db.StringField(required=True)
    phone_number=db.StringField(required=True)
    address=db.StringField(required=True)
    
class User(db.Document):
    name=db.StringField(required=True)
    password=db.StringField(required=True)
    email=db.StringField(required=True)