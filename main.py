from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI(title="Security & Geo API")

class Item(BaseModel):
    ip: str
    description: str

@app.get("/")
def read_root():
    return {"status": "online", "message": "API funcionando en Google Cloud"}

@app.post("/analyze")
def analyze_ip(item: Item):
    # Simulación de procesamiento/scoring (Puntos extra)
    response = requests.get(f"http://ip-api.com/json/{item.ip}")
    data = response.json()
    
    if data['status'] == 'fail':
        raise HTTPException(status_code=400, detail="IP no válida")
    
    return {
        "client_description": item.description,
        "geo_data": data,
        "security_score": 85  # Ejemplo de scoring
    }