from pathlib import Path

def create_project():
	print("Creando proyecto FastAPI...")

	# Crear estructura de carpetas
	folders = [
		"app",
		"app/core",
		"app/models",
		"app/schemas",
		"app/crud",
		"app/api/v1/endpoints",
		"app/services",
		"app/utils",
		"app/tests",
	]

	for folder in folders:
		Path(folder).mkdir(parents=True, exist_ok=True)
		print(f"✅ Carpeta creada: {folder}")

	# Crear archivo main.py
	main_content = """from fastapi import FastAPI

app = FastAPI(title="Auth Boilerplate", version="1.0.0")

@app.get("/")
def read_root():
	return {"message": "Bienvenido a Auth Boilerplate API"}

@app.get("/health")
def health_check():
	return {"status": "healthy"}
"""
	with open("app/main.py", "w", encoding="utf-8") as f:
		f.write(main_content)
	print("✅ app/main.py creado")

	# Crear requirements.txt
	requirements = """fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
python-dotenv==1.0.0
pydantic-settings==2.1.0
"""
	with open("requirements.txt", "w", encoding="utf-8") as f:
		f.write(requirements)
	print("✅ requirements.txt creado")

	print("\n🎉 Proyecto creado exitosamente!")
	print("Próximos pasos:")
	print("1. python -m venv venv")
	print("2. .\\venv\\Scripts\\activate    (Windows) or source venv/bin/activate (Linux/macOS)")
	print("3. pip install -r requirements.txt")
	print("4. uvicorn app.main:app --reload")

if __name__ == "__main__":
	create_project()