from app import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    restaurantid = db.Column(db.Integer, primary_key=True,autoincrement=True)
    restaurantname = db.Column(db.String(1024))
    menuid = db.Column(db.Integer, index=True)
    userid = db.Column(db.Integer, index=True)
    address = db.Column(db.String(1024))
    activestatus = db.Column(db.Integer)

    def __repr__(self):
        return '<Restaurants {}>'.format(self.restaurantname)

