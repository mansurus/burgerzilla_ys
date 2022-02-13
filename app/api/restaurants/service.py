import re
from flask import current_app,session
from app.models.schemas import RestaurantSchema
from app.utils import err_resp,internal_err_resp,message
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.restaurant import Restaurant
from app.models.order import Order
from app import db


class RestaurantService:
    @staticmethod
    def get_order(order_id):
        """
        get an order by id"""
        if not (order := Order.query.filter_by(orderid=order_id).first()):
            return err_resp(msg="Order not found",code=400,reason="no_orders")
        from  app.api.orders.utils import load_data
        from  .utils import load_data as load_restaurants
        try:
            current_user = get_jwt_identity()
            restaurant_idx = Restaurant.query.filter_by(userid=current_user).first()
            if order.restaurantid == restaurant_idx.restaurantid:
                order_data = load_data(order)
                resp=message(True,"Order loaded successfully")
                resp["order"]=order_data
                return resp,200
            else:
                return err_resp(msg="This order does not belong to your restaurant!",code=401,reason="Not Authorized!")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()


    @staticmethod
    def update_order(order_id,order_data):
        """
        update an order: orderStatus => 1:Yeni 2:Hazırlanıyor 3:Yolda 4:Teslim 5:Müşteri İptal 6:Restoran iptal"""
        if not (order:=Order.query.get(order_id)):
            return err_resp(msg="Order not found",code=400,reason="no order found")
        from  .utils import load_data as load_restaurants
        try:
            current_user = get_jwt_identity()
            rest_id = order_data.get('restaurantid')
            restaurant_idx = Restaurant.query.filter_by(rest_id).first()
            if order.restaurantid == restaurant_idx.restaurantid:
                Order.query.filter_by(orderid=order_id).update(order_data)
                db.session.commit()
                return message(True,"Order updated successfully")
            else:
                return err_resp(msg="This order does not belong to your restaurant!",code=401,reason="Not Authorized!")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()
        
    @staticmethod
    def get_orders(restaurant_id):
        """
        Get all orders by all users"""
        if not(orders := Order.query.filter_by(restaurantid=restaurant_id)):
            return err_resp(msg="No orders found",code=400,reason="no orders found")
        from  app.api.orders.utils import load_data as load_orders
        from  .utils import load_data
        try:
            current_user = get_jwt_identity()
            restaurant_idx = Restaurant.query.filter_by(userid=current_user).first()
            
            if restaurant_id == restaurant_idx.restaurantid:
                orders_data = [load_orders(order) for order in orders]
                resp=message(True,"Orders loaded successfully")
                resp["orders"]=orders_data
                return resp,200                   
            else:
                 return err_resp(msg="You cannot see orders of other restaurants!",code=401,reason="Not Authorized!")
            
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()