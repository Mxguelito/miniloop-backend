from flask import request

from app.services.entity_service import EntityService


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