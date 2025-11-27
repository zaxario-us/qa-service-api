from fastapi.routing import APIRouter

from core import service
from core.schemes import PartAnswerScheme

answers_router = APIRouter(prefix="/answers")
question_with_answers_router = APIRouter(prefix="/questions")


@answers_router.get("/{answer_id}")
async def get_answer(answer_id: int):
    return await service.generate_get_answer_api(answer_id)


@question_with_answers_router.post("/{question_id}/answers")
async def create_answer(question_id: int, answer: PartAnswerScheme):
    return await service.generate_create_answer_api(question_id, answer)


@answers_router.delete("/{answer_id}")
async def delete_answer(answer_id: int):
    return await service.generate_delete_answer_api(answer_id)