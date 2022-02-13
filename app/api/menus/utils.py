from flask_jwt_extended import get_jwt_identity
from app.api.user.service import UserService

def load_data(menu_db_obj):
    from app.models.schemas import MenuSchema
    menu_schema = MenuSchema()
    data = menu_schema.dump(menu_db_obj)
    return data
