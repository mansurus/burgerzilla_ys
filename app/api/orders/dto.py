from flask_restx import Namespace,fields

class OrderDto:

    api = Namespace('orders', description='Orders related operations')
    order = api.model('order', {
        "orderid": fields.Integer,
        "userid":fields.Integer, 
        "productid":fields.Integer, 
        "price":fields.Integer,
        "description":fields.String,
        "menuid":fields.Integer,
        "restaurantid":fields.Integer,
        "orderstatus":fields.Integer       
    })


    order_resp = api.model('order_resp', {
        'status':fields.Boolean,
        'message':fields.String,
        'order':fields.Nested(order)
    })

    order_list_resp = api.model('order_list_resp', {
        'status':fields.Boolean,
        'message':fields.String,
        'orders':fields.List(fields.Nested(order))})