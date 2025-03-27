from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORSの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NameRequest(BaseModel):
    name: str

@app.get("/")
async def root():
    return {"message": "Welcome to KoiLog API"} 

@app.post("/api/")
async def process_data(request: NameRequest):
    print(request)
    return {"name": request.name}