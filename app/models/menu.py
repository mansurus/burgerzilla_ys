from app import db

class Menu(db.Model):
    __tablename__ = 'menus'
    menuid = db.Column(db.Integer, primary_key=True,autoincrement=True)
    productid = db.Column(db.Integer)
    productname = db.Column(db.String(512))
    price = db.Column(db.Integer)
    description = db.Column(db.String(1024))
    image = db.Column(db.Integer)
    restaurantid = db.Column(db.Integer)
    menustatus = db.Column(db.Integer)
    
    
    def __repr__(self):
        return '<Menus {}>'.format(self.restaurantid)

