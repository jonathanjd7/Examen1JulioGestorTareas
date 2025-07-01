from flask import Flask, render_template, request, jsonify, session, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from datetime import datetime
import re

app = Flask(__name__, 
           template_folder='../frontend/templates',
           static_folder='../frontend/static')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'tu_clave_secreta_super_segura_aqui')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///tasks.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

# Modelo de Tarea
class Task(db.Model):
    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    priority = db.Column(db.String(50), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'priority': self.priority,
            'completed': self.completed,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

# Validación de datos
class TaskValidator:
    @staticmethod
    def validate_title(title):
        if not title or not title.strip():
            return False, "El título es obligatorio"
        if len(title.strip()) > 255:
            return False, "El título no puede exceder 255 caracteres"
        if not re.match(r'^[a-zA-Z0-9\sáéíóúÁÉÍÓÚñÑ.,!?-]+$', title.strip()):
            return False, "El título contiene caracteres no permitidos"
        return True, ""
    
    @staticmethod
    def validate_priority(priority):
        valid_priorities = ['baja', 'media', 'alta']
        if not priority or priority not in valid_priorities:
            return False, "La prioridad debe ser: baja, media o alta"
        return True, ""

# Controlador de Tareas
class TaskController:
    @staticmethod
    def get_all_tasks():
        try:
            tasks = Task.query.order_by(Task.created_at.desc()).all()
            return jsonify({
                'success': True,
                'tasks': [task.to_dict() for task in tasks]
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'error': 'Error al obtener las tareas'
            }), 500
    
    @staticmethod
    def get_tasks_by_priority(priority):
        try:
            if priority == 'todas':
                tasks = Task.query.order_by(Task.created_at.desc()).all()
            else:
                tasks = Task.query.filter_by(priority=priority).order_by(Task.created_at.desc()).all()
            
            return jsonify({
                'success': True,
                'tasks': [task.to_dict() for task in tasks]
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'error': 'Error al filtrar las tareas'
            }), 500
    
    @staticmethod
    def create_task(data):
        try:
            # Validar datos
            title_valid, title_error = TaskValidator.validate_title(data.get('title'))
            priority_valid, priority_error = TaskValidator.validate_priority(data.get('priority'))
            
            if not title_valid:
                return jsonify({
                    'success': False,
                    'error': title_error
                }), 400
            
            if not priority_valid:
                return jsonify({
                    'success': False,
                    'error': priority_error
                }), 400
            
            # Crear nueva tarea
            new_task = Task(
                title=data['title'].strip(),
                priority=data['priority']
            )
            
            db.session.add(new_task)
            db.session.commit()
            
            return jsonify({
                'success': True,
                'task': new_task.to_dict(),
                'message': 'Tarea creada exitosamente'
            }), 201
            
        except Exception as e:
            db.session.rollback()
            return jsonify({
                'success': False,
                'error': 'Error al crear la tarea'
            }), 500
    
    @staticmethod
    def update_task(task_id, data):
        try:
            task = Task.query.get(task_id)
            if not task:
                return jsonify({
                    'success': False,
                    'error': 'Tarea no encontrada'
                }), 404
            
            # Validar datos
            title_valid, title_error = TaskValidator.validate_title(data.get('title'))
            priority_valid, priority_error = TaskValidator.validate_priority(data.get('priority'))
            
            if not title_valid:
                return jsonify({
                    'success': False,
                    'error': title_error
                }), 400
            
            if not priority_valid:
                return jsonify({
                    'success': False,
                    'error': priority_error
                }), 400
            
            # Actualizar tarea
            task.title = data['title'].strip()
            task.priority = data['priority']
            task.updated_at = datetime.utcnow()
            
            db.session.commit()
            
            return jsonify({
                'success': True,
                'task': task.to_dict(),
                'message': 'Tarea actualizada exitosamente'
            }), 200
            
        except Exception as e:
            db.session.rollback()
            return jsonify({
                'success': False,
                'error': 'Error al actualizar la tarea'
            }), 500
    
    @staticmethod
    def delete_task(task_id):
        try:
            task = Task.query.get(task_id)
            if not task:
                return jsonify({
                    'success': False,
                    'error': 'Tarea no encontrada'
                }), 404
            
            db.session.delete(task)
            db.session.commit()
            
            return jsonify({
                'success': True,
                'message': 'Tarea eliminada exitosamente'
            }), 200
            
        except Exception as e:
            db.session.rollback()
            return jsonify({
                'success': False,
                'error': 'Error al eliminar la tarea'
            }), 500

# Rutas de la API
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    priority = request.args.get('priority', 'todas')
    if priority != 'todas':
        return TaskController.get_tasks_by_priority(priority)
    return TaskController.get_all_tasks()

@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data:
        return jsonify({
            'success': False,
            'error': 'Datos no proporcionados'
        }), 400
    return TaskController.create_task(data)

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    if not data:
        return jsonify({
            'success': False,
            'error': 'Datos no proporcionados'
        }), 400
    return TaskController.update_task(task_id, data)

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    return TaskController.delete_task(task_id)

# Manejo de errores
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 'Recurso no encontrado'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({
        'success': False,
        'error': 'Error interno del servidor'
    }), 500

# Crear tablas y datos de ejemplo
def create_tables():
    with app.app_context():
        db.create_all()
        
        # Insertar datos de ejemplo si la tabla está vacía
        if Task.query.count() == 0:
            sample_tasks = [
                Task(title='Completar proyecto Flask', priority='alta'),
                Task(title='Revisar documentación', priority='media'),
                Task(title='Hacer backup de datos', priority='baja'),
                Task(title='Actualizar dependencias', priority='media'),
                Task(title='Configurar servidor', priority='alta')
            ]
            
            for task in sample_tasks:
                db.session.add(task)
            
            db.session.commit()
            print("✅ Datos de ejemplo insertados")

if __name__ == '__main__':
    create_tables()
    app.run(debug=True, host='0.0.0.0', port=5000) 