from fastapi import APIRouter
from sqlalchemy import func

from app.database.db import SessionLocal
from app.database.models import ChatLog

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/summary")
def analytics_summary():

    db = SessionLocal()

    total_chats = db.query(ChatLog).count()

    failed_queries = db.query(ChatLog).filter(
        ChatLog.intent == "unknown"
    ).count()

    db.close()

    return {
        "total_chats": total_chats,
        "failed_queries": failed_queries
    }


@router.get("/intents")
def top_intents():

    db = SessionLocal()

    intent_data = db.query(
        ChatLog.intent,
        func.count(ChatLog.intent)
    ).group_by(ChatLog.intent).all()

    db.close()

    return {
        "intent_usage": [
            {
                "intent": item[0],
                "count": item[1]
            }
            for item in intent_data
        ]
    }