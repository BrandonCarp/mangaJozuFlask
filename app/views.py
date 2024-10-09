# General routes (home, about, etc.)
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return 'Manga Jozu Desu!'