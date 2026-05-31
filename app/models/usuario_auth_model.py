from app.config.db import db
from datetime import datetime


class UsuarioAuth(db.Model):

    __tablename__ = "usuarios_auth"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    persona_id = db.Column(
        db.BigInteger,
        db.ForeignKey("personas.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    username = db.Column(
        db.String(150),
        unique=True,
        nullable=False,
        index=True
    )

    password_hash = db.Column(
        db.Text,
        nullable=False
    )

    estado_sesion = db.Column(
        db.String(20),
        default="OFFLINE",
        nullable=False
    )

    ultimo_login = db.Column(
        db.DateTime,
        nullable=True
    )

    token_version = db.Column(
        db.Integer,
        default=1,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    persona = db.relationship(
        "Persona",
        backref=db.backref(
            "auth",
            uselist=False,
            cascade="all, delete"
        )
    )

    def to_dict(self):
        return {
            "id": self.id,
            "persona_id": self.persona_id,
            "username": self.username,
            "estado_sesion": self.estado_sesion,
            "ultimo_login": self.ultimo_login.isoformat() if self.ultimo_login else None,
            "token_version": self.token_version,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
    def __repr__(self):
     return f"<UsuarioAuth {self.username}>"