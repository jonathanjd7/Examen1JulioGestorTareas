# 🔧 Backend - Gestor de Tareas By Danilo

Esta carpeta contiene toda la lógica del servidor y la API REST de la aplicación.

## 📁 Estructura

```
backend/
├── app_sqlite.py              # Aplicación principal (SQLite)
├── requirements_simple.txt    # Dependencias mínimas
└── README.md                  # Este archivo
```

## 🚀 Instalación

### Opción 1: Desde la raíz del proyecto
```bash
# Desde la carpeta raíz
python install.py
python start_app.py
```

### Opción 2: Instalación manual
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements_simple.txt

# Ejecutar aplicación
python app_sqlite.py
```

## 📡 API Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/api/tasks` | Obtener todas las tareas |
| `GET` | `/api/tasks?priority=alta` | Filtrar por prioridad |
| `POST` | `/api/tasks` | Crear nueva tarea |
| `PUT` | `/api/tasks/{id}` | Actualizar tarea |
| `DELETE` | `/api/tasks/{id}` | Eliminar tarea |

## 🔧 Configuración

### Variables de Entorno
- `SECRET_KEY`: Clave secreta para Flask
- `DATABASE_URL`: URL de conexión a la base de datos

### Base de Datos
- **SQLite** (por defecto): No requiere configuración

## 🛠️ Desarrollo

### Estructura MVC
- **Model**: Clase `Task` con SQLAlchemy
- **View**: Plantillas HTML en `../frontend/templates`
- **Controller**: Clase `TaskController` con lógica de negocio

### Validación
- Validación de título (requerido, longitud, caracteres)
- Validación de prioridad (valores permitidos)
- Sanitización de datos

### Seguridad
- Prevención de inyección SQL (ORM)
- Escape de HTML
- Validación de entrada
- Manejo de errores estructurado

## 🚀 Despliegue

### Desarrollo
```bash
python app_sqlite.py
```

### Producción
```bash
python app_sqlite.py
```

## 📝 Notas

- La aplicación está configurada para servir archivos estáticos desde `../frontend/static`
- Las plantillas se cargan desde `../frontend/templates`
- La base de datos SQLite se crea automáticamente en la carpeta `instance/` 