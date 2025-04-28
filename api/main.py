from fastapi import FastAPI

from .db.database import create_db_and_tables
from .routers import product

app = FastAPI()

# Include all the routers
app.include_router(product.router)


# Likely will want to run migration script (alembic)
# SQLModel will have migration utilities wrapping alembic in the future
@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def root():
    return {"message": "Hello World"}
