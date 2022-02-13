from app import ma

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("email", "name", "username", "joined_date", "role_id","usertype","isactive")
 

class OrderSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("orderid","userid", "productid", "price","description","menuid","restaurantid","orderstatus")

class RestaurantSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("restaurantid","restaurantname" ,"userid","menuid", "address","activestatus")

class MenuSchema(ma.Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("menuid","productid" ,"productname","price", "description","image","restaurantid","menustatus")