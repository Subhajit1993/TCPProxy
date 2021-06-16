#!/usr/bin/env python3
import os

if os.getenv("FLASK_ENV") is None:
    raise Exception("No environment set")

from config import Config
from flaskr import create_app

app = create_app(config=Config)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=os.getenv("FLASK_ENV") != "production", port=os.getenv("PORT"))
