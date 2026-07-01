import os
from dotenv import load_dotenv
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate


from src.app.shared.config.db import db

from src.app.routes.main_routes import main
from src.app.auth.routes.auth_routes import auth
from src.app.entities.routes.entity_routes import entity
from src.app.entities.routes.admin_entity_routes import admin_entity

from src.app.authorization.routes.role_routes import role
from src.app.authorization.routes.permission_routes import permission
from src.app.routes.ai_routes import ai


def create_app():

    load_dotenv()

    app = Flask(__name__)

    # DATABASE

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # JWT

    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    # Guardar el JWT en cookies
    app.config["JWT_TOKEN_LOCATION"] = ["cookies"]

# Como estamos en localhost
    app.config["JWT_COOKIE_SECURE"] = False

# Toda la aplicación puede acceder a la cookie
    app.config["JWT_ACCESS_COOKIE_PATH"] = "/"

# Por ahora desactivamos CSRF hasta terminar el sistema
    app.config["JWT_COOKIE_CSRF_PROTECT"] = False

    # JWT EXPIRATION FUTURA
    # app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

    # INIT DB

    db.init_app(app)


    # MIGRATIONS
    Migrate(app, db)

    # INIT JWT

    JWTManager(app)

    # BLUEPRINTS

    app.register_blueprint(main)
    app.register_blueprint(ai)
    app.register_blueprint(auth)
    app.register_blueprint(entity)
    app.register_blueprint(admin_entity)
    app.register_blueprint(role)
    app.register_blueprint(permission)
    return app