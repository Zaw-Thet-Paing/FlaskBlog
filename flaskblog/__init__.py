from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)

# Get the absolute path to the application's directory
app_path = os.path.dirname(os.path.abspath(__file__))

app.config['SECRET_KEY'] = '8beea5a1700af3200bdf9de09ed34622'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{app_path}/site.db' # use flask shell to handle database

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes