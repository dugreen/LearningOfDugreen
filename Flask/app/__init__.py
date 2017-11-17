from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from config import basedir
from flask_login import LoginManager
from flask_openid import OpenID


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

lm = LoginManager()
lm.init_app(app)
oid = OpenID(app,os.path.join(basedir,'tmp'))
