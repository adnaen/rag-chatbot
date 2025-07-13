from datetime import datetime
from pydantic import BaseModel, UUID1, ConfigDict


class ChatCreateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    prompt: str
    assistant: str | None


class ChatSchema(ChatCreateSchema):
    id: UUID1
    created_at: datetime
