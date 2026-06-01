# MINILOOP — ARQUITECTURA GENERAL

## Visión

MiniLoop es una plataforma SaaS multi-tenant diseñada para administrar entidades, personas, consorcios, comercios, marketplace, delivery y servicios internos mediante una arquitectura modular y escalable.

---

# AUTH

Responsabilidad:

Autenticación, autorización y auditoría.

Componentes:

- Persona
- UsuarioAuth
- Auditoria

Funciones:

- Registro
- Login
- Logout
- Validación JWT
- Gestión de sesiones

---

# ENTITIES

Responsabilidad:

Gestión de entidades del sistema.

Componentes:

- Entidad
- Consorcio
- Comercio
- PersonaEntidad

Funciones:

- Crear entidad
- Aprobar entidad
- Rechazar entidad
- Asociar personas a entidades

---

# RBAC

Responsabilidad:

Control de acceso basado en roles.

Componentes futuros:

- Rol
- Permiso
- RolPermiso

Funciones:

- Permisos por módulo
- Permisos por acción
- Seguridad del sistema

---

# MEMBERS

Responsabilidad:

Administrar relaciones entre personas y entidades.

Funciones:

- Invitaciones
- Vinculaciones
- Solicitudes de acceso

---

# COMMERCE

Responsabilidad:

Marketplace y gestión comercial.

Componentes futuros:

- Producto
- Categoria
- Pedido
- DetallePedido

Funciones:

- Catálogo
- Compras
- Ventas
- Gestión de productos

---

# DELIVERY

Responsabilidad:

Logística y distribución.

Componentes futuros:

- Repartidor
- Entrega
- IncidenteDelivery

Funciones:

- Entregas
- Seguimiento
- Gestión de incidencias

---

# ECONOMY

Responsabilidad:

Gestión económica.

Componentes futuros:

- MovimientoEconomico
- Pago
- Expensa
- Multa

Funciones:

- Ingresos
- Egresos
- Balances
- Reportes financieros

---

# NOTIFICATIONS

Responsabilidad:

Comunicación interna del sistema.

Componentes futuros:

- Notificacion

Funciones:

- Alertas
- Recordatorios
- Eventos automáticos

---

# ROADMAP

FASE 1
- AUTH
- ENTITIES

FASE 2
- RBAC
- MEMBERS

FASE 3
- COMMERCE

FASE 4
- DELIVERY

FASE 5
- ECONOMY

FASE 6
- NOTIFICATIONS

MÓDULOS IMPLEMENTADOS

✅ AUTH
CU01 - CU07

✅ ENTITIES
CU08 - Crear Consorcio
CU09 - Aprobar Consorcio
CU10 - Rechazar Consorcio

🟡 EN DESARROLLO
CU11 - Crear Comercio

🔴 PENDIENTE
CU12 - Aprobar Comercio
CU13 - Rechazar Comercio
...

acepta_delivery_externo = db.Column(
    db.Boolean,
    default=True
)

delivery_propio = db.Column(
    db.Boolean,
    default=False
)