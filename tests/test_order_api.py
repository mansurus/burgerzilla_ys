import json
from pkgutil import get_data
from re import A

from flask_jwt_extended import create_access_token

from app import db
from app.models.order import Order

from utils.base import BaseTestCase

def get_order_data(self,accestoken,order_id):
    return self.client.get(
        f"/api/orders/{order_id}",
        headers={"Authorization": "Bearer " + accestoken},
    )

def get_orders_data(self,accestoken,user_id):
    return self.client.get(
        f"/api/orders/user/{user_id}",
        headers={"Authorization": "Bearer " + accestoken},
    )

def post_order_data(self,accestoken,order_data,user_id):
    return self.client.post(
        f"/api/orders/user/{user_id}",
        data=json.dumps(order_data),
        content_type="application/json",
        headers={"Authorization": "Bearer " + accestoken},
    )

def put_orders_data(self,accesstoken,order_data,order_id):
    return self.client.put(
        f"/api/orders/{order_id}",
        data=json.dumps(order_data),
        content_type="application/json",
        headers={"Authorization": "Bearer " + accesstoken},
    )

def delete_order_data(self,accesstoken,order_data,order_id):
    return self.client.delete(
        f"/api/orders/{order_id}",
        data=json.dumps(order_data),
        content_type="application/json",
        headers={"Authorization": "Bearer " + accesstoken},
    )

class TestDatasetBlueprint(BaseTestCase):
    def test_order_get(self):
        """
        Test for getting an order
        """
        d = Order(orderid=1,userid=1,productid=1,price=50,description='deneme',menuid=1,restaurantid=2,orderstatus=2)
        db.session.add(d)
        db.session.commit()
        
        access_token = create_access_token(identity=1)

        order_resp = get_order_data(self,access_token,d.orderid)
        order_data = json.loads(order_resp.data.decode())

        self.assertTrue(order_resp.status_code == 200)
        self.assertTrue(order_data["order"]['orderid'] == 1)
        self.assertTrue(order_data["order"]['userid'] == 1)
        self.assertTrue(order_data["order"]['productid'] == 1)
        self.assertTrue(order_data["order"]['description'] == 'deneme')
        self.assertTrue(order_data["order"]['menuid'] == 1)
        self.assertTrue(order_data["order"]['restaurantid'] == 2)
        self.assertTrue(order_data["order"]['orderstatus'] == 2)

        data_404_resp = get_order_data(self,access_token,100)
        self.assertEquals(data_404_resp.status_code, 400)
