from fastapi.routing import APIRouter

from core import service
from core.schemes import PartQuestionScheme


questions_router = APIRouter(prefix="/questions")

@questions_router.get("")
async def get_questions():
    return await service.generate_get_questions_api()


@questions_router.get("/{question_id}")
async def get_question(question_id: int):
    return await service.generate_get_question_and_answers_api(question_id)


@questions_router.post("")
async def create_question(question: PartQuestionScheme):
    return await service.generate_create_question_api(question)


@questions_router.delete("/{question_id}")
async def delete_question(question_id: int):
    return await service.generate_delete_question_api(question_id)