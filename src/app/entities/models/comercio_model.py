from src.app.shared.config.db import db
from datetime import datetime


class Comercio(db.Model):

    __tablename__ = "comercios"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    entidad_id = db.Column(
        db.BigInteger,
        db.ForeignKey("entidades.id"),
        nullable=False,
        unique=True
    )

    rubro = db.Column(
        db.String(100),
        nullable=False
    )

    descripcion = db.Column(
        db.Text,
        nullable=True
    )

    telefono = db.Column(
        db.String(50),
        nullable=True
    )

    email_contacto = db.Column(
        db.String(150),
        nullable=True
    )

    direccion = db.Column(
        db.String(255),
        nullable=False
    )

    horario_apertura = db.Column(
        db.String(20),
        nullable=True
    )

    horario_cierre = db.Column(
        db.String(20),
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

    entidad = db.relationship(
        "Entidad",
        backref="comercio"
    )

    def to_dict(self):

        return {
            "id": self.id,
            "entidad_id": self.entidad_id,
            "rubro": self.rubro,
            "descripcion": self.descripcion,
            "telefono": self.telefono,
            "email_contacto": self.email_contacto,
            "direccion": self.direccion,
            "horario_apertura": self.horario_apertura,
            "horario_cierre": self.horario_cierre,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }