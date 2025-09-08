from fastapi import (
    APIRouter,
    HTTPException,
    Depends,
    status,
    Security,
    BackgroundTasks,
    Request,
)

router = APIRouter(prefix="/auth", tags=["auth"])
