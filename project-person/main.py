import sqlalchemy
from fastapi import FastAPI
from db import database
from models.post import metadata
from routes.post import router



app = FastAPI()


DATABASE_URL = "sqlite:///jpr_inc_in.db"

sqlalchemy_engine = sqlalchemy.create_engine(DATABASE_URL)


@app.on_event("startup")
async def startup():
    await database.connect()
    metadata.create_all(sqlalchemy_engine)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

metadata.create_all(sqlalchemy_engine)
app.include_router(router, prefix="")
