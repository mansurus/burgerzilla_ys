from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from .service import OrderService
from .dto import OrderDto

api = OrderDto.api
order=OrderDto.order
order_resp=OrderDto.order_resp
order_list_resp=OrderDto.order_list_resp

@api.route('/<int:order_id>')
class Order(Resource):
    @api.doc('get specific order by order id',responses={
        200:('Success',order_resp),
        400:'Invalid Order ID',
    })
    @jwt_required()
    def get(self,order_id):
        """ get specific order"""
        return OrderService.get_order(order_id)
    
    @api.doc("Cancel a specific order",responses={
        200:"Success"})
    @api.expect(order)
    @jwt_required()
    def delete(self,order_id):
        """ Cancel a specific order"""
        orderStatus = request.get_json()
        return OrderService.delete_order(order_id,orderStatus)

    @api.doc("Update a specific order",responses={200:"Success"})
    @api.expect(order)
    @jwt_required()
    def put(self,order_id):
        """ Update a specific order"""
        data = request.get_json()
        return OrderService.update_order(order_id,data)

@api.route("/user/<int:user_id>")
class OrderList(Resource):
    @api.doc("Get all orders of a specific user",responses={200:"Success",500:"Internal Server Error"})
    @jwt_required()
    def get(self,user_id):
        """
        Get all orders of a specific user"""
        return OrderService.get_orders(user_id)


    @api.doc("Create a new order",responses={200:"Success",500:"Internal Server Error"})
    @api.expect(order)
    @jwt_required()
    def post(self,user_id):
        """
        Create a new order"""
        data = request.get_json()
        return OrderService.insert_order(user_id,data)