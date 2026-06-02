from datetime import datetime

from src.app.shared.config.db import db


class UsuarioRole(db.Model):

    __tablename__ = "usuario_roles"

    __table_args__ = (

        db.UniqueConstraint(
            "usuario_id",
            "rol_id",
            name="uq_usuario_rol"
        ),

    )

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    usuario_id = db.Column(
        db.BigInteger,
        db.ForeignKey("usuarios_auth.id"),
        nullable=False
    )

    rol_id = db.Column(
        db.BigInteger,
        db.ForeignKey("roles.id"),
        nullable=False
    )

    asignado_por = db.Column(
        db.BigInteger,
        db.ForeignKey("personas.id"),
        nullable=False
    )

    fecha_asignacion = db.Column(
        db.DateTime,
        default=datetime.utcnow,
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

            "usuario_id": self.usuario_id,

            "rol_id": self.rol_id,

            "asignado_por": self.asignado_por,

            "fecha_asignacion": (
                self.fecha_asignacion.isoformat()
                if self.fecha_asignacion
                else None
            ),

            "estado": self.estado,

            "created_at": (
                self.created_at.isoformat()
                if self.created_at
                else None
            ),

            "updated_at": (
                self.updated_at.isoformat()
                if self.updated_at
                else None
            )
        }