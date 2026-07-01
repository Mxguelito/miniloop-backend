# 🚀 MiniLoop Backend

Backend del sistema MiniLoop desarrollado con Flask.

MiniLoop es una plataforma orientada a la administración de consorcios, comercios y marketplace bajo una arquitectura modular y escalable.

---

# Tecnologías

- Python 3
- Flask
- PostgreSQL
- SQLAlchemy
- Flask-Migrate
- Alembic
- Flask-JWT-Extended
- Jinja2
- Gunicorn
- Render

---

# Funcionalidades implementadas

## Autenticación

- Registro de usuarios
- Inicio de sesión
- Cierre de sesión
- Validación de sesión
- Perfil
- Edición de perfil

---

## Administración

- Gestión de Roles
- Gestión de Permisos
- Auditoría

---

## Entidades

- Crear Consorcio
- Aprobar Consorcio
- Rechazar Consorcio
- Crear Comercio

---

## Inteligencia Artificial

- Predicción de prioridad de Consorcios mediante Machine Learning.

---

# Arquitectura

```
src/
│
├── ai/
├── auth/
├── authorization/
├── entities/
├── routes/
├── shared/
├── static/
├── templates/
└── models/
```

---

# Variables de entorno

Crear un archivo `.env`

```env
DATABASE_URL=

JWT_SECRET_KEY=

SECRET_KEY=
```

---

# Ejecutar localmente

Instalar dependencias

```bash
pip install -r requirements.txt
```

Aplicar migraciones

```bash
flask --app run.py db upgrade
```

Ejecutar

```bash
python run.py
```

---

# Deploy

Aplicación desplegada en Render.

Backend Flask + PostgreSQL + Gunicorn.

---

# Estado

Proyecto académico en desarrollo.

Arquitectura preparada para continuar con Marketplace, Delivery, Notificaciones, Economía y demás módulos.
