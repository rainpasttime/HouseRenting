# -*- encoding=UTF-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from HouseApp import views, models

app = Flask(__name__)
app.config.from_pyfile('app.conf')
app.secret_key = 'houserenting'
db = SQLAlchemy(app)




