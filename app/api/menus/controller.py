from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api import user

from .service import MenuService
from .dto import MenuDto

api = MenuDto.api
menu=MenuDto.menu
menu_resp=MenuDto.menu_resp
menu_list_resp=MenuDto.menu_list_resp

@api.route('/<int:restaurant_id>')
class Menu(Resource):
   
    @api.doc('get menu by restaurant id',responses={
        200:('Success',menu_resp),
        400:'Invalid restaurant_id',
    })
    @jwt_required()
    def get(self,restaurant_id):
        """ get specific menu"""
        return MenuService.get_menu(restaurant_id)
    
    @api.doc("Delete a specific menu",responses={
        200:"Success"})
    @api.expect(menu)
    @jwt_required()
    def delete(self,menu_id):
        """ Delete a specific menu"""
        menuStatus = request.get_json()
        return MenuService.delete_menu(menu_id,menuStatus)

    @api.doc("Update a specific menu",responses={200:"Success"})
    @api.expect(menu)
    @jwt_required()
    def put(self,menu_id):
        """ Update a specific menu"""
        data = request.get_json()
        return MenuService.update_menu(menu_id,data)

    @api.doc("Insert a new menu item",responses={200:"Success",500:"Internal Server Error"})
    @api.expect(menu)
    @jwt_required()
    def post(self,restaurant_id):
        """
        Create a new menu item"""
        data = request.get_json()
        return MenuService.insert_menu(restaurant_id,data)

@api.route("/menu/<int:menu_status>")
class ProductList(Resource):
    @api.doc("Get all products of a all menus",responses={200:"Success",500:"Internal Server Error"})
    @jwt_required()
    def get(self,menu_status):
        """
        Get all products of a all menus"""
        return MenuService.get_products(menu_status)

@api.route("/menu/<int:menu_id>")
class MenuList(Resource):
    @api.doc("Get all products of a specific menu",responses={200:"Success",500:"Internal Server Error"})
    @jwt_required()
    def get(self,restaurant_id):
        """
        Get all products of a specific menu"""
        return MenuService.get_menu(restaurant_id)

