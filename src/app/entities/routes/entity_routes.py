from flask import Blueprint

from src.app.entities.controllers.entity_controller import EntityController

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


# =========================
# CREATE COMERCIO
# =========================

@entity.route(
    "/api/v1/entities/comercios",
    methods=["POST"]
)
@token_required
def create_comercio(current_user):


    return EntityController.create_comercio(
        current_user
    )

# =========================
# UPDATE ENTITY
# =========================

@entity.route(
    "/api/v1/entities/<int:entidad_id>",
    methods=["PUT"]
)
@token_required
def update_entity(
    current_user,
    entidad_id
):

    return EntityController.update_entity(
        current_user,
        entidad_id
    )

# =========================
# DELETE ENTITY (soft delete)
# =========================
@entity.route(
    "/api/v1/entities/<int:entidad_id>",
    methods=["DELETE"]
)
@token_required
def delete_entity(
    current_user,
    entidad_id
):

    return EntityController.delete_entity(
        current_user,
        entidad_id
    )

# =========================
# GET ENTITIES
# =========================
@entity.route(
    "/api/v1/entities",
    methods=["GET"]
)
@token_required
def get_entities(current_user):

    return EntityController.get_entities(
        current_user
    )

# =========================
# GET ENTITY BY ID
# =========================
@entity.route(
    "/api/v1/entities/<int:entidad_id>",
    methods=["GET"]
)
@token_required
def get_entity_by_id(current_user, entidad_id):

    return EntityController.get_entity_by_id(
        current_user,
        entidad_id
    )


# =========================
# RESTORE ENTITY
# =========================
@entity.route(
    "/api/v1/entities/<int:entidad_id>/restore",
    methods=["PUT"]
)
@token_required
def restore_entity(
    current_user,
    entidad_id
):

    return EntityController.restore_entity(
        current_user,
        entidad_id
    )

# =========================
# GET AUDITORIA
# =========================
@entity.route(
    "/api/v1/auditoria",
    methods=["GET"]
)
@token_required
def get_auditoria(current_user):

    return EntityController.get_auditoria(
        current_user
    )