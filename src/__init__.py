from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_envvar('APPLICATION_CONFIG')

from core.models import db

migrate = Migrate(app, db, directory=app.config['MIGRATION_DIR_PATH'])

app.config.from_object('config')

app.secret_key = '868006bea618648fe66c6a76fac074dcbb24a690ae54c3c5db7f61f24355397f'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user.login'
login_manager.login_message = "User needs to be logged in to view this page"

config = app.config

# Calling the call which will serve services to view files
from src.services.app_services import AppServicesImpl
services = AppServicesImpl(config)

# calling view files
from src.views import game, user

# Initially run this function if want to add game data of games_data.csv in db
# from add_games import add_initial_games
# add_initial_games()