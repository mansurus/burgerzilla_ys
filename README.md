# Burgerzilla API
## Introduction
### Auth api
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
