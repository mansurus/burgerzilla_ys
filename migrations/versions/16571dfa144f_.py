"""empty message

Revision ID: 16571dfa144f
Revises: 
Create Date: 2022-02-12 19:21:54.571039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16571dfa144f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menus',
    sa.Column('menuId', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('productId', sa.Integer(), nullable=True),
    sa.Column('productName', sa.String(length=512), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('image', sa.Integer(), nullable=True),
    sa.Column('restaurantId', sa.Integer(), nullable=True),
    sa.Column('menuStatus', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('menuId')
    )
    op.create_table('restaurants',
    sa.Column('restaurantId', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('restaurantName', sa.String(length=1024), nullable=True),
    sa.Column('menuId', sa.Integer(), nullable=True),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=1024), nullable=True),
    sa.Column('activeStatus', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('restaurantId')
    )
    op.create_index(op.f('ix_restaurants_menuId'), 'restaurants', ['menuId'], unique=False)
    op.create_index(op.f('ix_restaurants_userId'), 'restaurants', ['userId'], unique=False)
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('default', sa.Boolean(), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=15), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('joined_date', sa.DateTime(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('orders',
    sa.Column('orderId', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.Column('productId', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('menuId', sa.Integer(), nullable=True),
    sa.Column('restaurantId', sa.Integer(), nullable=True),
    sa.Column('orderStatus', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('orderId')
    )
    op.create_index(op.f('ix_orders_price'), 'orders', ['price'], unique=False)
    op.create_index(op.f('ix_orders_productId'), 'orders', ['productId'], unique=False)
    op.create_index(op.f('ix_orders_userid'), 'orders', ['userid'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_orders_userid'), table_name='orders')
    op.drop_index(op.f('ix_orders_productId'), table_name='orders')
    op.drop_index(op.f('ix_orders_price'), table_name='orders')
    op.drop_table('orders')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_table('roles')
    op.drop_index(op.f('ix_restaurants_userId'), table_name='restaurants')
    op.drop_index(op.f('ix_restaurants_menuId'), table_name='restaurants')
    op.drop_table('restaurants')
    op.drop_table('menus')
    # ### end Alembic commands ###