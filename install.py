#!/usr/bin/env python3
"""
Script de instalación para Gestor de Tareas By Danilo
"""

import os
import sys
import subprocess
import platform

def run_command(command, description):
    """Ejecutar comando y mostrar resultado"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completado")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error en {description}: {e}")
        return False

def check_python():
    """Verificar que Python esté instalado"""
    try:
        version = subprocess.run([sys.executable, '--version'], 
                               capture_output=True, text=True, check=True)
        print(f"✅ Python detectado: {version.stdout.strip()}")
        return True
    except:
        print("❌ Python no está instalado o no es accesible")
        return False

def create_directories():
    """Crear directorios necesarios"""
    directories = [
        'frontend',
        'frontend/static',
        'frontend/templates',
        'backend'
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"📁 Directorio creado: {directory}")

def install_dependencies():
    """Instalar dependencias de Python"""
    print("📦 Instalando dependencias...")
    
    # Crear entorno virtual si no existe
    if not os.path.exists('venv'):
        print("🔧 Creando entorno virtual...")
        if not run_command(f"{sys.executable} -m venv venv", "Crear entorno virtual"):
            return False
    
    # Activar entorno virtual e instalar dependencias
    if platform.system() == "Windows":
        activate_cmd = "venv\\Scripts\\activate"
        pip_cmd = "venv\\Scripts\\pip"
    else:
        activate_cmd = "source venv/bin/activate"
        pip_cmd = "venv/bin/pip"
    
    # Instalar dependencias
    if not run_command(f"{pip_cmd} install -r backend/requirements_simple.txt", "Instalar dependencias"):
        return False
    
    return True

def main():
    print("🚀 Instalación de Gestor de Tareas By Danilo")
    print("=" * 50)
    
    # Verificar Python
    if not check_python():
        sys.exit(1)
    
    # Crear directorios
    create_directories()
    
    # Instalar dependencias
    if not install_dependencies():
        print("❌ Error al instalar dependencias")
        sys.exit(1)
    
    print("\n🎉 ¡Instalación completada!")
    print("\n📋 Para ejecutar la aplicación:")
    print("1. Activa el entorno virtual:")
    if platform.system() == "Windows":
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    print("2. Ejecuta: python start_app.py")
    print("3. Abre tu navegador en: http://localhost:5000")
    
    # Preguntar si quiere ejecutar ahora
    response = input("\n¿Quieres ejecutar la aplicación ahora? (y/n): ").lower()
    if response == 'y':
        print("\n🚀 Iniciando aplicación...")
        subprocess.run([sys.executable, 'start_app.py'])

if __name__ == "__main__":
    main() 