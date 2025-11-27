from sqlalchemy import select, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from database.db import new_session
from database.models import Answer, Question


async def get_questions() -> list[Question]:
    async with new_session() as session:
        query = select(Question).order_by(Question.id)
        questions = (await session.execute(query)).scalars().all()

        return questions


async def get_question_by_id(question_id: int) -> Question | None:
    async with (new_session() as session):
        query = select(Question).where(Question.id == question_id)
        question = (await session.execute(query)).scalars().one_or_none()

        return question


async def is_create_question(text: str) -> bool:
    async with new_session() as session:
        session.add(Question(text=text))

        return await __is_commit_changes(session)


async def is_delete_question(question_id: int) -> bool:
    async with new_session() as session:
        query = delete(Question).where(Question.id == question_id)
        await session.execute(query)

        return await __is_commit_changes(session)


async def get_answers_from_question(question_id: int) -> list[Answer]:
    async with new_session() as session:
        query = select(Answer).where(Answer.question_id == question_id)
        answers = (await session.execute(query)).scalars().all()

        return answers


async def get_answer_by_id(answer_id: int) -> Answer | None:
    async with new_session() as session:
        query = select(Answer).where(Answer.id == answer_id)
        answer = (await session.execute(query)).scalars().one_or_none()

        return answer


async def is_question_exists(question_id: int) -> bool:
    async with new_session() as session:
        query = select(Question).where(Question.id == question_id)
        return bool((await session.execute(query)).scalars().one_or_none())


async def is_create_answer(question_id: int, user_id: str, text: str) -> bool:
    async with new_session() as session:
        session.add(Answer(question_id=question_id, user_id=user_id, text=text))

        return await __is_commit_changes(session)


async def is_delete_answer(answer_id: int) -> bool:
    async with new_session() as session:
        query = delete(Answer).where(Answer.id == answer_id)
        await session.execute(query)

        return await __is_commit_changes(session)


async def __is_commit_changes(session: AsyncSession) -> bool:
    try:
        await session.commit()
        return True
    except IntegrityError:
        await session.rollback()
        return False