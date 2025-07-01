// Clase para gestionar las tareas con API REST
class TaskManager {
    constructor() {
        this.tasks = [];
        this.currentFilter = 'todas';
        this.editingTaskId = null;
        this.apiBaseUrl = '/api/tasks';
        this.initEventListeners();
        this.loadTasks();
    }

    // Mostrar loading
    showLoading() {
        const taskList = document.getElementById('taskList');
        taskList.innerHTML = `
            <li class="loading">
                <div class="spinner"></div>
                <p>Cargando tareas...</p>
            </li>
        `;
    }

    // Mostrar error
    showError(message) {
        const taskList = document.getElementById('taskList');
        taskList.innerHTML = `
            <li class="no-tasks">
                <p>Error: ${message}</p>
                <button onclick="taskManager.loadTasks()" class="btn-primary" style="margin-top: 10px;">
                    Reintentar
                </button>
            </li>
        `;
    }

    // Cargar tareas desde la API
    async loadTasks() {
        try {
            this.showLoading();
            
            const response = await fetch(`${this.apiBaseUrl}?priority=${this.currentFilter}`);
            const data = await response.json();
            
            if (data.success) {
                this.tasks = data.tasks;
                this.renderTasks();
            } else {
                this.showError(data.error || 'Error al cargar las tareas');
            }
        } catch (error) {
            console.error('Error:', error);
            this.showError('Error de conexión');
        }
    }

