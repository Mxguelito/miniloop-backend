from flask import Blueprint

from flask_jwt_extended import jwt_required

from src.app.shared.middleware.auth_middleware import token_required

from src.app.authorization.controllers.permission_controller import PermissionController

permission = Blueprint(
    "permission",
    __name__,
    url_prefix="/api/v1/permisos"
)


@permission.route(
    "",
    methods=["POST"]
)
@token_required
def create_permission(current_user):

    return PermissionController.create_permission(current_user)

@permission.route(
    "/asignar",
    methods=["POST"]
)
@token_required
def assign_permission(current_user):

    return PermissionController.assign_permission(current_user)

@permission.route(
    "",
    methods=["GET"]
)
@token_required
def get_permissions(current_user):

    return PermissionController.get_permissions()

@permission.route(
    "/revocar",
    methods=["POST"]
)
@token_required
def revoke_permission(current_user):

    return PermissionController.revoke_permission(current_user)


@permission.route(
    "/<int:permission_id>",
    methods=["PUT"]
)
@token_required
def update_permission(current_user, permission_id):

    return PermissionController.update_permission(current_user, permission_id)