from flask import Blueprint

from src.app.controllers.admin_entity_controller import (
    AdminEntityController
)

from src.app.middleware.auth_middleware import (
    token_required
)


admin_entity = Blueprint(
    "admin_entity",
    __name__
)


# =========================
# APPROVE CONSORCIO
# =========================

@admin_entity.route(
    "/api/v1/admin/entities/consorcios/<int:entidad_id>/approve",
    methods=["PUT"]
)
@token_required
def approve_consorcio(
    current_user,
    entidad_id
):

    return AdminEntityController.approve_consorcio(
        current_user,
        entidad_id
    )


# =========================
# REJECT CONSORCIO
# =========================

@admin_entity.route(
    "/api/v1/admin/entities/consorcios/<int:entidad_id>/reject",
    methods=["PUT"]
)
@token_required
def reject_consorcio(
    current_user,
    entidad_id
):

    return AdminEntityController.reject_consorcio(
        current_user,
        entidad_id
    )