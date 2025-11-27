import pytest
import pytest_asyncio
from pydantic import ValidationError

from main import app
from httpx import AsyncClient, ASGITransport

from core.schemes import QuestionScheme


@pytest_asyncio.fixture(scope="function")
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client


@pytest.mark.asyncio
async def test_create_questions(db_session, client):
    response = await client.post("/questions", json={
        "text": "Как дела, народ?"
    })

    data=response.json()
    assert data["message"] == "Question created"

    response = await client.get("/questions")
    data = response.json()

    assert len(data["questions"]) == 1

    with pytest.raises(ValidationError):
        QuestionScheme.model_validate_json(data["questions"][0])

