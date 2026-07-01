from src.app.shared.config.db import db


class Permission(db.Model):

    __tablename__ = "permisos"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    codigo = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    descripcion = db.Column(
        db.Text
    )

    modulo = db.Column(
        db.String(100)
    )

    estado = db.Column(
        db.String(20),
        default="ACTIVO",
        nullable=False
    )

    def to_dict(self):

        return {
            "id": self.id,
            "codigo": self.codigo,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "modulo": self.modulo,
            "estado": self.estado
        }