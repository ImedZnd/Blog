from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a3ab9ba58d166b8064117b6f628da7a7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from blog import routes