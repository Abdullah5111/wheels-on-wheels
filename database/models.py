from database.db import db

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
    description=db.StringField(required=True)
    image=db.StringField(required=True)
    creator=db.StringField(required=True)
