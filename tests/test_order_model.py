from app import db
from app.models.order import Order
from app.models.schemas import OrderSchema

from tests.utils.base import BaseTestCase

class TestDatasetModel(BaseTestCase):
    def test_create_order(self):
        d = Order(orderid=1,userid=1,productid=1,price=50,description='deneme',menuid=1,restaurantid=2,orderstatus=2)
        db.session.add(d)
        db.session.commit()
        self.assertTrue(d.orderid > 0)

    def test_update_order(self):
        d = Order(orderid=2,userid=2,productid=2,price=30,description='denememe',menuid=2,restaurantid=1,orderstatus=1)
        db.session.add(d)
        db.session.commit()
        d.description = 'denememelisin'
        db.session.commit()
        self.assertTrue(d.description == 'denememelisin')

    def test_delete_order(self):
        d = Order(orderid=3,userid=3,productid=3,price=80,description='denememelisinxd',menuid=1,restaurantid=1,orderstatus=1)
        db.session.add(d)
        db.session.commit()
        db.session.delete(d)
        db.session.commit()
        res =  Order.query.get(d.orderid)
        self.assertTrue(res is None)

    def test_schema(self):
        # d = Order(orderid=1)
        d = Order(orderid=5,userid=5,productid=5,price=55,description='denememelisinxdxd',menuid=2,restaurantid=2,orderstatus=1)
        order_dump = OrderSchema().dump(d)
        self.assertTrue(order_dump['description'] == 'denememelisinxdxd')
    
