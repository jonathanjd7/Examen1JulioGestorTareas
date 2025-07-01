# 🚀 Gestor de Tareas By Danilo

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey.svg)
![HTML5](https://img.shields.io/badge/HTML5-E34F26-orange.svg)
![CSS3](https://img.shields.io/badge/CSS3-1572B6-blue.svg)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow.svg)

Una aplicación web completa para gestionar tareas con diferentes niveles de prioridad, implementada con **Python Flask**, **SQLite** y arquitectura **MVC**. Proyecto optimizado y limpio, listo para producción.

[![Demo](https://img.shields.io/badge/Live-Demo-brightgreen.svg)](http://localhost:5000)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)](https://github.com/tu-usuario/gestor-tareas-by-danilo)

</div>

---

## 📋 Tabla de Contenidos

- [✨ Características](#-características)
- [🛠️ Tecnologías](#️-tecnologías)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [🚀 Instalación Rápida](#-instalación-rápida)
- [⚙️ Instalación Manual](#️-instalación-manual)
- [🎯 Uso](#-uso)
- [📡 API REST](#-api-rest)
- [🔒 Seguridad](#-seguridad)
- [🎨 Personalización](#-personalización)
- [🐛 Solución de Problemas](#-solución-de-problemas)
- [🤝 Contribuir](#-contribuir)
- [📄 Licencia](#-licencia)

---

## ✨ Características

### 🎨 Frontend
- ✅ **Interfaz moderna** con diseño glassmorphism
- ✅ **Imagen de fondo personalizable** con efecto overlay
- ✅ **Diseño responsivo** que se adapta a móviles y tablets
- ✅ **Animaciones suaves** y feedback visual
- ✅ **Modal de edición** elegante
- ✅ **Validación en tiempo real** de formularios

### 🔧 Backend
- ✅ **Operaciones CRUD completas** (Create, Read, Update, Delete)
- ✅ **Arquitectura MVC** (Model-View-Controller)
- ✅ **Base de datos SQLite** automática (sin configuración)
- ✅ **API REST** para comunicación frontend-backend
- ✅ **Validación de datos** en servidor y cliente
- ✅ **Manejo de errores** robusto

### 🎯 Funcionalidades
- ✅ **Crear tareas** con título y prioridad
- ✅ **Editar tareas** existentes con modal elegante
- ✅ **Eliminar tareas** con confirmación
- ✅ **Filtrar por prioridad** (Todas, Alta, Media, Baja)
- ✅ **Persistencia de datos** automática en SQLite
- ✅ **Datos de ejemplo** precargados
- ✅ **Validación en tiempo real** de formularios
- ✅ **Interfaz responsiva** para todos los dispositivos

---

## 🛠️ Tecnologías

### Backend
- **Python 3.8+** - Lenguaje principal
- **Flask 2.3.3** - Framework web ligero
- **Flask-SQLAlchemy** - ORM para base de datos
- **Flask-CORS** - Soporte para CORS
- **SQLite** - Base de datos embebida

### Frontend
- **HTML5** - Estructura semántica
- **CSS3** - Estilos modernos con glassmorphism
- **JavaScript ES6+** - Funcionalidad interactiva
- **Fetch API** - Comunicación con backend

### DevOps
- **Entorno virtual** - Aislamiento de dependencias
- **Scripts de instalación** - Automatización multiplataforma
- **GitHub Actions** - Plantillas de issues y configuración
- **Estructura modular** - Separación clara frontend/backend

---

## 📁 Estructura del Proyecto

```
gestor-tareas-by-danilo/
├── 📁 backend/                   # Lógica del servidor
│   ├── app_sqlite.py            # Aplicación principal (SQLite)
│   ├── requirements_simple.txt  # Dependencias mínimas
│   ├── instance/                # Base de datos SQLite (generada)
│   └── README.md                # Documentación del backend
├── 📁 frontend/                  # Interfaz de usuario
│   ├── 📁 static/               # Archivos estáticos
│   │   ├── deskpt.jpg           # Imagen de fondo
│   │   ├── styles.css           # Estilos CSS con glassmorphism
│   │   └── script.js            # JavaScript del frontend
│   ├── 📁 templates/            # Plantillas HTML
│   │   └── index.html           # Plantilla principal
│   └── README.md                # Documentación del frontend
├── 📁 .github/                   # Configuración de GitHub
│   └── 📁 ISSUE_TEMPLATE/       # Plantillas de issues
├── install.py                    # Instalador automático
├── start_app.py                  # Script de ejecución
├── .gitignore                    # Archivos a ignorar
├── LICENSE                       # Licencia MIT
└── README.md                     # Este archivo
```

---

## 🚀 Instalación Rápida

### ⚡ Instalación Automática (Recomendada)
```bash
# 1. Clonar el repositorio
git clone https://github.com/jonathanjd7/Examen1JulioGestorTareas
cd Examen1JulioGestorTareas

# 2. Ejecutar instalador automático
python install.py

# 3. Ejecutar la aplicación
python start_app.py

# 4. Abrir en el navegador
# http://localhost:5000
```

### 🔧 Instalación Manual
```bash
# 1. Clonar el repositorio
git clone https://github.com/jonathanjd7/Examen1JulioGestorTareas
cd Examen1JulioGestorTareas

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno virtual
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Instalar dependencias
pip install -r backend/requirements_simple.txt

# 5. Ejecutar aplicación
python start_app.py

# 6. Abrir en el navegador
# http://localhost:5000
```

---

## ⚙️ Instalación Manual

### 📋 Requisitos Previos
- **Python 3.8 o superior**
- **Git** (para clonar el repositorio)
- **Navegador web moderno** (Chrome, Firefox, Safari, Edge)

### Pasos Detallados

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/jonathanjd7/Examen1JulioGestorTareas
   cd Examen1JulioGestorTareas
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   ```

3. **Activar entorno virtual**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

4. **Instalar dependencias**
   ```bash
   pip install -r backend/requirements_simple.txt
   ```

5. **Ejecutar la aplicación**
   ```bash
   python start_app.py
   ```

6. **Abrir en el navegador**
   ```
   http://localhost:5000
   ```

---

## 🎯 Uso

### Interfaz Principal
1. **Crear tarea**: Completa el formulario con título y prioridad
2. **Filtrar tareas**: Usa los botones para ver tareas por prioridad
3. **Editar tarea**: Haz clic en "Editar" para modificar
4. **Eliminar tarea**: Haz clic en "Eliminar" con confirmación

### ✨ Características Especiales
- **Validación automática**: Los campos se validan en tiempo real
- **Persistencia**: Los datos se guardan automáticamente en SQLite
- **Responsive**: Funciona en móviles, tablets y desktop
- **Datos de ejemplo**: 5 tareas precargadas para probar
- **Diseño glassmorphism**: Interfaz moderna con efectos visuales
- **Modal de edición**: Formulario elegante para editar tareas

---

## 📡 API REST

### Endpoints Disponibles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/api/tasks` | Obtener todas las tareas |
| `GET` | `/api/tasks?priority=alta` | Filtrar por prioridad |
| `POST` | `/api/tasks` | Crear nueva tarea |
| `PUT` | `/api/tasks/{id}` | Actualizar tarea |
| `DELETE` | `/api/tasks/{id}` | Eliminar tarea |

### Ejemplo de Uso
```javascript
// Crear tarea
fetch('/api/tasks', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ 
        title: 'Nueva tarea', 
        priority: 'alta' 
    })
});

// Obtener tareas
fetch('/api/tasks')
    .then(response => response.json())
    .then(data => console.log(data.tasks));
```

---

## 🔒 Seguridad

- **Prevención de inyección SQL**: Uso de SQLAlchemy ORM
- **Validación de entrada**: Validación en servidor y cliente
- **Escape de HTML**: Prevención de ataques XSS
- **Sanitización de datos**: Limpieza de entrada del usuario
- **Manejo de errores**: Respuestas JSON estructuradas

---

## 🎨 Personalización

### 🖼️ Cambiar Imagen de Fondo
1. Reemplaza `frontend/static/deskpt.jpg` con tu imagen
2. Mantén el mismo nombre o actualiza la URL en `frontend/static/styles.css`
3. Formatos soportados: JPG, PNG, WebP

### 🎨 Modificar Colores y Estilos
Edita `frontend/static/styles.css` para cambiar:
- Colores de prioridad (alta, media, baja)
- Efectos de glassmorphism y transparencias
- Sombras y bordes redondeados
- Tipografías y tamaños

### ⚙️ Añadir Funcionalidades
- **Backend**: Modifica `backend/app_sqlite.py` para añadir nuevas rutas API
- **Frontend**: Actualiza `frontend/static/script.js` para nuevas funcionalidades
- **Interfaz**: Edita `frontend/templates/index.html` para cambios en la UI
- **Base de datos**: Modifica el modelo `Task` en `backend/app_sqlite.py`

---

## 🐛 Solución de Problemas

### Error: "No module named 'flask'"
```bash
# Activar entorno virtual
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Reinstalar dependencias
pip install -r backend/requirements_simple.txt
```

### Error: "Address already in use"
```bash
# Cambiar puerto en backend/app_sqlite.py
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Error: "Permission denied"
```bash
# Windows: Ejecutar como administrador
# macOS/Linux: Usar sudo si es necesario
```

### La aplicación no carga
1. Verificar que Python esté instalado: `python --version`
2. Verificar que el entorno virtual esté activado
3. Verificar que las dependencias estén instaladas
4. Revisar los logs en la terminal

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! 

1. **Fork** el proyecto
2. **Crea** una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. **Abre** un Pull Request

### 💡 Ideas para Contribuir
- [ ] Añadir autenticación de usuarios
- [ ] Implementar categorías de tareas
- [ ] Añadir fechas de vencimiento
- [ ] Crear sistema de notificaciones
- [ ] Implementar exportación de datos (CSV, PDF)
- [ ] Añadir temas oscuro/claro
- [ ] Implementar búsqueda de tareas
- [ ] Añadir estadísticas y reportes
- [ ] Crear API para aplicaciones móviles
- [ ] Implementar sincronización en la nube

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 👨‍💻 Autor

**Danilo** - Desarrollador Full Stack

- 📧 [Email] jonathanjd7@gmail.com  
- 💼 [LinkedIn]https://www.linkedin.com/in/danilo-doicela-878300114/
- 🐙 [GitHub] - https://github.com/jonathanjd7

---

## 📈 Estado del Proyecto

- ✅ **Estructura optimizada** - Proyecto limpio y organizado
- ✅ **Backend funcional** - API REST completa con SQLite
- ✅ **Frontend moderno** - Interfaz glassmorphism responsiva
- ✅ **Documentación completa** - READMEs detallados
- ✅ **Scripts de instalación** - Automatización multiplataforma
- ✅ **Listo para producción** - Configuración estable

---

<div align="center">

### ⭐ Si te gustó este proyecto, ¡dale una estrella en GitHub!

[![GitHub stars](https://img.shields.io/github/stars/tu-usuario/gestor-tareas-by-danilo.svg?style=social&label=Star)](https://github.com/tu-usuario/gestor-tareas-by-danilo)
[![GitHub forks](https://img.shields.io/github/forks/tu-usuario/gestor-tareas-by-danilo.svg?style=social&label=Fork)](https://github.com/tu-usuario/gestor-tareas-by-danilo)

**¡Gracias por usar Gestor de Tareas By Danilo! 🚀**

*Proyecto optimizado y listo para producción*

</div> 
