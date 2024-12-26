from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from flask_wtf.csrf import CSRFProtect

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    csrf = CSRFProtect(app)
    app.config.from_object(Config)
    return app

    