from src.app import create_app
from src.app.shared.config.db import db

# AUTH
from src.app.auth.models.persona_model import Persona
from src.app.auth.models.usuario_auth_model import UsuarioAuth
from src.app.auth.models.auditoria_model import Auditoria

# MULTI TENANT
from src.app.entities.models.entidad_model import Entidad
from src.app.entities.models.consorcio_model import Consorcio
from src.app.entities.models.persona_entidad_model import PersonaEntidad


app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)