#!/usr/bin/env python3
import sys
import os

# Añadir el directorio app al path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.core.database import engine
from app.models.base import Base
from app.models.user import User, RefreshToken, PasswordResetCode

def create_tables():
    """Crea todas las tablas en la base de datos"""
    print("🗃️ Creando tablas en la base de datos...")
    
    try:
        # Crear todas las tablas
        Base.metadata.create_all(bind=engine)
        print("✅ Tablas creadas exitosamente!")
        print("📊 Tablas creadas:")
        print("   - users")
        print("   - refresh_tokens") 
        print("   - password_reset_codes")
        
    except Exception as e:
        print(f"❌ Error creando tablas: {e}")
        return False
    
    return True

if __name__ == "__main__":
    create_tables()