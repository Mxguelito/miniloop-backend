from app.config.db import db
from datetime import datetime


class Persona(db.Model):

    __tablename__ = "personas"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    apellido = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False,
        index=True
    )

    telefono = db.Column(
        db.String(20),
        nullable=True
    )

    documento = db.Column(
        db.String(20),
        unique=True,
        nullable=False,
        index=True
    )

    estado = db.Column(
        db.String(20),
        default="ACTIVO",
        nullable=False
    )

    email_verified = db.Column(
    db.Boolean,
    default=False,
    nullable=False
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
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "telefono": self.telefono,
            "documento": self.documento,
            "estado": self.estado,
            "email_verified": self.email_verified,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
    def __repr__(self):
      return f"<Persona {self.email}>"