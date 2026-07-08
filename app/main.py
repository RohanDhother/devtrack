from fastapi import FastAPI
from app.routers import applications
from app.database import engine, Base
from app.routers import auth

app = FastAPI(
    title="DevTrack",
    description="Job application tracker API",
    version="0.1.0",
)

app.include_router(applications.router)
app.include_router(auth.router)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root():
    return {"message": "DevTrack API is running"}
