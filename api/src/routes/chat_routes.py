from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from src.schemas import ChatCreateSchema, ChatSchema
from src.core.db import get_session
from src.models import Chat


router = APIRouter()


@router.get("/chats", response_model=List[ChatSchema])
def get_all_chats(session=Depends(get_session)):
    try:
        chats = session.query(Chat).all()
        if not chats:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="no chats available"
            )
        return chats
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.post("/chat", response_model=ChatSchema)
def create_new_chat(chat: ChatCreateSchema, session=Depends(get_session)):
    try:
        new_chat = Chat(
            prompt=chat.prompt,
            assistant=chat.assistant if chat.assistant is not None else None,
        )
        session.add(new_chat)
        session.commit()
        session.refresh(new_chat)
        return new_chat

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
