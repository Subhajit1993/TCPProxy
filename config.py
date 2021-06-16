from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path('.env.' + os.getenv("FLASK_ENV"))
load_dotenv(dotenv_path=dotenv_path, override=True)

print("Loading == ", os.getenv("FLASK_ENV"))


class Config(object):
    SECRET_KEY = 'YOU WILL NEVER GUESS',
    STATIC_PATH = 'static',
    TEMPLATES_DIR = 'templates',
    MONGODB_SETTINGS = {
        'host': os.getenv("DB_HOST"),
    }
