from flask_jwt_extended import create_access_token
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from datetime import datetime

from src.app.shared.config.db import db

from src.app.auth.models.persona_model import Persona
from src.app.auth.models.usuario_auth_model import UsuarioAuth
from src.app.auth.models.auditoria_model import Auditoria


class AuthService:

    @staticmethod
    def register(data):

        try:

            nombre = data.get("nombre")
            apellido = data.get("apellido")
            email = data.get("email")
            documento = data.get("documento")
            password = data.get("password")

            # VALIDACIONES

            if not nombre or not apellido or not email or not documento or not password:
                return {
                    "body": {
                        "success": False,
                        "message": "Todos los campos son obligatorios"
                    },
                    "status": 400
                }

            # NORMALIZACIÓN

            email = email.strip().lower()

            # VALIDAR EMAIL DUPLICADO

            existing_email = Persona.query.filter_by(
                email=email
            ).first()

            if existing_email:
                return {
                    "body": {
                        "success": False,
                        "message": "Email ya registrado"
                    },
                    "status": 409
                }

            # VALIDAR DOCUMENTO DUPLICADO

            existing_documento = Persona.query.filter_by(
                documento=documento
            ).first()

            if existing_documento:
                return {
                    "body": {
                        "success": False,
                        "message": "Documento ya registrado"
                    },
                    "status": 409
                }

            # HASH PASSWORD

            password_hash = generate_password_hash(password)

            # CREAR PERSONA

            persona = Persona(
                nombre=nombre,
                apellido=apellido,
                email=email,
                documento=documento
            )

            db.session.add(persona)

            # NECESARIO PARA OBTENER persona.id
            db.session.flush()

            # CREAR AUTH

            auth = UsuarioAuth(
                persona_id=persona.id,
                username=email,
                password_hash=password_hash,
                estado_sesion="ONLINE"
            )

            db.session.add(auth)

            # AUDITORÍA

            auditoria = Auditoria(
                persona_id=persona.id,
                evento="USER_REGISTERED",
                severidad="INFO",
                descripcion=f"Usuario registrado: {email}"
            )

            db.session.add(auditoria)

            # COMMIT

            db.session.commit()

            # JWT

            access_token = create_access_token(
                identity=str(persona.id)
            )

            return {
                "body": {
                    "success": True,
                    "message": "Usuario registrado correctamente",
                    "token": access_token,
                    "user": persona.to_dict()
                },
                "status": 201
            }

        except Exception as e:

            db.session.rollback()

            return {
                "body": {
                    "success": False,
                    "message": "Error interno del servidor",
                    "error": str(e)
                },
                "status": 500
            }

    @staticmethod
    def login(data):

        try:

            email = data.get("email")
            password = data.get("password")

            # VALIDACIONES

            if not email or not password:
                return {
                    "body": {
                        "success": False,
                        "message": "Email y password son obligatorios"
                    },
                    "status": 400
                }

            # NORMALIZACIÓN

            email = email.strip().lower()

            # BUSCAR PERSONA

            persona = Persona.query.filter_by(
                email=email
            ).first()

            if not persona:
                return {
                    "body": {
                        "success": False,
                        "message": "Credenciales inválidas"
                    },
                    "status": 401
                }

            # BUSCAR AUTH

            auth = UsuarioAuth.query.filter_by(
                persona_id=persona.id
            ).first()

            if not auth:
                return {
                    "body": {
                        "success": False,
                        "message": "Credenciales inválidas"
                    },
                    "status": 401
                }

            # VALIDAR PASSWORD

            password_correct = check_password_hash(
                auth.password_hash,
                password
            )

            if not password_correct:

                auditoria = Auditoria(
                    persona_id=persona.id,
                    evento="LOGIN_FAILED",
                    severidad="WARN",
                    descripcion=f"Password incorrecta para {email}"
                )

                db.session.add(auditoria)
                db.session.commit()

                return {
                    "body": {
                        "success": False,
                        "message": "Credenciales inválidas"
                    },
                    "status": 401
                }

            # ACTUALIZAR SESIÓN

            auth.estado_sesion = "ONLINE"
            auth.ultimo_login = datetime.utcnow()

            # AUDITORÍA LOGIN

            auditoria = Auditoria(
                persona_id=persona.id,
                evento="USER_LOGGED_IN",
                severidad="INFO",
                descripcion=f"Login exitoso: {email}"
            )

            db.session.add(auditoria)

            db.session.commit()

            # JWT

            access_token = create_access_token(
                identity=str(persona.id)
            )

            return {
                "body": {
                    "success": True,
                    "message": "Login exitoso",
                    "token": access_token,
                    "user": persona.to_dict()
                },
                "status": 200
            }

        except Exception as e:

            db.session.rollback()

            return {
                "body": {
                    "success": False,
                    "message": "Error interno del servidor",
                    "error": str(e)
                },
                "status": 500
            }
        
           
           
           
    
    

    @staticmethod
    def logout(current_user):

        try:

            # BUSCAR AUTH

            auth = UsuarioAuth.query.filter_by(
                persona_id=current_user.id
            ).first()

            if not auth:
                return {
                    "body": {
                        "success": False,
                        "message": "Sesión no encontrada"
                    },
                    "status": 404
                }

            # CAMBIAR ESTADO SESIÓN

            auth.estado_sesion = "OFFLINE"

            # INVALIDAR TOKENS FUTUROS

            auth.token_version += 1

            # AUDITORÍA

            auditoria = Auditoria(
                persona_id=current_user.id,
                evento="USER_LOGGED_OUT",
                severidad="INFO",
                descripcion=f"Logout exitoso: {current_user.email}"
            )

            db.session.add(auditoria)

            # COMMIT

            db.session.commit()

            return {
                "body": {
                    "success": True,
                    "message": "Logout exitoso"
                },
                "status": 200
            }

        except Exception as e:

            db.session.rollback()

            return {
                "body": {
                    "success": False,
                    "message": "Error interno del servidor",
                    "error": str(e)
                },
                "status": 500
            }
        

    
    @staticmethod
    def dashboard(current_user):


        try:

            dashboard_data = {
                "user": current_user.to_dict(),

                "modules": [
                    {
                        "name": "Dashboard",
                        "enabled": True
                    },
                    {
                        "name": "Consorcios",
                        "enabled": False
                    },
                    {
                        "name": "Marketplace",
                        "enabled": False
                    },
                    {
                        "name": "Delivery",
                        "enabled": False
                    }
                ],

                "stats": {
                    "entities": 0,
                    "notifications": 0,
                    "active_sessions": 1
                }
            }

            # AUDITORÍA

            auditoria = Auditoria(
                persona_id=current_user.id,
                evento="DASHBOARD_LOADED",
                severidad="INFO",
                descripcion=f"Dashboard cargado: {current_user.email}"
            )

            db.session.add(auditoria)

            db.session.commit()

            return {
                "body": {
                    "success": True,
                    "dashboard": dashboard_data
                },
                "status": 200
            }

        except Exception as e:

            db.session.rollback()

            return {
                "body": {
                    "success": False,
                    "message": "Error cargando dashboard",
                    "error": str(e)
                },
                "status": 500
            }
        


    @staticmethod
    def profile(current_user):

          try:
              auditoria = Auditoria(
                  persona_id=current_user.id,
                  evento="PROFILE_VIEWED",
                  severidad="INFO",
                    descripcion=f"Perfil consultado: {current_user.email}"
              )

              db.session.add(auditoria)
              db.session.commit()

              return {
                  "body": {
                      "success": True,
                      "profile": current_user.to_dict()
                  },
                  "status": 200
              }

          except Exception as e:
              db.session.rollback()
              return {
                  "body": {
                      "success": False,
                      "message": "Error cargando perfil",
                      "error": str(e)
                  },
                  "status": 500
              }
          



    @staticmethod
    def audit():

        try:

            auditorias= Auditoria.query.order_by(
                Auditoria.id.desc()
            ).all()

           

            return {
                "body": {
                    "success": True,
                    "auditorias": auditorias
                },
                "status": 200
            }

        except Exception as e:

            db.session.rollback()

            return {
                "body": {
                    "success": False,
                    "message": "Error cargando auditoría",
                    "error": str(e)
                },
                "status": 500
            }

    @staticmethod
    def update_profile(current_user, data):

        try:

            nombre = data.get("nombre")
            apellido = data.get("apellido")
            telefono = data.get("telefono")

            # UPDATE CAMPOS

            if nombre:
                current_user.nombre = nombre

            if apellido:
                current_user.apellido = apellido

            if telefono:
                current_user.telefono = telefono

            # AUDITORÍA

            auditoria = Auditoria(
                persona_id=current_user.id,
                evento="USER_PROFILE_UPDATED",
                severidad="INFO",
                descripcion=f"Perfil actualizado: {current_user.email}"
            )

            db.session.add(auditoria)

            db.session.commit()

            return {
                "body": {
                    "success": True,
                    "message": "Perfil actualizado correctamente",
                    "user": current_user.to_dict()
                },
                "status": 200
            }

        except Exception as e:

            db.session.rollback()

            return {
                "body": {
                    "success": False,
                    "message": "Error actualizando perfil",
                    "error": str(e)
                },
                "status": 500
            }
        
    

        
    @staticmethod
    def validate_session(current_user):

        try:

            usuario_auth = UsuarioAuth.query.filter_by(
                persona_id=current_user.id
            ).first()

            if not usuario_auth:
                return {
                    "body": {
                        "success": False,
                        "authenticated": False,
                        "message": "Sesión inválida"
                    },
                    "status": 401
                }

            # AUDITORÍA

            auditoria = Auditoria(
                persona_id=current_user.id,
                evento="SESSION_VALIDATED",
                severidad="INFO",
                descripcion=f"Sesión validada: {current_user.email}"
            )

            db.session.add(auditoria)

            db.session.commit()

            return {
                "body": {
                    "success": True,
                    "authenticated": True,
                    "user": current_user.to_dict()
                },
                "status": 200
            }

        except Exception as e:

            db.session.rollback()

            return {
                "body": {
                    "success": False,
                    "authenticated": False,
                    "message": "Error validando sesión",
                    "error": str(e)
                },
                "status": 500
            }