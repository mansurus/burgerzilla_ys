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
# burgerzilla_ys

* [app/](.\burgerzilla_ys\app)
  * [api/](.\burgerzilla_ys\app\api)
    * [menus/](.\burgerzilla_ys\app\api\menus)
      * [controller.py](.\burgerzilla_ys\app\api\menus\controller.py)
      * [dto.py](.\burgerzilla_ys\app\api\menus\dto.py)
      * [service.py](.\burgerzilla_ys\app\api\menus\service.py)
      * [utils.py](.\burgerzilla_ys\app\api\menus\utils.py)
      * [__init__.py](.\burgerzilla_ys\app\api\menus\__init__.py)
    * [orders/](.\burgerzilla_ys\app\api\orders)
      * [controller.py](.\burgerzilla_ys\app\api\orders\controller.py)
      * [dto.py](.\burgerzilla_ys\app\api\orders\dto.py)
      * [service.py](.\burgerzilla_ys\app\api\orders\service.py)
      * [utils.py](.\burgerzilla_ys\app\api\orders\utils.py)
      * [__init__.py](.\burgerzilla_ys\app\api\orders\__init__.py)
    * [restaurants/](.\burgerzilla_ys\app\api\restaurants)
      * [controller.py](.\burgerzilla_ys\app\api\restaurants\controller.py)
      * [dto.py](.\burgerzilla_ys\app\api\restaurants\dto.py)
      * [service.py](.\burgerzilla_ys\app\api\restaurants\service.py)
      * [utils.py](.\burgerzilla_ys\app\api\restaurants\utils.py)
      * [__init__.py](.\burgerzilla_ys\app\api\restaurants\__init__.py)
    * [user/](.\burgerzilla_ys\app\api\user)
      * [controller.py](.\burgerzilla_ys\app\api\user\controller.py)
      * [dto.py](.\burgerzilla_ys\app\api\user\dto.py)
      * [service.py](.\burgerzilla_ys\app\api\user\service.py)
      * [utils.py](.\burgerzilla_ys\app\api\user\utils.py)
      * [__init__.py](.\burgerzilla_ys\app\api\user\__init__.py)
    * [__init__.py](.\burgerzilla_ys\app\api\__init__.py)
  * [auth/](.\burgerzilla_ys\app\auth)
    * [controller.py](.\burgerzilla_ys\app\auth\controller.py)
    * [dto.py](.\burgerzilla_ys\app\auth\dto.py)
    * [service.py](.\burgerzilla_ys\app\auth\service.py)
    * [utils.py](.\burgerzilla_ys\app\auth\utils.py)
    * [__init__.py](.\burgerzilla_ys\app\auth\__init__.py)
  * [models/](.\burgerzilla_ys\app\models)
    * [menu.py](.\burgerzilla_ys\app\models\menu.py)
    * [order.py](.\burgerzilla_ys\app\models\order.py)
    * [restaurant.py](.\burgerzilla_ys\app\models\restaurant.py)
    * [schemas.py](.\burgerzilla_ys\app\models\schemas.py)
    * [user.py](.\burgerzilla_ys\app\models\user.py)
    * [__init__.py](.\burgerzilla_ys\app\models\__init__.py)
  * [extensions.py](.\burgerzilla_ys\app\extensions.py)
  * [utils.py](.\burgerzilla_ys\app\utils.py)
  * [__init__.py](.\burgerzilla_ys\app\__init__.py)
* [tests/](.\burgerzilla_ys\tests)
  * [utils/](.\burgerzilla_ys\tests\utils)
    * [base.py](.\burgerzilla_ys\tests\utils\base.py)
    * [common.py](.\burgerzilla_ys\tests\utils\common.py)
    * [__init__.py](.\burgerzilla_ys\tests\utils\__init__.py)
  * [test_auth_api.py](.\burgerzilla_ys\tests\test_auth_api.py)
  * [test_config.py](.\burgerzilla_ys\tests\test_config.py)
  * [test_order_api.py](.\burgerzilla_ys\tests\test_order_api.py)
  * [test_order_model.py](.\burgerzilla_ys\tests\test_order_model.py)
  * [test_restaurant_api.py](.\burgerzilla_ys\tests\test_restaurant_api.py)
  * [test_user_api.py](.\burgerzilla_ys\tests\test_user_api.py)
  * [test_user_model.py](.\burgerzilla_ys\tests\test_user_model.py)
  * [__init__.py](.\burgerzilla_ys\tests\__init__.py)
* [.env](.\burgerzilla_ys\.env)
* [.gitignore](.\burgerzilla_ys\.gitignore)
* [boot.sh](.\burgerzilla_ys\boot.sh)
* [config.py](.\burgerzilla_ys\config.py)
* [data-dev.sqlite](.\burgerzilla_ys\data-dev.sqlite)
* [docker-compose.yml](.\burgerzilla_ys\docker-compose.yml)
* [Dockerfile](.\burgerzilla_ys\Dockerfile)
* [requirements.txt](.\burgerzilla_ys\requirements.txt)
* [runservice.py](.\burgerzilla_ys\runservice.py)
