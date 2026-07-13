from flask import jsonify, request



from src.app.authorization.services.role_service import RoleService


class RoleController:

    @staticmethod
    def create_role(current_user):

        response, status_code = (
            RoleService.create_role(
                request.get_json(),
                current_user
            )
        )

        return jsonify(response), status_code
    


    @staticmethod
    def assign_role(current_user):

        data = request.get_json()

        usuario_id = data.get("usuario_id")
        rol_id = data.get("rol_id")
        

        
        return RoleService.assign_role(
                usuario_id,
                rol_id,
                current_user
            )
    
    @staticmethod
    def revoke_role(current_user):

        data = request.get_json()

        usuario_id = data.get("usuario_id")
        rol_id = data.get("rol_id")
        
        return RoleService.revocar_rol(
                usuario_id,
                rol_id,
                current_user
            )