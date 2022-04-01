"""
Created on 4/1/22
@author: b4rt
@mail: root.b4rt@gmail.com
"""
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import app
from api_nmap.models import Model

db = SQLAlchemy(app, model_class=Model)

migrate = Migrate(app, db)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


