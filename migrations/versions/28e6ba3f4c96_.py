"""empty message

Revision ID: 28e6ba3f4c96
Revises: 7d16ef780b0d
Create Date: 2022-02-13 01:18:45.800358

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28e6ba3f4c96'
down_revision = '7d16ef780b0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('menus', sa.Column('menuid', sa.Integer(), autoincrement=True, nullable=False))
    op.add_column('menus', sa.Column('productid', sa.Integer(), nullable=True))
    op.add_column('menus', sa.Column('productname', sa.String(length=512), nullable=True))
    op.add_column('menus', sa.Column('restaurantid', sa.Integer(), nullable=True))
    op.add_column('menus', sa.Column('menustatus', sa.Integer(), nullable=True))
    op.drop_column('menus', 'productName')
    op.drop_column('menus', 'menuId')
    op.drop_column('menus', 'restaurantId')
    op.drop_column('menus', 'productId')
    op.drop_column('menus', 'menuStatus')
    op.add_column('orders', sa.Column('orderid', sa.Integer(), autoincrement=True, nullable=False))
    op.add_column('orders', sa.Column('productid', sa.Integer(), nullable=True))
    op.add_column('orders', sa.Column('menuid', sa.Integer(), nullable=True))
    op.add_column('orders', sa.Column('restaurantid', sa.Integer(), nullable=True))
    op.add_column('orders', sa.Column('orderstatus', sa.Integer(), nullable=True))
    op.drop_index('ix_orders_productId', table_name='orders')
    op.create_index(op.f('ix_orders_productid'), 'orders', ['productid'], unique=False)
    op.drop_column('orders', 'menuId')
    op.drop_column('orders', 'orderId')
    op.drop_column('orders', 'restaurantId')
    op.drop_column('orders', 'productId')
    op.drop_column('orders', 'orderStatus')
    op.add_column('restaurants', sa.Column('restaurantid', sa.Integer(), autoincrement=True, nullable=False))
    op.add_column('restaurants', sa.Column('restaurantname', sa.String(length=1024), nullable=True))
    op.add_column('restaurants', sa.Column('menuid', sa.Integer(), nullable=True))
    op.add_column('restaurants', sa.Column('userid', sa.Integer(), nullable=True))
    op.add_column('restaurants', sa.Column('activestatus', sa.Integer(), nullable=True))
    op.drop_index('ix_restaurants_menuId', table_name='restaurants')
    op.drop_index('ix_restaurants_userId', table_name='restaurants')
    op.create_index(op.f('ix_restaurants_menuid'), 'restaurants', ['menuid'], unique=False)
    op.create_index(op.f('ix_restaurants_userid'), 'restaurants', ['userid'], unique=False)
    op.drop_column('restaurants', 'menuId')
    op.drop_column('restaurants', 'userId')
    op.drop_column('restaurants', 'activeStatus')
    op.drop_column('restaurants', 'restaurantId')
    op.drop_column('restaurants', 'restaurantName')
    op.add_column('user', sa.Column('usertype', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('isactive', sa.Boolean(), nullable=True))
    op.drop_column('user', 'isActive')
    op.drop_column('user', 'userType')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('userType', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('isActive', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('user', 'isactive')
    op.drop_column('user', 'usertype')
    op.add_column('restaurants', sa.Column('restaurantName', sa.VARCHAR(length=1024), autoincrement=False, nullable=True))
    op.add_column('restaurants', sa.Column('restaurantId', sa.INTEGER(), server_default=sa.text('nextval(\'"restaurants_restaurantId_seq"\'::regclass)'), autoincrement=True, nullable=False))
    op.add_column('restaurants', sa.Column('activeStatus', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('restaurants', sa.Column('userId', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('restaurants', sa.Column('menuId', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_restaurants_userid'), table_name='restaurants')
    op.drop_index(op.f('ix_restaurants_menuid'), table_name='restaurants')
    op.create_index('ix_restaurants_userId', 'restaurants', ['userId'], unique=False)
    op.create_index('ix_restaurants_menuId', 'restaurants', ['menuId'], unique=False)
    op.drop_column('restaurants', 'activestatus')
    op.drop_column('restaurants', 'userid')
    op.drop_column('restaurants', 'menuid')
    op.drop_column('restaurants', 'restaurantname')
    op.drop_column('restaurants', 'restaurantid')
    op.add_column('orders', sa.Column('orderStatus', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('orders', sa.Column('productId', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('orders', sa.Column('restaurantId', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('orders', sa.Column('orderId', sa.INTEGER(), server_default=sa.text('nextval(\'"orders_orderId_seq"\'::regclass)'), autoincrement=True, nullable=False))
    op.add_column('orders', sa.Column('menuId', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_orders_productid'), table_name='orders')
    op.create_index('ix_orders_productId', 'orders', ['productId'], unique=False)
    op.drop_column('orders', 'orderstatus')
    op.drop_column('orders', 'restaurantid')
    op.drop_column('orders', 'menuid')
    op.drop_column('orders', 'productid')
    op.drop_column('orders', 'orderid')
    op.add_column('menus', sa.Column('menuStatus', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('menus', sa.Column('productId', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('menus', sa.Column('restaurantId', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('menus', sa.Column('menuId', sa.INTEGER(), server_default=sa.text('nextval(\'"menus_menuId_seq"\'::regclass)'), autoincrement=True, nullable=False))
    op.add_column('menus', sa.Column('productName', sa.VARCHAR(length=512), autoincrement=False, nullable=True))
    op.drop_column('menus', 'menustatus')
    op.drop_column('menus', 'restaurantid')
    op.drop_column('menus', 'productname')
    op.drop_column('menus', 'productid')
    op.drop_column('menus', 'menuid')
    # ### end Alembic commands ###