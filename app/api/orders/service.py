import re
from flask import current_app,session
from app.models.schemas import OrderSchema
from app.utils import err_resp,internal_err_resp,message
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.order import Order
from app import db


class OrderService:
    @staticmethod
    def get_order(order_id):
        """
        get an order by id"""
        if not (order := Order.query.get(order_id)):
            return err_resp(msg="Order not found",code=400,reason="no_orders")
        from .utils import load_data
        try:
            order_data = load_data(order)
            resp=message(True,"Order loaded successfully")
            resp["order"]=order_data
            current_user = get_jwt_identity()
            if order_data['userid'] == current_user:
                return resp,200
            else:
                return err_resp(msg="This order does not belong to you!",code=401,reason="Not Authorized!")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def delete_order(order_id,orderStatus):
        """
        cancel an order"""
        if not (order:=Order.query.get(order_id)):
            return err_resp(msg="Order not found",code=400,reason="no order found")
        try:
            current_user = get_jwt_identity()
            if current_user==order.userid:
                Order.query.filter_by(orderid=order_id).update(orderStatus)
                db.session.commit()
                return message(True,"Order updated successfully")
            else:
                return err_resp(msg="This order does not belong to you!",code=401,reason="Not Authorized!")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def insert_order(user_id,order_data):
        """
        Insert a new order"""
        try:
            current_user = get_jwt_identity()
            if user_id == current_user:
                order = Order(userid=current_user,productid=order_data["productid"],price=order_data["price"],description=order_data["description"],menuid=order_data["menuid"],
                restaurantid=order_data["restaurantid"],orderstatus=1)

                db.session.add(order)
                db.session.commit()
                return message(True,"Order created successfully")
            else:
                return err_resp(msg="You cannot make orders for others!",code=401,reason="Not Authorized!")
            
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def update_order(order_id,order_data):
        """
        update an order"""
        if not (order:=Order.query.get(order_id)):
            return err_resp(msg="Order not found",code=400,reason="no order found")
        try:
            current_user = get_jwt_identity()
            if current_user==order.userid:
                Order.query.filter_by(orderid=order_id).update(order_data)
                db.session.commit()
                return message(True,"Order updated successfully")
            else:
                return err_resp(msg="This order does not belong to you!",code=401,reason="Not Authorized!")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()
        
    @staticmethod
    def get_orders(user_id):
        """
        Get all orders of a specific user"""
        if not(orders := Order.query.filter_by(userid=user_id)):
            return err_resp(msg="No orders found",code=400,reason="no orders found")
        from .utils import load_data
        try:
            current_user = get_jwt_identity()
            if current_user==user_id:
                orders_data = [load_data(order) for order in orders]
                resp=message(True,"Orders loaded successfully")
                resp["orders"]=orders_data
                return resp,200
            else:
                return err_resp(msg="You cannot see orders of other users!",code=401,reason="Not Authorized!")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()