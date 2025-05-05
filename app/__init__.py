from flask import Flask
from .models import db  # Import db from models.py
from .routes import main  # Import the renamed Blueprint

def create_app():
    app_instance = Flask(__name__, instance_relative_config=True)
    app_instance.config.from_pyfile('config.py')
    db.init_app(app_instance)  # Initialize db with the app
    app_instance.register_blueprint(main)  # Register the renamed Blueprint
    return app_instance