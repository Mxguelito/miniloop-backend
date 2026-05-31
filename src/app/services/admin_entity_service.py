from datetime import datetime

from src.app.config.db import db

from src.app.models.entidad_model import Entidad
from src.app.models.auditoria_model import Auditoria


class AdminEntityService:

    @staticmethod
    def approve_consorcio(
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
            # VALIDAR TIPO ENTIDAD
            # =========================

            if entidad.tipo_entidad != "CONSORCIO":

                return {
                    "success": False,
                    "message": "La entidad no es un consorcio"
                }, 400

            # =========================
            # VALIDAR ESTADO
            # =========================

            if entidad.estado != "PENDIENTE_APROBACION":

                return {
                    "success": False,
                    "message": "La entidad ya fue procesada"
                }, 400

            # =========================
            # APROBAR CONSORCIO
            # =========================

            entidad.estado = "ACTIVO"

            entidad.updated_at = datetime.utcnow()

            # =========================
            # AUDITORÍA
            # =========================

            auditoria = Auditoria(

                persona_id=current_user.id,

                evento="CONSORCIO_APPROVED",

                severidad="INFO",

                descripcion=f"Consorcio aprobado: {entidad.nombre}"
            )

            db.session.add(auditoria)

            # =========================
            # COMMIT
            # =========================

            db.session.commit()

            return {
                "success": True,
                "message": "Consorcio aprobado correctamente",
                "entidad": entidad.to_dict()
            }, 200

        # =========================
        # ROLLBACK
        # =========================

        except Exception as e:

            db.session.rollback()

            return {
                "success": False,
                "message": str(e)
            }, 500
        
    @staticmethod
    def reject_consorcio(
        entidad_id,
        current_user,
        motivo_rechazo
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
            # VALIDAR TIPO ENTIDAD
            # =========================

            if entidad.tipo_entidad != "CONSORCIO":

                return {
                    "success": False,
                    "message": "La entidad no es un consorcio"
                }, 400

            # =========================
            # VALIDAR ESTADO
            # =========================

            if entidad.estado != "PENDIENTE_APROBACION":

                return {
                    "success": False,
                    "message": "La entidad ya fue procesada"
                }, 400

            # =========================
            # VALIDAR MOTIVO
            # =========================

            if not motivo_rechazo:

                return {
                    "success": False,
                    "message": "El motivo de rechazo es obligatorio"
                }, 400

            # =========================
            # RECHAZAR CONSORCIO
            # =========================

            entidad.estado = "RECHAZADO"

            entidad.motivo_rechazo = motivo_rechazo

            entidad.fecha_rechazo = datetime.utcnow()

            entidad.rechazado_por = current_user.id

            entidad.updated_at = datetime.utcnow()

            # =========================
            # AUDITORÍA
            # =========================

            auditoria = Auditoria(

                persona_id=current_user.id,

                evento="CONSORCIO_REJECTED",

                severidad="WARNING",

                descripcion=f"Consorcio rechazado: {entidad.nombre}"
            )

            db.session.add(auditoria)

            # =========================
            # COMMIT
            # =========================

            db.session.commit()

            return {
                "success": True,
                "message": "Consorcio rechazado correctamente",
                "entidad": entidad.to_dict()
            }, 200

        # =========================
        # ROLLBACK
        # =========================

        except Exception as e:

            db.session.rollback()

            return {
                "success": False,
                "message": str(e)
            }, 500

    


