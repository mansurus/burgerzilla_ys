from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from .service import RestaurantService
from .dto import RestaurantDto
from app.api.orders.dto import OrderDto

api = RestaurantDto.api
order=OrderDto.order
restaurant_resp=RestaurantDto.restaurant_resp
restaurant_list_resp=RestaurantDto.restaurant_list_resp

@api.route('/<int:order_id>')
class Restaurant(Resource):
    @api.doc('get specific order by order id',responses={
        200:('Success',restaurant_resp),
        400:'Invalid Order ID',
    })
    @jwt_required()
    def get(self,order_id):
        """ get specific order"""
        return RestaurantService.get_order(order_id)
    
    @api.doc("Update a specific order",responses={
        200:"Success"})
    @api.expect(order)
    @jwt_required()
    def put(self,order_id):
        """ Cancel a specific order"""
        orderStatus = request.get_json()
        return RestaurantService.update_order(order_id,orderStatus)


@api.route("/restaurant/<int:restaurant_id>")
class OrdersList(Resource):
    @api.doc("Get all orders of by all users",responses={200:"Success",500:"Internal Server Error"})
    @jwt_required()
    def get(self,restaurant_id):
        """
        Get all orders of a specific user"""
        return RestaurantService.get_orders(restaurant_id)


