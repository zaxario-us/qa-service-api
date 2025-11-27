from typing import Annotated
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True


class Question(Base):
    __tablename__ = "question"

    id: Mapped[Annotated[int, mapped_column(primary_key=True, autoincrement=True)]]
    text: Mapped[str]
    created_at: Mapped[Annotated[datetime, mapped_column(default=datetime.now())]]

    answers = relationship("Answer", back_populates="question")


class Answer(Base):
    __tablename__ = "answer"

    id: Mapped[Annotated[int, mapped_column(primary_key=True, autoincrement=True)]]
    question_id: Mapped[Annotated[int, mapped_column(ForeignKey("question.id", ondelete="CASCADE"))]]
    user_id: Mapped[str]
    text: Mapped[str]
    created_at: Mapped[Annotated[datetime, mapped_column(default=datetime.now())]]

    question = relationship("Question", back_populates="answers")