 # Other database models (besides users)
from .extensions import db  # Import the initialized db instance

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

# You can define more models here as needed