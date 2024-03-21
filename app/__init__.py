from flask import Flask
from .config import Config
from .models import db
from .routes import main
from flask_jwt_extended import JWTManager
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    CORS(app)
    JWTManager(app)

    app.register_blueprint(main)

    return app
