from fastapi import FastAPI

from app.routers import applications, auth


def create_app() -> FastAPI:
    app = FastAPI(
        title="DevTrack",
        description="Job application tracker API",
        version="0.1.0",
    )
    app.include_router(applications.router)
    app.include_router(auth.router)
    return app


app = create_app()


@app.get("/")
async def root():
    return {"message": "DevTrack API is running"}
