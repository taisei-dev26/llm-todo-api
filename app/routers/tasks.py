from fastapi import APIRouter
from pydantic import BaseModel
from app.services.tasks import breakdown_task

router = APIRouter(prefix="/api/tasks", tags=["tasks"])

class BreakdownRequest(BaseModel):
  task: str

class BreakdownResponse(BaseModel):
  subtasks: list[str]

@router.post("/breakdown", response_model=BreakdownResponse)
async def breakdown(request: BreakdownRequest):
    """タスクをサブタスクに分解する"""
    subtasks = breakdown_task(request.task)
    return {"subtasks": subtasks}
