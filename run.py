 # Entry point to start the Flask app

from __init__ import create_app  # Import from __init__.py

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


# to run : python run.py
