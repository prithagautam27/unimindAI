from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database.db import Base

class ChatLog(Base):

    __tablename__ = "chat_logs"

    id = Column(Integer, primary_key=True, index=True)

    user_message = Column(String)

    bot_response = Column(String)

    intent = Column(String)

    timestamp = Column(DateTime, default=datetime.utcnow)