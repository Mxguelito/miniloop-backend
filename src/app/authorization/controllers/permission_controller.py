from flask import request





from src.app.authorization.services.permission_service import PermissionService


class PermissionController:

    @staticmethod
    def create_permission(current_user):


        data = request.get_json()

        response, status_code = PermissionService.create_permission(
            data,
            current_user
        )

        return response, status_code
    
    @staticmethod
    def assign_permission(current_user):

        data=request.get_json()

        rol_id = data.get('rol_id')
        permiso_id = data.get('permiso_id')

        response, status_code = PermissionService.assign_permission(
            rol_id,
            permiso_id,
            current_user
        )

        return response, status_code
    

    @staticmethod
    def get_permissions():

        response, status_code = PermissionService.get_permissions()

        return response, status_code
    
    @staticmethod
    def revoke_permission(current_user):

        data=request.get_json()

        rol_id = data.get('rol_id')
        permiso_id = data.get('permiso_id')

        response, status_code = PermissionService.revoke_permission(
            rol_id,
            permiso_id,
            current_user
        )

        return response, status_code
    
    @staticmethod
    def update_permission(current_user, permission_id):

        data = request.get_json()

        response, status_code = PermissionService.update_permission(
            permission_id,
            data,
            current_user
        )

        return response, status_code