from flask import jsonify, request

from src.app.entities.services.entity_service import EntityService


class EntityController:

    @staticmethod
    def create_consorcio(current_user):

        try:

            data = request.get_json()

            required_fields = [
                "nombre",
                "direccion",
                "ciudad",
                "provincia"
            ]

            # =========================
            # VALIDAR CAMPOS
            # =========================

            for field in required_fields:

                if field not in data:

                    return {
                        "success": False,
                        "message": f"Falta el campo: {field}"
                    }, 400

            # =========================
            # CREATE CONSORCIO
            # =========================

            result = EntityService.create_consorcio(
                data,
                current_user
            )

            return result, 201

        except Exception as e:

            return {
                "success": False,
                "message": "Error al crear consorcio",
                "error": str(e)
            }, 500
        

        
        
    @staticmethod
    def create_comercio(current_user):

        try:

            data = request.get_json()

            required_fields = [
                "nombre",
                "rubro",
                "direccion"
            ]

            # =========================
            # VALIDAR CAMPOS
            # =========================

            for field in required_fields:

                if field not in data:

                    return {
                        "success": False,
                        "message": f"Falta el campo: {field}"
                    }, 400

            # =========================
            # CREATE COMERCIO
            # =========================

            result = EntityService.create_comercio(
                data,
                current_user
            )

            return result, 201

        except Exception as e:

            return {
                "success": False,
                "message": "Error al crear comercio",
                "error": str(e)
            }, 500
        

    @staticmethod
    def update_entity(
    current_user,
    entidad_id
       ):

     data = request.get_json()

     result, status_code = (
        EntityService.update_entity(
            entidad_id,
            current_user,
            data
         )
      )

     return result, status_code
    

    @staticmethod
    def delete_entity(
    current_user,
    entidad_id
    ):

     result, status_code = (
        EntityService.delete_entity(
            entidad_id,
            current_user
         )
      )

     return jsonify(result), status_code
    

    
    @staticmethod
    def get_entities(
        current_user
    ):
        response, status_code = EntityService.get_entities(
            current_user
        )
        return jsonify(response), status_code
    


    @staticmethod
    def get_entity_by_id(
        current_user,
        entidad_id
    ):
        response, status_code = EntityService.get_entity_by_id(
            entidad_id,
            current_user
        )
        return jsonify(response), status_code
    


    @staticmethod
    def restore_entity(
        current_user,
        entidad_id
    ):
        response, status_code = EntityService.restore_entity(
            entidad_id,
            current_user
        )
        return jsonify(response), status_code
    

    @staticmethod
    def get_auditoria(
        current_user
    ):
        response, status_code = EntityService.get_auditoria(
            current_user
        )
        return jsonify(response), status_code