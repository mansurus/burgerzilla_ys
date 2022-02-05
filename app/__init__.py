from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy
from config import Config 


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app,doc="/docs",title="Burgerzilla Api - Swagger",description="Burgerzilla Api",version="1.0")


from app import routes, models,errors