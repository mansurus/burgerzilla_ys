import json
from pkgutil import get_data
from re import A

from flask_jwt_extended import create_access_token

from app import db
from app.models.restaurant import Restaurant
from app.models.order import Order

from utils.base import BaseTestCase

def get_orderbyorderid_data(self,accestoken,order_id):
    return self.client.get(
        f"/api/restaurants/{order_id}",
        headers={"Authorization": "Bearer " + accestoken},
    )

def get_orderbyrestid_data(self,accestoken,restaurant_id):
    return self.client.get(
        f"/api/restaurants/restaurant/{restaurant_id}",
        headers={"Authorization": "Bearer " + accestoken},
    )


def put_orders_data(self,accesstoken,order_data,order_id):
    return self.client.put(
        f"/api/restaurants/{order_id}",
        data=json.dumps(order_data),
        content_type="application/json",
        headers={"Authorization": "Bearer " + accesstoken},
    )


class TestDatasetBlueprint(BaseTestCase):
    def test_orderbyorderid_get(self):
        """
        Test for getting an order
        """
        d = Order(orderid=11,userid=11,productid=11,price=50,description='restoran',menuid=1,restaurantid=2,orderstatus=1)
        db.session.add(d)
        db.session.commit()
        
        access_token = create_access_token(identity=11)

        order_resp = get_orderbyorderid_data(self,access_token,d.orderid)
        order_data = json.loads(order_resp.data.decode())

        self.assertTrue(order_resp.status_code == 200)
        self.assertTrue(order_data["order"]['orderid'] == 11)
        self.assertTrue(order_data["order"]['userid'] == 11)
        self.assertTrue(order_data["order"]['productid'] == 11)
        self.assertTrue(order_data["order"]['description'] == 'restoran')
        self.assertTrue(order_data["order"]['menuid'] == 1)
        self.assertTrue(order_data["order"]['restaurantid'] == 2)
        self.assertTrue(order_data["order"]['orderstatus'] == 1)

        data_404_resp = get_orderbyorderid_data(self,access_token,100)
        self.assertEquals(data_404_resp.status_code, 400)

    def test_orderbyorderid_put(self):
        """
        Test for updating an order
        """
        d = Order(orderid=11,userid=11,productid=11,price=50,description='restoran',menuid=1,restaurantid=2,orderstatus=1)
        db.session.add(d)
        db.session.commit()
        
        data_d = dict(
            orderid=11,
            userid=11,
            productid=11,
            price=50,
            menuid=1,
            restaurantid=2,
            orderstatus=1,
            description="restoranchanged",
        )
        db.session.commit()
        access_token = create_access_token(identity=1)

        order_resp = put_orders_data(self,access_token,data_d,d.orderid)
        order_data = json.loads(order_resp.data.decode())

       
        self.assertEquals(order_data["orders"]['description'], data_d['description'])
   