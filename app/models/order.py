from app import db

class Order(db.Model):
    __tablename__ = 'orders'
    orderid = db.Column(db.Integer, primary_key=True,autoincrement=True)
    userid = db.Column(db.Integer,  index=True)
    productid = db.Column(db.Integer, index=True)
    price = db.Column(db.Integer, index=True)
    description = db.Column(db.String(1024))
    menuid = db.Column(db.Integer)
    restaurantid = db.Column(db.Integer)
    orderstatus = db.Column(db.Integer)
    
    def __repr__(self):
        return '<Order {}>'.format(self.orderid)
