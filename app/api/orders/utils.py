def load_data(order_db_obj):
    from app.models.schemas import OrderSchema
    order_schema = OrderSchema()
    data = order_schema.dump(order_db_obj)
    return data

