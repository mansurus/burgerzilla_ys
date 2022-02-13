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

## Cloning and running the project
### Prerequisites 
There are two way of running the project: local environment and docker. <br />
#### In Local Environment
Before you run in local you need to install python and postgresql in your local environment, the necessary links are respectively <a href="https://www.python.org/downloads/">here</a> and <a href="https://www.postgresql.org/download/">here</a>. Do not forget to add python to path and create a database server in postgres with database to be used in the db configuration.<br />
To run in local, copy the following command:<br />
`git clone https://github.com/mansurus/burgerzilla_ys.git` and then open "burgerzilla_ys" folder in terminal. If you are using Windows type `python -m venv env` and hit enter. With this way, you will create a virtual environment to create our libraries. To activate the virtual env in our terminal type `.\env\Scripts\activate`. If you see (env) in the beginning of your terminal command line, then it is activated. Otherwise please visit this <a href="https://docs.python.org/3/library/venv.html">link</a>. To do the same in linux based systems please follow this <a href="https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/">link</a>. Now, we can create our libraries inside env. The necessary command is `pip install -r requirements.txt`. After the libraries installed, we need to perform db operation with following commands `flask db init`, `flask db migrate`, `flask db upgrade`. But before you do this, you need to specify DATABASE_URL in .env file as `DATABASE_URL=postgresql://<databaseuser>:<databasepassword>@localhost:<port>/<databasetoconnect>`. If all is success, `flask run`. The api can be tested with swaggerui.
#### In Docker Container
To run in docker, you need to install Docker first. Link for installation guide can be found <a href="https://docs.docker.com/desktop/">here</a>, there are helper links for both Windows and Linux systems in the left menu.
<br />
After installing docker, open terminal and type `docker build -t <imagename>:<tagname> . ` and enter. In this command "imagename" and "tagname" will be specified by you and the image name will be used in our docker-compose.yml file. After building our image, please replace its name with the image name in docker-compose.yml file and the container name can also be set the same. Here the environment will be `DATABASE_URL=postgresql://<POSTGRES_USER>:<POSTGRES_PASSWORD>@db:<5432>/<POSTGRES_DB>`, and the necessary info will be set in db's environment by you. After everything is set, please type `docker compose up --build web` and hit enter. Application can be tested on <a href="">localhost:5000</a>.

### Future Work
As the future work of this project, API endpoints will be improved and new features will be implemented. Roles feature will be activated for creating different employee roles for a restaurant. Test cases will be improved and all endpoints will be tested. Queue mechanism can be added to the system. And to be able to run on the internet, a deployment will be done. 

<br />
## Ali Mansur
