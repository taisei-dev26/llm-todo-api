from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import translate

app = FastAPI(
    title="LLM Todo API",
    description="OpenAI APIを使った翻訳・テキスト生成API",
    version="0.1.0"
)

# CORS設定（フロントエンドからのアクセス許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーター登録
app.include_router(translate.router)
# app.include_router(generate.router)  # 他のルーターも追加

@app.get("/")
async def root():
    return {"message": "LLM Todo API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}