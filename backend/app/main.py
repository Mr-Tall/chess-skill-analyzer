from fastapi import FastAPI
from app.api.routes_health import router as health_router
from app.api.routes_analysis import router as analysis_router

app = FastAPI(title="Chess Skill Analyzer")

app.include_router(health_router)
app.include_router(analysis_router)