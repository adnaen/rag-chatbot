from uuid import uuid1
from datetime import datetime
from sqlalchemy import Column, TEXT, UUID, DATETIME
from src.core.db import Base


class Chat(Base):
    __tablename__ = "chats"

    id = Column(UUID, primary_key=True, default=uuid1)
    prompt = Column(TEXT, nullable=False, unique=False)
    assistant = Column(TEXT, nullable=True, unique=False)
    created_at = Column(DATETIME, default=datetime.now())
    updated_at = Column(DATETIME, default=datetime.now())
