from src.app.shared.config.db import db
from datetime import datetime


class Role(db.Model):

    __tablename__ = "roles"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False,
        unique=True,
        index=True
    )

    descripcion = db.Column(
        db.Text,
        nullable=True
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

            "nombre": self.nombre,

            "descripcion": self.descripcion,

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

    def __repr__(self):

        return f"<Role {self.nombre}>"