from flask import request, jsonify
from src.app.services.admin_entity_service import (
    AdminEntityService
)


class AdminEntityController:

    @staticmethod
    def approve_consorcio(
        current_user,
        entidad_id
    ):

        return AdminEntityService.approve_consorcio(
            entidad_id,
            current_user
        )
    
       
       
    @staticmethod
    def reject_consorcio(
        current_user,
        entidad_id
        ):

        data = request.get_json()

        motivo_rechazo = data.get(
            "motivo_rechazo"
        )

        

        response, status_code = (
            AdminEntityService.reject_consorcio(
                entidad_id,
                current_user,
                motivo_rechazo
            )
        )

        return jsonify(response), status_code