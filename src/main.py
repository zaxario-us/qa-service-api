import uvicorn

from os import environ
from fastapi import FastAPI

from api import main_router


app = FastAPI(debug=True)
app.include_router(main_router)


if __name__ == "__main__":
    host = environ.get("APP_HOST")
    port = int(environ.get("APP_PORT"))

    uvicorn.run(app, host=host, port=port)
