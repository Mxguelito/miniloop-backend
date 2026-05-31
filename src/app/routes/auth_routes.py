from flask import Blueprint

from src.app.controllers.auth_controller import AuthController
from src.app.shared.middleware.auth_middleware import token_required


auth = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/v1/auth"
)


# REGISTER
@auth.route("/register", methods=["POST"])
def register():
    return AuthController.register()


# LOGIN
@auth.route("/login", methods=["POST"])
def login():
    return AuthController.login()

# LOGOUT
@auth.route("/logout", methods=["POST"])
@token_required
def logout(current_user):
    return AuthController.logout(current_user)


# PROFILE
@auth.route("/profile", methods=["GET"])
@token_required
def profile(current_user):
    return AuthController.profile(current_user)

# DASHBOARD
@auth.route("/dashboard", methods=["GET"])
@token_required
def dashboard(current_user):
    return AuthController.dashboard(current_user)

# UPDATE PROFILE
@auth.route("/profile", methods=["PUT"])
@token_required
def update_profile(current_user):
    return AuthController.update_profile(current_user)


# VALIDATE SESSION
@auth.route("/validate-session", methods=["GET"])
@token_required
def validate_session(current_user):
    return AuthController.validate_session(current_user)