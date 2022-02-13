# Burgerzilla API
## Introduction
### Auth
The application is a small food ordering system that allows users to register the system to create food orders from restaurants. There are two types of users stored in User table with specified user type, respectively 1 and 2 for normal users and restaurants. User table keeps active status of each user or restaurant, allowing any member to freeze their membership. The benefit of this approach is that with only one update user membership can be activa again. The other columns are about user's personal information namely: email, username, name, password(hashed), joined_date and role_id. Role id is a column for future work for creating different levels of membership. For example, a restaurant employee might get menu edit right with but still be lower than admin(owner of the restaurant).<br />
<br />
### The Table Overview of the Food Ordering System
Tables with Columns
| User Table    |     Menu Table      |  Restaurant Table | Order Table |
|----------|-------------|------|------|
| id (PK)|  menuid(PK) | restaurantid |orderid |
| email |    productid   |   restaurantname |userid |
| username | productname |   menuid |productid |
| name | price |   userid |price |
| password_hash | description |    address |description |
| joined_date | image |    activestatus |menuid |
| role_id | restaurantid |     |restaurantid|
| usertype | menustatus |     |orderstatus |
| isactive |  |     | |<br />

### The Table Overview of the Food Ordering System
Project structure:<br />

```
burgerzilla_ys/
┣ app/
┃ ┣ api/
┃ ┃ ┣ menus/
┃ ┃ ┃ ┣ controller.py
┃ ┃ ┃ ┣ dto.py
┃ ┃ ┃ ┣ service.py
┃ ┃ ┃ ┣ utils.py
┃ ┃ ┃ ┗ __init__.py
┃ ┃ ┣ orders/
┃ ┃ ┃ ┣ controller.py
┃ ┃ ┃ ┣ dto.py
┃ ┃ ┃ ┣ service.py
┃ ┃ ┃ ┣ utils.py
┃ ┃ ┃ ┗ __init__.py
┃ ┃ ┣ restaurants/
┃ ┃ ┃ ┣ controller.py
┃ ┃ ┃ ┣ dto.py
┃ ┃ ┃ ┣ service.py
┃ ┃ ┃ ┣ utils.py
┃ ┃ ┃ ┗ __init__.py
┃ ┃ ┣ user/
┃ ┃ ┃ ┣ controller.py
┃ ┃ ┃ ┣ dto.py
┃ ┃ ┃ ┣ service.py
┃ ┃ ┃ ┣ utils.py
┃ ┃ ┃ ┗ __init__.py
┃ ┃ ┗ __init__.py
┃ ┣ auth/
┃ ┃ ┣ controller.py
┃ ┃ ┣ dto.py
┃ ┃ ┣ service.py
┃ ┃ ┣ utils.py
┃ ┃ ┗ __init__.py
┃ ┣ models/
┃ ┃ ┣ menu.py
┃ ┃ ┣ order.py
┃ ┃ ┣ restaurant.py
┃ ┃ ┣ schemas.py
┃ ┃ ┣ user.py
┃ ┃ ┗ __init__.py
┃ ┣ extensions.py
┃ ┣ utils.py
┃ ┗ __init__.py
┣ tests/
┃ ┣ utils/
┃ ┃ ┣ base.py
┃ ┃ ┣ common.py
┃ ┃ ┗ __init__.py
┃ ┣ test_auth_api.py
┃ ┣ test_config.py
┃ ┣ test_order_api.py
┃ ┣ test_order_model.py
┃ ┣ test_restaurant_api.py
┃ ┣ test_user_api.py
┃ ┣ test_user_model.py
┃ ┗ __init__.py
┣ .env
┣ .gitignore
┣ boot.sh
┣ config.py
┣ data-dev.sqlite
┣ docker-compose.yml
┣ Dockerfile
┣ requirements.txt
┗ runservice.py
```
### Api 
The folders under api have common structure as controller.py, dto.py, service.py and utils.py. <br />
#### controller.py
The endpoints are defined here. All operations like get, post, put, delete are under controller.py to make requests to the db.
#### dto.py
The structural models for each table are defined under dto.py. Related table fields are defined under specified names using Namespace from flask-restx and created with the model method of Namespace class. 
#### service.py
Business operations are defined under service.py. Logical code blocks are created to be able to perform get, post, update and delete operations that will be send to the db. Related models are imported in service.py and queries are formed using those models.
#### utils.py
Helper functions are stored here. For example, dump operation for a db model got from related schema are returned in the functions created in utils.py
<br />
### Models
Under models folder, for each of our table, there is one .py file with the name of that table. Each model file containts a class named the same with the database table and has attributes corresponds to the columns of the related table. Classes import db(SqlAlchemy) from app to create columns and assigned their properties like primary key, foreign key, index etc. Besides model files there is a file named schema which contains a class for each table to represent them as schemas and uses Marshmallow's schema which is a serializer. After that schemas are loaded under utils files to represent db objects.
### Tests
To test the endpoints unittest model is implemented in this project. There are functions for endpoints to test different methods like get, post, put, delete. Mock datas are prepared and with necessary assertion functions from unittes library, endpoints are tested.


