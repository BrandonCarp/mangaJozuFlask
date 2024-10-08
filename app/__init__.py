import os
from flask import Flask, jsonify

 # Initializes the app


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    
    @app.route('/')
    def index():
        return "the MangaJozu Flask app"

    @app.route('/login')
    def hello():
        return "Login to MangaJozu"
    


    @app.route('/api/data', methods=['GET'])
    def get_data():
        return jsonify({'message': 'flask is neat'})

    return app


# https://medium.com/@mlmason11/secure-user-authentication-in-flask-with-bcrypt-b2aacecb607e 












      
