from flask import Flask
from .config import Config
from .extensions import bcrypt, db  # Import Bcrypt and SQLAlchemy
from .views import main  # Import the blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions with the app
    bcrypt.init_app(app)
    db.init_app(app)  # Initialize SQLAlchemy with the app

    # Register blueprints
    app.register_blueprint(main)

    return app

# https://medium.com/@mlmason11/secure-user-authentication-in-flask-with-bcrypt-b2aacecb607e 












      
