from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db.database import create_db_and_tables
from .routers import product, user

app = FastAPI()

# Include all the routers
app.include_router(product.router)
app.include_router(user.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],  # The frontend URL: TODO make this configurable from externalConfig
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Set up the database
    # TODO: run alembic migrations
    create_db_and_tables()
    yield
    # Put shutdown logic / cleanup here


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
    return {"message": "Refetch"}
