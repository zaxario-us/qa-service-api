import uvicorn

from fastapi import FastAPI

from api import main_router
from core.settings import AppSettings


app = FastAPI(debug=True)
app.include_router(main_router)


if __name__ == "__main__":
    app_settings = AppSettings()

    uvicorn.run(app, host=app_settings.host, port=app_settings.port)
