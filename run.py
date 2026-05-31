from app import create_app
from app.config.db import db

# AUTH
from app.models.persona_model import Persona
from app.models.usuario_auth_model import UsuarioAuth
from app.models.auditoria_model import Auditoria

# MULTI TENANT
from app.models.entidad_model import Entidad
from app.models.consorcio_model import Consorcio
from app.models.persona_entidad_model import PersonaEntidad


app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)