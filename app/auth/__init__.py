# # Initializes the auth module
from flask import Flask
from .config import Config
from .extensions import db
from .views import main  # Assuming you have views set up in views.py

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(main)

    return app