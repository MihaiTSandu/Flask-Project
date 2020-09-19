from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os


app= Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mykey'

db = SQLAlchemy(app)
Migrate(app, db)

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view='users.login'


from pupcomp.core.views import core
app.register_blueprint(core)
  
from pupcomp.error_pages.handlers import error_pages
app.register_blueprint(error_pages)

from pupcomp.users.views import users
app.register_blueprint(users)

from pupcomp.blog_posts.views import blog_posts
app.register_blueprint(blog_posts)