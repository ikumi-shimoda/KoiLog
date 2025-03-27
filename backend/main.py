from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import get_db_connection
import mysql.connector

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

@app.get("/api/users")
async def get_users():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)  # 辞書形式で結果を取得
        
        # ユーザーテーブルから全ユーザーを取得
        cursor.execute("SELECT id, username, email, created_at FROM users")
        users = cursor.fetchall()
        
        return {"users": users}
        
    except mysql.connector.Error as err:
        return {"error": f"データベースエラー: {err}"}
        
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()  