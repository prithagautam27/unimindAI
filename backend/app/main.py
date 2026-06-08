from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.db import engine
from app.database.models import Base
from app.routes.chatbot_routes import router as chatbot_router
from app.routes.analytics_routes import router as analytics_router

app = FastAPI(
    title="UniMind API",
    version="1.0.0"
)
Base.metadata.create_all(bind=engine)
# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include chatbot routes
app.include_router(chatbot_router)
app.include_router(analytics_router)

@app.get("/")
def home():
    return {
        "message": "UniMind Backend Running Successfully"
    }