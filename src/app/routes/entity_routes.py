from flask import Blueprint

from src.app.controllers.entity_controller import EntityController

from src.app.shared.middleware.auth_middleware import token_required


entity = Blueprint(
    "entity",
    __name__
)


# =========================
# CREATE CONSORCIO
# =========================

@entity.route(
    "/api/v1/entities/consorcios",
    methods=["POST"]
)
@token_required
def create_consorcio(current_user):

    return EntityController.create_consorcio(
        current_user
    )