    // Añadir nueva tarea
    async addTask(title, priority) {
        try {
            const response = await fetch(this.apiBaseUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ title, priority })
            });
            
            const data = await response.json();
            
            if (data.success) {
                this.loadTasks(); // Recargar tareas
                return true;
            } else {
                alert(data.error || 'Error al crear la tarea');
                return false;
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error de conexión');
            return false;
        }
    }

    // Eliminar tarea
    async deleteTask(taskId) {
        if (!confirm('¿Estás seguro de que quieres eliminar esta tarea?')) {
            return;
        }
        
        try {
            const response = await fetch(`${this.apiBaseUrl}/${taskId}`, {
                method: 'DELETE'
            });
            
            const data = await response.json();
            
            if (data.success) {
                this.loadTasks(); // Recargar tareas
            } else {
                alert(data.error || 'Error al eliminar la tarea');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error de conexión');
        }
    }

    // Editar tarea
    editTask(taskId) {
        const task = this.tasks.find(t => t.id === taskId);
        if (task) {
            this.editingTaskId = taskId;
            this.openEditModal(task);
        }
    }

    // Abrir modal de edición
    openEditModal(task) {
        const modal = document.getElementById('editModal');
        const editTitle = document.getElementById('editTitle');
        const editPriority = document.getElementById('editPriority');
        
        editTitle.value = task.title;
        editPriority.value = task.priority;
        
        modal.style.display = 'block';
        editTitle.focus();
    }

    // Cerrar modal de edición
    closeEditModal() {
        const modal = document.getElementById('editModal');
        modal.style.display = 'none';
        this.editingTaskId = null;
        
        // Limpiar formulario
        document.getElementById('editForm').reset();
        document.getElementById('editTitleError').textContent = '';
    }

    // Guardar cambios de edición
    async saveEditTask(title, priority) {
        try {
            const response = await fetch(`${this.apiBaseUrl}/${this.editingTaskId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ title, priority })
            });
            
            const data = await response.json();
            
            if (data.success) {
                this.loadTasks(); // Recargar tareas
                this.closeEditModal();
            } else {
                alert(data.error || 'Error al actualizar la tarea');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error de conexión');
        }
    }

    // Cambiar filtro
    setFilter(filter) {
        this.currentFilter = filter;
        this.updateFilterButtons();
        this.loadTasks();
    }

    // Actualizar botones de filtro
    updateFilterButtons() {
        const filterButtons = document.querySelectorAll('.filter-btn');
        filterButtons.forEach(btn => {
            btn.classList.remove('active');
            if (btn.dataset.filter === this.currentFilter) {
                btn.classList.add('active');
            }
        });
    }

    // Renderizar tareas en la lista
    renderTasks() {
        const taskList = document.getElementById('taskList');
        
        if (this.tasks.length === 0) {
            taskList.innerHTML = '<li class="no-tasks">No hay tareas para mostrar</li>';
            return;
        }

        taskList.innerHTML = this.tasks.map(task => `
            <li class="task-item" data-id="${task.id}">
                <div class="task-info">
                    <div class="task-title">${this.escapeHtml(task.title)}</div>
                    <span class="task-priority priority-${task.priority}">${task.priority}</span>
                </div>
                <div class="task-actions">
                    <button class="edit-btn" onclick="taskManager.editTask(${task.id})">
                        Editar
                    </button>
                    <button class="delete-btn" onclick="taskManager.deleteTask(${task.id})">
                        Eliminar
                    </button>
                </div>
            </li>
        `).join('');
    }

    // Escapar HTML para prevenir XSS
    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    // Validar campo título
    validateTitle(title) {
        const titleInput = document.getElementById('title');
        const titleError = document.getElementById('titleError');
        
        if (!title.trim()) {
            titleInput.classList.add('error');
            titleError.textContent = 'El título es obligatorio';
            return false;
        } else {
            titleInput.classList.remove('error');
            titleError.textContent = '';
            return true;
        }
    }

    // Validar campo título de edición
    validateEditTitle(title) {
        const editTitleInput = document.getElementById('editTitle');
        const editTitleError = document.getElementById('editTitleError');
        
        if (!title.trim()) {
            editTitleInput.classList.add('error');
            editTitleError.textContent = 'El título es obligatorio';
            return false;
        } else {
            editTitleInput.classList.remove('error');
            editTitleError.textContent = '';
            return true;
        }
    }

    // Inicializar event listeners
    initEventListeners() {
        // Formulario de tareas
        const taskForm = document.getElementById('taskForm');
        taskForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const titleInput = document.getElementById('title');
            const prioritySelect = document.getElementById('priority');
            
            const title = titleInput.value;
            const priority = prioritySelect.value;
            
            // Validar título
            if (!this.validateTitle(title)) {
                return;
            }
            
            if (priority) {
                const success = await this.addTask(title, priority);
                if (success) {
                    taskForm.reset();
                    titleInput.focus();
                    // Limpiar mensaje de error al enviar exitosamente
                    this.validateTitle('');
                }
            }
        });

        // Validación en tiempo real del campo título
        const titleInput = document.getElementById('title');
        titleInput.addEventListener('input', () => {
            this.validateTitle(titleInput.value);
        });

        // Botones de filtro
        const filterButtons = document.querySelectorAll('.filter-btn');
        filterButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                this.setFilter(btn.dataset.filter);
            });
        });

        // Modal de edición
        const editForm = document.getElementById('editForm');
        editForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const editTitle = document.getElementById('editTitle');
            const editPriority = document.getElementById('editPriority');
            
            const title = editTitle.value;
            const priority = editPriority.value;
            
            // Validar título
            if (!this.validateEditTitle(title)) {
                return;
            }
            
            if (priority) {
                await this.saveEditTask(title, priority);
            }
        });

        // Validación en tiempo real del campo título de edición
        const editTitleInput = document.getElementById('editTitle');
        editTitleInput.addEventListener('input', () => {
            this.validateEditTitle(editTitleInput.value);
        });

        // Cerrar modal
        const closeModal = document.getElementById('closeModal');
        const cancelEdit = document.getElementById('cancelEdit');
        const modal = document.getElementById('editModal');
        
        closeModal.addEventListener('click', () => {
            this.closeEditModal();
        });
        
        cancelEdit.addEventListener('click', () => {
            this.closeEditModal();
        });
        
        // Cerrar modal al hacer clic fuera de él
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                this.closeEditModal();
            }
        });
    }
}

// Inicializar la aplicación cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    window.taskManager = new TaskManager();
}); 