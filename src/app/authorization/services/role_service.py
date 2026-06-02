from src.app.auth.models.usuario_auth_model import UsuarioAuth
from src.app.authorization.models.usuario_role_model import UsuarioRole
from src.app.shared.config.db import db

from src.app.authorization.models.role_model import Role

from src.app.auth.models.auditoria_model import Auditoria


class RoleService:

    @staticmethod
    def create_role(data, current_user):

        try:

            nombre = data.get("nombre")
            descripcion = data.get("descripcion")

            # CU21.3
            if not nombre:

                return {
                    "success": False,
                    "message": "El nombre del rol es obligatorio"
                }, 400

            # CU21.4
            existing_role = Role.query.filter_by(
                nombre=nombre
            ).first()

            if existing_role:

                return {
                    "success": False,
                    "message": "El rol ya existe"
                }, 409

            # CU21.5
            role = Role(
                nombre=nombre,
                descripcion=descripcion
            )

            db.session.add(role)
            db.session.flush()

            # CU21.6
            auditoria = Auditoria(

                persona_id=current_user.id,

                evento="ROLE_CREATED",

                severidad="INFO",

                descripcion=f"Rol creado: {role.nombre}"
            )

            db.session.add(auditoria)

            db.session.commit()

            return {

                "success": True,

                "message": "Rol creado correctamente",

                "data": role.to_dict()

            }, 201

        except Exception as e:

            db.session.rollback()

            return {

                "success": False,

                "message": str(e)

            }, 500
        

    @staticmethod
    def assign_role(usuario_id, rol_id, asignado_por):
        usuario = UsuarioAuth.query.get(usuario_id)

        if not usuario:

            return {
                "success": False,
                "message": "Usuario no encontrado"
            }, 404
        rol = Role.query.get(rol_id)
        if not rol:

            return {
                "success": False,
                "message": "Rol no encontrado"
            }, 404
        
        asignacion_existente = UsuarioRole.query.filter_by(
            usuario_id=usuario_id,
            rol_id=rol_id
        ).first()

        if asignacion_existente:

            return {
                "success": False,
                "message": "El usuario ya tiene asignado este rol"
            }, 409
        
        try:

            usuario_role = UsuarioRole(
                usuario_id=usuario_id,
                rol_id=rol_id,
                asignado_por=asignado_por.id
            )

            db.session.add(usuario_role)
            

            auditoria = Auditoria(

                persona_id=asignado_por.id,

                evento="ROLE_ASSIGNED",

                severidad="INFO",

                descripcion=f"Rol {rol.nombre} asignado al usuario {usuario.username}"
            )

            db.session.add(auditoria)

            db.session.commit()

            return {

                "success": True,

                "message": "Rol asignado correctamente",

                "data": usuario_role.to_dict()

            }, 201
        except Exception as e:

            db.session.rollback()

            return {

                "success": False,

                "message": str(e)

            }, 500

    
