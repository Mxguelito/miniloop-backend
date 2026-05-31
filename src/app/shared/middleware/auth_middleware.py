from functools import wraps

from flask_jwt_extended import (
    verify_jwt_in_request,
    get_jwt_identity
)

from src.app.auth.models.persona_model import Persona


def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):

        try:

            # VERIFICAR JWT
            verify_jwt_in_request()

            # OBTENER ID DEL TOKEN
            current_user_id = get_jwt_identity()

            # BUSCAR PERSONA
            current_user = Persona.query.get(
                int(current_user_id)
            )

            if not current_user:
                return {
                    "success": False,
                    "message": "Usuario no encontrado"
                }, 404

            return f(current_user, *args, **kwargs)

        except Exception as e:

            return {
                "success": False,
                "message": "Token inválido o expirado",
                "error": str(e)
            }, 401

    return decorated