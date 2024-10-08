import os
from flask import Flask

def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)  # Use __name__ instead of _name_
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)  # Use makedirs instead of makesirs
    except OSError:
        pass

    # A simple page that says hello
    @app.route('/hello')
    def hello():
        return "Hello MangaJozu!"

    return app

      
    # https://flask.palletsprojects.com/en/3.0.x/tutorial/factory/
    # Install Code :

    #Virtual Environment (Recomended)
        # python3 -m venv venv
# source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

#upgrade pip
 # python3 -m pip install --upgrade pip


# Install flask and other packages
    # python3 -m pip install Flask flask-bcrypt Flask-SQLAlchemy



    #/my_flask_app
   # /app
    #    __init__.py
    #    routes.py (optional, if you want to separate your routes)
   # config.py (optional)
   # run.py