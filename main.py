from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI(title="Security & Geo API")

class Item(BaseModel):
    ip: str
    description: str

@app.get("/")
def read_root():
    return {"status": "online", "message": "API Geolocalización y Seguridad Direcciones IP"}

@app.post("/analyze")
def analyze_ip(item: Item):
    # Consulta direcciones IP a API externa
    response = requests.get(f"http://ip-api.com/json/{item.ip}")
    data = response.json()
    # Validación dirección IP
    if data['status'] == 'fail':
        raise HTTPException(status_code=400, detail="IP no válida")
    
    return {
        "client_description": item.description,
        "geo_data": data,
        "security_score": 85  # Ejemplo de scoring
    }