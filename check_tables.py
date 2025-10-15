#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.core.database import SessionLocal
from sqlalchemy import text

def check_tables():
    print("🔍 Verificando tablas...")
    try:
        db = SessionLocal()
        result = db.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"))
        tables = [row[0] for row in result]
        print("📊 Tablas encontradas:")
        for table in tables:
            print(f"   ✅ {table}")
        db.close()
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    check_tables()