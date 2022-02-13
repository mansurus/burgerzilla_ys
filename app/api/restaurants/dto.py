from flask_restx import Namespace,fields

class RestaurantDto:
    api = Namespace('restaurants', description='Restaurants related operations')
    restaurant = api.model('restaurant', {
        "restaurantid": fields.Integer,
        "restaurantName":fields.String, 
        "menuid":fields.Integer, 
        "userid":fields.Integer,
        "address":fields.String,
        "activestatus":fields.Integer      
    })


    restaurant_resp = api.model('restaurant_resp', {
        'status':fields.Boolean,
        'message':fields.String,
        'restaurant':fields.Nested(restaurant)
    })

    restaurant_list_resp = api.model('restaurant_list_resp', {
        'status':fields.Boolean,
        'message':fields.String,
        'restaurants':fields.List(fields.Nested(restaurant))})