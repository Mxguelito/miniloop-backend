from app.config.db import db
from datetime import datetime


class Entidad(db.Model):

    __tablename__ = "entidades"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    nombre = db.Column(
        db.String(150),
        nullable=False,
        unique=True,
        index=True
    )

    tipo_entidad = db.Column(
        db.String(50),
        nullable=False
    )

    estado = db.Column(
        db.String(30),
        nullable=False,
        default="PENDIENTE_APROBACION"
    )

    owner_persona_id = db.Column(
        db.BigInteger,
        db.ForeignKey("personas.id"),
        nullable=False
    )

    email_contacto = db.Column(
        db.String(150),
        nullable=True
    )

    telefono_contacto = db.Column(
        db.String(30),
        nullable=True
    )

    descripcion = db.Column(
        db.Text,
        nullable=True
    )

    motivo_rechazo = db.Column(db.Text, nullable=True)

    fecha_rechazo = db.Column(db.DateTime, nullable=True)

    rechazado_por = db.Column(
      db.BigInteger,
      db.ForeignKey("personas.id"),
      nullable=True
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

    owner = db.relationship(
    "Persona",
    foreign_keys=[owner_persona_id],
    backref="entidades_creadas"
)

    def to_dict(self):

        return {
            "id": self.id,
            "nombre": self.nombre,
            "tipo_entidad": self.tipo_entidad,
            "estado": self.estado,
            "owner_persona_id": self.owner_persona_id,
            "email_contacto": self.email_contacto,
            "telefono_contacto": self.telefono_contacto,
            "descripcion": self.descripcion,
            "motivo_rechazo": self.motivo_rechazo,

            "fecha_rechazo": (
            self.fecha_rechazo.isoformat()
            if self.fecha_rechazo
            else None
            ),

            "rechazado_por": self.rechazado_por,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }