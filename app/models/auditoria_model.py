from app.config.db import db
from datetime import datetime


class Auditoria(db.Model):

    __tablename__ = "auditoria"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    persona_id = db.Column(
        db.BigInteger,
        db.ForeignKey(
            "personas.id",
            ondelete="SET NULL"
        ),
        nullable=True
    )

    evento = db.Column(
        db.String(100),
        nullable=False,
        index=True
    )

    severidad = db.Column(
        db.String(20),
        nullable=False,
        index=True
    )

    descripcion = db.Column(
        db.Text,
        nullable=False
    )

    ip_address = db.Column(
        db.String(100),
        nullable=True
    )

    user_agent = db.Column(
        db.Text,
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    persona = db.relationship(
        "Persona",
        backref=db.backref(
            "auditorias",
            lazy=True
        )
    )

    def to_dict(self):
        return {
            "id": self.id,
            "persona_id": self.persona_id,
            "evento": self.evento,
            "severidad": self.severidad,
            "descripcion": self.descripcion,
            "ip_address": self.ip_address,
            "user_agent": self.user_agent,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f"<Auditoria {self.evento}>"