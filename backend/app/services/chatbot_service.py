from app.database.db import SessionLocal
from app.database.models import ChatLog

from app.services.gemini_service import get_gemini_response


def get_chatbot_response(message: str):

    response = get_gemini_response(message)

    db = SessionLocal()

    chat_log = ChatLog(
        user_message=message,
        bot_response=response,
        intent="gemini"
    )

    db.add(chat_log)

    db.commit()

    db.close()

    return response