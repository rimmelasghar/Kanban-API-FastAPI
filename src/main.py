from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import time
import uvicorn
from src.auth import router as auth_router
from src.tasks import router as task_router
from src.admin import router as admin_router
from src.project import router as project_router
from src.config import ALLOWED_ORIGINS

app = FastAPI(title="Fast API Blog",
    docs_url="/kanban-api-docs",
    version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router.router)
app.include_router(task_router.router)
app.include_router(admin_router.router)
app.include_router(project_router.router)


# Middleware to calculate response time of an API
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

