from datetime import datetime
from typing import Annotated
from pydantic import BaseModel, Field, field_serializer


class PartQuestionScheme(BaseModel):
    text: Annotated[str, Field(min_length=1, max_length=4096)]


class PartAnswerScheme(BaseModel):
    user_id: Annotated[
        str,
        Field(pattern=r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-4[0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$")
    ]
    text: Annotated[str, Field(min_length=1, max_length=4096)]


class QuestionScheme(BaseModel):
    id: int
    text: Annotated[str, Field(min_length=1, max_length=4096)]
    created_at: datetime

    @field_serializer('created_at')
    def serialize_timestamp(self, dt: datetime) -> str:
        return dt.strftime("%Y-%m-%d %H:%M:%S")


class AnswerScheme(BaseModel):
    id: int
    question_id: int
    user_id: Annotated[
        str,
        Field(pattern=r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-4[0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$")
    ]
    text: Annotated[str, Field(min_length=1, max_length=4096)]
    created_at: datetime

    @field_serializer('created_at')
    def serialize_timestamp(self, dt: datetime) -> str:
        return dt.strftime("%Y-%m-%d %H:%M:%S")
