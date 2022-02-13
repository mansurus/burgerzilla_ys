from flask_restx import Namespace,fields

class MenuDto:
    api = Namespace('menus', description='Menu related operations')
    menu = api.model('menu', {
        "menuid": fields.Integer,
        "productid":fields.Integer, 
        "productname":fields.String, 
        "price":fields.Integer,
        "description":fields.String,
        "image":fields.Integer,
        "restaurantid":fields.Integer
    })


    menu_resp = api.model('menu_resp', {
        'status':fields.Boolean,
        'message':fields.String,
        'menu':fields.Nested(menu)
    })

    menu_list_resp = api.model('menu_list_resp', {
        'status':fields.Boolean,
        'message':fields.String,
        'menus':fields.List(fields.Nested(menu))})