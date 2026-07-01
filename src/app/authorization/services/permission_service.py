from src.app.shared.config.db import db

from src.app.authorization.models.permission_model import Permission

from src.app.auth.models.auditoria_model import Auditoria

from src.app.authorization.models.role_model import Role
from src.app.authorization.models.rol_permiso_model import RolPermiso


class PermissionService:

    @staticmethod
    def create_permission(data, current_user):

        try:

            codigo = data.get("codigo")
            nombre = data.get("nombre")
            descripcion = data.get("descripcion")
            modulo = data.get("modulo")

            if not codigo:

                return {
                    "success": False,
                    "message": "El código es obligatorio"
                }, 400

            existing_permission = Permission.query.filter_by(
                codigo=codigo
            ).first()

            if existing_permission:

                return {
                    "success": False,
                    "message": "El permiso ya existe"
                }, 409

            permission = Permission(
                codigo=codigo,
                nombre=nombre,
                descripcion=descripcion,
                modulo=modulo
            )

            db.session.add(permission)
            db.session.flush()

            auditoria = Auditoria(

                persona_id=current_user.id,

                evento="PERMISSION_CREATED",

                severidad="INFO",

                descripcion=f"Permiso creado: {permission.codigo}"
            )

            db.session.add(auditoria)

            db.session.commit()

            return {

                "success": True,

                "message": "Permiso creado correctamente",

                "data": permission.to_dict()

            }, 201

        except Exception as e:

            db.session.rollback()

            return {

                "success": False,

                "message": str(e)

            }, 500
        

    @staticmethod
    def assign_permission(
        rol_id,
        permiso_id,
        asignado_por   
    
    ):
        rol = Role.query.get(rol_id)

        if not rol:
            
            return {
                "success": False,
                "message": "Rol no encontrado"
            }, 404
        
        permiso = Permission.query.get(permiso_id)

        if not permiso:
            
            return {
                "success": False,
                "message": "Permiso no encontrado"
            }, 404
        

        asignacion_existente = RolPermiso.query.filter_by(
            rol_id=rol_id,
            permiso_id=permiso_id
        ).first()


        if asignacion_existente:
            return {
                "success": False,
                "message": "El permiso ya está asignado al rol"
            }, 409

        try:
            rol_permiso = RolPermiso(
                rol_id=rol_id,
                permiso_id=permiso_id,
                asignado_por=asignado_por.id
            )

            db.session.add(rol_permiso)

            auditoria = Auditoria(
                persona_id=asignado_por.id,
                evento="PERMISSION_ASSIGNED",
                severidad="INFO",
                descripcion=f"Permiso {permiso.codigo} asignado al rol {rol.nombre}"
            )
            db.session.add(auditoria)
            db.session.commit()

            return {
                "success": True,
                "message": "Permiso asignado correctamente",
                "data": rol_permiso.to_dict()
            }, 201

        except Exception as e:

            db.session.rollback()

            return {
                
                "success": False,
                "message": str(e)
            }, 500    
        
    @staticmethod
    def get_permissions():

        permisos=Permission.query.order_by(Permission.codigo).all()

        return {
            "success": True,
            "data": [permiso.to_dict() for permiso in permisos]
        }, 200
    
    @staticmethod
    def revoke_permission(rol_id, permiso_id, revocado_por):

        rol = Role.query.get(rol_id)

        if not rol:
            
            return {
                "success": False,
                "message": "Rol no encontrado"
            }, 404
        
        permiso = Permission.query.get(permiso_id)

        if not permiso:
            
            return {
                "success": False,
                "message": "Permiso no encontrado"
            }, 404
        

        asignacion = RolPermiso.query.filter_by(
            rol_id=rol_id,
            permiso_id=permiso_id
        ).first()


        if not asignacion:
            return {
                "success": False,
                "message": "El rol no tiene asignado este permiso"
            }, 404

        try:
            asignacion.estado = "INACTIVO"
           

            auditoria = Auditoria(
                persona_id=revocado_por.id,
                evento="PERMISSION_REVOKED",
                severidad="WARNING",
                descripcion=f"Permiso {permiso.codigo} revocado del rol {rol.nombre}"
            )
            db.session.add(auditoria)
            db.session.commit()

            return {
                "success": True,
                "message": "Permiso revocado correctamente"
            }, 200

        except Exception as e:

            db.session.rollback()

            return {
                
                "success": False,
                "message": str(e)
            }, 500
        

    @staticmethod
    def update_permission(permission_id,data,current_user):

        permission = Permission.query.get(permission_id)

        if not permission:

            return {
                "success": False,
                "message": "Permiso no encontrado"
            }, 404

        try:

            
            permission.nombre = data.get("nombre", permission.nombre)
            permission.descripcion = data.get("descripcion", permission.descripcion)
            permission.modulo = data.get("modulo", permission.modulo)
            permission.estado = data.get("estado", permission.estado)

            

            auditoria = Auditoria(
                persona_id=current_user.id,
                evento="PERMISSION_UPDATED",
                severidad="INFO",
                descripcion=f"Permiso actualizado: {permission.codigo}"
            )
            db.session.add(auditoria)
            db.session.commit()

            return {
                "success": True,
                "message": "Permiso actualizado correctamente",
                "data": permission.to_dict()
            }, 200

        except Exception as e:

            db.session.rollback()

            return {
                
                "success": False,
                "message": str(e)
            }, 500    