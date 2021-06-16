from flaskr.controllers.home import home_bp
from flask import current_app, render_template, request, json, Response
import logging
import os


@home_bp.before_app_request
def before_request():
    pass


@home_bp.route('/', methods=['GET'])
def index():
    data = {
        "env": os.getenv("FLASK_ENV")
    }
    return render_template('index.html', data=data)
