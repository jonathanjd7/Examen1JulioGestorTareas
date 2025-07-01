#!/usr/bin/env python3
"""
Script principal para ejecutar la aplicación Gestor de Tareas By Danilo
"""

import os
import sys
import subprocess

def main():
    print("🚀 Gestor de Tareas By Danilo")
    print("=" * 40)
    
    # Verificar que estamos en el directorio correcto
    if not os.path.exists('backend/app_sqlite.py'):
        print("❌ Error: No se encontró el archivo backend/app_sqlite.py")
        print("Asegúrate de ejecutar este script desde la raíz del proyecto")
        sys.exit(1)
    
    # Cambiar al directorio backend
    os.chdir('backend')
    
    try:
        print("📁 Cambiando al directorio backend...")
        print("🔧 Iniciando aplicación Flask...")
        print("🌐 La aplicación estará disponible en: http://localhost:5000")
        print("⏹️  Presiona Ctrl+C para detener")
        print("-" * 40)
        
        # Ejecutar la aplicación Flask
        subprocess.run([sys.executable, 'app_sqlite.py'])
        
    except KeyboardInterrupt:
        print("\n👋 Aplicación detenida por el usuario")
    except Exception as e:
        print(f"❌ Error al ejecutar la aplicación: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 