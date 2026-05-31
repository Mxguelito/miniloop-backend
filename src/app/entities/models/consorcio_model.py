from src.app.shared.config.db import db
from datetime import datetime


class Consorcio(db.Model):

    __tablename__ = "consorcios"

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

    direccion = db.Column(
        db.String(255),
        nullable=False
    )

    ciudad = db.Column(
        db.String(100),
        nullable=False
    )

    provincia = db.Column(
        db.String(100),
        nullable=False
    )

    codigo_postal = db.Column(
        db.String(20),
        nullable=True
    )

    cantidad_unidades = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    cantidad_pisos = db.Column(
        db.Integer,
        nullable=True
    )

    tiene_seguridad = db.Column(
        db.Boolean,
        default=False
    )

    tiene_cochera = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    entidad = db.relationship(
        "Entidad",
        backref="consorcio"
    )

    def to_dict(self):

        return {
            "id": self.id,
            "entidad_id": self.entidad_id,
            "direccion": self.direccion,
            "ciudad": self.ciudad,
            "provincia": self.provincia,
            "codigo_postal": self.codigo_postal,
            "cantidad_unidades": self.cantidad_unidades,
            "cantidad_pisos": self.cantidad_pisos,
            "tiene_seguridad": self.tiene_seguridad,
            "tiene_cochera": self.tiene_cochera,
            "created_at": self.created_at.isoformat()
        }