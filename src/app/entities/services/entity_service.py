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
