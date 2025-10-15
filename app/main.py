from fastapi import FastAPI

app = FastAPI(title="Auth Boilerplate", version="1.0.0")

@app.get("/")
def read_root():
	return {"message": "Bienvenido a Auth Boilerplate API"}

@app.get("/health")
def health_check():
	return {"status": "healthy"}
