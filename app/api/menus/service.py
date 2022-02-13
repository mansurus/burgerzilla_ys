import re
from flask import current_app,session
from app.models.schemas import MenuSchema
from app.utils import err_resp,internal_err_resp,message
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.order import Order
from app.models.menu import Menu
from app.models.restaurant import Restaurant
from app.models.user import User
from app import db


class MenuService:
    @staticmethod
    def get_menu(restaurant_id):
        """
        Get all orders of a specific user"""
        if not(menus := Menu.query.filter_by(restaurantid=restaurant_id)):
            return err_resp(msg="No orders found",code=400,reason="no orders found")
        from .utils import load_data
        try:
            
            menus_data = [load_data(menu) for menu in menus]
            resp=message(True,"Menus loaded successfully")
            resp["menus"]=menus_data
            return resp,200
        
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()


    @staticmethod
    def insert_menu(restaurant_id,menu_data):
        """
        Insert a new menu item"""
        from  app.api.restaurants.utils import load_data as load_restaurants
        try:
            current_user = get_jwt_identity()
            rest_id = menu_data.get('restaurantid')
            user_type = User.query.get(current_user)
            restaurant_idx = Restaurant.query.get(rest_id)
            if user_type.usertype == 2:
                if user_type.id == restaurant_idx.userid:
                    menu = Menu(menuid=menu_data['menuid'],productid=menu_data["productid"],productname=menu_data["productname"],price=menu_data["price"],description=menu_data["description"],image=menu_data["image"],restaurantid=menu_data["restaurantid"],menustatus=menu_data["menustatus"])
                    db.session.add(menu)
                    db.session.commit()
                    return message(True,"Menu created successfully")
                else:
                    return err_resp(msg="You cannot add a product to the menu of other restaurant!",code=401,reason="Not Authorized!")
            else:
                return err_resp(msg="Normal users cannot perform menu operations!",code=401,reason="Not Authorized!")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def update_menu(menu_id,menu_data):
        """
        update a menu"""
        if not (menu:=Menu.query.get(menu_id)):
            return err_resp(msg="Menu not found",code=400,reason="no menu found")
        from  app.api.restaurants.utils import load_data as load_restaurants
        try:
            current_user = get_jwt_identity()
            rest_id = menu_data.get('restaurantid')
            user_type = User.query.get(current_user)
            restaurant_idx = Restaurant.query.get(rest_id)
            if user_type.usertype == 2:
                if menu.restaurantid == restaurant_idx.restaurantid:
                    Menu.query.filter_by(menuid=menu_id).update(menu_data)
                    db.session.commit()
                    return message(True,"Menu updated successfully")
                else:
                    return err_resp(msg="This menu does not belong to your restaurant!",code=401,reason="Not Authorized!")
            else:
                return err_resp(msg="Normal users cannot perform menu operations!",code=401,reason="Not Authorized!")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()
        
   

    @staticmethod
    def delete_menu(menu_id,menuStatus):
        """
        delete a menu"""
        if not (menu:=Menu.query.get(menu_id)):
            return err_resp(msg="Menu not found",code=400,reason="no menu found")
        from  app.api.restaurants.utils import load_data as load_restaurants
        try:
            current_user = get_jwt_identity()
            rest_id = menuStatus.get('restaurantid')
            user_type = User.query.get(current_user)
            restaurant_idx = Restaurant.query.get(rest_id)
            if user_type.usertype == 2:
                if menu.restaurantid == restaurant_idx.restaurantid:
                    Menu.query.filter_by(menuid=menu_id).update(menuStatus)
                    db.session.commit()
                    return message(True,"Menu deleted successfully")
                else:
                    return err_resp(msg="This menu does not belong to your restaurant!",code=401,reason="Not Authorized!")
            else:
                return err_resp(msg="Normal users cannot perform menu operations!",code=401,reason="Not Authorized!")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_products(menu_status):
        """
        Get all products of a specific menu"""
        if not(products := Menu.query.filter_by(menustatus=menu_status)):
            return err_resp(msg="No products found",code=400,reason="no products found")
        from .utils import load_data
        try:
            product_data = [load_data(product) for product in products]
            resp=message(True,"Products loaded successfully")
            resp["products"]=product_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()