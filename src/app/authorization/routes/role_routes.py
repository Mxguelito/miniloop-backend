from flask import Blueprint

from src.app.shared.middleware.auth_middleware import token_required

from src.app.authorization.controllers.role_controller import RoleController


role = Blueprint(

    "role",

    __name__,

    url_prefix="/api/v1/roles"
)


@role.route(

    "",

    methods=["POST"]
)
@token_required
def create_role(current_user):

    return RoleController.create_role(
        current_user
    )


@role.route(
    "/asignar",
    methods=["POST"]
)
@token_required
def assign_role(current_user):

    return RoleController.assign_role(
        current_user
    )

@role.route(
    "/revocar",
    methods=["POST"]
)
@token_required
def revoke_role(current_user):

    return RoleController.revoke_role(
        current_user
    )
