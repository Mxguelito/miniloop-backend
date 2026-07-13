from datetime import datetime

from src.app.shared.config.db import db

from src.app.entities.models.entidad_model import Entidad
from src.app.entities.models.consorcio_model import Consorcio
from src.app.entities.models.persona_entidad_model import PersonaEntidad
from src.app.entities.models.comercio_model import Comercio
from src.app.auth.models.auditoria_model import Auditoria


class EntityService:

    @staticmethod
    def create_consorcio(data, current_user):

        try:

            # =========================
            # CREAR ENTIDAD
            # =========================

            entidad = Entidad(

                nombre=data["nombre"],

                tipo_entidad="CONSORCIO",

                estado="PENDIENTE_APROBACION",

                owner_persona_id=current_user.id,

                email_contacto=data.get("email_contacto"),

                telefono_contacto=data.get("telefono_contacto"),

                descripcion=data.get("descripcion")
            )

            db.session.add(entidad)
            db.session.flush()

            # =========================
            # CREAR CONSORCIO
            # =========================

            consorcio = Consorcio(

                entidad_id=entidad.id,

                direccion=data["direccion"],

                ciudad=data["ciudad"],

                provincia=data["provincia"],

                codigo_postal=data.get("codigo_postal"),

                cantidad_unidades=data.get(
                    "cantidad_unidades",
                    0
                ),

                cantidad_pisos=data.get(
                    "cantidad_pisos"
                ),

                tiene_seguridad=data.get(
                    "tiene_seguridad",
                    False
                ),

                tiene_cochera=data.get(
                    "tiene_cochera",
                    False
                )
            )

            db.session.add(consorcio)

            # =========================
            # OWNER RELATION
            # =========================

            persona_entidad = PersonaEntidad(

                persona_id=current_user.id,

                entidad_id=entidad.id,

                rol="OWNER",

                estado="ACTIVO"
            )

            db.session.add(persona_entidad)

            auditoria = Auditoria(

                persona_id=current_user.id,

                evento="CONSORCIO_CREATED",

                severidad="INFO",

                descripcion=f"Consorcio creado: {entidad.nombre}"
            )

            db.session.add(auditoria)

            db.session.commit()

            return {
                "success": True,
                "message": "Consorcio creado correctamente",
                "entidad": entidad.to_dict(),
                "consorcio": consorcio.to_dict()
            }

        except Exception as e:

            db.session.rollback()

            return {
                "success": False,
                "message": str(e)
            }

    @staticmethod
    def create_comercio(data, current_user):

        try:

            # =========================
            # CREAR ENTIDAD
            # =========================

            entidad = Entidad(

                nombre=data["nombre"],

                tipo_entidad="COMERCIO",

                estado="PENDIENTE_APROBACION",

                owner_persona_id=current_user.id,

                email_contacto=data.get("email_contacto"),

                telefono_contacto=data.get("telefono"),

                descripcion=data.get("descripcion")
            )

            db.session.add(entidad)
            db.session.flush()

            # =========================
            # CREAR COMERCIO
            # =========================

            comercio = Comercio(

                entidad_id=entidad.id,

                rubro=data["rubro"],

                descripcion=data.get("descripcion"),

                telefono=data.get("telefono"),

                email_contacto=data.get("email_contacto"),

                direccion=data["direccion"],

                horario_apertura=data.get(
                    "horario_apertura"
                ),

                horario_cierre=data.get(
                    "horario_cierre"
                )
            )

            db.session.add(comercio)

            # =========================
            # OWNER RELATION
            # =========================

            persona_entidad = PersonaEntidad(

                persona_id=current_user.id,

                entidad_id=entidad.id,

                rol="OWNER",

                estado="ACTIVO"
            )

            db.session.add(persona_entidad)
            
            auditoria = Auditoria(

                persona_id=current_user.id,

                evento="COMERCIO_CREATED",

                severidad="INFO",

                descripcion=f"Comercio creado: {entidad.nombre}"
            )

            db.session.add(auditoria)

            db.session.commit()

            return {

                "success": True,

                "message": "Comercio creado correctamente",

                "entidad": entidad.to_dict(),

                "comercio": comercio.to_dict()
            }

        except Exception as e:

            db.session.rollback()

            return {

                "success": False,

                "message": str(e)
            }
        
    


    @staticmethod
    def update_entity(
    entidad_id,
    current_user,
    data
    ):

     try:

        entidad = Entidad.query.get(
            entidad_id
        )

        # =========================
        # VALIDAR EXISTENCIA
        # =========================

        if not entidad:

            return {
                "success": False,
                "message": "Entidad no encontrada"
            }, 404
        # =========================
       # VALIDAR PROPIETARIO
       # =========================

        if entidad.owner_persona_id != current_user.id:

         return {
        "success": False,
        "message": "No tiene permisos para editar esta entidad"
            }, 403
        # =========================
        # ACTUALIZAR CAMPOS
        # ========================= 
        entidad.nombre = data.get(
            "nombre",
            entidad.nombre
        )
        entidad.descripcion = data.get(
            "descripcion",
            entidad.descripcion
        )
        entidad.telefono_contacto = data.get(
            "telefono_contacto",
            entidad.telefono_contacto
        )
        entidad.email_contacto = data.get(
            "email_contacto",
            entidad.email_contacto
        )
        entidad.updated_at = datetime.utcnow()

        # =========================
        #AUDITORIA
        # =========================
        auditoria = Auditoria(

            persona_id=current_user.id,

            evento="ENTIDAD_UPDATED",

            severidad="INFO",

            descripcion=f"Entidad actualizada: {entidad.nombre}"
        )

        db.session.add(auditoria)
        # =========================
        # GUARDAR CAMBIOS
        # =========================
        db.session.commit()
        return {
            "success": True,
            "message": "Entidad actualizada correctamente",
            "entidad": entidad.to_dict()
        }, 200

     except Exception as e:

        db.session.rollback()

        return {
            "success": False,
            "message": str(e)
        }, 500
     

    @staticmethod
    def delete_entity(
        entidad_id,
        current_user
    ):

        try:

            entidad = Entidad.query.get(
                entidad_id
            )

            # =========================
            # VALIDAR EXISTENCIA
            # =========================

            if not entidad:

                return {
                    "success": False,
                    "message": "Entidad no encontrada"
                }, 404

            # =========================
            # VALIDAR PROPIETARIO
            # =========================

            if entidad.owner_persona_id != current_user.id:

                return {
                    "success": False,
                    "message": "No tiene permisos para eliminar esta entidad"
                }, 403
            
            # =========================
            # VALIDAR ESTADO    

            if entidad.estado == "INACTIVO":

                return {
                    "success": False,
                    "message": "La entidad ya está inactiva"
                }, 400
            # =========================
            # SOFT DELETE (CAMBIAR ESTADO A INACTIVO)
            # =========================

            entidad.estado = "INACTIVO"
            entidad.updated_at = datetime.utcnow()

            # AUDITORIA
            auditoria = Auditoria(

                persona_id=current_user.id,

                evento="ENTIDAD_DELETED",

                severidad="WARNING",

                descripcion=f"Entidad eliminada: {entidad.nombre}"
            )
            db.session.add(auditoria)


            # =========================
            # GUARDAR CAMBIOS
            # =========================
            db.session.commit()

            return {
                "success": True,
                "message": "Entidad eliminada correctamente"
            }, 200

        except Exception as e:

            db.session.rollback()

            return {
                "success": False,
                "message": str(e)
            }, 500
        

    @staticmethod
    def get_entities(current_user):

        try:

            entidades= Entidad.query.filter(
                Entidad.estado != "INACTIVO"
            ).all()

            auditoria = Auditoria(

                persona_id=current_user.id,

                evento="ENTITY_LIST_VIEWED",

                severidad="INFO",

                descripcion="Consulta de entidades realizada"
            )
            db.session.add(auditoria)
            db.session.commit()

            return {
                "success": True,
                "count": len(entidades),
                "data": [entidad.to_dict() for entidad in entidades]
            }, 200
        except Exception as e:

            db.session.rollback()
            return {
                "success": False,
                "message": str(e)
            }, 500
        
    

    @staticmethod
    def get_entity_by_id(
        entidad_id,
        current_user
    ):

        try:

            entidad = Entidad.query.get(
                entidad_id
            )

            if not entidad or entidad.estado == "INACTIVO":

                return {
                    "success": False,
                    "message": "Entidad no encontrada"
                }, 404

            auditoria = Auditoria(

                persona_id=current_user.id,

                evento="ENTITY_DETAIL_VIEWED",

                severidad="INFO",

                descripcion=f"Consulta de entidad realizada: {entidad.nombre}"
            )
            db.session.add(auditoria)
            db.session.commit()

            return {
                "success": True,
                "data": entidad.to_dict()
            }, 200

        except Exception as e:

            db.session.rollback()

            return {
                "success": False,
                "message": str(e)
            }, 500
        

    
    @staticmethod
    def restore_entity(
        entidad_id,
        current_user
    ):

        try:

            entidad = Entidad.query.get(
                entidad_id
            )

            # =========================
            # VALIDAR EXISTENCIA
            # =========================

            if not entidad:

                return {
                    "success": False,
                    "message": "Entidad no encontrada"
                }, 404

            # =========================
            # VALIDAR PROPIETARIO
            # =========================

            if entidad.owner_persona_id != current_user.id:

                return {
                    "success": False,
                    "message": "No tiene permisos para restaurar esta entidad"
                }, 403
            
            # =========================
            # VALIDAR ESTADO    

            if entidad.estado != "INACTIVO":

                return {
                    "success": False,
                    "message": "La entidad ya está activa"
                }, 400
            # =========================
            # RESTAURAR ENTIDAD (CAMBIAR ESTADO A ACTIVO)
            # =========================

            entidad.estado = "ACTIVO"
            entidad.updated_at = datetime.utcnow()

             # AUDITORIA
            auditoria = Auditoria(

                persona_id=current_user.id,

                evento="ENTIDAD_RESTORED",

                severidad="INFO",

                descripcion=f"Entidad restaurada: {entidad.nombre}"
            )
            db.session.add(auditoria)

             # =========================
             # GUARDAR CAMBIOS
             # =========================
            db.session.commit()

            return {
                "success": True,
                "message": "Entidad restaurada correctamente",
                "entidad": entidad.to_dict()
            }, 200

        except Exception as e:

            db.session.rollback()

            return {
                "success": False,
                "message": str(e)
            }, 500
        
    @staticmethod
    def get_auditoria(
        current_user
    ):

        try:

            auditorias = Auditoria.query.order_by(
                Auditoria.created_at.desc()
            ).all()

            return {
                "success": True,
                "count": len(auditorias),
                "data": [auditoria.to_dict() for auditoria in auditorias]
            }, 200

        except Exception as e:

            return {
                "success": False,
                "message": str(e)
            }, 500
