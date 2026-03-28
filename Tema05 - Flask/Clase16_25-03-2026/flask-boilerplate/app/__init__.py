from flask import Flask
from config import Config
from flask_migrate import Migrate
from db import db
from app.models import role_model, user_model

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
