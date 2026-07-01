from datetime import datetime

from src.app.shared.config.db import db


class RolPermiso(db.Model):

    __tablename__ = "rol_permisos"

    __table_args__ = (

        db.UniqueConstraint(
            "rol_id",
            "permiso_id",
            name="uq_rol_permiso"
        ),

    )

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    rol_id = db.Column(
        db.BigInteger,
        db.ForeignKey("roles.id"),
        nullable=False
    )

    permiso_id = db.Column(
        db.BigInteger,
        db.ForeignKey("permisos.id"),
        nullable=False
    )

    asignado_por = db.Column(
        db.BigInteger,
        db.ForeignKey("personas.id"),
        nullable=False
    )

    estado = db.Column(
        db.String(20),
        nullable=False,
        default="ACTIVO"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    def to_dict(self):

        return {

            "id": self.id,

            "rol_id": self.rol_id,

            "permiso_id": self.permiso_id,

            "asignado_por": self.asignado_por,

            "estado": self.estado
        }