from flask import Blueprint
from flask_cors import CORS

home_bp = Blueprint('home', __name__)
CORS(home_bp, supports_credentials=True)  # enable CORS on the API_v1 blue print
from flaskr.controllers.home import home
