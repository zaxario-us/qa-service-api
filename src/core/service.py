from fastapi import status
from starlette.responses import JSONResponse

from database import query
from database.models import Question, Answer
from core.schemes import QuestionScheme, AnswerScheme, PartQuestionScheme, PartAnswerScheme


async def generate_get_questions_api() -> JSONResponse:
    questions: list[Question] = await query.get_questions()
    questions_dump: list[QuestionScheme] = [
            QuestionScheme.model_validate(question, from_attributes=True).model_dump()
            for question in questions
        ]

    return JSONResponse(status_code=status.HTTP_200_OK, content={"questions": questions_dump})


async def generate_get_question_and_answers_api(question_id: int) -> JSONResponse:
    question: Question = await query.get_question_by_id(question_id)
    answers: list[Answer] = await query.get_answers_from_question(question_id)

    if not question:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Question not found"})

    question_dump: QuestionScheme = QuestionScheme.model_validate(question, from_attributes=True).model_dump()
    answers_dump: list[AnswerScheme] = [
            AnswerScheme.model_validate(answer, from_attributes=True).model_dump()
            for answer in answers
    ]

    return JSONResponse(status_code=status.HTTP_200_OK, content={
        "question": question_dump,
        "answers": answers_dump
    })


async def generate_create_question_api(question_part: PartQuestionScheme) -> JSONResponse:
    result: bool = await query.is_create_question(**question_part.model_dump())

    if result:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Question created"})

    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": "Question not created"})


async def generate_delete_question_api(question_id: int) -> JSONResponse:
    question: Question = await query.get_question_by_id(question_id)

    if not question:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Question not found"})

    result: bool = await query.is_delete_question(question_id)

    if result:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Question deleted"})

    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": "Question not deleted"})


async def generate_get_answer_api(answer_id: int) -> JSONResponse:
    answer: Answer = await query.get_answer_by_id(answer_id)

    if not answer:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Answer not found"})

    answer_dump: AnswerScheme = AnswerScheme.model_validate(answer, from_attributes=True).model_dump()
    return JSONResponse(status_code=status.HTTP_200_OK, content={"answer": answer_dump})


async def generate_create_answer_api(question_id: int, answer_part: PartAnswerScheme) -> JSONResponse:
    question_exists = await query.is_question_exists(question_id)

    if not question_exists:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Question not found"})

    result: bool = await query.is_create_answer(question_id=question_id, **answer_part.model_dump())

    if result:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Answer created"})

    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": "Answer not created"})


async def generate_delete_answer_api(answer_id: int) -> JSONResponse:
    answer: Answer = await query.get_answer_by_id(answer_id)

    if not answer:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Answer not found"})

    result: bool = await query.is_delete_answer(answer_id)

    if result:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Answer deleted"})

    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": "Answer not deleted"})
