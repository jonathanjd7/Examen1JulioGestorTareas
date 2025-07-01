# 🎨 Frontend - Gestor de Tareas By Danilo

Esta carpeta contiene toda la interfaz de usuario y los archivos estáticos de la aplicación.

## 📁 Estructura

```
frontend/
├── templates/
│   └── index.html              # Plantilla HTML principal
├── static/
│   ├── deskpt.jpg              # Imagen de fondo
│   ├── styles.css              # Estilos CSS
│   └── script.js               # JavaScript del frontend
├── index.html                  # Versión standalone (sin Flask)
├── styles.css                  # Versión standalone
├── script.js                   # Versión standalone
└── README.md                   # Este archivo
```

## 🎨 Características del Frontend

### Diseño
- **Glassmorphism**: Efecto de cristal esmerilado moderno
- **Responsive**: Se adapta a móviles, tablets y desktop
- **Imagen de fondo**: Personalizable con overlay
- **Animaciones**: Transiciones suaves y feedback visual

### Funcionalidades
- **Formulario de tareas**: Crear nuevas tareas
- **Lista dinámica**: Mostrar tareas con prioridades
- **Filtros**: Filtrar por prioridad (Todas, Alta, Media, Baja)
- **Modal de edición**: Editar tareas existentes
- **Validación**: Validación en tiempo real de formularios

### Tecnologías
- **HTML5**: Estructura semántica
- **CSS3**: Estilos modernos con glassmorphism
- **JavaScript ES6+**: Funcionalidad interactiva
- **Fetch API**: Comunicación con backend

## 🚀 Uso

### Con Backend (Recomendado)
```bash
# Desde la raíz del proyecto
python start_app.py
# Luego visita: http://localhost:5000
```

### Standalone (Solo Frontend)
```bash
# Abre directamente en el navegador
frontend/index.html
```

## 🎨 Personalización

### Cambiar Imagen de Fondo
1. Reemplaza `static/deskpt.jpg` con tu imagen
2. Mantén el mismo nombre o actualiza la URL en `static/styles.css`

### Modificar Colores
Edita `static/styles.css` para cambiar:
- Colores de prioridad (rojo=alta, amarillo=media, verde=baja)
- Efectos de glassmorphism
- Transparencias y sombras
- Animaciones

### Añadir Funcionalidades
- Modifica `static/script.js` para nuevas funcionalidades
- Edita `templates/index.html` para cambios en la estructura
- Actualiza `static/styles.css` para nuevos estilos

## 🔧 Configuración

### API Endpoints
El frontend se comunica con el backend a través de:
- `GET /api/tasks` - Obtener tareas
- `POST /api/tasks` - Crear tarea
- `PUT /api/tasks/{id}` - Actualizar tarea
- `DELETE /api/tasks/{id}` - Eliminar tarea

### Validación
- Validación de título en tiempo real
- Prevención de envío con datos inválidos
- Mensajes de error visuales
- Escape de HTML para prevenir XSS

## 📱 Responsive Design

### Breakpoints
- **Desktop**: > 800px
- **Tablet**: 600px - 800px
- **Mobile**: < 600px

### Características Mobile
- Formulario adaptado
- Botones de acción apilados
- Modal optimizado para touch
- Navegación táctil

## 🎯 Componentes

### Formulario de Tareas
- Campo de título con validación
- Selector de prioridad
- Botón de envío con feedback

### Lista de Tareas
- Items con información de prioridad
- Botones de acción (Editar/Eliminar)
- Estados visuales (hover, focus)

### Filtros
- Botones de filtro por prioridad
- Estado activo visual
- Transiciones suaves

### Modal de Edición
- Formulario de edición
- Validación en tiempo real
- Botones de acción (Guardar/Cancelar)

## 🛠️ Desarrollo

### Estructura de Archivos
- **HTML**: Estructura y contenido
- **CSS**: Estilos y animaciones
- **JavaScript**: Lógica y interactividad

### Patrones de Diseño
- **Módulo**: JavaScript organizado en clases
- **Observer**: Event listeners para interactividad
- **Factory**: Creación de elementos DOM

## 📝 Notas

- Los archivos en la raíz de `frontend/` son versiones standalone
- Los archivos en `static/` y `templates/` son para uso con Flask
- La imagen de fondo debe estar en `static/` para que Flask la sirva
- El JavaScript está optimizado para comunicación con API REST 