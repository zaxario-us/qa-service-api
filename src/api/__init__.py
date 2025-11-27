from fastapi.routing import APIRouter

from api.answers import answers_router, question_with_answers_router
from api.questions import questions_router

main_router = APIRouter()

main_router.include_router(questions_router)

main_router.include_router(answers_router)
main_router.include_router(question_with_answers_router)
