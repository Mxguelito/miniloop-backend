from flask import Flask
from flask_jwt_extended import JWTManager

from src.app.config.db import db

from src.app.routes.main_routes import main
from src.app.routes.auth_routes import auth
from src.app.routes.entity_routes import entity
from src.app.routes.admin_entity_routes import admin_entity


def create_app():

    app = Flask(__name__)

    # DATABASE

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:admin123@localhost/miniloop"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # JWT

    app.config["JWT_SECRET_KEY"] = "miniloop_super_ultra_enterprise_jwt_secret_key_2026_backend_production"

    # JWT EXPIRATION FUTURA
    # app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

    # INIT DB

    db.init_app(app)

    # INIT JWT

    JWTManager(app)

    # BLUEPRINTS

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(entity)
    app.register_blueprint(admin_entity)

    return app