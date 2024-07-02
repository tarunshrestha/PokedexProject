from fastapi import FastAPI, Depends
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
import models
from database import SessionLocal, engine
import router

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def custom_swagger_ui_html():
    return JSONResponse(content=get_openapi(title="API docs", version="1.0.0", routes=app.routes))


app.include_router(router.router, prefix='/api/v1/pokemons', tags=["pokemon"])
