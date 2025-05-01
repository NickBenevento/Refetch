from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from .db.database import create_db_and_tables
from .routers import product

app = FastAPI()

# Include all the routers
app.include_router(product.router)


@app.on_event("startup")
async def startup_event():
    create_db_and_tables()


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Set up the database
#     # TODO: run alembic migrations
#     create_db_and_tables()
#     yield
#     # Put shutdown logic / cleanup here


# @app.exception_handler(SQLAlchemyError)
# async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
#     return JSONResponse(
#         status_code=500,
#         content={
#             "detail": "An unrecognized error occurred. Please try again later. ({exc})"
#         },
#     )


@app.get("/")
async def root():
    return {"message": "Hello World"}
