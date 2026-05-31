from src.app.shared.config.db import db
from datetime import datetime


class PersonaEntidad(db.Model):

    __tablename__ = "persona_entidad"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    persona_id = db.Column(
        db.BigInteger,
        db.ForeignKey("personas.id"),
        nullable=False
    )

    entidad_id = db.Column(
        db.BigInteger,
        db.ForeignKey("entidades.id"),
        nullable=False
    )

    rol = db.Column(
        db.String(50),
        nullable=False,
        default="MIEMBRO"
    )

    estado = db.Column(
        db.String(30),
        nullable=False,
        default="ACTIVO"
    )

    fecha_union = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    persona = db.relationship(
        "Persona",
        backref="entidades_asociadas"
    )

    entidad = db.relationship(
        "Entidad",
        backref="miembros"
    )

    def to_dict(self):

        return {
            "id": self.id,
            "persona_id": self.persona_id,
            "entidad_id": self.entidad_id,
            "rol": self.rol,
            "estado": self.estado,
            "fecha_union": self.fecha_union.isoformat(),
            "created_at": self.created_at.isoformat()
        }