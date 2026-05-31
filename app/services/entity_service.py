from app.config.db import db

from app.models.entidad_model import Entidad
from app.models.consorcio_model import Consorcio
from app.models.persona_entidad_model import PersonaEntidad


class EntityService:

    @staticmethod
    def create_consorcio(data, current_user):

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

        db.session.commit()

        return {
            "success": True,
            "message": "Consorcio creado correctamente",
            "entidad": entidad.to_dict(),
            "consorcio": consorcio.to_dict()
        }